from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from .forms import SignUp,EditProfileForm,MessageForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.core.mail import EmailMultiAlternatives
from django.template import loader, Context
from .models import Friend_request

# Create your views here.
def regi(request):
    if request.method=="POST":
        data_dict = {'is_staff':True}
        fm = SignUp(request.POST)
        if fm.is_valid():
            # username = fm.cleaned_data['first_name']
            # password = fm.cleaned_data['last_name']
            # staff=f.cleaned_data['is_data']
            # print(username+password)
            user= fm.save(commit=False)
            user.is_active=True
            user.is_staff=True
            user.save()
            # fm.save()
            messages.add_message(request, messages.SUCCESS, "yoUR ACCOUNT HAS BEEN CREATED")

    else:
        fm = SignUp()
    return render(request, 'enroll/user.html',{'form':fm})

def user_login(request):
    print("i am here ")
    if not request.user.is_authenticated:
        print("i am where ")
        
        if request.method == "POST":
            fm=AuthenticationForm(request,data=request.POST)
            print(fm)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user= authenticate(username=username, password=password)
                print("i am there ")
                print(user)
                print(username+password)
                if user is not None:
                    login(request,user)
                    print('here ther whwerew')
                    messages.add_message(request, messages.SUCCESS, "yoUR ACCOUNT HAS BEEN loggin Sucessfully")
                    return HttpResponseRedirect("/show/profile/")
        else:
            fm=AuthenticationForm()
        return render(request,'enroll/newuser.html',{'form':fm})
    else:
        return HttpResponseRedirect("/show/profile/")


def user_profile(request):
    # user = User.objects.get(id=request.user.id)
    if request.user.is_authenticated:
        if request.method=="POST":
            # user_profile = User.objects.get(user=request.user)
            fm=EditProfileForm(instance=request.user,data=request.POST)
            if fm.is_valid():

                fm.save()
            return render(request,'enroll/profile.html',{'name':request.user,'fm':fm})


        else:
            fm=EditProfileForm(instance=request.user)
            print(fm)
            # allusers=User.objects.exclude(id=request.user.id)
            # fr= Friend_request.objects.filter(to_user=request.user)
            return render(request,'enroll/profile.html',{'name':request.user,'fm':fm})
    else:
        return HttpResponseRedirect("/show/user_login/")
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/show/data/")

def changepass(request):
    if  request.user.is_authenticated:
        if request.method=="POST":
            
                fm = PasswordChangeForm(user=request.user,data=request.POST)
                if fm.is_valid():
                    fm.save()
                    update_session_auth_hash(request,fm.user)
                    return HttpResponseRedirect("/show/profile/")
        else:
            fm = PasswordChangeForm(user=request.user)
            
        return render(request,"enroll/changepass.html",{'fm':fm})
    else:
        return HttpResponseRedirect("/show/user_login/")

def setcookie(request):
    response = render(request , "enroll/setcookie.html")
    response.set_cookie('name','DHannu')
    return response

def getcookie(request):
    name = request.COOKIES.get('name',"Dummy data")
    return render(request,"enroll/getcookie.html",{'cook':name},max_age=6)

def delcookie(request):
    response = render(request , "enroll/delcookie.html")
    response.delete_cookie('name')
    return response



def user_mail(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            print(request.user.id)
            pi=request.user.id
            myuser = User.objects.get(pk=pi)
            fm=MessageForm(request.POST,instance=myuser)
            if fm.is_valid():
                email = fm.cleaned_data['message']
                user = fm.cleaned_data['email']
                fm.save()
                print('--------------------------------------------------------------------------')
                print(email+user)
                print(type(email))
                print(type(user))
                
                subject, from_email, to = email, user, 'ashubajpai161@gmail.com'
                variables = {'user': user,'email': email}
                text_content = 'This is an important message .'
                html_content = loader.get_template('enroll/maildata.html').render(variables,request=request)
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                messages.add_message(request, messages.SUCCESS, " Your mail has been sent succesfully!!!! ")
                return HttpResponseRedirect('/show/profile/')
        else:
            print(request.user.id)
            pi=request.user.id
            myuser = User.objects.get(pk=pi)
            fm=MessageForm(instance=myuser)
        return render(request,'enroll/mail.html',{'form':fm})
    else:
        return HttpResponseRedirect("/show/user_login/")


def send_friend_request(request,requestid):
    print('---------------------------------------------------------------------------')
    print(requestid)
    from_user = User.objects.get(id=request.user.id)
    print(from_user)
    print('---------------------------------------------------------------------------')
    to_user = User.objects.get(id=requestid)
    print(to_user)
    friends_request= Friend_request.objects.get_or_create(id=request.user.id,from_user=from_user,to_user=to_user)
    print('---------------------------------------------------------------------------')
    print(friends_request)
    print('---------------------------------------------------------------------------')
    return HttpResponseRedirect('/show/profile/')

def accept_friend_request(request,requestid):
    friend_request= Friend_request.objects.get(id=requestid)
    friend_request.to_user.friends.add(friend_request.from_user)
    friend_request.from_user.friends.add(friend_request.to_user)
    user1=request.user
    user2=friend_request.user.from_user
    user1.friends.add(user2)
    user2.friends.add(user1)
    return HttpResponseRedirect('/show/profile/')

def all_users(request):
    stu=Friend_request.objects.filter(to_user=request.user)
    return render(request,"enroll/users.html",{'stu':stu})
