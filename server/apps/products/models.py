from django.db import models

class Product:
    title = None
    price = None
    price_discount = None
    image = None
    description = None
    category = None

class ProductCategory:
    name = None
    image = None

    