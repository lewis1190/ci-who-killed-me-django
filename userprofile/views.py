from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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

        print(request.FILES)
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

    context = {
        'user_profile': user_profile,
        'form': form,
        'reports': reports,
    }
    return render(request, 'userprofile/user_profile.html', context)
