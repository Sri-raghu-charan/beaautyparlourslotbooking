from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('about/',views.aboutus,name='aboutus'),
    path('contact/',views.contactus,name='contactus')
]



