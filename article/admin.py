from django.contrib import admin

from .models import Article,Comment
# Register your models here.
#admin.site.register(Comment)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=["comment_author","comment_content"]#Tabloda gösterir.
    list_display_links=["comment_author"]#link özelliği ekleyerek tıkladığım zaman makale ekranını açar.
    search_fields=["comment_content"]#arama çubuğu oluşturur title göre.
    list_filter=["comment_date"]#Örneğin son yedi gün veya son gün yazılan makalerrimiz görmemizi sağlar.
    class Meta():
        model=Comment

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=["title","author","created_date"]#Tabloda gösterir.
    list_display_links=["title","created_date"]#link özelliği ekleyerek tıkladığım zaman makale ekranını açar.
    search_fields=["title"]#arama çubuğu oluşturur title göre.
    list_filter=["created_date"]#Örneğin son yedi gün veya son gün yazılan makalerrimiz görmemizi sağlar.
    class Meta():
        model=Article