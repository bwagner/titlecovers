from django.http import HttpResponse
import cacheamz
from  django.shortcuts import redirect

def detailurl(request, isbn):
    url = cacheamz.getItemUrl(isbn)
    return HttpResponse(url)

def imgurl(request, isbn, size):
    url = cacheamz.getImgUrl(isbn, size)
    return redirect(url)

