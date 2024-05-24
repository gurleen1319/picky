from django.conf.urls import url
from . import views
from django.urls import path
# from stock.views import index as stock_index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^consult/$', views.consult, name='consult'),
    url(r'^management/$', views.management, name='management'),
    url(r'^market/$', views.market, name='market'),
    url(r'^monitoring/$', views.monitoring, name='monitoring'),
    url(r'^investment/$', views.investment, name='investment'),
    url(r'^stock/$', views.stock, name='stock'),
    url(r'^streamlit/$', views.streamlit_view , name='streamlit-view'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
