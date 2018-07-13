
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in
            return redirect('articles:list') # in articles/urls.py: app_name and name in urlpatterns
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'formName':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            return redirect('articles:list')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'formName':form})
