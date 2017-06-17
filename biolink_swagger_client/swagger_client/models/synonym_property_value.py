# coding: utf-8

"""
    BioLink API

    API integration layer for linked biological objects.   __Source:__ https://github.com/monarch-initiative/biolink-api/

    OpenAPI spec version: 0.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SynonymPropertyValue(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, xrefs=None, pred=None, val=None):
        """
        SynonymPropertyValue - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'xrefs': 'list[str]',
            'pred': 'str',
            'val': 'str'
        }

        self.attribute_map = {
            'xrefs': 'xrefs',
            'pred': 'pred',
            'val': 'val'
        }

        self._xrefs = xrefs
        self._pred = pred
        self._val = val

    @property
    def xrefs(self):
        """
        Gets the xrefs of this SynonymPropertyValue.
        Xrefs provenance for property-value

        :return: The xrefs of this SynonymPropertyValue.
        :rtype: list[str]
        """
        return self._xrefs

    @xrefs.setter
    def xrefs(self, xrefs):
        """
        Sets the xrefs of this SynonymPropertyValue.
        Xrefs provenance for property-value

        :param xrefs: The xrefs of this SynonymPropertyValue.
        :type: list[str]
        """

        self._xrefs = xrefs

    @property
    def pred(self):
        """
        Gets the pred of this SynonymPropertyValue.
        predicate (attribute) part

        :return: The pred of this SynonymPropertyValue.
        :rtype: str
        """
        return self._pred

    @pred.setter
    def pred(self, pred):
        """
        Sets the pred of this SynonymPropertyValue.
        predicate (attribute) part

        :param pred: The pred of this SynonymPropertyValue.
        :type: str
        """

        self._pred = pred

    @property
    def val(self):
        """
        Gets the val of this SynonymPropertyValue.
        value part

        :return: The val of this SynonymPropertyValue.
        :rtype: str
        """
        return self._val

    @val.setter
    def val(self, val):
        """
        Sets the val of this SynonymPropertyValue.
        value part

        :param val: The val of this SynonymPropertyValue.
        :type: str
        """

        self._val = val

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, SynonymPropertyValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
