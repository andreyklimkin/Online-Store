from django.contrib import admin
from .models import Post
from .models import Article, Comments

class ArticleInline(admin.StackedInline):
	model = Comments
	extra = 2


class ArticleAdmin(admin.ModelAdmin):
	fields = ['article_title', 'article_text', 'article_date']
	inlines = [ArticleInline]
	list_filter = ['article_date']

admin.site.register(Post)
admin.site.register(Article, ArticleAdmin)
# Register your models here.
