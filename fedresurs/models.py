from django.contrib.postgres.fields.jsonb import JSONField
from django.db import models


class Guid(models.Model):
    task_guid = models.CharField(max_length=200)
    info = JSONField()

    def __str__(self):
        return self.task_guid
