from django.shortcuts import render

# Create your views here.
def login_accounts(request):
    return render(request,'accounts/login.html')
def profile_accounts(request):
    return render(request,'accounts/profile.html')
def register_accounts(request):
    return render(request,'accountsregister.html')