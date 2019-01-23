# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json
from aldryn_client import forms


class Form(forms.BaseForm):
    enabled = forms.CheckboxField(
        'Enabled', required=False, initial=True
    )


    def to_settings(self, data, settings):
        if data['enabled']:
            settings["INSTALLED_APPS"].append('admin_reorder')
            settings["MIDDLEWARE_CLASSES"].append('admin_reorder.middleware.ModelAdminReorder')
        return settings
