from django.contrib.auth.models import AbstractUser
from django.conf import settings


class DbLimitException(BaseException):
      pass

class User(AbstractUser):
    REQUIRED_FIELDS = settings.REQUIRED_USER_FIELDS

    def save(self, *args, **kwargs):
        if User.objects.count() >= 1:
            raise DbLimitException({"message": "Db limit reached please delete to add more data"})
        else:
            super().save(*args,**kwargs)
