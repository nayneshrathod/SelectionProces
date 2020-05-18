from django.db import models


from django.contrib.auth.models import auth,User

# Create your models here.


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.CharField(max_length=120, null=True, blank=True)
    password = models.CharField(max_length=120, null=True, blank=True)
    username = models.CharField(max_length=120, null=True, blank=True)
    #
    # username = models.ForeignKey('auth_User', related_name='username', on_delete=models.CASCADE)

    #
    # class Meta:
    #     app_label = 'default'

    class Meta:
        # db_table = 'auth_user'
        app_label = 'UserApp'

    def __str__(self):
        return self.first_name + " " + self.last_name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    #
    class Meta:
        app_label = 'UserApp'

    def __str__(self):
        return str(self.id)
