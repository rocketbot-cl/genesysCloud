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

class DialerResponsesetConfigChangeResponseSet(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DialerResponsesetConfigChangeResponseSet - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'version': 'int',
            'responses': 'dict(str, DialerResponsesetConfigChangeReaction)',
            'beep_detection_enabled': 'bool',
            'additional_properties': 'object'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'version': 'version',
            'responses': 'responses',
            'beep_detection_enabled': 'beepDetectionEnabled',
            'additional_properties': 'additionalProperties'
        }

        self._id = None
        self._name = None
        self._date_created = None
        self._date_modified = None
        self._version = None
        self._responses = None
        self._beep_detection_enabled = None
        self._additional_properties = None

    @property
    def id(self):
        """
        Gets the id of this DialerResponsesetConfigChangeResponseSet.


        :return: The id of this DialerResponsesetConfigChangeResponseSet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DialerResponsesetConfigChangeResponseSet.


        :param id: The id of this DialerResponsesetConfigChangeResponseSet.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this DialerResponsesetConfigChangeResponseSet.


        :return: The name of this DialerResponsesetConfigChangeResponseSet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DialerResponsesetConfigChangeResponseSet.


        :param name: The name of this DialerResponsesetConfigChangeResponseSet.
        :type: str
        """
        
        self._name = name

    @property
    def date_created(self):
        """
        Gets the date_created of this DialerResponsesetConfigChangeResponseSet.


        :return: The date_created of this DialerResponsesetConfigChangeResponseSet.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this DialerResponsesetConfigChangeResponseSet.


        :param date_created: The date_created of this DialerResponsesetConfigChangeResponseSet.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this DialerResponsesetConfigChangeResponseSet.


        :return: The date_modified of this DialerResponsesetConfigChangeResponseSet.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this DialerResponsesetConfigChangeResponseSet.


        :param date_modified: The date_modified of this DialerResponsesetConfigChangeResponseSet.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def version(self):
        """
        Gets the version of this DialerResponsesetConfigChangeResponseSet.


        :return: The version of this DialerResponsesetConfigChangeResponseSet.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this DialerResponsesetConfigChangeResponseSet.


        :param version: The version of this DialerResponsesetConfigChangeResponseSet.
        :type: int
        """
        
        self._version = version

    @property
    def responses(self):
        """
        Gets the responses of this DialerResponsesetConfigChangeResponseSet.


        :return: The responses of this DialerResponsesetConfigChangeResponseSet.
        :rtype: dict(str, DialerResponsesetConfigChangeReaction)
        """
        return self._responses

    @responses.setter
    def responses(self, responses):
        """
        Sets the responses of this DialerResponsesetConfigChangeResponseSet.


        :param responses: The responses of this DialerResponsesetConfigChangeResponseSet.
        :type: dict(str, DialerResponsesetConfigChangeReaction)
        """
        
        self._responses = responses

    @property
    def beep_detection_enabled(self):
        """
        Gets the beep_detection_enabled of this DialerResponsesetConfigChangeResponseSet.


        :return: The beep_detection_enabled of this DialerResponsesetConfigChangeResponseSet.
        :rtype: bool
        """
        return self._beep_detection_enabled

    @beep_detection_enabled.setter
    def beep_detection_enabled(self, beep_detection_enabled):
        """
        Sets the beep_detection_enabled of this DialerResponsesetConfigChangeResponseSet.


        :param beep_detection_enabled: The beep_detection_enabled of this DialerResponsesetConfigChangeResponseSet.
        :type: bool
        """
        
        self._beep_detection_enabled = beep_detection_enabled

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this DialerResponsesetConfigChangeResponseSet.


        :return: The additional_properties of this DialerResponsesetConfigChangeResponseSet.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this DialerResponsesetConfigChangeResponseSet.


        :param additional_properties: The additional_properties of this DialerResponsesetConfigChangeResponseSet.
        :type: object
        """
        
        self._additional_properties = additional_properties

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
