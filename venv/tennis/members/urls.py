from django.contrib import admin # type: ignore
from django.urls import include, path # type: ignore
# from . import views

urlpatterns = [
    path('members/', include('members.urls')),
    path('admin/', admin.site.urls),
    # path('',views.home, name='home'),
    # path('members/', include('members.urls')),
]