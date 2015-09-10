
from django.db import models


class What(models.Model):
	art_is = models.TextField(max_length='140')
