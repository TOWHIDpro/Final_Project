from django.shortcuts import render, redirect
from . import calculator_func
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from . models import Healthdata

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        user = User.objects.all().last()
        name = f"user{user.id+1}"
        usr = User.objects.create(username=name)
        login(request, usr)

    # after clicking submit button this run
    if request.method == 'POST':
        # Retriv data from html form
        age = request.POST.get('age')
        systolicbp = request.POST.get('systolicbp')
        diastolicbp = request.POST.get('diastolicbp')
        bs = request.POST.get('bs')
        heartRate = request.POST.get('heartRate')

        # Result
        all_data = [age, systolicbp, diastolicbp, bs, heartRate]
        k = calculator_func.Forest.predict([all_data])
        if(k==2):
            message = "You are in High Risk"
        elif(k==1):
            message = 'You are in Mid Risk'
        else:
            message = "You are in Low Risk"

        # Save to database
        Healthdata.objects.create(
            user=request.user,
            age=age,
            systolicbp=systolicbp,
            diastolicbp=diastolicbp,
            bs=bs,
            heartRate=heartRate,
            message=message
            )
        return redirect('result')
    return render(request, 'index/index.html')


def result(request):
    data = Healthdata.objects.filter(user=request.user).last()
    return render(request, 'index/result.html', {
        'data': data  
    })

def all_result(request):
    data = Healthdata.objects.filter(user=request.user).all()
    return render(request, 'index/all_result.html', {
        'data': data  
    })


def create_user(request):
    return render(request, 'index/create_user.html')

def usr_login(request):
    if request.method == 'POST':
        userid = (request.POST.get('userid')).lower()
        try:
            usr = User.objects.get(username=userid)
            login(request, usr)
            return redirect('index')
        except:
            pass
        return render(request, 'index/login.html')

    if request.method == 'GET':
        return render(request, 'index/login.html')