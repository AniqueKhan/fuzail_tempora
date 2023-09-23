from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name} messaged {self.message} at {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
