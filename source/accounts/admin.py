from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from accounts.models import Review, Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    fields = ['avatar']


class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline]


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id','author','product','review','rating']
    exclude=[]
    list_display_links = ['id']
    list_filter = ['author', 'product','rating']


admin.site.register(Review, ReviewAdmin)
admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)

