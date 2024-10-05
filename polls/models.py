from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField()
    create_data = models.DateTimeField()
    update_data = models.DateTimeField()
    content = models.TextField()
    numbers_of_likes = models.IntegerField(default=0)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)

    class Meta:
        pass
    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    age = models.IntegerField()
    number_of_posts = models.IntegerField(default=0)
    class Meta:
        pass
    def __str__(self):
        return self.first_name + ' ' + self.last_name
