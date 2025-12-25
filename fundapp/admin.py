from django.contrib import admin
from .models import userdetails, userdonation,cretecampaign
# Register your models here.


admin.site.register(userdetails)
admin.site.register(userdonation)
admin.site.register(cretecampaign)