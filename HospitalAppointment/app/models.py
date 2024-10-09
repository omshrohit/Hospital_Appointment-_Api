from django.db import models

# Create your models here.
class user(models.Model):
    fisrt_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12,unique=True)

    def __str__(self):
        return str(self.fisrt_name) +" "+str(self.last_name)


    
class user_contact_details(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    address = models.TextField(max_length=100)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=6)

    def __str__(self):
        return str(self.user) + " " + str(self.city)

class Appointment(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    doctor_name = models.CharField(max_length=100)
    reason = models.CharField(max_length=200)

    def __str__(self):
        return str(self.user) + " " + str(self.appointment_date)

class Payment(models.Model):
    payment_status=[('success','success'),('cancle','cancle'),('pending','pending')]
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    amount=models.FloatField(max_length=6)
    status = models.CharField(max_length=10,choices=payment_status)
    
    def __str__(self):
        return str(self.user.fisrt_name) + " " + self.status