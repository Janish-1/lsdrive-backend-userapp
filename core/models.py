from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUsers(AbstractUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=20)
    address = models.TextField(null=True, blank=True)
    eligible = models.BooleanField(default=False , null=True, blank=True)
    available = models.BooleanField(default=False , null=True, blank=True)
    updated = models.BooleanField(default=False , null=True, blank=True)
    gender = models.CharField(max_length=10,  blank=True, null=True)
    adhaar_id = models.CharField(max_length=12, unique=True, null=True, blank=True)
    driving_id = models.CharField(max_length=30, unique=True, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    loaction_address = models.TextField(max_length=300 )
    location = models.OneToOneField('PDLocation', on_delete=models.CASCADE, null=True, blank=True)
    people_count = models.IntegerField(null=True, blank=True)
    pickup_time = models.CharField(max_length=30,null=True, blank=True)
    def __str__(self):
        return self.full_name
class PDLocation(models.Model):
    user = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)
    pickup_latitude = models.DecimalField(max_digits=50, decimal_places=16)
    drop_latitude = models.DecimalField(max_digits=50, decimal_places=16)
    pickup_longitude = models.DecimalField(max_digits=50, decimal_places=16)
    drop_longitude = models.DecimalField(max_digits=50, decimal_places=16)
    drop_address = models.TextField()
    pickup_address = models.TextField()
# class DropLocation(models.Model):
    # user = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)
    # latitude = models.DecimalField(max_digits=50, decimal_places=16)
    # longitude = models.DecimalField(max_digits=50, decimal_places=16)
# class PickupLocation(models.Model):
#     user = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)
#     latitude = models.DecimalField(max_digits=50, decimal_places=16)
#     longitude = models.DecimalField(max_digits=50, decimal_places=16)
    


    # def __str__(self):
    #     return self.user
# @receiver(post_save, sender=AbstractUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         CustomUsers.objects.create(user=instance)

# @receiver(post_save, sender=AbstractUser)
# def save_user_profile(sender, instance, **kwargs):
#     try:
#         instance.userprofile.save()
#     except CustomUsers.DoesNotExist:
#         pass
class OTP(models.Model):
    user = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.otp}'