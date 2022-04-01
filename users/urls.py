from django.urls import path
from .views import SubscribeView, RegisterView, LoginView, UserView, LogoutView, HardRegisterView

urlpatterns = [
    path('subscribe', SubscribeView.as_view()),
    path('register', RegisterView.as_view()),
    path('hard-register', HardRegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
]
