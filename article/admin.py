from django.contrib import admin

from.models import Article, Comment

# Register your models here.


admin.site.register(Comment)


"""admin.site.register(Article)#kaydettik.2-Oluşturduğumuz article uygulamasını settings'e söylememiz gerek.(INSTALLED_APPS)"""
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author","created_date"]
    list_display_links = ["title","created_date"]
    search_fields = ["title","content"]
    list_filter = ["created_date"]
    list_per_page = 20
    

    class Meta:
        model = Article #ArticleAdmin sınıfıyla decorator içindeki Article ı birleştirdik.




