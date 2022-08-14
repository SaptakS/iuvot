from django.contrib.auth.models import AbstractUser


class DbLimitException(BaseException):
      pass

class User(AbstractUser):
    def save(self, *args, **kwargs):
        if User.objects.count() >= 1:
            raise DbLimitException({"message": "Db limit reached please delete to add more data"})
        else:
            super().save(*args,**kwargs)
