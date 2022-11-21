from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Country)
admin.site.register(Discover)
admin.site.register(Diseasetype)
admin.site.register(Disease)
admin.site.register(Record)
admin.site.register(Users)
admin.site.register(PublicServant)
admin.site.register(Doctor)
admin.site.register(Specialize)