from django.shortcuts import render,  redirect, get_object_or_404
from django.http import HttpResponse
from .models import Customer
from .forms import RecipeForm
import requests
# Create your views here.
