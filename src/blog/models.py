from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext as _


User = settings.AUTH_USER_MODEL

def upload_location(object, filename):
	return f'{object.author}/{object.slug}_{filename}'



class Post(models.Model):
	subject			= models.CharField(_("Subject"), max_length=50)
	description		= models.TextField(_("Description"))
	author			= models.ForeignKey("Author", verbose_name=_("Author"), on_delete=models.CASCADE)
	image			= models.ImageField(_("Image"), upload_to=upload_location, height_field='height_field', width_field='width_field', blank=True)
	height_field	= models.IntegerField(_("Height"), null=True)
	width_field		= models.IntegerField(_("Width"), null=True)
	category		= models.ForeignKey("Category", verbose_name=_("Category"), on_delete=models.CASCADE)
	slug			= models.SlugField(_("Slug"), max_length=50, unique=True)
	publish_date	= models.DateTimeField(_("Publish Date"), auto_now_add=True)
	last_modify		= models.DateTimeField(_("Last Modify"), auto_now=True)
	hide			= models.BooleanField(_("Hide"))
	
	class Meta:
		verbose_name        = _("Post")
		verbose_name_plural = _("Posts")

	def __str__(self):
		return self.subject

	def get_absolute_url(self):
		return reverse("blog:post_detail", kwargs={"slug": self.slug})



class Category(models.Model):
	category = models.CharField(_("Category"), max_length=50)
	
	class Meta:
		verbose_name        = _("Category")
		verbose_name_plural = _("Categories")

	def __str__(self):
		return self.category



class Author(models.Model):
	user	= models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
	email	= models.EmailField(_("Email"))
	phone	= models.CharField(_("Phone"), max_length=50, blank=True, help_text='Contact Phone Number')
	
	class Meta:
		verbose_name        = _("Author")
		verbose_name_plural = _("Authors")

	def __str__(self):
		return self.user.username
