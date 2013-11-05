'''
Examples for reading extensible markup language (XML) files.
'''
import unittest

def readXml():
    from xml.etree import ElementTree

    sourceXmlPath = 'customers.xml'
    customerTree = ElementTree.parse(sourceXmlPath)

    # Obtain document root element <customers>.
    customerRoot = customerTree.getroot()

    # Print the tags of all customer elements and their attributes.
    for customer in customerRoot:
        print(customer.tag, customer.attrib)

    # Print all surnames (using an XPath expression).
    xpathToFind = './customer/surname'
    for surnameElement in customerRoot.findall(xpathToFind):
        print(surnameElement.text)


def readXmlWithNamespace():
    from xml.etree import ElementTree

    sourceXmlPath = 'customers_namespace.xml'
    customerTree = ElementTree.parse(sourceXmlPath)

    # Obtain document root element <customers>.
    customerRoot = customerTree.getroot()

    # Print the tags of all customer elements and their attributes.
    for customer in customerRoot:
        print(customer.tag, customer.attrib)

    # Print all surnames (using an XPath expression).
    xpathToFind = \
        './' + \
        '{http://www.example.com/crm}customer/' + \
        '{http://www.example.com/crm}surname'
    for surnameElement in customerRoot.findall(xpathToFind):
        print(surnameElement.text)


class XmlTest(unittest.TestCase):
    def testCanReadXml(self):
        readXml()
        readXmlWithNamespace()


if __name__ == '__main__':
    unittest.main()
