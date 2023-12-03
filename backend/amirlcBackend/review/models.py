from django.db import models

# Create your models here.


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    reviewer = models.ForeignKey(
        'users.User', related_name='reviewer', on_delete=models.CASCADE)
    paper = models.ForeignKey(
        'paper.Paper', related_name='paper', on_delete=models.CASCADE)
    score = models.IntegerField()
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.reviewer + " " + self.paper + " " + str(self.score) + " " + self.comment
