from django.contrib import admin
from .models import *


@admin.register(HomeBackground)
class HomeBackgroundAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('background_type', 'name')}),
        (('Image and Particles'), {'fields': ('image',)}),
        (('Color'), {'fields': ('color',)}),
        (('Video'), {'fields': ('video_url',)}),
    )



@admin.register(Downloader)
class DownloaderAdmin(admin.ModelAdmin):
    filter_horizontal = ('social_links',)



@admin.register(ServiceBlock)
class ServiceBlockAdmin(admin.ModelAdmin):
    filter_horizontal = ('service_items',)



@admin.register(PricingBlock)
class PricingBlockAdmin(admin.ModelAdmin):
    filter_horizontal = ('pricing_items',)



@admin.register(PricingItem)
class PricingItemAdmin(admin.ModelAdmin):
    filter_horizontal = ('elements',)



@admin.register(FactBlock)
class FactBlockAdmin(admin.ModelAdmin):
    filter_horizontal = ('fact_items',)



@admin.register(ClientBlock)
class ClientBlockAdmin(admin.ModelAdmin):
    filter_horizontal   = ('client_items',)



@admin.register(ClientItem)
class ClientItemAdmin(admin.ModelAdmin):
    readonly_fields     = ('height_field', 'width_field')



@admin.register(TimelineBlock)
class TimelineBlockAdmin(admin.ModelAdmin):
    filter_horizontal   = ('timeline_items',)



@admin.register(SkillBlock)
class SkillBlockAdmin(admin.ModelAdmin):
    filter_horizontal   = ('skill_items',)



admin.site.register(TypingTitle)
admin.site.register(SideImage)
admin.site.register(SideMap)
admin.site.register(ServiceItem)
admin.site.register(PricingElement)
admin.site.register(FactItem)
admin.site.register(TimelineItem)
admin.site.register(SkillItem)
