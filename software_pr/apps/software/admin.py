from django.contrib import admin

from .models import *
admin.site.register(Software)
admin.site.register(Addition)
# admin.site.register(Software_Classification_Value)
admin.site.register(Classification_Value)
admin.site.register(Classification)
# admin.site.register(tag_softwares)
admin.site.register(Tag)