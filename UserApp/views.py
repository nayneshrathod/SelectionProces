from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from UserApp.models import *


# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs

# sys.setrecursionlimit(10 ** 6)

# Create your views here.
def index(request):
    context = {"title": "Base Page"}
    return render(request, 'base.html', context)


def home(request):
    context = {"title": "This Is A HOME PAGE"}
    return render(request, 'Index.html', context)


'''
def Use_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['usernm']
        password1 = request.POST['pwd1']
        usr = User.objects.get(username=username, password=password1)
        if usr:
            login(request, usr)
            # return redirect('/home/')
            return HttpResponseRedirect(reverse('usr_login'))
        else:
            context["error"] = "Provide Valid Data"
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', context)
    # return render(request, 'login.html', context)

'''


def Use_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['usernm']
        password1 = request.POST['pwd1']
        user = authenticate(request, username=username, password=password1)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
            # return HttpResponseRedirect('/main/')
            # login(request, user)
            # return redirect('/home/')
            # return HttpResponseRedirect(reverse('home'))
        else:
            context["error"] = "Provide Valid Data"
            return render(request, 'login.html', context)

    else:
        return render(request, 'login.html', context)


# return render(request, 'login.html', context)


def uslogout(request):
    if request.method == 'POST':
        logout(request)
    return HttpResponseRedirect(reverse('usr_login'))
    # return render(request, 'logout.html')


def register(request):
    context = {}
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['emai']
        password1 = request.POST['pwd1']
        password2 = request.POST['pwd2']
        username = request.POST['usernm']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                context['error'] = {"msd": "Usr Alredry register"}
            elif User.objects.filter(email=email).exists():

                context['error'] = {"msd": "Email Alredy register"}
            else:
                user1 = User.objects.create(first_name=first_name, last_name=last_name,
                                            email=email,
                                            username=username,
                                            password=password1)
                user1.save()
                context['error'] = {"msd": "user crate"}
                return HttpResponseRedirect(reverse('usr_login'))
                # return HttpResponseRedirect('login')
        else:
            print("WRONG PASSWORD")

        return HttpResponseRedirect(reverse('usr_login'))
    return render(request, 'register.html', context)


def AAddpost(request):
    context = {}
    if request.method == 'POST':
        text = request.POST['comt']
        US = User.objects.filter(username=User).exists()
        if US:
            user1 = Post.objects.create(username=US, text=text)
            user1.save()
        # context['error'] = {"msd": "user crate"}
        return HttpResponseRedirect(reverse('adingpost'))
        # return HttpResponseRedirect('login')
    else:
        print("WRONG PASSWORD")

        # return HttpResponseRedirect(reverse('adingpost'))

        return render(request, 'addpost.html', context)

    # return render(request, 'addpost.html')


'''
#
def uslogin(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['usernm']
        password1 = request.POST['pwd1']
        user = authenticate(request, username=username, password=password1)
        if user:
            login(request, user)
            return redirect('usr_success')
            # return HttpResponseRedirect(reverse(''))
        else:
            context["error"] = "Provide Valid Data"
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', context)


def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'success.html', context)


def uslogout(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse('usr_login'))
    # return render(request, 'logout.html')
 

def login(request):
    if request.method == 'POST':
        username = request.POST['usernm']
        password1 = request.POST['pwd1']
        usr = auth.authenticate(username=username, password=password1)
        if usr is not None:
            auth.login(request, usr)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    context = {}
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['emai']
        password1 = request.POST['pwd1']
        password2 = request.POST['pwd2']
        username = request.POST['usernm']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                context = {"msd": "Usr Alredry register"}
            elif User.objects.filter(email=email).exists():

                context = {"msd": "Email Alredy register"}
            else:
                user1 = User.objects.create(first_name=first_name, last_name=last_name,
                                            email=email,
                                            username_id=username,
                                            password=password1)
                user1.save()
                context = {"msd": "user crate"}
                return HttpResponseRedirect('login')
        else:
            print("WRONG PASSWORD")

        return HttpResponseRedirect('/')
    return render(request, 'register.html', context)
 

#
'''


def addpost(request):
    context = {}
    if request.method == 'POST':
        text = request.Post['comt']
        new = Post(text=text, user=request.user)
        new.save()
        return render(request, 'addpost.html', context)
    else:
        return render(request, 'addpost.html', context)
