from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from .models import Shop


# --------------------------
# SHOP FORM (Your existing code)
# --------------------------
class ShopForm(forms.ModelForm):
    latitude = forms.FloatField(widget=forms.HiddenInput())
    longitude = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Shop
        fields = ["name", "address", "category", "latitude", "longitude"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.TextInput(attrs={"class": "form-control"}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)

        lat = self.cleaned_data.get("latitude")
        lon = self.cleaned_data.get("longitude")

        if lat is None or lon is None:
            raise forms.ValidationError("Please select a location on the map.")

        instance.location = Point(lon, lat, srid=4326)

        if commit:
            instance.save()
        return instance


# --------------------------
# LOGIN FORM
# --------------------------
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"})
    )


# --------------------------
# SIGNUP FORM
# --------------------------
class CustomSignupForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Choose a username"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter password"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm password"})
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
