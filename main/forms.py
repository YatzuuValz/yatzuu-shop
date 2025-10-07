from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags
# from main.Seller import Seller

class ProductForms(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "thumbnail","category","is_featured"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_content(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
# class SellerForms(ModelForm):
#     class Meta:
#         model = Seller
#         fields = ["name", "tanggallahir", "email", "notelp", "linksocmed","password"]