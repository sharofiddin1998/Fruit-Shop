from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Categories)
admin.site.register(Sub_categories)
admin.site.register(Product)
admin.site.register(Filter_Price)
admin.site.register(Tag)