from django.contrib import admin
from .models import BaseModel, Brand, Category, Gadget, Specification, User

# Register your models here.
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Gadget)
admin.site.register(Specification)
admin.site.register(User)
