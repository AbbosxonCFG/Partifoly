from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

from account.models import User

class Category(models.Model):
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Banner(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to='banner/',null=True,blank=True)
    is_active = models.BooleanField(default=True)


    def __str__ (self):
        return self.title

class Book(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='book/',null=True,blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='book')
    raiting=models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.name

# class Shop(models.Model):
#     title=models.CharField(max_length=100)
#     category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='shop')
#     is_active = models.BooleanField(default=True)





class Course(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='course/',null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='course')
    price=models.DecimalField(max_digits=10,decimal_places=2)
    is_active=models.BooleanField(default=True)
    raiting=models.CharField(max_length=100,default=1,validators=[MaxLengthValidator(5), MinLengthValidator(1)])
    durations=models.IntegerField(default=10)
    lessons=models.IntegerField(default=10)
    certificate=models.CharField(max_length=100,choices=(
        ('yes','yes'),
        ('no','no')

    ))
    language=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title



class Courseplaylist(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='courseplaylist')
    title=models.CharField(max_length=100)
    type=models.CharField(max_length=32,blank=True,null=True,choices=(
        ('auido_class','audio_class'),
        ('live_class','live_class' ),
        ('recorded_class','recorded_class'),
    ))

    def __str__(self) -> str:
        return self.title




class Review(models.Model):
    feedback=models.CharField(max_length=255,blank=True,null=True)
    rating=models.CharField(max_length=100 ,default=1,validators=[MaxLengthValidator(5), MinLengthValidator(1)])
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='review')

    def __str__(self) -> str:
        return str(self.rating)





class Mentor(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='mentor')
    image=models.ImageField(upload_to='mentor/',blank=True,null=True)
    description=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE,related_name='mentor')

    def __str__(self) -> str:
        return self.user.first_name






class Payment(models.Model):
    title=models.CharField(max_length=100)
    type=models.CharField(max_length=100,choices=(
        ('0','basic_pack'),
        ('1','standart_pack'),
        ('2','premium_pack')
    ))
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)


    def __str__(self) -> str:
        return self.type



class Cart(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,blank=True,null=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='carts')































# class Register(models.Model):
#     title=models.CharField(max_length=100)
#     description=models.TextField()
#     image=models.ImageField(upload_to='register/')
#     is_active=models.BooleanField(default=True)



# class CareerInformation(models.Model):
#     title=models.CharField(max_length=100)
#     description=models.TextField()
#     image=models.ImageField(upload_to='career/')
#     is_active=models.BooleanField(default=True)




# class Subscribe(models.Model):
#     title=models.CharField(max_length=100)
#     description=models.TextField()

    












