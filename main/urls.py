from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.ContactCreateView.as_view(), name='homepage'),
    path('contact/', views.contact_thanks, name='contact')

]