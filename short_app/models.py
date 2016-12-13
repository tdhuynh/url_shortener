from django.db import models
from django.contrib.auth.models import User

class Bookmark(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField()
    short_url = models.CharField(max_length=10, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created",)

    def click_count(self):
        return self.click_set.count()

class Click(models.Model):
    bookmark = models.ForeignKey('short_app.Bookmark')
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-timestamp",)

    def __str__(self):
        return self.bookmark.title
