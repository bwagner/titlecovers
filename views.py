from django.http import HttpResponse
import amazon
from  django.shortcuts import redirect

def detailurl(request, isbn):
    url = amazon.getItemUrl(isbn)
    return HttpResponse(url)

def imgurl(request, isbn, size):
    url = amazon.getImgUrl(isbn, size)
    return redirect(url)

