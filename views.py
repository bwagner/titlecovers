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

from django.http import HttpResponse
import cacheamz
from  django.shortcuts import redirect

def detailurl(request, isbn):
    url = cacheamz.getItemUrl(isbn)
    return HttpResponse(url)

def imgurl(request, isbn, size):
    url = cacheamz.getImgUrl(isbn, size)
    return redirect(url)

