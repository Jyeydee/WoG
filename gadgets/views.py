from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Brand, Category, Gadget, Specification, User
# Create your views here.


def home(request):
    return render(request, 'home.html', {})

def brand_view(request):
    all_brand = Brand.objects.all()
    p = Paginator(all_brand, 5)
    page = request.GET.get('page')
    brand_list = p.get_page(page)
    return render(request, 'brand.html', {'brand': brand_list})

def category_view(request):
    all_category = Category.objects.all()
    p = Paginator(all_category, 4)
    page = request.GET.get('page')
    category_list = p.get_page(page)
    return render(request, 'category.html', {'category': category_list})

def gadget_view(request):
    all_gadget = Gadget.objects.all()
    p = Paginator(all_gadget, 4)
    page = request.GET.get('page')
    gadget_list = p.get_page(page)
    return render(request, 'gadget.html', {'gadget': gadget_list})

def specification_view(request):
    all_specs = Specification.objects.all()
    p = Paginator(all_specs, 5)
    page = request.GET.get('page')
    specification_list = p.get_page(page)
    return render(request, 'specification.html', {'specification': specification_list})

def user_view(request):
    all_user = User.objects.all()
    p = Paginator(all_user, 5)
    page = request.GET.get('page')
    user_list = p.get_page(page)
    return render(request, 'user.html', {'user': user_list})
