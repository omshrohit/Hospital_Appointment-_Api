from . models import user,user_contact_details,Appointment,Payment
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'



#user contact details serailizer

class UserContactDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_contact_details
        fields = '__all__'


# appointment
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

# payment serializer
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"