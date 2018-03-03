from django.db import models
from django.utils import timezone


# create an object of type django model so it's saved in a database
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # link to another model
    title = models.CharField(max_length=200)  # text field with a limited number of chars
    text = models.TextField()  # text field without limit
    created_date = models.DateTimeField(
            default=timezone.now)  # datetime field
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()  # this is defined in django Model

    def __str__(self):
        return self.title
