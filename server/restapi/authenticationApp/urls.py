from django.urls import path
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

from .views import UserRegister, UserGetInfoView, UserUpdateView, UserDeleteView

urlpatterns = [
    url(r'^login/', obtain_jwt_token),
    url(r'^status/', verify_jwt_token ),
    url(r'^refresh/', refresh_jwt_token),
    url(r'^register/', UserRegister.as_view()),
    url(r'^get-info/', UserGetInfoView.as_view()),
    url(r'^update/', UserUpdateView.as_view()),
    url(r'^delete/', UserDeleteView.as_view()),
]