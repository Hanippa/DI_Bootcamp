
from django.urls import path
from django.contrib.auth.views import LoginView , LogoutView
from .views import signup_view , ProfileView

urlpatterns = [
    path('login/' , LoginView.as_view(template_name='login.html') , name = 'login'),
    path('logout/', LogoutView.as_view(template_name='logout.html') , name='logout'),
    path('signup' , signup_view.as_view() , name='signup'),
    path('profile/<int:pk>' , ProfileView.as_view() , name='profile')
]
