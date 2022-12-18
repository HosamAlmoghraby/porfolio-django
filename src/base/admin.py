from django.contrib import admin
from .models import SiteSetting, Social, Icon, Currency


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    filter_horizontal = ('social_on_header',)
    

admin.site.register(Social)
admin.site.register(Icon)
admin.site.register(Currency)
