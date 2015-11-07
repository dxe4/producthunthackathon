from django.views.generic import FormView, TemplateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.contrib.auth import authenticate

from rest_framework.response import Response
from rest_framework import mixins, generics

from base import forms
from base.utils import Meetup


class SignupView(FormView):
    template_name = "signup.html"
    form_class = forms.SignUpForm
    success_url = "/profile"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(SignupView, self).form_valid(form)


class LoginView(FormView):
    template_name = "login.html"
    form_class = forms.LoginForm
    success_url = "/profile"

    def form_valid(self, form):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return redirect("/login")


class ProfileView(TemplateView):
    template_name = "profile.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProfileView, self).dispatch(request, *args, **kwargs)


class MyMeetups(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
        user_info = request.user.userinfo
        meetup = Meetup(user_info=user_info)
        return Response({}, status=200)
