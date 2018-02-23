from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^course/', include('apps.course_app.urls')),
    url(r'^', include('apps.login_app.urls')),

]
