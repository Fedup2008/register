from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from apps.forms import LoginForm, RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login

from service.bot_send import send_msg


class IndexView(TemplateView):
    template_name = 'index.html'



class RegisterView(FormView):
    template_name = 'auth/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')


    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        send_msg(first_name=first_name, last_name=last_name, username=username, email=email)
        form.save()
        return super().form_valid(form)



class LoginView(FormView):
    template_name = 'auth/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request,username=username, password=password)
        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Invalid username or password')
            return self.form_invalid(form)


