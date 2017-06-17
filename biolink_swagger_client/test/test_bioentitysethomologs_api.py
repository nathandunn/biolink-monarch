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
from swagger_client.apis.bioentitysethomologs_api import BioentitysethomologsApi


class TestBioentitysethomologsApi(unittest.TestCase):
    """ BioentitysethomologsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.bioentitysethomologs_api.BioentitysethomologsApi()

    def tearDown(self):
        pass

    def test_get_entity_set_homologs(self):
        """
        Test case for get_entity_set_homologs

        Returns homology associations for a given input set of genes
        """
        pass


if __name__ == '__main__':
    unittest.main()
