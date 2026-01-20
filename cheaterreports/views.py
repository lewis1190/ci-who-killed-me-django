from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpRequest, JsonResponse
from typing import cast
from .models import CheaterPost, Vote
from userprofile.models import UserProfile

# Create your views here.


def list_reports(request: HttpRequest):
    # Get all reports, ordered by most recent
    reports = CheaterPost.objects.all().order_by('-created_on')

    # Get the search query from the URL parameter
    suspect_query = request.GET.get('suspect', '').strip()

    # Filter by suspect username if provided
    if suspect_query:
        reports = reports.filter(suspect_username__icontains=suspect_query)

    # Pagination (10 reports per page)
    paginator = Paginator(reports, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'reports': page_obj.object_list,
        'suspect_query': suspect_query,
    }
    return render(request, 'cheaterreports/reports_list.html', context)


@login_required
def new_report(request: HttpRequest):
    if request.method == 'POST':
        title = request.POST.get('title')
        suspect_username = request.POST.get('suspect_username')
        game_name = request.POST.get('game_name')
        youtube_url = request.POST.get('youtube_url')
        hack_types = request.POST.getlist('hack_types')
        description = request.POST.get('description')

        # Prepare form data for error responses
        form_data = {
            'title': title,
            'suspect_username': suspect_username,
            'game_name': game_name,
            'youtube_url': youtube_url,
            'hack_types': hack_types,
            'description': description,
        }

        # Validate required fields
        if not all([title, suspect_username, game_name, youtube_url,
                    hack_types, description]):
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'cheaterreports/report_form.html',
                          {'form_data': form_data})

        # Create and save the report
        try:
            report = CheaterPost(
                author=request.user,
                title=title,
                suspect_username=suspect_username,
                game_name=game_name,
                youtube_url=youtube_url,
                suspected_hack_types=hack_types,
                description=description,
            )
            report.save()
            messages.success(
                request, 'Your report has been submitted successfully!')
            return redirect('report_detail', report_id=report.pk)
        except Exception as e:
            messages.error(
                request,
                f'An error occurred while submitting your report: {str(e)}')
            return render(request, 'cheaterreports/report_form.html',
                          {'form_data': form_data})

    return render(request, 'cheaterreports/report_form.html')


def report_detail(request: HttpRequest, report_id: int):
    report = get_object_or_404(CheaterPost, pk=report_id)
    context = {
        'report': report,
    }
    return render(request, 'cheaterreports/report_detail.html', context)


@login_required
def report_edit(request: HttpRequest, report_id: int):
    report = get_object_or_404(CheaterPost, pk=report_id)

    # Check if the user is the author
    if report.author != request.user:
        messages.error(
            request, 'You do not have permission to edit this report.')
        return redirect('report_detail', report_id=report_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        suspect_username = request.POST.get('suspect_username')
        game_name = request.POST.get('game_name')
        youtube_url = request.POST.get('youtube_url')
        hack_types = request.POST.getlist('hack_types')
        description = request.POST.get('description')

        # Prepare form data for error responses
        form_data = {
            'title': title,
            'suspect_username': suspect_username,
            'game_name': game_name,
            'youtube_url': youtube_url,
            'hack_types': hack_types,
            'description': description,
        }

        # Validate required fields
        if not all([title, suspect_username, game_name, youtube_url,
                    hack_types, description]):
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'cheaterreports/report_form.html', {
                'report': report,
                'is_edit': True,
                'form_data': form_data,
            })

        # Update the report
        try:
            report.title = title or ''
            report.suspect_username = suspect_username or ''
            report.game_name = game_name or ''
            report.youtube_url = youtube_url or ''
            report.suspected_hack_types = hack_types
            report.description = description or ''
            report.save()
            messages.success(request,
                             'Your report has been updated successfully!')
            return redirect('report_detail', report_id=report.pk)
        except Exception as e:
            messages.error(
                request,
                f'An error occurred while updating your report: {str(e)}')
            return render(request, 'cheaterreports/report_form.html', {
                'report': report,
                'is_edit': True,
                'form_data': form_data,
            })

    context = {
        'report': report,
        'is_edit': True,
    }
    return render(request, 'cheaterreports/report_form.html', context)


@login_required
def report_delete(request: HttpRequest, report_id: int):
    report = get_object_or_404(CheaterPost, pk=report_id)

    # Check if the user is the author
    if report.author != request.user:
        messages.error(
            request, 'You do not have permission to delete this report.')
        return redirect('report_detail', report_id=report_id)

    if request.method == 'POST':
        # Delete the report
        try:
            report.delete()
            messages.success(request,
                             'Your report has been deleted successfully!')
            # Check if there's a redirect destination specified
            next_page: str = request.POST.get('next', 'home')
            return redirect(next_page)
        except Exception as e:
            messages.error(
                request,
                f'An error occurred while deleting your report: {str(e)}')
            return redirect('report_detail', report_id=report_id)

    # If GET request, redirect to report detail (shouldn't normally happen)
    return redirect('report_detail', report_id=report_id)


@login_required
def vote_report(request: HttpRequest, report_id: int, vote_type: str):
    """
    Handle voting on a report. Vote types are 'up' or 'down'.
    If the user has already voted the same way, remove the vote.
    If the user voted the opposite way, change the vote.
    """
    if vote_type not in ['up', 'down']:
        return JsonResponse({'error': 'Invalid vote type'}, status=400)

    report = get_object_or_404(CheaterPost, pk=report_id)

    # Check if user is trying to vote on their own post
    if report.author == request.user:
        messages.error(request, 'You cannot vote on your own reports.')
        return redirect('report_detail', report_id=report_id)

    # Check if user has already voted on this post
    existing_vote = Vote.objects.filter(user=request.user, post=report).first()

    if existing_vote:
        if existing_vote.vote_type == vote_type:
            # User is removing their vote
            old_vote_type = existing_vote.vote_type
            existing_vote.delete()

            # Adjust score and author reputation
            score_change = -1 if old_vote_type == 'up' else 1
            report.score += score_change
            report.save()

            # We're using a cast here. This is normally risky, but we know:
            # - There is always a UserProfile connected to a User via
            #   a OneToOneField
            # - The linter cannot infer the OneToOneField from the codebase
            # Therefore, all usages of this in this file are safe.
            profile = cast(
                UserProfile, getattr(report.author, 'profile', None)
            )
            if profile:
                profile.reputation += score_change
                profile.save()

            messages.success(request, 'Your vote has been removed.')
        else:
            # User is changing their vote
            old_vote_type = existing_vote.vote_type
            existing_vote.vote_type = vote_type
            existing_vote.save()

            # Adjust score and author reputation (remove old, add new)
            old_change = 1 if old_vote_type == 'up' else -1
            new_change = 1 if vote_type == 'up' else -1
            total_change = new_change - old_change

            report.score += total_change
            report.save()

            profile = cast(
                UserProfile, getattr(report.author, 'profile', None)
            )
            if profile:
                profile.reputation += total_change
                profile.save()

            messages.success(
                request, f'Your vote has been changed to {vote_type}vote.')
    else:
        # Create new vote
        Vote.objects.create(user=request.user, post=report,
                            vote_type=vote_type)

        # Adjust score and author reputation
        score_change = 1 if vote_type == 'up' else -1
        report.score += score_change
        report.save()

        profile = cast(
            UserProfile, getattr(report.author, 'profile', None)
        )
        if profile:
            profile.reputation += score_change
            profile.save()

        messages.success(request, f'You have {vote_type}voted this report.')

    return redirect('report_detail', report_id=report_id)
