from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from .models import Priority, Task

class TaskModelTest(TestCase):
    def setUp(self):
        self.priority = Priority.objects.create(name='High')

    def test_task_creation(self):
        task = Task.objects.create(
            name='Ejemplo',
            description='Test de ejemplo',
            comment='',
            status='Test',
            priority=self.priority
        )

        saved_task = Task.objects.get(pk=task.pk)

        self.assertEqual(saved_task.name, 'Ejemplo')
        self.assertEqual(saved_task.priority, self.priority)

        expected_deadline = timezone.now().date() + timedelta(days=30)
        self.assertEqual(saved_task.deadline, expected_deadline)

        self.assertEqual(saved_task.deadline, expected_deadline)