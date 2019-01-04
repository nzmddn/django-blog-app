from django.shortcuts import render,HttpResponse,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages


# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None) #post olduğunda alttaki if durumuna geçer.
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username =username)
        newUser.set_password(password)

        newUser.save()
        login(request, newUser)
        messages.success(request, 'Başarıyla kaydoldunuz.')

        return redirect("index")
    
    context = {
            "form" : form
        }
    return render(request,"register.html",context)#is_valid olmadığında context yeniden gelecek.
    
    """form = RegisterForm()
    context={"form":form}
    return render(request,"register.html",context)"""

def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username= username,password=password) #kullanıcının varlığını sorgular. yoksa none döner.
        
        if user is None:
            messages.info(request,"Kullanıcı adı veya Parola Yanlış!")
            return render(request,"login.html",context)

        messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,user)
        
        return redirect("index")
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")

