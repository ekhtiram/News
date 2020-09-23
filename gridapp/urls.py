from django.conf.urls import url,include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', auth_views.login, name='login'),
    url(r'^home/', views.home, name='home'),
    url(r'^giris/', views.giris, name='giris'),
    url(r'^register/', views.register, name='register'),
    url(r'^notfound/', views.notfound, name='notfound'),
    url(r'^sil/', views.sil, name='sil'),
    url(r'^kayitformu/', views.kayit, name='kayit'),
    url(r'^accounts/login/', auth_views.login, name='login'),
    url(r'^accounts/logout/', auth_views.logout, name='logout'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^reset/email/', views.password_reset_email, name='password_reset_email'),
    url(r'^haberekle/', views.haberekle, name='haberekle'),
    url(r'^accounts/profile/', admin.site.urls),
    url(r'^haberler/', views.haberler, name='haberler'),
    url(r'^hesabim/', views.hesabim, name='hesabim'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
