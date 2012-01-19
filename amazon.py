#!/usr/bin/python
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


from lxml import etree

import bottlenose

try:
    import localsettings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'localsettings.py' in the directory containing %r. (If the file localsettings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

allvars = dict(vars(localsettings))
unwanted = set(allvars) - set(['AWSAccessKeyId', 'AWSSecretAccessKey', 'AssociateTag', 'Operation', 'Style', 'Version', 'Region', 'Timeout'])
for unwanted_key in unwanted: del allvars[unwanted_key]

amazon = bottlenose.Amazon(**allvars)

ns = {'ns': "http://webservices.amazon.com/AWSECommerceService/2010-11-01"}

xpaths = {
        'swatch': '//ns:ImageSets[1]/ns:ImageSet[1]/ns:SwatchImage[1]/ns:URL[1]',
        'small': '//ns:ImageSets[1]/ns:ImageSet[1]/ns:SmallImage[1]/ns:URL[1]',
        'tiny': '//ns:ImageSets[1]/ns:ImageSet[1]/ns:TinyImage[1]/ns:URL[1]',
        'medium': '//ns:ImageSets[1]/ns:ImageSet[1]/ns:MediumImage[1]/ns:URL[1]',
        'large': '//ns:ImageSets[1]/ns:ImageSet[1]/ns:LargeImage[1]/ns:URL[1]',
        }

def getImgUrl(isbn, size):
    isbn = normalizeIsbn(isbn)
    if(size in xpaths):
        xpath = xpaths[size]
    else:
        #TODO: possibly notify user of error condition
        xpath = xpaths['small']

    response = amazon.ItemLookup( 
        ItemId = isbn, 
        ResponseGroup = "Images", 
        SearchIndex = "Books", 
        IdType = "ISBN"
    )
    tree = etree.fromstring(response)
    return tree.xpath(xpath, namespaces=ns)[0].text

def getItemUrl(isbn):
    isbn = normalizeIsbn(isbn)
    response = amazon.ItemLookup( ItemId = isbn, ResponseGroup = "ItemAttributes", SearchIndex = "Books", IdType = "ISBN")
    tree = etree.fromstring(response)
    return tree.xpath("/ns:ItemLookupResponse/ns:Items[1]/ns:Item[1]/ns:DetailPageURL[1]", namespaces=ns)[0].text

def getItemAttributes(isbn):
    isbn = normalizeIsbn(isbn)
    response = amazon.ItemLookup( ItemId = isbn, ResponseGroup = "ItemAttributes", SearchIndex = "Books", IdType = "ISBN")
    return response

def normalizeIsbn(isbn):
    return isbn.replace('-','')

def getAllImages(isbn):
    """Returns all image urls as list

    in order swatch, small, tiny, medium, large"""
    sizes = ['swatch', 'small', 'tiny', 'medium', 'large']
    isbn = normalizeIsbn(isbn)
    response = amazon.ItemLookup( ItemId = isbn, ResponseGroup = "Images", SearchIndex = "Books", IdType = "ISBN")
    tree = etree.fromstring(response)
    result = [tree.xpath(xpaths[size], namespaces=ns)[0].text for size in sizes ]
    return result

def getAllImagesRaw(isbn):
    isbn = normalizeIsbn(isbn)
    response = amazon.ItemLookup( ItemId = isbn, ResponseGroup = "Images", SearchIndex = "Books", IdType = "ISBN")
    return response

def test():
    import unittest
    class Test(unittest.TestCase):
        def test_normalizeIsbnNone(self):
            self.assertEqual("9783866480919", normalizeIsbn("9783866480919"))
        def test_normalizeIsbn(self):
            self.assertEqual("9783866480919", normalizeIsbn("978-3-86648-091-9"))
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    import sys
    import os.path
    if(len(sys.argv) != 2):
        print "\n\tusage: ",os.path.basename(sys.argv[0]) ," [isbn | 'test']\n"
        exit(1)
    arg = sys.argv[1]
    if(arg == "test"):
        test()
    else:
        print normalizeIsbn(int(arg))
