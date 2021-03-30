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

class CommonCampaign(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CommonCampaign - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'division': 'Division',
            'media_type': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'division': 'division',
            'media_type': 'mediaType',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._division = None
        self._media_type = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this CommonCampaign.
        The globally unique identifier for the object.

        :return: The id of this CommonCampaign.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CommonCampaign.
        The globally unique identifier for the object.

        :param id: The id of this CommonCampaign.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this CommonCampaign.
        The name of the Campaign.

        :return: The name of this CommonCampaign.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CommonCampaign.
        The name of the Campaign.

        :param name: The name of this CommonCampaign.
        :type: str
        """
        
        self._name = name

    @property
    def division(self):
        """
        Gets the division of this CommonCampaign.
        The division to which this entity belongs.

        :return: The division of this CommonCampaign.
        :rtype: Division
        """
        return self._division

    @division.setter
    def division(self, division):
        """
        Sets the division of this CommonCampaign.
        The division to which this entity belongs.

        :param division: The division of this CommonCampaign.
        :type: Division
        """
        
        self._division = division

    @property
    def media_type(self):
        """
        Gets the media_type of this CommonCampaign.
        The media type used for this campaign.

        :return: The media_type of this CommonCampaign.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """
        Sets the media_type of this CommonCampaign.
        The media type used for this campaign.

        :param media_type: The media_type of this CommonCampaign.
        :type: str
        """
        allowed_values = ["sms", "voice"]
        if media_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for media_type -> " + media_type)
            self._media_type = "outdated_sdk_version"
        else:
            self._media_type = media_type

    @property
    def self_uri(self):
        """
        Gets the self_uri of this CommonCampaign.
        The URI for this object

        :return: The self_uri of this CommonCampaign.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this CommonCampaign.
        The URI for this object

        :param self_uri: The self_uri of this CommonCampaign.
        :type: str
        """
        
        self._self_uri = self_uri

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
