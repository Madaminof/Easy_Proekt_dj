from django.db import models

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=64)

    class Meta:
        db_table='category'

    def __str__(self) -> str:
        return self.name
    

class Product(models.Model):
    category=models.ForeignKey(to="Category",on_delete=models.CASCADE)
    brend=models.CharField(max_length=64)
    color=models.CharField(max_length=64)
    razmer=models.IntegerField()
    image=models.ImageField(upload_to="products/",blank=True,null=True)


    class Meta:
        db_table='products'

    def __str__(self) -> str:
        return f"{self.category.name}  {self.brend}"
        
