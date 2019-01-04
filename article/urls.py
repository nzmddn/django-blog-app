from django.contrib import admin
from django.urls import path,include
from . import views



#bu dosyayı biz açtık. ve dizindeki views'ı dahil ettik. Bunun içerisine
#yazacağımız şeyler için blog/urls'te buraya bakmasını söyledik.
#localhost/articles ı gördüğünde django buraya bakacak. Daha sonra
#create varsa buradaki işlemi çalıştıracak.


app_name = "article"

urlpatterns = [
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('addarticle/', views.addArticle, name = "addarticle"),
    path('article/<int:id>', views.detail, name = "detail"),
    path('update/<int:id>', views.updateArticle, name = "update"),
    path('delete/<int:id>', views.deleteArticle, name = "delete"),
    path('', views.articles, name = "articles"),#blog/urls'te dahil ettiğimiz için burada belirtmemeliyiz. boşluk bıraktık bu yüzden.
    path('comment/<int:id>', views.addComment, name = "comment"),
]