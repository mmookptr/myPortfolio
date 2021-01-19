from django.db import models


class ContactMessage(models.Model):
    email = models.EmailField(max_length=254)
    topic = models.CharField(max_length=30)
    message = models.CharField(
        max_length=2000,
    )
