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

class EdgeLogsJobRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EdgeLogsJobRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'path': 'str',
            'query': 'str',
            'recurse': 'bool'
        }

        self.attribute_map = {
            'path': 'path',
            'query': 'query',
            'recurse': 'recurse'
        }

        self._path = None
        self._query = None
        self._recurse = None

    @property
    def path(self):
        """
        Gets the path of this EdgeLogsJobRequest.
        A relative directory to the root Edge log folder to query from.

        :return: The path of this EdgeLogsJobRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this EdgeLogsJobRequest.
        A relative directory to the root Edge log folder to query from.

        :param path: The path of this EdgeLogsJobRequest.
        :type: str
        """
        
        self._path = path

    @property
    def query(self):
        """
        Gets the query of this EdgeLogsJobRequest.
        The pattern to use when searching for logs, which may include the wildcards {*, ?}.  Multiple search patterns may be combined using a pipe '|' as a delimiter.

        :return: The query of this EdgeLogsJobRequest.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this EdgeLogsJobRequest.
        The pattern to use when searching for logs, which may include the wildcards {*, ?}.  Multiple search patterns may be combined using a pipe '|' as a delimiter.

        :param query: The query of this EdgeLogsJobRequest.
        :type: str
        """
        
        self._query = query

    @property
    def recurse(self):
        """
        Gets the recurse of this EdgeLogsJobRequest.
        Boolean whether or not to recurse into directories.

        :return: The recurse of this EdgeLogsJobRequest.
        :rtype: bool
        """
        return self._recurse

    @recurse.setter
    def recurse(self, recurse):
        """
        Sets the recurse of this EdgeLogsJobRequest.
        Boolean whether or not to recurse into directories.

        :param recurse: The recurse of this EdgeLogsJobRequest.
        :type: bool
        """
        
        self._recurse = recurse

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
