from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import UserProfile
from .forms import UserProfileForm
from cheaterreports.models import CheaterPost

# Create your views here.


@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES,
                               instance=user_profile)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your profile has been successfully updated!')
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=user_profile)

    # Get all reports created by the logged-in user
    reports = CheaterPost.objects.filter(author=request.user).order_by(
        '-created_on'
    )

    # Paginate reports (5 per page)
    paginator = Paginator(reports, 5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'user_profile': user_profile,
        'form': form,
        'page_obj': page_obj,
        'reports': page_obj.object_list,
    }
    return render(request, 'userprofile/user_profile.html', context)
