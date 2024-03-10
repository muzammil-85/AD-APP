from django.db import models


class Stand(models.Model):
    auto_stand = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.auto_stand if self.auto_stand else self.username


class Ad(models.Model):
    stand = models.ManyToManyField(Stand, related_name='ads')
    ad_name = models.CharField(max_length=255, null=True, blank=True)
    image_ad = models.ImageField(upload_to='ads/', null=True, blank=True)
    video_ad = models.FileField(upload_to='ads/', null=True, blank=True)
    time = models.TimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now=True)
    ad_shown_duration = models.IntegerField(default=0)

    def __str__(self):
        return self.ad_name
