#!/usr/bin/python

from lxml import etree

import bottlenose
amazon = bottlenose.Amazon(
    'xxx', 
    'xxx', 
    'xxx', 
    Region="DE"
)

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
