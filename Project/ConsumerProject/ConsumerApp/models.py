from django.db import models

class UserModel(models.Model):
    username = models.CharField(blank=True, default="", max_length=100)
    email = models.EmailField(blank=True, default="", max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    @staticmethod
    def create_user(username, email, password):
        user = UserModel(username=username, email=email, password=password)
        user.save()
        return user

    @staticmethod
    def list_users():
        return UserModel.objects.all()