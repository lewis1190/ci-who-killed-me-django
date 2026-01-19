from django import forms
from .models import UserProfile
from allauth.account.forms import SignupForm


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']
        widgets = {
            'profile_picture': forms.FileInput(attrs={
                'class': 'd-none',
                'id': 'profilePictureInput',
                'accept': 'image/*',
            })
        }


# AllAuth OVERRIDE. This will create a user profile when a user signs up.


class CreateUserProfileWithAccountForm(SignupForm):

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super().save(request)

        # Add your own processing here.
        user_profile = UserProfile(user=user)
        user_profile.save()

        # You must return the original result.
        return user
