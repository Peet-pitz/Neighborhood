from django import forms
from .models import User,Hood,Business,Post,Health

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['writer']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = '__all__'

# class HealthForm(forms.ModelForm):
#     class Meta:
#         model = Health
#         fields = '__all__'

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = User
#         exclude = ['user']

# class HoodForm(forms.ModelForm):
#     class Meta:
#         model = User
#         exclude = ['user','user_image','user_email']