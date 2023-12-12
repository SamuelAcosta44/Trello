from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS_NAME = [
        ('BACKLOG', 'Backlog'),
        ('TO DO', 'To Do'),
        ('DOING', 'Doing'),
        ('TEST', 'Test'),
        ('DONE', 'Done')
    ]

    name = models.CharField(max_length=40)
    description = models.TextField()
    deadline = models.DateField()
    comment = models.TextField()
    status = models.CharField(max_length = 10, choices = STATUS_NAME)

    def __str__(self):
        return self.name