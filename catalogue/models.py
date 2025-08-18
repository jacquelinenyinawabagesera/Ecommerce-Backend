from django.db import models
# class Category(models.Model):
#     name = models.CharField(max_length=28)
#     def __str__(self):
#         return self.name
# class Tag(models.Model):
#     name = models.CharField(max_length=28)
#     def __str__(self):
#         return self.name
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveBigIntegerField()
    # category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.PROTECT)
    # tags = models.ManyToManyField('Tag', blank=True)
    def __str__(self):
        return f"{self.name}, price {self.price}"
class Subscription(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name