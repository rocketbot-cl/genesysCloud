# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re
import json

from ..utils import sanitize_for_serialization

class ScimGroupListResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ScimGroupListResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'total_results': 'int',
            'start_index': 'int',
            'items_per_page': 'int',
            'resources': 'list[ScimV2Group]',
            'schemas': 'list[str]'
        }

        self.attribute_map = {
            'total_results': 'totalResults',
            'start_index': 'startIndex',
            'items_per_page': 'itemsPerPage',
            'resources': 'Resources',
            'schemas': 'schemas'
        }

        self._total_results = None
        self._start_index = None
        self._items_per_page = None
        self._resources = None
        self._schemas = None

    @property
    def total_results(self):
        """
        Gets the total_results of this ScimGroupListResponse.
        The total number of results.

        :return: The total_results of this ScimGroupListResponse.
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """
        Sets the total_results of this ScimGroupListResponse.
        The total number of results.

        :param total_results: The total_results of this ScimGroupListResponse.
        :type: int
        """
        
        self._total_results = total_results

    @property
    def start_index(self):
        """
        Gets the start_index of this ScimGroupListResponse.
        The 1-based index of the first result returned by this request. Add this to \"itemsPerPage\" when requesting the next page of results.

        :return: The start_index of this ScimGroupListResponse.
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """
        Sets the start_index of this ScimGroupListResponse.
        The 1-based index of the first result returned by this request. Add this to \"itemsPerPage\" when requesting the next page of results.

        :param start_index: The start_index of this ScimGroupListResponse.
        :type: int
        """
        
        self._start_index = start_index

    @property
    def items_per_page(self):
        """
        Gets the items_per_page of this ScimGroupListResponse.
        The number of resources returned per page.

        :return: The items_per_page of this ScimGroupListResponse.
        :rtype: int
        """
        return self._items_per_page

    @items_per_page.setter
    def items_per_page(self, items_per_page):
        """
        Sets the items_per_page of this ScimGroupListResponse.
        The number of resources returned per page.

        :param items_per_page: The items_per_page of this ScimGroupListResponse.
        :type: int
        """
        
        self._items_per_page = items_per_page

    @property
    def resources(self):
        """
        Gets the resources of this ScimGroupListResponse.
        The list of requested resources. If \"count\" is 0, then the list will be empty.

        :return: The resources of this ScimGroupListResponse.
        :rtype: list[ScimV2Group]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this ScimGroupListResponse.
        The list of requested resources. If \"count\" is 0, then the list will be empty.

        :param resources: The resources of this ScimGroupListResponse.
        :type: list[ScimV2Group]
        """
        
        self._resources = resources

    @property
    def schemas(self):
        """
        Gets the schemas of this ScimGroupListResponse.
        The list of supported schemas.

        :return: The schemas of this ScimGroupListResponse.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """
        Sets the schemas of this ScimGroupListResponse.
        The list of supported schemas.

        :param schemas: The schemas of this ScimGroupListResponse.
        :type: list[str]
        """
        
        self._schemas = schemas

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

    def to_json(self):
        """
        Returns the model as raw JSON
        """
        return json.dumps(sanitize_for_serialization(self.to_dict()))

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
