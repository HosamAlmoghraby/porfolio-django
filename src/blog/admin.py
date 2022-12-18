from django.contrib import admin
from .models import Post, Category, Author


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display		= ('subject', 'author', 'publish_date', 'last_modify', 'category', 'hide')
	list_display_links	= ('subject',)
	list_filter			= ('author', 'publish_date', 'last_modify', 'category')
	list_editable		= ('category', 'hide')
	search_fields		= ('__all__',)
	readonly_fields		= ('height_field', 'width_field')
	list_per_page		= 10


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display		= ('category',)
	list_display_links	= ('category',)
	list_filter			= ('category',)
	list_editable		= ()
	search_fields		= ('__all__',)
	list_per_page		= 10


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display		= ('user', 'email', 'phone')
	list_display_links	= ('user',)
	list_filter			= ('user', 'email', 'phone')
	list_editable		= ()
	search_fields		= ('__all__',)
	list_per_page		= 10
