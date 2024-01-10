from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Brand(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Gadget(BaseModel):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    release_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='gadget_images/')

    def __str__(self):
        return self.name

class Specification(BaseModel):
    gadget = models.ForeignKey(Gadget, on_delete=models.CASCADE)
    key = models.TextField()
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.gadget.name} - {self.key}: {self.value}"

class User(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    favorite_gadgets = models.ManyToManyField(Gadget)

    def __str__(self):
        return self.name