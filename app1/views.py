from django.shortcuts import render,redirect,HttpResponse
from .models import House
from .forms import HouseForm,UserForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def display_all(request):
    data=House.objects.all()
    print(data)
    return render(request,'home.html',{'data':data})

def create_user(request):
    print(request.user)
    f=UserForm()
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('app1:home')
        else:
            return HttpResponse('Duplicated User')
    return render(request,'sign_up_form.html',{'form':f})

@login_required
def edit_house(request, id):
    house = House.objects.get(id=id)



    
    if request.method == 'POST':
        form = HouseForm(request.POST, request.FILES, instance=house)
        if form.is_valid():
            form.save()
            return redirect('app1:home')
        # When form is invalid, we need to render the template with the form
        return render(request, 'edit_house.html', {'form': form})
    else:
        form = HouseForm(instance=house)
        return render(request, 'edit_house.html', {'form': form})

@login_required
def logout_user(request):
    logout(request)
    return redirect('app1:home')

def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user=user)
            return redirect('app1:home')
        else:
            return HttpResponse('The username or password is incorrect..!')
    return render(request,'login_form.html')

@login_required
def forms(request):
    print(request.user)
    f=HouseForm()
    if request.method=='POST':
        data=request.POST
        data1=request.FILES
        form=HouseForm(data,data1)
        if form.is_valid():
            purchasing_date=data.get('purchasing_date') if data.get('purchasing_date') else None 
            registration_time=data.get('registration_time') if data.get('purchasing_date') else None
            ready_to_sale=True if data.get('ready_to_sale')=='on' else False
            name=data.get('name')
            owner_mail=data.get('owner_mail')
            price=data.get('price')
            no_of_bedrooms=data.get('no_of_bedrooms')
            description=data.get('description')
            location=data.get('location')
            image=data1.get('image')
            House.objects.create(ready_to_sale=ready_to_sale,name=name,owner_mail=owner_mail,price=price,no_of_bedrooms=no_of_bedrooms,description=description,location=location,purchasing_date=purchasing_date,registration_time=registration_time,image=image)
            return redirect('app1:home')
        else:
            return HttpResponse("The data is duplicate")
    return render(request,'forms.html',{'form':f})

@login_required
def delete_all(request):
    all_=House.objects.all()
    for one in all_:
        one.delete()
    return HttpResponse("all are deleted")

def contact(request):
    return render(request,'contact.html')

def info(request,id):
    if id==1:
        data={
            'name':'vamshi',
            'age':22,
            'sex':'male'
        }
    elif id==2:
        data={
            'name':'varun',
            'age':25,
            'sex':'male'
        }
    else:
        data={
            'name':'unknown',
            'age':None,
            'sex':'Unknown'
        }
    return render(request,'info.html',{'data':data})

def house_detail(request,id):
    house=House.objects.get(id=id)
    return render(request,'house_detail.html',{'house':house})

@login_required
def delete_one(request):
    if request.method=='POST':
        house_name=request.POST.get('house_name')
        print(house_name)
        house=House.objects.get(name__iexact=house_name)
        house.delete()
        return HttpResponse('House is deleted')
    return render(request,'delete_one.html')