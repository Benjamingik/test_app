from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView

from user.forms import RegisterForm
from user.models import User


# Create your views here.
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'pages/register_page.html', {'form': form})

    def post(self, request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        return render(request, 'pages/register_page.html', {'form': form})


class ProfileView(DetailView):
    model = User
    template_name = 'pages/profile_page.html'
    context_object_name = 'user'


def logout_view(request):
    logout(request)
    return redirect('home')


class DetailProfileView(View):
    pass


class EditProfileView(UpdateView):
    model = User
    fields = ["username", "email", "first_name", "last_name", "avatar"]
    template_name = 'pages/edit_profile_page.html'
    succes_url = reversed('profile_detail')

    def get_success_url(self):
        return reverse_lazy('accaunt:profile_detail', kwargs={"pk", self.object.pk})


class DeleteProfileView(DeleteView):
    model = User
    template_name = 'pages/delete_profile_page.html'

    def get_success_url(self):
        return reverse_lazy('home')
