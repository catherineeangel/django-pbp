from django.urls import path
from wishlist.views import show_wishlist, show_wishlist_xml, show_wishlist_json, get_one_json, get_one_xml

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_wishlist_xml, name='show_wishlist_xml'), 
    path('xml/<int:id>', get_one_xml, name='get_one_xml'), 
    path('json/', show_wishlist_json, name='show_wishlist_json'), 
    path('json/<int:id>', get_one_json, name='get_one_json'), 
]