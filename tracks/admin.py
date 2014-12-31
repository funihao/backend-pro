from django.contrib import admin

from .models import Track

from actions import export_as_excel


class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'order',
                    'album', 'player', 'es_pharell')
    list_filter = ('artist', 'album')
    search_fields = ('title', 'artist__first_name', 'artist__last_name')
    list_editable = ('title', 'album')
    raw_id_fields = ('artist', )
    actions = (export_as_excel, )

    def es_pharell(self, obj):
        return obj.id == 2

    es_pharell.boolean = True


admin.site.register(Track, TrackAdmin)
