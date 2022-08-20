from django.db import models
from django.utils import timezone

# Create your models here.

class Categories(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Sub_categories(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Filter_Price(models.Model):
    FILTER_PRICE=(
        ('5000 TO 20000','5000 TO 20000'),
        ('20000 TO 30000','20000 TO 30000'),
        ('30000 TO 40000','30000 TO 40000'),
        ('40000 TO 50000','40000 TO 50000'),
    )

    price=models.CharField(choices=FILTER_PRICE, max_length=60)

    def __str__(self):
        return self.price



class Product(models.Model):
    STOCK=(('Mavjud','Mavjud'),('Mavjud emas','Mavjud emas'))
    QUANT=(('kg','kg'),
    ('litr','litr'),
    ('pors','pors'),
    ('dona','dona')
    )
    image = models.ImageField(upload_to='Product_image/img')
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    information=models.TextField()
    stock=models.CharField(choices=STOCK, max_length=200)
    create_date=models.DateTimeField(default=timezone.now)
    quant=models.CharField(choices=QUANT, max_length=200,default=0)
    categories=models.ForeignKey(Categories,on_delete=models.CASCADE)
    sub_categories=models.ForeignKey(Sub_categories,on_delete=models.CASCADE)
    filter_price=models.ForeignKey(Filter_Price,on_delete=models.CASCADE)
 

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=200)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

