from django.urls import path
from item_page.views import catalog_page

urlpatterns = [
    path("", catalog_page, name="catalog_page")
]