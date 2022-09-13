from django.db import models

class Order:
    state = None
    created = None
    delivered = None
    client = None

class OrderProduct:
    order = None
    product = None
    count = None

class ClientProductCart:
    client = None
    product = None
    count = None

class Review:
    client = None
    title = None
    content = None

class SiteSettings:
    hotline_phone = None
    support_email = None
    brand_logo = None
    brand_name = None
    working_hours__start = None
    working_hours__end = None
    working_days_exclude = None

