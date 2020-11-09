from django.db import models
from item.models import Item


class Item_page(models.Model):
    brend = Item.brend
    model = Item.model
    cost = Item.cost
    photo = Item.photo
    desc = Item.desc

    class Meta:
        db_table = "Каталог товаров"
        verbose_name = "Каталог"
        verbose_name_plural = "Каталоги"
