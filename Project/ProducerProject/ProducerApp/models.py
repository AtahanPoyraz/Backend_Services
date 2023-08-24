from django.db import models

class MessageModel(models.Model):
    message = models.TextField()

    def __str__(self):
        return self.message
