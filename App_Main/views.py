from django.shortcuts import render, get_object_or_404, redirect
from . models import *
from . forms import *
from . Calcul import DER
# 함수형 뷰에서 사용하는 권한 제한
from django.contrib.auth.decorators import login_required

def Main_Home(request):
    return render(request, 'Main_Home.html')

def Pet_info_View(request):
    try:
        Pet = Pet_info.objects.get(pet_owner=request.user)
    except:
        Pet = None
   
    try:
        Pet_diet_info = get_object_or_404(Pet_diet_set, pet_name = Pet)
    except:
        Pet_diet_info = None

    context = {'Pet' : Pet, 'Pet_diet_info' : Pet_diet_info}

    if request.path == '/pet/info':
        return render(request, 'Pet_info.html',context)
    elif request.path == '/pet/diet/info':
        return render(request, 'Pet_diet_info.html',context)
    
@login_required(login_url='App_Auth:login')
def Pet_create_View(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            Pet_info = form.save(commit=False)
            Pet_info.pet_owner = request.user
            Pet_info.save()   
            return redirect("App_Main:pet")
    else:
        form = PetForm() # -> unboundForm

    return render(request, 'Pet_create.html',{'form': form})
  
@login_required(login_url='App_Auth:login')
def Pet_update_View(request):
    pet_info = get_object_or_404(Pet_info, pet_owner = request.user)
    
    if request.method == 'POST':
        form = PetForm(request.POST, instance = pet_info)
        if form.is_valid():
            Pet = form.save(commit=False)
            Pet.pet_owner = request.user
            Pet.save()   
            return redirect("App_Main:pet")
    else:
        form = PetForm(instance = pet_info) # -> unboundForm
    context = {'form': form, 'pet_info' : pet_info}
    return render(request, 'Pet_create.html',context)

def Pet_statistics_View(request):
    return render(request, 'Pet_statistics.html')

@login_required(login_url='App_Auth:login')
def Pet_diet_set_View(request):
    pet_info = get_object_or_404(Pet_info, pet_owner = request.user)
    if request.path == '/pet/diet/update':
        pet_diet_info = get_object_or_404(Pet_diet_set, pet_name = pet_info )
        
    else:
        pet_diet_info = None

    if request.method == 'POST':
        form = PetdietForm(request.POST, instance = pet_diet_info)
        if form.is_valid():
            
            Pet_diet_info = form.save(commit=False)
            Pet_diet_info.pet_name = pet_info
            Pet_diet_info.pet_needKcal = DER(Pet_diet_info.pet_weight, Pet_diet_info.pet_status)
            Pet_diet_info.save()   
            return redirect("App_Main:pet_diet_info")
    else:
        form = PetdietForm(instance = pet_diet_info) # -> unboundForm

    context = {'pet_diet_set':pet_diet_info,'pet_info' : pet_info, 'form': form}
    return render(request, 'Pet_diet_set.html', context)

