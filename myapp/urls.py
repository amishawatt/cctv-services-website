from django.urls import path
from.import views
urlpatterns=[
    path('',views.index),
    path('home/', views.index),
    path('regester/',views.reg),
    path('login/regester/',views.reg),
    path('login/forgot/',views.frogot),
    path('login/',views.log),
    path('login/contactus/',views.contact)

]