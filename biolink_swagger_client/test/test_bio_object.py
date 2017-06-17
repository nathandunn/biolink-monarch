# coding: utf-8

"""
    BioLink API

    API integration layer for linked biological objects.   __Source:__ https://github.com/monarch-initiative/biolink-api/

    OpenAPI spec version: 0.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.bio_object import BioObject


class TestBioObject(unittest.TestCase):
    """ BioObject unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBioObject(self):
        """
        Test BioObject
        """
        model = swagger_client.models.bio_object.BioObject()


if __name__ == '__main__':
    unittest.main()
