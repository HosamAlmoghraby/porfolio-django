from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BlocksConfig(AppConfig):
    name = 'blocks'
    verbose_name = _('Block Management')
