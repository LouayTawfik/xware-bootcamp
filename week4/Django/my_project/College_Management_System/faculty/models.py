from django.db import models

from professor import Professor

class Faculty(models.Model):
    name = models.CharField(max_length=50)
    p_id = models.ForeignKey()


