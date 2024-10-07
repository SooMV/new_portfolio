from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    objective = models.TextField(blank=True)
    thumbnails1 = models.ImageField(upload_to="projects", blank=True, null=True)
    thumbnails2 = models.ImageField(upload_to="projects", blank=True, null=True)
    thumbnails3 = models.ImageField(upload_to="projects", blank=True, null=True)
    thumbnails4 = models.ImageField(upload_to="projects", blank=True, null=True)
    duration = models.DurationField()
    logo =  models.ImageField(upload_to="projects", blank=True, null=True)
    launch_screen = models.ImageField(upload_to="projects", blank=True, null=True)
    type = models.CharField(
        max_length=64, 
        choices=[('ios', 'iOS'), ('android', 'Android'), ('python', 'Python')],
        blank=True  
    )

    def __str__(self) -> str:
        return self.name
    
    def duration_in_days(self):
        return self.duration.days 
    
class MyCV(models.Model):
    title = models.CharField(max_length=50)
    pdf_file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title 