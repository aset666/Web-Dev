from django.contrib import admin
from django.urls import include, path
from task_m_s import views
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task_m_s.urls')),
    
]