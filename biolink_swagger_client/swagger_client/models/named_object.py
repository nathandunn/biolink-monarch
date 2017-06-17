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


class NamedObject(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, types=None, categories=None, replaced_by=None, synonyms=None, label=None, deprecated=None, id=None, description=None, consider=None):
        """
        NamedObject - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'types': 'list[str]',
            'categories': 'list[str]',
            'replaced_by': 'list[str]',
            'synonyms': 'list[SynonymPropertyValue]',
            'label': 'str',
            'deprecated': 'bool',
            'id': 'str',
            'description': 'str',
            'consider': 'list[str]'
        }

        self.attribute_map = {
            'types': 'types',
            'categories': 'categories',
            'replaced_by': 'replaced_by',
            'synonyms': 'synonyms',
            'label': 'label',
            'deprecated': 'deprecated',
            'id': 'id',
            'description': 'description',
            'consider': 'consider'
        }

        self._types = types
        self._categories = categories
        self._replaced_by = replaced_by
        self._synonyms = synonyms
        self._label = label
        self._deprecated = deprecated
        self._id = id
        self._description = description
        self._consider = consider

    @property
    def types(self):
        """
        Gets the types of this NamedObject.

        :return: The types of this NamedObject.
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """
        Sets the types of this NamedObject.

        :param types: The types of this NamedObject.
        :type: list[str]
        """

        self._types = types

    @property
    def categories(self):
        """
        Gets the categories of this NamedObject.

        :return: The categories of this NamedObject.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this NamedObject.

        :param categories: The categories of this NamedObject.
        :type: list[str]
        """

        self._categories = categories

    @property
    def replaced_by(self):
        """
        Gets the replaced_by of this NamedObject.

        :return: The replaced_by of this NamedObject.
        :rtype: list[str]
        """
        return self._replaced_by

    @replaced_by.setter
    def replaced_by(self, replaced_by):
        """
        Sets the replaced_by of this NamedObject.

        :param replaced_by: The replaced_by of this NamedObject.
        :type: list[str]
        """

        self._replaced_by = replaced_by

    @property
    def synonyms(self):
        """
        Gets the synonyms of this NamedObject.
        list of synonyms or alternate labels

        :return: The synonyms of this NamedObject.
        :rtype: list[SynonymPropertyValue]
        """
        return self._synonyms

    @synonyms.setter
    def synonyms(self, synonyms):
        """
        Sets the synonyms of this NamedObject.
        list of synonyms or alternate labels

        :param synonyms: The synonyms of this NamedObject.
        :type: list[SynonymPropertyValue]
        """

        self._synonyms = synonyms

    @property
    def label(self):
        """
        Gets the label of this NamedObject.
        RDFS Label

        :return: The label of this NamedObject.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this NamedObject.
        RDFS Label

        :param label: The label of this NamedObject.
        :type: str
        """

        self._label = label

    @property
    def deprecated(self):
        """
        Gets the deprecated of this NamedObject.
        True if the node is deprecated/obsoleted.

        :return: The deprecated of this NamedObject.
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """
        Sets the deprecated of this NamedObject.
        True if the node is deprecated/obsoleted.

        :param deprecated: The deprecated of this NamedObject.
        :type: bool
        """

        self._deprecated = deprecated

    @property
    def id(self):
        """
        Gets the id of this NamedObject.
        ID or CURIE e.g. MGI:1201606

        :return: The id of this NamedObject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this NamedObject.
        ID or CURIE e.g. MGI:1201606

        :param id: The id of this NamedObject.
        :type: str
        """

        self._id = id

    @property
    def description(self):
        """
        Gets the description of this NamedObject.
        Descriptive text for the entity. For ontology classes, this will be a definition.

        :return: The description of this NamedObject.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this NamedObject.
        Descriptive text for the entity. For ontology classes, this will be a definition.

        :param description: The description of this NamedObject.
        :type: str
        """

        self._description = description

    @property
    def consider(self):
        """
        Gets the consider of this NamedObject.

        :return: The consider of this NamedObject.
        :rtype: list[str]
        """
        return self._consider

    @consider.setter
    def consider(self, consider):
        """
        Sets the consider of this NamedObject.

        :param consider: The consider of this NamedObject.
        :type: list[str]
        """

        self._consider = consider

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
        if not isinstance(other, NamedObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
