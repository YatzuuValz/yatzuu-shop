from django.urls import path
from main import views



app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('create-product/', views.create_product, name='create_product'),
    path('product/<str:id>/', views.show_product, name='show_product'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<str:product_id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', views.show_json_by_id, name='show_json_by_id'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('product/<uuid:id>/edit', views.edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', views.delete_product, name='delete_product'),
    path('create-product-ajax', views.add_product_entry_ajax, name='add_product_entry_ajax'),
    path('ajax-login/', views.ajax_login, name='ajax_login'),
    path('ajax-register/', views.ajax_register, name='ajax_register'),
    path('proxy-image/', views.proxy_image, name='proxy_image'),
    path('create-product-flutter/', views.create_product_flutter, name='create_product_flutter'),
]