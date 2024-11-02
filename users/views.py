from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

# Create your views here.


class SignUpView(CreateView):
    '''
    View allowing users to sign up, using the CustomUserCreationForm,
    returns to login page upon success
    '''
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super(SignUpView, self).get(request, *args, **kwargs)
