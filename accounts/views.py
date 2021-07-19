from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView # noqa
from .forms import AccountRegistrationForm


class AccountRegistrationView(CreateView):
    model = User
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('index')
    form_class = AccountRegistrationForm


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_redirect_url(self):
        param_next = self.request.GET.get('next')
        if param_next:
            return param_next
        return reverse('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, f'User {self.request.user} successfully logged in')
        messages.info(self.request, f'User {self.request.user} successfully logged in')
        messages.warning(self.request, f'User {self.request.user} successfully logged in')

        return result

class AccountLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
