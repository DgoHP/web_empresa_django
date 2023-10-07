from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="personal").exists():
            return ('name', 'key')
        else:
            return ('created', 'updated')


admin.site.register(Link, LinkAdmin)