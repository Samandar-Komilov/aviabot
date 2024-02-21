from django.contrib import admin
from .models import CustomUser, News
from django.utils.html import format_html


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']

admin.site.register(News, NewsAdmin)