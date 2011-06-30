from django.db import models

class AmazonInfo(models.Model):
	isbn = models.CharField(max_length=20, primary_key=True)
	swatchimgurl = models.CharField(max_length=200)
	smallimgurl = models.CharField(max_length=200)
	tinyimgurl = models.CharField(max_length=200)
	mediumimgurl = models.CharField(max_length=200)
	largeimgurl = models.CharField(max_length=200)
	detailurl = models.CharField(max_length=500)
	lastretrieved = models.DateTimeField()
