from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator, MaxValueValidator
import re
from base.choices import home_background_choices
from base.models import Social, Icon, Currency


TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)


class HomeBackground(models.Model):
    background_type = models.CharField(_("Background Type"), max_length=10, choices=home_background_choices)
    name            = models.CharField(_("Name"), max_length=100)
    image           = models.ImageField(_("Image"), upload_to="background", height_field=None, width_field=None, max_length=None, blank=True)
    color           = models.CharField(_("Color"), max_length=10, blank=True)
    video_url       = models.URLField(_("Video URL"), max_length=200, blank=True)


    class Meta:
        verbose_name        = _("Home Background")
        verbose_name_plural = _("Home Backgrounds")

    def __str__(self):
        return f"{self.name} ({self.background_type})"



class TypingTitle(models.Model):
    typing_title = models.CharField(_("Typing Title"), max_length=100, unique=True)

    class Meta:
        verbose_name        = _("Typing Title")
        verbose_name_plural = _("Typing Titles")

    def __str__(self):
        return remove_tags(self.typing_title)



class SideImage(models.Model):
    name = models.CharField(_("Name"), max_length=50, unique=True)
    image = models.ImageField(_("Image"), upload_to="background", height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name        = _("Side Image")
        verbose_name_plural = _("Side Images")

    def __str__(self):
        return self.name



class SideMap(models.Model):
    place = models.CharField(_("Place"), max_length=50, unique=True)

    class Meta:
        verbose_name        = _("Side Map")
        verbose_name_plural = _("Side Maps")

    def __str__(self):
        return self.place



class Downloader(models.Model):
    name            = models.CharField(_("Name"), max_length=50, unique=True)
    button_name     = models.CharField(_("Button Name"), max_length=50)
    icon            = models.ForeignKey(Icon, verbose_name=_("Icon"), on_delete=models.DO_NOTHING, blank=True, null=True)
    file            = models.FileField(_("File"), upload_to="download", max_length=100)
    social_links    = models.ManyToManyField(Social, verbose_name=_("Social Links"), blank=True)

    class Meta:
        verbose_name        = _("Downloader")
        verbose_name_plural = _("Downloaders")

    def __str__(self):
        return self.name



class ServiceBlock(models.Model):
    title           = models.CharField(_("Title"), max_length=50, unique=True)
    service_items   = models.ManyToManyField("ServiceItem", verbose_name=_("Service Items"))

    class Meta:
        verbose_name        = _("Service Block")
        verbose_name_plural = _("Service Blocks")

    def __str__(self):
        return remove_tags(self.title)



class ServiceItem(models.Model):
    icon        = models.ForeignKey(Icon, verbose_name=_("Icon"), on_delete=models.DO_NOTHING, blank=True, null=True)
    title       = models.CharField(_("Title"), max_length=50, unique=True)
    description = models.TextField(_("Description"), blank=True)
    order       = models.IntegerField(_("Order"), default=0, blank=True, null=True)

    class Meta:
        verbose_name        = _("Service Item")
        verbose_name_plural = _("Service Items")

    def __str__(self):
        return self.title



class PricingBlock(models.Model):
    title           = models.CharField(_("Title"), max_length=50, unique=True)
    pricing_items   = models.ManyToManyField("PricingItem", verbose_name=_("Pricing Items"))

    class Meta:
        verbose_name        = _("Pricing Block")
        verbose_name_plural = _("Pricing Blocks")

    def __str__(self):
        return remove_tags(self.title)



class PricingItem(models.Model):
    icon        = models.ForeignKey(Icon, verbose_name=_("Icon"), on_delete=models.DO_NOTHING, blank=True, null=True)
    title       = models.CharField(_("Title"), max_length=50, unique=True)
    currency    = models.ForeignKey(Currency, verbose_name=_("Currency"), on_delete=models.DO_NOTHING, blank=True, null=True)
    amount      = models.IntegerField(_("Amount"), default=0, blank=True, null=True)
    unit        = models.CharField(_("Unit"), max_length=50, blank=True)
    elements    = models.ManyToManyField("PricingElement", verbose_name=_("Elements"), blank=True)
    button_name = models.CharField(_("Button Name"), max_length=50, blank=True)
    button_url  = models.URLField(_("Button URL"), max_length=200, blank=True)
    order       = models.IntegerField(_("Order"), default=0, blank=True, null=True)

    class Meta:
        verbose_name        = _("Pricing Item")
        verbose_name_plural = _("Pricing Items")

    def __str__(self):
        return self.title



class PricingElement(models.Model):
    title       = models.CharField(_("Title"), max_length=50)
    excluded    = models.BooleanField(_("Excluded"))
    new         = models.BooleanField(_("New"))
    order       = models.IntegerField(_("Order"), default=0, blank=True, null=True)

    class Meta:
        verbose_name        = _("Pricing Element")
        verbose_name_plural = _("Pricing Elements")

    def __str__(self):
        return_string = self.title
        if self.excluded:
            return_string += " (excluded)"
        if self.new:
            return_string += " (new)"
        return return_string



class FactBlock(models.Model):
    title       = models.CharField(_("Title"), max_length=50, unique=True)
    fact_items  = models.ManyToManyField("FactItem", verbose_name=_("Fact Items"))

    class Meta:
        verbose_name        = _("Fact Block")
        verbose_name_plural = _("Fact Blocks")

    def __str__(self):
        return remove_tags(self.title)



class FactItem(models.Model):
    icon    = models.ForeignKey(Icon, verbose_name=_("Icon"), on_delete=models.DO_NOTHING, blank=True, null=True)
    title   = models.CharField(_("Title"), max_length=50, unique=True)

    class Meta:
        verbose_name        = _("Fact Item")
        verbose_name_plural = _("Fact Items")

    def __str__(self):
        return self.title



class ClientBlock(models.Model):
    title           = models.CharField(_("Title"), max_length=50, unique=True)
    client_items    = models.ManyToManyField("ClientItem", verbose_name=_("Client Items"))

    class Meta:
        verbose_name        = _("Client Block")
        verbose_name_plural = _("Client Blocks")

    def __str__(self):
        return remove_tags(self.title)



class ClientItem(models.Model):
    title           = models.CharField(_("Title"), max_length=50, unique=True)
    image           = models.ImageField(_("Image"), upload_to="clients", height_field='height_field', width_field='width_field', max_length=None)
    height_field	= models.IntegerField(_("Height"), null=True)
    width_field		= models.IntegerField(_("Width"), null=True)
    alt             = models.CharField(_("Image alt"), max_length=100, blank=True)
    url             = models.URLField(_("URL"), max_length=200, blank=True)

    class Meta:
        verbose_name        = _("Client Item")
        verbose_name_plural = _("Client Items")

    def __str__(self):
        return self.title



class TimelineBlock(models.Model):
    title           = models.CharField(_("Title"), max_length=50, unique=True)
    timeline_items  = models.ManyToManyField("TimelineItem", verbose_name=_("Timeline Items"))

    class Meta:
        verbose_name        = _("Timeline Block")
        verbose_name_plural = _("Timeline Blocks")

    def __str__(self):
        return remove_tags(self.title)



class TimelineItem(models.Model):
    title       = models.CharField(_("Title"), max_length=50, unique=True)
    from_date   = models.DateField(_("From Date"), blank=True, null=True)
    to_date     = models.DateField(_("To Date"), blank=True, null=True)
    place       = models.CharField(_("Place"), max_length=50, blank=True)
    description = models.TextField(_("Description"), blank=True)

    class Meta:
        verbose_name        = _("Timeline Item")
        verbose_name_plural = _("Timeline Items")
    
    def year_from(self):
        return f"{self.from_date.strftime('%B').upper()[:3]} {self.from_date.strftime('%Y')}"

    def year_to(self):
        return f"{self.to_date.strftime('%B').upper()[:3]} {self.to_date.strftime('%Y')}"

    def __str__(self):
        return self.title



class SkillBlock(models.Model):
    title       = models.CharField(_("Title"), max_length=50, unique=True)
    skill_items = models.ManyToManyField("SkillItem", verbose_name=_("Skill Items"))

    class Meta:
        verbose_name        = _("Skill Block")
        verbose_name_plural = _("Skill Blocks")

    def __str__(self):
        return remove_tags(self.title)



class SkillItem(models.Model):
    name        = models.CharField(_("Title"), max_length=100, unique=True)
    percentage  = models.PositiveSmallIntegerField(_("Percentage"), validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        verbose_name        = _("Skill Item")
        verbose_name_plural = _("Skill Items")

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"