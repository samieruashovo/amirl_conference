from django.db import models


class Conference(models.Model):
    name = models.CharField(max_length=200)
    acronym = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(
        upload_to='conference_thumbnails/', blank=True, null=True)
    organizers = models.ManyToManyField(
        'users.User', related_name='conferences_organized')
    submission_satrt = models.DateTimeField()
    submission_deadline = models.DateTimeField()
    conference_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    place = models.CharField(max_length=500, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    reviewers = models.ManyToManyField(
        'users.User', related_name='conferences_reviewed')
