from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import *

def home(request):
    return render(request, 'users/dashboard.html')

def users(request):
    users=Users.objects.all()
    return render(request, 'users/users.html',{'users':users})


def country(request):
    countries=Country.objects.all()
    return render(request,'users/country.html',{'countries':countries})

def disease_type(request):
    disease_type=Diseasetype.objects.all()
    return render(request,'users/disease_type.html',{'disease_type':disease_type})


def disease(request):
    disease=Disease.objects.all()
    return render(request,'users/disease.html',{'disease':disease})

def discover(request):
    discover=Discover.objects.all()
    return render(request,'users/discover.html',{'discover':discover})

def doctor(request):
    doctor=Doctor.objects.all()
    return render(request,'users/doctor.html',{'doctor':doctor})

def public_servant(request):
    public_servant=PublicServant.objects.all()
    return render(request,'users/public_servant.html',{'public_servant':public_servant})

def records(request):
    records=Record.objects.all()
    return render(request,'users/records.html',{'records':records})

def specialize(request):
    specialize=Specialize.objects.all()
    return render(request,'users/specialize.html',{'specialize':specialize})

####################################################################
######################## CRUD OPERATIONS ###########################
####################################################################

#Country
def create_country(request):
    form=CountryForm()

    if request.method=='POST':
        #print('Printing request',request.POST)
        form=CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('country')
    context={'form':form}
    return render(request,'users/country_form.html',context)

def update_country(request,pk):
    country=Country.objects.get(cname=pk)
    form=CountryForm(instance=country)

    if request.method=='POST':
        form=CountryForm(request.POST,instance=country)
        if form.is_valid():
            form.save()
            return redirect('country')

    context={'form':form}
    return render(request,'users/country_form.html',context)

def delete_country(request,pk):
    country=Country.objects.get(cname=pk)
    if request.method=='POST':
        country.delete()
        return redirect('country')
    context={'item':country}
    return render(request,'users/delete_country.html',context)

#Disease type
def create_diseasetype(request):
    form=DiseaseTypeForm()

    if request.method=='POST':
        form=DiseaseTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disease_type')
    context={'form':form}
    return render(request,'users/diseasetype_form.html',context)

def update_diseasetype(request,pk):
    disease_type=Diseasetype.objects.get(id=pk)
    form=DiseaseTypeForm(instance=disease_type)

    if request.method=='POST':
        form=DiseaseTypeForm(request.POST,instance=disease_type)
        if form.is_valid():
            form.save()
            return redirect('disease_type')

    context={'form':form}
    return render(request,'users/diseasetype_form.html',context)

def delete_diseasetype(request,pk):
    disease_type=Diseasetype.objects.get(id=pk)
    if request.method=='POST':
        disease_type.delete()
        return redirect('disease_type')
    context={'item':disease_type}
    return render(request,'users/delete_diseasetype.html',context)

#Disease

def create_disease(request):
    form=DiseaseForm()

    if request.method=='POST':
        form=DiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disease')
    context={'form':form}
    return render(request,'users/disease_form.html',context)

def update_disease(request,pk):
    disease=Disease.objects.get(disease_code=pk)
    form=DiseaseForm(instance=disease)

    if request.method=='POST':
        form=DiseaseForm(request.POST,instance=disease)
        if form.is_valid():
            form.save()
            return redirect('disease')

    context={'form':form}
    return render(request,'users/disease_form.html',context)

def delete_disease(request,pk):
    disease=Disease.objects.get(disease_code=pk)
    if request.method=='POST':
        disease.delete()
        return redirect('disease')
    context={'item':disease}
    return render(request,'users/delete_disease.html',context)


#Discover

def create_discover(request):
    form=DiscoverForm()

    if request.method=='POST':
        form=DiscoverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discover')
    context={'form':form}
    return render(request,'users/discover_form.html',context)

def update_discover(request,pk):
    discover=Discover.objects.get(cname=pk)

    form=DiscoverForm(instance=discover)

    if request.method=='POST':
        form=DiscoverForm(request.POST,instance=discover)
        if form.is_valid():
            form.save()
            return redirect('discover')

    context={'form':form}
    return render(request,'users/discover_form.html',context)

def delete_discover(request,pk):
    discover=Discover.objects.get(cname=pk)
    if request.method=='POST':
        discover.delete()
        return redirect('discover')
    context={'item':discover}
    return render(request,'users/delete_discover.html',context)

#Doctor

def create_doctor(request):
    form=DoctorForm()

    if request.method=='POST':
        form=DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor')
    context={'form':form}
    return render(request,'users/doctor_form.html',context)

def update_doctor(request,pk):
    doctor=Doctor.objects.get(email=pk)

    form=DoctorForm(instance=doctor)

    if request.method=='POST':
        form=DoctorForm(request.POST,instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor')

    context={'form':form}
    return render(request,'users/doctor_form.html',context)

def delete_doctor(request,pk):
    doctor=Doctor.objects.get(email=pk)
    if request.method=='POST':
        doctor.delete()
        return redirect('doctor')
    context={'item':doctor}
    return render(request,'users/delete_doctor.html',context)

#Users

def create_user(request):
    form=UserForm()

    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    context={'form':form}
    return render(request,'users/user_form.html',context)

def update_user(request,pk):
    user=Users.objects.get(email=pk)

    form=UserForm(instance=user)

    if request.method=='POST':
        form=UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')

    context={'form':form}
    return render(request,'users/user_form.html',context)

def delete_user(request,pk):
    user=Users.objects.get(email=pk)
    if request.method=='POST':
        user.delete()
        return redirect('users')
    context={'item':user}
    return render(request,'users/delete_user.html',context)
    
#Public servant

def create_ps(request):
    form=PSForm()

    if request.method=='POST':
        form=PSForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('public_servant')
    context={'form':form}
    return render(request,'users/ps_form.html',context)

def update_ps(request,pk):
    ps=PublicServant.objects.get(email=pk)

    form=PSForm(instance=ps)

    if request.method=='POST':
        form=PSForm(request.POST,instance=ps)
        if form.is_valid():
            form.save()
            return redirect('public_servant')

    context={'form':form}
    return render(request,'users/ps_form.html',context)

def delete_ps(request,pk):
    ps=PublicServant.objects.get(email=pk)
    if request.method=='POST':
        ps.delete()
        return redirect('public_servant')
    context={'item':ps}
    return render(request,'users/delete_ps.html',context)
    

#Specialize
def create_spec(request):
    form=SpecForm()

    if request.method=='POST':
        form=SpecForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('specialize')
    context={'form':form}
    return render(request,'users/spec_form.html',context)

def update_spec(request,pk):
    spec=Specialize.objects.get(id=pk)

    form=SpecForm(instance=spec)

    if request.method=='POST':
        form=SpecForm(request.POST,instance=spec)
        if form.is_valid():
            form.save()
            return redirect('specialize')

    context={'form':form}
    return render(request,'users/spec_form.html',context)

def delete_spec(request,pk):
    spec=Specialize.objects.get(id=pk)
    if request.method=='POST':
        spec.delete()
        return redirect('specialize')
    context={'item':spec}
    return render(request,'users/delete_spec.html',context)
    
#Records
def create_rec(request):
    form=RecForm()

    if request.method=='POST':
        form=RecForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('records')
    context={'form':form}
    return render(request,'users/rec_form.html',context)

def update_rec(request,pk):
    rec=Record.objects.get(email=pk)

    form=RecForm(instance=rec)

    if request.method=='POST':
        form=RecForm(request.POST,instance=rec)
        if form.is_valid():
            form.save()
            return redirect('records')

    context={'form':form}
    return render(request,'users/rec_form.html',context)

def delete_rec(request,pk):
    rec=Record.objects.get(email=pk)
    if request.method=='POST':
        rec.delete()
        return redirect('records')
    context={'item':rec}
    return render(request,'users/delete_rec.html',context)