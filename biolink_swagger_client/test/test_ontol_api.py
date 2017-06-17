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
from swagger_client.apis.ontol_api import OntolApi


class TestOntolApi(unittest.TestCase):
    """ OntolApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.ontol_api.OntolApi()

    def tearDown(self):
        pass

    def test_get_information_content_resource(self):
        """
        Test case for get_information_content_resource

        Returns information content (IC) for a set of relevant ontology classes
        """
        pass


if __name__ == '__main__':
    unittest.main()
