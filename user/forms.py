from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _
# from django import forms

from user.models import User


class RegisterForm(UserCreationForm):
    error_messages = {
        "unique": _("Bunday username ega foydalanuvchi allaqachon mavjud."),
    }

    def init(self, *args, **kwargs):
        super(RegisterForm, self).init(*args, **kwargs)

        self.fields['email'].label = ''
        self.fields['email'].help_text = None
        self.fields['email'].widget.attrs.update({'placeholder': 'Email...'})

        self.fields['username'].label = ''
        self.fields['username'].help_text = None
        self.fields['username'].widget.attrs.update({'placeholder': _('Foydalanuvchi nomi...')})

        self.fields['password1'].label = ''
        self.fields['password1'].help_text = None
        self.fields['password1'].widget.attrs.update({'placeholder': _('Parol...')})

        self.fields['password2'].label = ''
        self.fields['password2'].help_text = None
        self.fields['password2'].widget.attrs.update({'placeholder': _('Parolni tasdiqlang...')})

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        help_texts = {
            "username": _("150 yoki undan kam belgi. Faqat harflar, raqamlar va @/./+/-/_"),
        }


class CustomAuthenticationForm(AuthenticationForm):
    error_message = {
        'invalid_login': 'Login yoki parol xato. Iltimos qaytadan urinib ko`ring!'
    }