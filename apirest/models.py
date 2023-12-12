from django.db import models

# Create your models here.
class Priority(models.Model):
    name = models.CharField(max_length=40, default='High')

    def __str__(self):
        return self.name


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
    status = models.CharField(max_length = 10, choices = STATUS_NAME, default = 'Backlog')
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, default = 1)

    def __str__(self):
        return self.name