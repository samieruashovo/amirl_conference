from django.db import models

# Create your models here.


class Paper(models.Model):

    title = models.CharField(max_length=200)
    abstract = models.TextField(blank=True, null=True)
    authors = models.ManyToManyField(
        'users.User', related_name='papers_authored')
    conference = models.ForeignKey(
        'conference.Conference', on_delete=models.CASCADE, related_name='papers')
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='papers/', blank=True, null=True)
    status = models.CharField(max_length=50, default='submitted')
    reviewers = models.ManyToManyField(
        'users.User', related_name='papers_reviewed')
    reviews = models.TextField(blank=True, null=True)
