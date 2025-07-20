import uuid

from django.db import models

# Create your models here.


class SecretKey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    value = models.TextField()

    def __str__(self):
        return self.value
