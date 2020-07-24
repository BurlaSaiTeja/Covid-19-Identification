from django.contrib import admin

from covid.models import TestStatus


class TestStatusView(admin.ModelAdmin):
    list_display = ("name", "status",)
    list_filter = ("name", "status",)


admin.site.register(TestStatus, TestStatusView)
