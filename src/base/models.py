from django.db import models
from django.utils.translation import gettext as _
from .choices import theme_color_choices, language_choices


class SiteSetting(models.Model):
    language            = models.CharField(_("Language"), max_length=50, choices=language_choices)
    right_to_left       = models.BooleanField(_("Right To Left"))
    title               = models.CharField(_("Title"), max_length=70, blank=True)
    description         = models.TextField(_("Description"), max_length=320, blank=True)
    keywords            = models.CharField(_("Keywords"), max_length=100, blank=True)
    logo                = models.CharField(_("Logo"), max_length=1, blank=True)
    favicon             = models.ImageField(_("Favicon"), upload_to="favicon", height_field=None, width_field=None, max_length=None, blank=True)
    author              = models.CharField(_("Author"), max_length=100, blank=True)
    theme_color         = models.CharField(_("Theme Color"), max_length=50, choices=theme_color_choices)
    social_on_header    = models.ManyToManyField("Social", verbose_name=_("Social On Header"), blank=True)

    class Meta:
        verbose_name        = _("Site Setting")
        verbose_name_plural = _("Site Settings")

    def __str__(self):
        return self.language



class Social(models.Model):
    name    = models.CharField(_("Name"), max_length=50, unique=True)
    icon    = models.ForeignKey("Icon", verbose_name=_("Icon"), on_delete=models.CASCADE)
    url     = models.URLField(_("URL"), max_length=200)

    class Meta:
        verbose_name        = _("Social")
        verbose_name_plural = _("Socials")

    def __str__(self):
        return self.name



class Icon(models.Model):
    name    = models.CharField(_("Name"), max_length=50, unique=True)
    code    = models.CharField(_("Code"), max_length=50, unique=True, help_text="find icon from the link: https://icons8.com/line-awesome  and paste the code")

    class Meta:
        verbose_name        = _("Icon")
        verbose_name_plural = _("Icons")

    def __str__(self):
        return self.name



class Currency(models.Model):
    name    = models.CharField(_("Name"), max_length=50, unique=True, help_text="e.g.: US Dollar, For the full list: https://www.xe.com/symbols.php")
    code    = models.CharField(_("Code"), max_length=3, unique=True, help_text="e.g.: USD")
    symbol  = models.CharField(_("Symbol"), max_length=1, help_text="e.g.: $")

    class Meta:
        verbose_name        = _("Currency")
        verbose_name_plural = _("Currencies")

    def __str__(self):
        return f"{self.name} ({self.symbol})"
