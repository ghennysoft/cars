from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .forms import UserUpdateForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser


User = CustomUser

def Register(request):
    if request.method == 'POST':
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        if User.objects.filter(email=email):
            messages.warning(request, "Cet email existe déjà")
            return redirect('accounts:register')
        elif User.objects.filter(phone=phone):
            messages.warning(request, "Ce numéro existe déjà !")
            return redirect('accounts:register')
        else:
            user = User.objects.create_user(email, phone, password)
            user.last_name = last_name
            user.first_name = first_name
            user.save()
            if user:
                auth = authenticate(username=user.email, password=password)
                if auth is not None:
                    login(request, auth)
                    return redirect('home:home')
    return render(request, 'accounts/register.html', {})


def Login(request):
    email_phone = request.POST.get('email_phone')
    password = request.POST.get('password')
    if request.method=='POST':
        if(User.objects.filter(email=email_phone).exists()):
            user = authenticate(username=email_phone, password=password)
        elif(User.objects.filter(phone=email_phone).exists()):
            user = User.objects.get(phone=email_phone)
            user = authenticate(username=user.email, password=password)
        else:
            messages.error(request, "Données incorrects! Réessayez")
            return redirect('accounts:login')
        if user is not None:
            login(request, user)
            return redirect('home:home')
        else:
            messages.error(request, "Mot de passe incorrects! Réessayez")
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')


@login_required
def Logout(request):
    logout(request)
    return redirect('home:home')


@login_required
def profile(request):
    template_name = 'accounts/profile.html'
    context = {}
    return render(request, template_name, context)


@login_required
def UpdateUser(request, pk):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accounts:profile', args=[pk]))
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'accounts/update_profile.html', {'form': form})
    