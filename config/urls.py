from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import indexfunc, signupfunc, loginfunc, logoutfunc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexfunc, name='index'),
    path('menu/', include('menuapp.urls')),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    path('requests/', include('requestapp.urls')),
    path('group/', include('groupapp.urls')),
    path('search/', include('searchapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
