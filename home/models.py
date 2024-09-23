from django.db import models

class Blog(models.Model):
    LANGUAGES = [
        ('en', 'English'),
        ('dv', 'Spanish'),
        # Add more languages as needed
    ]

    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    meta = models.CharField(max_length=300)
    language = models.CharField(max_length=50, choices=LANGUAGES, blank=True)  # Ensure choices are here
    content = models.TextField()
    thumbnail_img = models.ImageField(null=True, blank=True, upload_to="images/")
    thumbnail_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=255, default="uncategorized")
    slug = models.CharField(max_length=100)
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title



class Stat(models.Model):
    goals = models.CharField(max_length=200)
    ratio = models.CharField(max_length=200)
    assists = models.CharField(max_length=200)
    matches = models.CharField(max_length=200)
    titles = models.CharField(max_length=200)
    awards = models.CharField(max_length=200)

class Achievements(models.Model):
    championship = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    teams = models.CharField(max_length=200)
    achievement = models.CharField(max_length=200)