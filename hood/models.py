from django.db import models
from django.core.validators import URLValidator
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Hood(models.Model):
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    occupants_count = models.PositiveIntegerField(choices=list(zip(range(0,50), range(0,50))),default=0)

    def __str__(self):
        return self.name

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    def update_hood(self,location):
        self.location = location
        self.save()

    def update_hood(self,occupants_count):
        self.occupants_count = occupants_count
        self.save()

    @classmethod
    def get_all(cls):
        hoods = cls.objects.all()
        return hood

    @classmethod
    def get_hood(cls, hood_id):
        project = cls.objects.get(id=hood_id)
        return hood

class User(models.Model):
    user_image = models.ImageField(upload_to = 'profile_pic/',null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True,related_name = 'user')
    hood = models.ForeignKey(Hood,on_delete=models.CASCADE, null=True)
    user_email = models.EmailField()
    
    def __str__(self):
        return self.user_email

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()

    def update_user(self,hood):
        self.hood = hood
        self.save()

    

# class Business(models.Model):
#     business_image = models.ImageField(upload_to = 'business/', null=True)
#     business_name = models.CharField(max_length = 50)
#     user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
#     hood = models.ForeignKey(Hood,on_delete=models.CASCADE, null=True)
#     business_email = models.EmailField()

#     def __str__(self):
#         return self.business_name

#     def save_business(self):
#         self.save()

#     def delete_business(self):
#         self.delete()

#     def update_business(self,business_name):
#         self.business_name = business_name
#         self.save()

#     @classmethod
#     def get_all(cls):
#         business = cls.objects.all()
#         return business

#     @classmethod
#     def get_business(cls, business_id):
#         business = cls.objects.get(id=business_id)
#         return business

#     @classmethod
#     def search_by_title(cls,search_term):
#         business = cls.objects.filter(business_name__icontains=search_term)
#         return business

# class Post(models.Model):
#     post_image = models.ImageField(upload_to = 'post/', null=True)
#     title = models.CharField(max_length = 50, null = True)
#     description = models.TextField(max_length = 500,null=True)
#     writer= models.ForeignKey(User,on_delete=models.CASCADE,null = True)

#     def save_post(self):
#         self.save()

#     def delete_post(self):
#         self.delete()

#     @classmethod
#     def get_all(cls):
#         post = cls.objects.all()
#         return post

#     @classmethod
#     def get_post(cls, post_id):
#         post = cls.objects.get(id=post_id)
#         return post

# class Health(models.Model):
#     contact_name = models.CharField(max_length=30)
#     contacts = models.PositiveIntegerField()
#     hospital = models.CharField(max_length = 50)
#     neighborhood_contact = models.ForeignKey('Hood',on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.contact_name}'

#     def save_health(self):
#         self.save()

#     def delete_health(self):
#         self.delete()

#     @classmethod
#     def get_all(cls):
#         health = cls.objects.all()
#         return health

# class Police(models.Model):
#     Station = models.CharField(max_length=30)
#     contacts = models.PositiveIntegerField()
#     neighborhood_contact = models.ForeignKey('Hood',on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.Station}'

#     def save_police(self):
#         self.save()

#     def delete_police(self):
#         self.delete()

#     @classmethod
#     def get_all(cls):
#         police = cls.objects.all()
#         return police