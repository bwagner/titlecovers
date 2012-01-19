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

import amazon
import datetime
from titlecovers.models import AmazonInfo

# timedelta(weeks=, days=, hours=, minutes=, seconds=)
year = datetime.timedelta(days=365)
week = datetime.timedelta(weeks=1)
day = datetime.timedelta(days=1)
hour = datetime.timedelta(hours=1)
minute = datetime.timedelta(minutes=1)
tensecs = datetime.timedelta(seconds=10)
twensecs = datetime.timedelta(seconds=20)
maxage = week

def getItemUrl(theIsbn):
    amz = __getAmazon__(theIsbn)
#    print "getItemUrl: amz: " + str(amz)
    url = amz.detailurl
#    print "getItemUrl: " + str(url)
    return url

def getImgUrl(theIsbn, theSize):
    amz = __getAmazon__(theIsbn)
#    print "getImgUrl: amz: " + str(amz)
    url = amz.getImgUrl(theSize)
#    print "getImgUrl: " + str(url)
    return url

def __getAmazon__(theIsbn):
#    print "__getAmazon__" + theIsbn
    # TODO race condition
    theIsbn = amazon.normalizeIsbn(theIsbn)
    hits = AmazonInfo.objects.filter(isbn=theIsbn)
    if(len(hits) > 0):
        obj = hits[0]
#        print "retrieved locally:" + str(obj)
        if datetime.datetime.now() - obj.lastretrieved < maxage :
            return obj
        else:
#            print "but timed out, deleting"
            obj.delete()

#    print "retrieving from amazon"
    imgs = amazon.getAllImages(theIsbn);

    obj = AmazonInfo(
        isbn=theIsbn, 
        lastretrieved=datetime.datetime.now(),
        detailurl = amazon.getItemUrl(theIsbn)
    )
    i = 0
    obj.swatchimgurl = imgs[i]
    i+=1
    obj.smallimgurl = imgs[i]
    i+=1
    obj.tinyimgurl = imgs[i]
    i+=1
    obj.mediumimgurl = imgs[i]
    i+=1
    obj.largeimgurl = imgs[i]

    obj.save()
    return obj
