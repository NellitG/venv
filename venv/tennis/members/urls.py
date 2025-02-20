from django.contrib import admin
from django.urls import include, path
# from . import views

urlpatterns = [
    path('members/', include('members.urls')),
    path('admin/', admin.site.urls),
    # path('',views.home, name='home'),
    # path('members/', include('members.urls')),
]