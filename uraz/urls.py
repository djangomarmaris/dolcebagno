"""uraz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns
from yoga import views



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('pwa.urls')),
    path('',views.index,name='index'),
    path('cart/',include('cart.urls', namespace='cart')),
    path('order/', include('orders.urls',namespace='orders')),
    path('shop/',include('shop.urls', namespace='shop')),
    path('user/',include("user.urls")),
    path('blog/',include('yoga.urls')),
    path('sss/',views.sss,name='sss',),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('<str:slug>/',views.blog_detail,name='blog_detail'),
    #path('zeynep/',include("yoga.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)