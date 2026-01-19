from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

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
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'userprofile/user_profile.html', context)
