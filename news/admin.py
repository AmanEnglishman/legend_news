from django.contrib import admin

from news.models import News, Category, Comments

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'views')
    list_filter = ('category', )
    search_fields = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    pass