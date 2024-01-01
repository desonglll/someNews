from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import pages.views as pages_views
import news.views as news_views
import products.views as products_views

urlpatterns = [
                  path('', pages_views.home_view, name='home'),
                  path('home', pages_views.home_view, name='home'),
                  path('admin/', admin.site.urls),
                  path('buy', pages_views.buy_view, name="buy_page"),
                  path('login_page', pages_views.login_view, name="login_page"),
                  path("api/buy", products_views.purchase_product, name="api_buy"),
                  path("api/nav_app", news_views.get_nav, name="api_nav_app"),
                  path("api/login", news_views.user_login, name='login'),
                  path("api/get_all_news", news_views.get_all_news, name="api_get_all_news"),
                  path("api/get_by_nid", news_views.get_by_nid, name="api_get_by_nid"),
                  path("api/get_by_id", news_views.get_by_id, name="api_get_by_id"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# static for access upload files
