from django.conf.urls import url

from base import views


urlpatterns = [
    url(r'^signup$', views.SignupView.as_view(), name="signup"),
    url(r'^login$', views.LoginView.as_view(), name="login"),
    url(r'^profile$', views.ProfileView.as_view(), name="profile"),
]
