from django.shortcuts import render
from rest_framework import generics
from .models import user,user_contact_details,Appointment,Payment
from . serializers import UserSerializer,UserContactDetailsSerializer,AppointmentSerializer,PaymentSerializer
# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset=user.objects.all()
    serializer_class = UserSerializer

class UserDetailviews(generics.RetrieveAPIView):
    queryset=user.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

class UserListViews(generics.ListAPIView):
    queryset=user.objects.all()
    serializer_class = UserSerializer

class UserUpdateViews(generics.UpdateAPIView):
    queryset=user.objects.all()
    serializer_class=UserSerializer
    lookup_field = 'pk'

class UserRemoveView(generics.DestroyAPIView):
    queryset=user.objects.all()
    serializer_class=UserSerializer
    lookup_field = 'pk'



# User Contact details view
class CreateUserContactDetailsView(generics.ListCreateAPIView):
    queryset = user_contact_details.objects.all()
    serializer_class = UserContactDetailsSerializer


class UserContactDetailsView(generics.RetrieveAPIView):
    queryset = user_contact_details.objects.all()
    serializer_class = UserContactDetailsSerializer
    lookup_field = 'pk'


class CrateAppointment(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


# payment view (end point)
class ListCreatePaymentView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer