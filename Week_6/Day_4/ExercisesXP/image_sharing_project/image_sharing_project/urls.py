from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from image_share.views import signup_view , ImageCreateView , ImageListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name = 'registration/login.html'), name= 'login'),
    path('logout/', LogoutView.as_view(template_name = 'registration/logout.html'), name= 'logout'),
    path('signup/', signup_view.as_view(), name='signup'),
    path('create-image/' , ImageCreateView.as_view() , name='create_image'),
    path('images/' , ImageListView.as_view() , name='images')
]