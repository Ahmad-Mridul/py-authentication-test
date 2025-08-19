from django.contrib import admin
from .models import Member
# Register your models here.

class AdminModel(admin.ModelAdmin):
    list_display = ('fname','lname','age')
    prepopulated_fields = {'slug':('fname','lname')}

admin.site.register(Member,AdminModel)