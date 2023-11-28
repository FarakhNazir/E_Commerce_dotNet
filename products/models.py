from django.db import models

# Create your models here.
from base.models  import BaseModel
from django.utils.text import slugify

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to="categories")
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category , self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.category_name
        
    
class ColorVariant(BaseModel):
        color_name = models.CharField(max_length=100)
        price = models.IntegerField(default=0)
        
        def __str__(self) -> str:
             return self.color_name
    
class SizeVariant(BaseModel):
        size_name = models.CharField(max_length=100)
        price = models.IntegerField(default=0)
        
        def __str__(self) -> str:
             return self.size_name

    
class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.IntegerField()
    product_description = models.TextField()
    color_variant = models.ManyToManyField(ColorVariant , blank = True)
    size_variant = models.ManyToManyField(SizeVariant, blank = True)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product , self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.product_name
    
    def get_product_price_by_size(self, size):
        #return self.size + SizeVariant.objects.get(size_name = size)   
        product_size = SizeVariant.objects.get(size_name = size)  
        price = product_size.price 
        return price 
    
    
class ProductImage(BaseModel):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to= "product")
    
