from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('thankyou/<int:id>/', views.recipe_list, name='thankyou')
]
