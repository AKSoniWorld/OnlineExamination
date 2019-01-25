from django.db import models

# Create your models here.


class Profile(models.Model):
    """
    This model will handle user profiles for whole system 
    1. It will be of 2 types 
        - "TE" : "teacher"
        - "SU" : "Student"

    For login and session purpose each profile will be connected to 
    auth.django user
    """

    user = models.OneToOneField(
        'auth.User',
        on_delete=models.CASCADE,
        related_name = "profile",
    )
    fullname = models.CharField( # must not be greater then 20 char
        max_length=20,
        null=True, # for initial blank in case need user to update profile him self 
        blank=True, # same as above
    )
    address = models.TextField(
        null=True,
        blank=True,
    )

    join_on = models.DateTimeField(
        auto_now_add=True, # to log when user joined system 
    )

    update_on = models.DateTimeField(
        auto_now=True,
    )

    status = models.BooleanField( # to manage user status in system by admin 
        default=True,
    )

    type_of_profile = models.CharField(
        max_length=2,
        choices=(
            ("AD", "Admin"),
            ("TE", "Teacher"),
            ("SU", "Student"),
        ),
        default = "SU",
    )

    def __str__(self, *args, **kwargs): # args, kwargs are to manage unexpected incomming parameters
        return self.fullname

