from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'age', 'telephone_number', 'birth_date')
    list_filter = ('user', 'bio', 'age')
    search_fields = ('user__email', 'telephone_number', 'location')


admin.site.register(UserProfile, UserProfileAdmin)
