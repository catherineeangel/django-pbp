import datetime
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.shortcuts import render, redirect
from wishlist.models import BarangWishlist
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

data_barang_wishlist = BarangWishlist.objects.all()
# Create your views here.
@login_required(login_url='/wishlist/login/')
def show_wishlist(request):
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Catherine',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "wishlist.html", context)

def show_wishlist_xml(request):
    return HttpResponse(serializers.serialize("xml", data_barang_wishlist), content_type="application/xml")

def show_wishlist_json(request):
    return HttpResponse(serializers.serialize("json", data_barang_wishlist), content_type="application/json")

def get_one_xml(request, id):
    data_satu_barang = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_satu_barang), content_type="application/xml")

def get_one_json(request, id):
    data_satu_barang = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_satu_barang), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('wishlist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("wishlist:show_wishlist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('wishlist:login'))
    response.delete_cookie('last_login')
    return response