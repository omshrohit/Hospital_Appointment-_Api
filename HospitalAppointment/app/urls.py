from django.contrib import admin
from django.urls import path
from . views import  CreateUserView,UserDetailviews,UserListViews,UserUpdateViews,UserRemoveView
from . views import CreateUserContactDetailsView,UserContactDetailsView ,CrateAppointment,ListCreatePaymentView
urlpatterns = [
    path("", CreateUserView.as_view(),name="create-user"),
    path("users/",UserListViews.as_view(),name="users"),
    path("users/<int:pk>/",UserDetailviews.as_view(),name="user-details"),
    path("users/update/<int:pk>/",UserUpdateViews.as_view(),name='update-user'),
    path("users/remove/<int:pk>/",UserRemoveView.as_view(),name='remove-user'),
    # user contact details urls
    path('users/create-contact-details/',CreateUserContactDetailsView.as_view(),name='create-contact-detail'),
    path('users/create/appointment/',CrateAppointment.as_view(),name="create-appointment"),
    path('users/payment/',ListCreatePaymentView.as_view(),name='payment-list-create')
    
]
