from django.db import models


# Create your models here.
class Email(models.Model):
    email_id = models.EmailField(max_length=30)

