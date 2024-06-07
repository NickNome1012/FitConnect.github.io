from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from FitConnect import views


urlpatterns = [
    path('', views.start),
    path('login', views.login_usuario),
    path('cadastro/', views.cadastro_usuario),
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('sobre/', views.sobre),
    path('logout/', views.logout_usuario)
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)