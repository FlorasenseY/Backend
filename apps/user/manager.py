from django.contrib.auth.models import BaseUserManager



class UserManager(BaseUserManager):
    def create_user(self, username, **kwargs):
        user = self.model(username=username, **kwargs)
        user.set_password(username)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_superuser", True)
        user = self.create_user(email, password, **kwargs)
        return user
