from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

# ----------------------------
# Registration Form
# ----------------------------
class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

    # Optional: add clean_email or clean_username if you want to check for duplicates

# ----------------------------
# Login Form
# ----------------------------
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    user_cache = None  # Store authenticated user

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise ValidationError("Invalid username or password.")
            self.user_cache = user  # Store for view
        return cleaned_data

    def get_user(self):
        return self.user_cache

# ----------------------------
# Profile Update Form
# ----------------------------
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "bio", "avatar")
