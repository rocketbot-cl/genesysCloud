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

class RoutePathResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        RoutePathResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'queue': 'QueueReference',
            'media_type': 'str',
            'language': 'LanguageReference',
            'skills': 'list[RoutingSkillReference]'
        }

        self.attribute_map = {
            'queue': 'queue',
            'media_type': 'mediaType',
            'language': 'language',
            'skills': 'skills'
        }

        self._queue = None
        self._media_type = None
        self._language = None
        self._skills = None

    @property
    def queue(self):
        """
        Gets the queue of this RoutePathResponse.
        The ID of the queue associated with the route path

        :return: The queue of this RoutePathResponse.
        :rtype: QueueReference
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """
        Sets the queue of this RoutePathResponse.
        The ID of the queue associated with the route path

        :param queue: The queue of this RoutePathResponse.
        :type: QueueReference
        """
        
        self._queue = queue

    @property
    def media_type(self):
        """
        Gets the media_type of this RoutePathResponse.
        The media type of the given queue associated with the route path

        :return: The media_type of this RoutePathResponse.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """
        Sets the media_type of this RoutePathResponse.
        The media type of the given queue associated with the route path

        :param media_type: The media_type of this RoutePathResponse.
        :type: str
        """
        allowed_values = ["Voice", "Chat", "Email", "Callback", "Message"]
        if media_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for media_type -> " + media_type)
            self._media_type = "outdated_sdk_version"
        else:
            self._media_type = media_type

    @property
    def language(self):
        """
        Gets the language of this RoutePathResponse.
        The ID of the language associated with the route path

        :return: The language of this RoutePathResponse.
        :rtype: LanguageReference
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this RoutePathResponse.
        The ID of the language associated with the route path

        :param language: The language of this RoutePathResponse.
        :type: LanguageReference
        """
        
        self._language = language

    @property
    def skills(self):
        """
        Gets the skills of this RoutePathResponse.
        The set of skills associated with the route path

        :return: The skills of this RoutePathResponse.
        :rtype: list[RoutingSkillReference]
        """
        return self._skills

    @skills.setter
    def skills(self, skills):
        """
        Sets the skills of this RoutePathResponse.
        The set of skills associated with the route path

        :param skills: The skills of this RoutePathResponse.
        :type: list[RoutingSkillReference]
        """
        
        self._skills = skills

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
