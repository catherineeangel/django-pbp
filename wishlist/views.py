from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from wishlist.models import BarangWishlist

data_barang_wishlist = BarangWishlist.objects.all()
context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Catherine'
}
# Create your views here.
def show_wishlist(request):
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