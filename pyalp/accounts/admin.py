from django.contrib import admin

# Register your models here.
from .models import UserMetadata, ComputerSpecification

admin.site.register([
    UserMetadata,
    ComputerSpecification
])
