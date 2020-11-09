from django.contrib import admin
from item_page.models import Item_page

class AdminCatalogPage(admin.ModelAdmin):
    list_display = ["brend","model", "cost"]

admin.site.register(Item_page, AdminCatalogPage)
