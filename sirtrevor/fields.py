from django.db import models
from django.utils.translation import gettext_lazy as _
from . import SirTrevorContent
from .forms import SirTrevorFormField


class SirTrevorField(models.Field):
    description = _("TODO")

    def get_internal_type(self):
        return 'TextField'

    def formfield(self, **kwargs):
        defaults = {
            'form_class': SirTrevorFormField
        }
        defaults.update(kwargs)
        return super(SirTrevorField, self).formfield(**defaults)

    def to_python(self, value):
        return SirTrevorContent(value)

    def get_db_prep_value(self, value, connection, prepared=False):
        return str(value)
