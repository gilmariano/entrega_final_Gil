"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from AppPesca.views import PescaList, PescaMineList, PescaUpdate, PescaDelete, PescaCreate, Login, Logout, SignUp, ProfileCreate, ProfileUpdate, about, PescaDetail, MensajeList, MensajeCreate, MensajeDelete, PescaSearch, IndexView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('about/', about, name= 'about'),
    path('pesca/list', PescaList.as_view(), name='pescado-list'),
    path('pesca/mine', PescaMineList.as_view(), name='pescado-mine'),
    path('pesca/<pk>/update', PescaUpdate.as_view(), name='pescado-update'),
    path('pesca/<pk>/delete', PescaDelete.as_view(), name='pescado-delete'),
    path('pesca/<pk>/detail', PescaDetail.as_view(), name='pescado-detail'),
    path('pesca/create', PescaCreate.as_view(), name='pescado-create'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/create', ProfileCreate.as_view(), name='profile-create'),
    path('profile/<pk>/update', ProfileUpdate.as_view(), name='profile-update'),
    path('mensaje/list', MensajeList.as_view(), name="mensaje-list"),
    path('mensaje/create', MensajeCreate.as_view(), name="mensaje-create"),
    path('mensaje/<pk>/delete', MensajeDelete.as_view(), name="mensaje-delete"),
    path('search/', PescaSearch.as_view(), name='pescado-search'), 
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)