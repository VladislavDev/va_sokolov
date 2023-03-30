from django.db import models
from django.core.files.images import get_image_dimensions

from userprofile.models import Profile


class Feed(models.Model):
    
    pub_date = models.DateTimeField('published')
    text = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.pub_date) + ' ' + self.text
    
    @property
    def image_rows(self):
        
        if self.images.count() == 0:
            return None
        
        image_rows_groupping_template = [
            [1], [2], [1, 2], [2, 2], 
            [2, 3], [2, 4], [3, 4], [2, 6],
            [3, 3, 3], [3, 3, 4]
        ]
        image_rows_template = image_rows_groupping_template[self.images.count()-1]
        
        rows = [ {'images': [] } for i in range(len(image_rows_template))]
        
        # Images groupping in rows
        for ind, image in enumerate(self.images.all()):
            for i, row in enumerate(image_rows_template):
                if row > 0:
                    width, height = get_image_dimensions(image.image.file)
                    
                    rows[i]['images'].append({
                        'url': image.image.url,
                        'grow': width / height,
                        'index': ind
                    })
                    
                    image_rows_template[i] -= 1
                    break
        
        return rows
                    
                    
    
class FeedImage(models.Model):
    
    image = models.ImageField(upload_to='feeds-images')
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name='images')