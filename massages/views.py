from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from .models import Massage
from .forms import MassageForm, ReservationForm

from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegistrationForm

def is_admin(user):
  
    return user.is_superuser

def home(request):
    
    return render(request, 'massages/home.html')

def massages_home(request):
   
    massages = Massage.objects.all()
    return render(request, 'massages/massages.html', {'massages': massages})

@login_required
def reserve_massage(request, massage_id):
    
    massage = get_object_or_404(Massage, id=massage_id)

    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.massage = massage
            reservation.save()
            return HttpResponse(f"Réservation confirmée pour {massage.name} !")
    else:
        form = ReservationForm()

    return render(request, 'massages/reserve.html', {'massage': massage, 'form': form})

@login_required
@user_passes_test(is_admin)
def create_massage(request):
   
    if request.method == 'POST':
        form = MassageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('massages_home')
    else:
        form = MassageForm()
    return render(request, 'massages/create_massage.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def update_massage(request, massage_id):
   
    massage = get_object_or_404(Massage, id=massage_id)
    if request.method == 'POST':
        form = MassageForm(request.POST, request.FILES, instance=massage)
        if form.is_valid():
            form.save()
            return redirect('massages_home')
    else:
        form = MassageForm(instance=massage)
    return render(request, 'massages/update_massage.html', {'form': form, 'massage': massage})

@login_required
@user_passes_test(is_admin)
def delete_massage(request, massage_id):

    massage = get_object_or_404(Massage, id=massage_id)
    if request.method == 'POST':
        massage.delete()
        return redirect('massages_home')
    return render(request, 'massages/delete_massage.html', {'massage': massage})


def register(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Votre compte a été créé avec succès !")
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'massages/register.html', {'form': form})