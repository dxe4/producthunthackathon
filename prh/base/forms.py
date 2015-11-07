import time
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from base.utils import meetup_signup, timestamp_to_datetime
from base.models import UserInfo


class LoginForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    meetup_code = forms.CharField(
        widget=forms.HiddenInput
    )
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def save(self, *args, **kwargs):
        # http://www.meetup.com/meetup_api/auth/#oauth2
        reuslt = meetup_signup(
            self.cleaned_data['meetup_code']
        )

        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User(
            username=username,
            email=self.cleaned_data['email'],
        )

        user.set_password(password)
        user.save()

        user = authenticate(username=username, password=password)

        user_info_data = reuslt['me']
        user_auth_data = reuslt['auth']

        user_data = {
            'user': user,
            'joined': timestamp_to_datetime(
                user_info_data.get('joined')
            ),
            'expires_in': timestamp_to_datetime(
                time.time() + user_auth_data.get('expires_in')
            ),
            'access_token': user_auth_data.get("access_token"),
            'token_type': user_auth_data.get("token_type"),
            'refresh_token': user_auth_data.get("refresh_token"),
        }

        # joined
        user_info_keys = [
            "city", "country",
            "lat", "lon", "name", "other_services",
        ]
        user_info = {
            key: user_info_data.get(key) for key in user_info_keys
        }

        user_data.update(user_info)

        user_info = UserInfo(**user_data)
        user_info.save()

        return user
