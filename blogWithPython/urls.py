from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog.views import blog, post_detail, home, jobs, contact
from authentication.views import register, login
from investment.views import inversiones

urlpatterns = [
    path('', home, name='home'),
    path('', jobs, name='jobs'),
    path('', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('investment/', inversiones, name='inversiones'),
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('<slug:slug>/', post_detail, name='post_detail')
] + static(settings.STATIC_URL)
