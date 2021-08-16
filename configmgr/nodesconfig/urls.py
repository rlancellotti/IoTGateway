from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # Form-based interface: server-side only
    path('', views.node_form, name="node_form"),
    path('<int:node_id>/<slug:capability>', views.capability_form, name="capability_form"),
    # Read-only list API
    #path('api/<int:node_id>/<slug:capability>', views.capability_list_api, name="capability_list_api"),
    # Read-write single object API
    #path('api/<int:node_id>', views.node_api, name="node_api"),
    #path('api/<int:node_id>/<slug:capability>/<int:entry_id>', views.capability_api, name="capability_api"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)