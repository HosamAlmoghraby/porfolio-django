from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from blocks.models import HomeBackground, TypingTitle, SideImage, SideMap, Downloader, ServiceBlock, PricingBlock, FactBlock, ClientBlock, TimelineBlock, SkillBlock
from base.models import Icon
from base.choices import side_choices


class Head(models.Model):
    name    = models.CharField(_("Name"), max_length=50, unique=True, help_text='e.g.: Home, About, Resume, Portfolio, Blog, Contacts')
    route   = models.CharField(_("Route"), max_length=50, unique=True)
    icon    = models.ForeignKey(Icon, verbose_name=_("Icon"), on_delete=models.CASCADE)

    class Meta:
        verbose_name        = _("Head")
        verbose_name_plural = _("Heads")

    def __str__(self):
        return self.name



class Page(Head):
    background          = models.ForeignKey(HomeBackground, verbose_name=_("Background"), on_delete=models.DO_NOTHING, blank=True, null=True)
    title_name          = models.CharField(_("Title Name"), max_length=100, blank=True)
    subtitle            = models.CharField(_("Subtitle"), max_length=100, blank=True)
    typing_title        = models.ManyToManyField(TypingTitle, verbose_name=_("Typing Title"), blank=True)
    background_title    = models.CharField(_("Background Title"), max_length=8, blank=True)
    side                = models.CharField(_("Side"), max_length=50, choices=side_choices, blank=True)
    side_image          = models.ForeignKey(SideImage, verbose_name=_("Side Image"), on_delete=models.DO_NOTHING, blank=True, null=True)
    side_map            = models.ForeignKey(SideMap, verbose_name=_("Side Map"), on_delete=models.DO_NOTHING, blank=True, null=True)
    text                = models.TextField(_("Text"), blank=True)
    downloader          = models.ManyToManyField(Downloader, verbose_name=_("Downloader"), blank=True)
    service_blocks      = models.ManyToManyField(ServiceBlock, verbose_name=_("Service Blocks"), blank=True)
    pricing_blocks      = models.ManyToManyField(PricingBlock, verbose_name=_("Pricing Blocks"), blank=True)
    fact_blocks         = models.ManyToManyField(FactBlock, verbose_name=_("Fact Blocks"), blank=True)
    client_blocks       = models.ManyToManyField(ClientBlock, verbose_name=_("Client Blocks"), blank=True)
    timeline_blocks     = models.ManyToManyField(TimelineBlock, verbose_name=_("Timeline Blocks"), blank=True)
    skill_blocks        = models.ManyToManyField(SkillBlock, verbose_name=_("Skill Blocks"), blank=True)
    last_modify         = models.DateTimeField(_("Last Modify"), auto_now=True)
    active              = models.BooleanField(_("Active"), default=True)
    order               = models.IntegerField(_("Order"), default=0, blank=True, null=True)

    class Meta:
        verbose_name        = _("Page")
        verbose_name_plural = _("Pages")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"#{self.route}"




# class HomePage(Head):
#     background      = models.ForeignKey(HomeBackground, verbose_name=_("Background"), on_delete=models.DO_NOTHING)
#     title_first     = models.CharField(_("Title First"), max_length=100, blank=True)
#     title_second    = models.CharField(_("Title Seccond"), max_length=100, blank=True)
#     subtitle        = models.CharField(_("Subtitle"), max_length=100, blank=True)
#     typing_title    = models.ManyToManyField(TypingTitle, verbose_name=_("Typing Title"), blank=True)

#     class Meta:
#         verbose_name        = _("Home Page")
#         verbose_name_plural = _("Home Pages")

#     def __str__(self):
#         return self.name