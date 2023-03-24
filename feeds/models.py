from django.db import models
from userprofile.models import Profile


class Feed(models.Model):
    
    pub_date = models.DateTimeField('published')
    text = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.pub_date) + ' ' + self.text
    
    
class FeedImage(models.Model):
    
    image = models.ImageField(upload_to='feeds-images')
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)