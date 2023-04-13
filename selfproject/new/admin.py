from django.contrib import admin

# Register your models here.

from new.models import Country, State, District


admin.site.register(Country)
admin.site.register(State)
admin.site.register(District)
