#!/usr/bin/env python

class Shapes(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            'ShapesLinks': 'list[ResourceUriElement]',
            'SelfUri': 'ResourceUri',
            'AlternateLinks': 'list[ResourceUri]',
            'Links': 'list[ResourceUri]'

        }

        self.attributeMap = {
            'ShapesLinks': 'ShapesLinks','SelfUri': 'SelfUri','AlternateLinks': 'AlternateLinks','Links': 'Links'}       

        self.ShapesLinks = None # list[ResourceUriElement]
        self.SelfUri = None # ResourceUri
        self.AlternateLinks = None # list[ResourceUri]
        self.Links = None # list[ResourceUri]
        
