from django.db import models

class CodeExplainer(models.Model):
    _input = models.TextField()
    _output = models.TextField()

    class Meta:
        db_table = "t_code_explainer"