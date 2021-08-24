from factory import django, Faker

from users.models import CustomUser


class UserssFactory(django.DjangoModelFactory):
    username = 'ddrwiei22'
    password = 'james22ee'

    class Meta:
        model = CustomUser