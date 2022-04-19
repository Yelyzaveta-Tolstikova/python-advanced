from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    publication_status = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
