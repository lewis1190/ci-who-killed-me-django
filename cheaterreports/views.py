from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpRequest
from .models import CheaterPost

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
