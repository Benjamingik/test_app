from django.urls import path

# from click.views import   result_view, subject_list_view, subject_view, variant_view
from user.views import RegisterView, ProfileView, EditProfileView, DeleteProfileView, DetailProfileView, logout_view
from django.contrib.auth.views import LoginView, LogoutView
from user.forms import CustomAuthenticationForm

app_name = 'accaunt'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/',
         LoginView.as_view(authentication_form=CustomAuthenticationForm, template_name='pages/login_page.html'),
         name='login'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/detail/<int:pk>/', DetailProfileView.as_view(), name='profile_detail'),
    path('profile/edit/<int:pk>/', EditProfileView.as_view(), name='profile_edit'),
    path('profile/delete/<int:pk>/', DeleteProfileView.as_view(), name='profile_delete'),
    path('logout/', logout_view, name='logout'),
]
