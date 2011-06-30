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
    def __unicode__(self):
                return str(self.isbn) + " " + str(self.lastretrieved)

    # TODO nicer solution
    def getImgUrl(self, size):
        sizes = ['swatch', 'small', 'tiny', 'medium', 'large']
        if(size == 'swatch'):
            return self.swatchimgurl
        elif(size == 'small'):
            return self.smallimgurl
        elif(size == 'tiny'):
            return self.tinyimgurl
        elif(size == 'medium'):
            return self.mediumimgurl
        elif(size == 'large'):
            return self.largeimgurl
        else:
            return None

