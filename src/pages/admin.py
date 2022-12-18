from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display        = ('name', 'last_modify', 'active', 'order')
    list_display_links  = ('name',)
    list_filter         = ('last_modify',)
    list_editable       = ('order',)
    search_fields       = ('__all__',)
    # readonly_fields     = ('last_modify',)
    list_per_page       = 10
    filter_horizontal   = ('typing_title', 'downloader', 'service_blocks', 'pricing_blocks', 'fact_blocks', 'client_blocks', 'timeline_blocks', 'skill_blocks')
    fieldsets           = (
        (('Page Style'), {'fields': ('name', 'route', 'icon')}),
        (('Home Page'), {'classes': ('collapse',), 'fields': ('background', 'title_name', 'subtitle', 'typing_title')}),
        (('Page Body'), {'classes': ('collapse',), 'fields': ('background_title', 'side', 'side_image', 'side_map', 'text', 'downloader', 'service_blocks', 'pricing_blocks', 'fact_blocks', 'client_blocks', 'timeline_blocks', 'skill_blocks', 'active')}),
    )
