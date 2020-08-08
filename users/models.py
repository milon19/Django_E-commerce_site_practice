from django.db import models


class GuestEmail(models.Model):
    email = models.EmailField(max_length=255)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
