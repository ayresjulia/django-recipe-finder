from django.contrib import admin
from .models import Customer

# TEST-admin username: 'admin', password: 'password'

admin.site.register(Customer)
