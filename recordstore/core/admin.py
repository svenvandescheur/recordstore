from django.contrib import admin

from core.models import Collection, Artist, Release, Track


def collect_info(modeladmin, request, queryset):
    """
    Collects and stores information
    """
    for object in queryset:
        object.collect_info()


class ReleaseAdmin(admin.ModelAdmin):
    actions = [collect_info]

admin.site.register((Collection, Artist, Track))
admin.site.register(Release, ReleaseAdmin)
