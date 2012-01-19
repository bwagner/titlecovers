#   This file is part of titlecovers.
#
#   titlecovers is free software: you can redistribute it and/or modify it
#   under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   titlecovers is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#   Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public
#   License along with titlecovers. If not, see <http://www.gnu.org/licenses/>.

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

