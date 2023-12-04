from django.db import models

# Create your models here.


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    reviewer = models.ForeignKey(
        'users.User', related_name='reviewer', on_delete=models.CASCADE)
    paper = models.ForeignKey(
        'paper.Paper', related_name='paper', on_delete=models.CASCADE)
    score = models.IntegerField()
    comment = models.TextField(max_length=200)

    originality = models.IntegerField(choices=[
        (5, 'Very High'),
        (4, 'High'),
        (3, 'Moderate'),
        (2, 'Low'),
        (1, 'Very Low'),
    ], null=True, blank=True)

    # Question 2
    writing_and_organization = models.IntegerField(choices=[
        (5, 'Excellent'),
        (4, 'Good'),
        (3, 'Adequate'),
        (2, 'Needs Improvement'),
        (1, 'Bad'),
    ], null=True, blank=True)

    # Question 3
    alignment_with_scope = models.IntegerField(choices=[
        (5, 'Very High'),
        (4, 'High'),
        (3, 'Moderate'),
        (2, 'Low'),
        (1, 'Very Low'),
    ], null=True, blank=True)

    # Question 4
    contribution_to_field = models.IntegerField(choices=[
        (5, 'Very Significant'),
        (4, 'Significant'),
        (3, 'Moderate'),
        (2, 'Limited'),
        (1, 'Negligible'),
    ], null=True, blank=True)

    # Question 5
    ethical_considerations = models.IntegerField(choices=[
        (5, 'Fully Addressed'),
        (4, 'Addressed'),
        (3, 'Partially Addressed'),
        (2, 'Somehow Addressed'),
        (1, 'Not Addressed'),
    ], null=True, blank=True)

    # Question 6
    introduction_quality = models.IntegerField(choices=[
        (5, 'Excellent'),
        (4, 'Good'),
        (3, 'Adequate'),
        (2, 'Needs Improvement'),
        (1, 'Bad'),
    ], null=True, blank=True)

    # Question 7
    literature_review_quality = models.IntegerField(choices=[
        (5, 'Excellent'),
        (4, 'Good'),
        (3, 'Adequate'),
        (2, 'Needs Improvement'),
        (1, 'Bad'),
    ], null=True, blank=True)

    # Question 8
    methodology_quality = models.IntegerField(choices=[
        (5, 'Excellent'),
        (4, 'Good'),
        (3, 'Adequate'),
        (2, 'Needs Improvement'),
        (1, 'Bad'),
    ], null=True, blank=True)

    # Question 9
    results_clarity_and_validity = models.IntegerField(choices=[
        (5, 'Very High'),
        (4, 'High'),
        (3, 'Moderate'),
        (2, 'Low'),
        (1, 'Very Low'),
    ], null=True, blank=True)

    # Question 10
    references_and_citations_quality = models.IntegerField(choices=[
        (5, 'Excellent'),
        (4, 'Good'),
        (3, 'Fair'),
        (2, 'Poor'),
        (1, 'Very Poor'),
    ], null=True, blank=True)

    # ... existing fields

    # Overall recommendation
    overall_recommendation = models.CharField(choices=[
        ('accept_as_is', 'Accept as Is'),
        ('accept_with_minor_revisions', 'Accept with Minor Revisions'),
        ('accept_with_major_revisions', 'Accept with Major Revisions'),
        ('reject', 'Reject'),
    ], max_length=30, null=True, blank=True)

    # Comments to the Authors
    comments_to_authors = models.TextField(null=True, blank=True)

    # Comments to the Editors
    comments_to_editors = models.TextField(null=True, blank=True)

    # Annotated PDF
    annotated_pdf = models.FileField(
        upload_to='annotated_pdfs/', null=True, blank=True)

    def __str__(self):
        return f'{self.reviewer} {self.paper} {self.score} {self.comment}'
