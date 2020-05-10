from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {'count': count})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def member_home(request):
    return render(request, 'member_home.html')

@login_required
def list_member(request):
    members = User.objects.all()
    count = members.count()
    context = {'count': count, 'members': members}

    return render(request, 'admin/member_list.html', context)
