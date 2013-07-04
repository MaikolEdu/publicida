# encoding:utf-8
from django.db import models


class Publicidad(models.Model):

	codigo 		=	models.CharField(max_length=25, unique=True)
	imagen		=	models.FileField(upload_to='img_publi/')
	whidth		=	models.IntegerField()
	high		=	models.IntegerField()

	def __unicode__(self):
		return self.codigo
