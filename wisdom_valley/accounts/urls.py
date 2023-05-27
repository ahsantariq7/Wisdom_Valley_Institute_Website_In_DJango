from xml.dom.minidom import Document
from django.urls import path
from accounts.views import SignUpView, ProfileView
from accounts import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path("contact",views.contact, name='contact'),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)