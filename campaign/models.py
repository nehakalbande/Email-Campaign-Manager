from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

class Campaign(models.Model):
    subject = models.CharField(max_length=255)
    preview_text = models.CharField(max_length=255)
    article_url = models.URLField()
    html_content = models.TextField()
    plain_text_content = models.TextField()
    published_date = models.DateTimeField()
