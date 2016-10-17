from django.db import models


class Bookmark(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created",)


class Click(models.Model):
    bookmark = models.ForeignKey('short_app.Bookmark')
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-timestamp",)

    def __str__(self):
        return self.bookmark.title
