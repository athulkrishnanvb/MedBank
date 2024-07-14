from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# class Master(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()

#     def __str__(self):
#         return self.name

class Bloodrequest(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    # master = models.ForeignKey(Master, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    patient_age = models.IntegerField()
    reason = models.TextField()
    bloodgroup = models.CharField(max_length=10)
    quantity_ml = models.IntegerField()
    request_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.patient_name} - {self.bloodgroup} - {self.status}"
    
class BloodDonation(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    # master = models.ForeignKey(Master, on_delete=models.CASCADE)
    donor_name = models.CharField(max_length=100)
    donor_age = models.PositiveIntegerField()
    blood_group = models.CharField(max_length=10)
    quantity_ml = models.PositiveIntegerField()
    donation_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.donor_name} - {self.blood_group} - {self.status}"
    
class MedicalProduct(models.Model):
    # master = models.ForeignKey(Master, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='med_photos/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    posted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Booking(models.Model):
    PAYMENT_METHODS = [
        ('COD','Cash on Delivery'),
        ('CARD', 'Debit/Credit Card'),
        ('UPI', 'UPI Payment')
    ]
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Canceled', 'Canceled'),
        ('Completed', 'Completed')
    ]

    product = models.ForeignKey(MedicalProduct, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    address = models.TextField()
    booked_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')


    def __str__(self):
        return f"{self.product.name} - {self.user.username} - {self.status}"
    
