Titlecovers
===========

This project consists of a django application that provides detail-url
and images of different sizes as offered by the 
[amazon api](http://docs.amazonwebservices.com/AWSECommerceService/latest/DG/index.html) for a given product ASIN/isbn number. It uses the German amazon site, but can easily be configured to use other amazon sites (US, UK, etc.)

It uses [bottlenose](https://github.com/dlo/bottlenose) under the hood. As 
described in its [README](https://github.com/dlo/bottlenose/blob/master/README.md), before you get started, make sure you have both Amazon Product Advertising and AWS accounts. You need to enter these into a file localsettings.py according
to this format (parameters are passed along to `bottlenose.Amazon`):
    AWSAccessKeyId=...
    AWSSecretAccessKey=...
    AssociateTag=...

The application retrieves detail urls of amazon books by requesting them as follows:

    curl http://127.0.0.1:8000/titlecovers/978-3865053053/detailurl

It retrieves images of different sizes ('swatch', 'small', 'tiny', 'medium', 'large') and redirects immediately to the url given by the amazon service.

    curl -L http://127.0.0.1:8000/titlecovers/978-3865053053/small

The '-L' option is required for curl to follow the redirection.

The application caches the retrieved urls for a configurable time (default: one week). NOTE: the images themselves are not cached by the application (as this would violate amazon usage terms).


Prerequisite installs
------------------------

* [Django](https://www.djangoproject.com/)
* You need both Amazon Product Advertising and AWS accounts (see [Product Advertising API Developer Guide](http://docs.amazonwebservices.com/AWSECommerceService/latest/DG/index.html))

Authors
-------

**Bernhard Wagner**

+ http://xmlizer.net
+ http://github.com/bwagner

License
---------------------

Copyright 2011 SBS.

Licensed under GNU Affero General Public License as published by the Free Software Foundation,
either [version 3](http://www.gnu.org/licenses/agpl-3.0.html) of the License, or (at your option) any later version.
