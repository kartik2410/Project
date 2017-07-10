from django.conf.urls import url,include
from project1 import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    url(r'^$', views.Home, name = "Home"),
    url(r'^blog/$', views.Blog, name = "Blog"),
    url(r'^art/$', views.Art, name = "Art"),
    url(r'^cakes/$', views.Cakes, name = "Cakes"),
    url(r'^gifts/$', views.Gifts, name = "Gifts"),

]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)