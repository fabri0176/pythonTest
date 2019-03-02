from django.db import models


class Course(models.Model):
    create_at = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=180)
    description = models.TextField()

    def __str__(self):
        return "Curso: {}, Descripción: {}".format(self.name, self.description)
