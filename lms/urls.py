from core.views import index

import debug_toolbar

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('groups/', include('groups.urls')),
    path('teachers/', include('teachers.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]