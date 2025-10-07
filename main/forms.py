from django.forms import ModelForm
from main.models import Product
from main.Seller import Seller

class ProductForms(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "thumbnail","category","is_featured"]
class SellerForms(ModelForm):
    class Meta:
        model = Seller
        fields = ["Nama", "tanggallahir", "email", "notelp", "linksocmed","password"]