from django.db import models
from ckeditor.fields import RichTextField
# Create your models here. 

#Veritabanında bir model oluşturmak için. 1-Admin paneline git ve kaydet.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE, verbose_name = "Yazar")#bu alan user kısmına denk geliyor diyoruz. Bu kullanıcı silindiğinde makale de silinecek
    title = models.CharField(max_length = 50, verbose_name = "Başlık")
    content = RichTextField(verbose_name = "İçerik")
    created_date = models.DateTimeField(auto_now=True, verbose_name = "Oluşturulma Tarihi")#o anki tarih
    article_image = models.FileField(blank = True, null=True, verbose_name="Fotoğraf Ekle")#bu alanımız dolu veya boş olabilir.
    def __str__(self): 
        return self.title
    class Meta:
        ordering = ['-created_date'] #son ekleme tarihine sahip olan ilk gösterilecek.


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, verbose_name = "Makale",related_name="comments") #article ile comment i bağlantılı hale getirdik.
                                                                                                #articleların commentlerini almak için related_name verdik. İleride article.comments diyerek bu tabloya ulaşabileceğiz.
    comment_author = models.CharField(max_length = 50, verbose_name = "İsim") #yorum yazarı
    comment_content = models.CharField(max_length = 200, verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']