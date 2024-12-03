from django.db import models

# Create your predict_model here.
class Text(models.Model):
    def __str__(self):
        return self.content

    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    label = models.IntegerField()

