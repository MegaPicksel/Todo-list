from django.db import models


class ToDoList(models.Model):
    Task = models.CharField(max_length=300)
    Due = models.DateField(null=True)
    Done = models.BooleanField(default=False)


