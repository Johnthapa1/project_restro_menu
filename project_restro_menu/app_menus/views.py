from django.shortcuts import render

# Create your views here.
def list_menu(request):
    return render(request, 'menus/list_menu.html')

def add_menu(request):
    return render(request, 'menus/add_menu.html')

def show_menu(request):
    return render(request, 'menus/show_menu.html')