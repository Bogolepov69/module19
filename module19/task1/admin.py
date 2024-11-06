from django.contrib import admin
from .models import Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'content',
                    'author',
                    'published_date',
                    )
    search_fields = ('title',
                    'content',
                    'author',
                    'published_date',
                    )