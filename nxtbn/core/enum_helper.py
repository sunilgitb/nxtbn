from django.db import models

class WeightUnits(models.TextChoices):
    GRAM = 'GRAM', 'Gram'
    KILOGRAM = 'KG', 'Kilogram'
    POUND = 'LB', 'Pound'
    OUNCE = 'OZ', 'Ounce'
    TON = 'TON', 'Ton'


class ProductType(models.TextChoices):
    SIMPLE_PRODUCT = 'SIMPLE_PRODUCT', 'Simple Product'
    GROUPED_PRODUCT = 'GROUPED_PRODUCT', 'Services'
    EXTERNAL_PRODUCT = 'EXTERNAL_PRODUCT', 'External/Affiliate Product'
    VARIABLE_PRODUCT = 'VARIABLE_PRODUCT', 'Variables Product'
    SIMPLE_SUBSCRIPTION = 'SIMPLE_SUBSCRIPTION', 'Simple Subscription'
    VARIABLE_SUBSCRIPTION = 'VARIABLE_SUBSCRIPTION', 'Variables Subscription'
    PRODUCT_BUNDLE = 'PRODUCT_BUNDLE', 'Product Bundle'

class StockStatus(models.TextChoices):
        IN_STOCK = 'IN_STOCK', 'In Stock'
        OUT_OF_STOCK = 'OUT_OF_STOCK', 'Out of Stock'