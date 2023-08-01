from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from app_menus.forms import CategoryCreateForm, MenuCreateForm
from app_menus.models import Menu, Category
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.

@login_required(login_url='/login/')
@csrf_protect

def list_menu(request):
    menu_list = Menu.objects.all()
    paginator = Paginator(menu_list,4) # 4 date in one page
    page_number= request.GET.get("page")
    page_obj= paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, 'menus/list_menu.html', context)

@login_required(login_url='/login/')
@csrf_protect
def show_menu(request, id):
    menu_obj = Menu.objects.get(id=id)
    context= {"data": menu_obj}
    return render(request, 'menus/show_menu.html', context)

@login_required(login_url='/login/')
@csrf_protect
def edit_menu(request, id):
    menu_obj = Menu.objects.get(id=id)
   
    category_obj= Category.objects.all()
    
    context= {"data": menu_obj, "categories":category_obj}
    
    # to update
    if request.method == "POST":
        menu_obj = MenuCreateForm(data=request.POST, instance=menu_obj, files=request.FILES)
        if menu_obj.is_valid():
            menu_obj.save()
            return redirect("menu-edit", id) #redirecting to url having id
    
    return render(request, 'menus/edit_menu.html', context)

@login_required(login_url='/login/')
@csrf_protect
def delete_menu(request, id):
    menu_obj= Menu.objects.get(id=id)
    menu_obj.delete()
    return redirect ('menu-list')

@login_required(login_url='/login/')
@csrf_protect
def add_menu(request):
    menu_create_form = MenuCreateForm() #creating Form Class object
    context= {"menu_create_form": menu_create_form, "title": "Create Menu Here.."}
    
    if request.method =="POST":
        menu_title = request.POST.get('menu_title')
        menu_price = request.POST.get('menu_price')
        menu_ingredient = request.POST.get('menu_ingredient')
      
        Category_obj = Category.objects.get(id=request.POST.get('menu_category'))
        
        #method 1
        # menu_obj = Menu()
        # menu_obj.menu_title =menu_title
        # menu_obj.menu_price =menu_price
        # menu_obj.menu_category = Category_obj  #passing category object (foreign key objcet)
        # menu_ingredient = menu_ingredient
        # menu_obj.save()
        
        # method 2
        
        # menu =Menu(menu_title = menu_title, menu_price=menu_price, menu_category=Category_obj, menu_ingredient=menu_ingredient)
        # menu.save()
        
        # method 3  - storing data with form class object
        menu = MenuCreateForm(request.POST, request.FILES)
        if menu.is_valid():
            menu.menu_category = Category_obj
            menu.save()
            return redirect("menu-list")
        return redirect("menu-add")

    return render(request, 'menus/add_menu.html', context)

# def show_menu(request):

#     return render(request, 'menus/show_menu.html')
