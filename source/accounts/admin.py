from django.contrib import admin

from accounts.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id','author','product','review','rating']
    exclude=[]
    list_display_links = ['id']
    list_filter = ['author', 'product','rating']


admin.site.register(Review, ReviewAdmin)
