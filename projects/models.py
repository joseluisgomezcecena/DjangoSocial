from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    # image = models.ImageField(upload_to='projects/images/')
    demo_link = models.CharField(max_length=255, null=True, blank=True)
    source_link = models.CharField(max_length=255, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # id = models.AutoField(primary_key=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews')
    #owner = models.CharField(max_length=255)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=255, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
