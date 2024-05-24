from django.conf.urls import url
from . import views
from .views import streamlit_view

urlpatterns = [
    url(r'^stock/streamlit/$',streamlit_view, name='streamlit-view'),
]
