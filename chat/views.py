from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView

from .forms import SignUpForm  # SignUpForm function from forms.py

# Create your views here.
def frontpage(request):
    return render(request, 'chat/frontpage.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()

    return render(request, 'chat/signup.html', {'form': form}) # context dictionary: used to pass context variables to the template

class CustomLoginView(LoginView):   # Inheriting LoginView class from auth module
     def dispatch(self, request, *args, **kwargs):  # overriding dispatch method
          if request.user.is_authenticated: # redirect users to frontpage, if already logged in (manually enters login url)
               return redirect('frontpage')
          return super().dispatch(request, *args, **kwargs)

def user_logout(request):
        logout(request)
        return redirect('login')