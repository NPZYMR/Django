from multiprocessing import context
from pyexpat import features
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def index(request):

    features = Feature.objects.all()
    return render(request,'index.html', {'features' : features})
    # feature1 =Feature()
    # feature1.id = 0
    # feature1.name = 'Fast'
    # feature1.is_true = 'True'
    # feature1.details = 'Our serive is very quick'

    # feature2 =Feature()
    # feature2.id = 1
    # feature2.name = 'affordadble'
    # feature2.is_true = 'True'
    # feature2.details = 'Our serive is economical.'

    # feature3 =Feature()
    # feature3.id = 2
    # feature3.name = 'comm'
    # feature3.is_true = 'False'
    # feature3.details = 'Our serive is economical.'

    # feature4 =Feature()
    # feature4.id = 3
    # feature4.name = 'low'
    # feature4.is_true = 'True'
    # feature4.details = 'Our serive is economical.'

    # features = [feature1,feature2,feature3,feature4]
   # name = 'Naveen'   basic example
#    context= {
#        'name' : 'Naveen',
#        'nationality' : 'Indian'
#    }
#    return render(request, 'index.html', context)
    



def counter(request):
    text = request.POST['text'] 
    amount_of_words= len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})



def register(request):

    if request.method == 'POST':


        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in use.')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Exists. ')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email, password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request, 'Password not same.')
            return redirect('register')
    
    else:
        return render(request, 'register.html')


def login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user= auth.authenticate(username=username, password=password)

        if user is not None:
            
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Not Valid.')
            return redirect('login')
    else:
        return render(request,'login.html')

