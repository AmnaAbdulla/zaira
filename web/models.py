from django.db import models

class Featured(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    image = models.ImageField(upload_to="imagess",null=True,blank=True)
    price=models.FloatField(null=False,blank=False)


class Ethnic(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    image = models.ImageField(upload_to="imagess",null=True,blank=True)
    price=models.FloatField(null=False,blank=False)

class Western(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    image = models.ImageField(upload_to="imagess",null=True,blank=True)
    price=models.FloatField(null=False,blank=False)

class Party(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    image = models.ImageField(upload_to="imagess",null=True,blank=True)
    price=models.FloatField(null=False,blank=False)

class Paksthani(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    image = models.ImageField(upload_to="imagess",null=True,blank=True)
    price=models.FloatField(null=False,blank=False)

class Prayer(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    image = models.ImageField(upload_to="imagess",null=True,blank=True)
    price=models.FloatField(null=False,blank=False)

class Product(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    image = models.ImageField(upload_to="imagess",null=True,blank=True)
    price=models.FloatField(null=False,blank=False)



class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class CheckOut(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# class Product(models.Model):
#     filter_class = (
#         ('nature', 'nature'),
#         ('people', 'people'),
#         ('cars', 'cars'),
#         ('buildings', 'buildings'),
#     )
#     filter_class = models.CharField(max_length=40, choices=filter_class)
#     name = models.CharField(max_length=50)
#     price = models.FloatField()
#     image = models.ImageField(upload_to="")

#     def __str__(self):
#         return self.name

