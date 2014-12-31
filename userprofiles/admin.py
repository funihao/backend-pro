from django.contrib import admin

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')
    #list_filter = ('user')
    #search_fields = ('user',    )
    list_editable = ('user', 'avatar')


admin.site.register(UserProfile, UserProfileAdmin)
