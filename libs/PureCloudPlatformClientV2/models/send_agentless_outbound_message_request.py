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

class SendAgentlessOutboundMessageRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SendAgentlessOutboundMessageRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'from_address': 'str',
            'to_address': 'str',
            'to_address_messenger_type': 'str',
            'text_body': 'str'
        }

        self.attribute_map = {
            'from_address': 'fromAddress',
            'to_address': 'toAddress',
            'to_address_messenger_type': 'toAddressMessengerType',
            'text_body': 'textBody'
        }

        self._from_address = None
        self._to_address = None
        self._to_address_messenger_type = None
        self._text_body = None

    @property
    def from_address(self):
        """
        Gets the from_address of this SendAgentlessOutboundMessageRequest.
        The messaging address of the sender of the message. For an SMS messenger type, this must be a currently provisioned sms phone number.

        :return: The from_address of this SendAgentlessOutboundMessageRequest.
        :rtype: str
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """
        Sets the from_address of this SendAgentlessOutboundMessageRequest.
        The messaging address of the sender of the message. For an SMS messenger type, this must be a currently provisioned sms phone number.

        :param from_address: The from_address of this SendAgentlessOutboundMessageRequest.
        :type: str
        """
        
        self._from_address = from_address

    @property
    def to_address(self):
        """
        Gets the to_address of this SendAgentlessOutboundMessageRequest.
        The messaging address of the recipient of the message. For an SMS messenger type, the phone number address must be in E.164 format. E.g. +13175555555 or +34234234234.

        :return: The to_address of this SendAgentlessOutboundMessageRequest.
        :rtype: str
        """
        return self._to_address

    @to_address.setter
    def to_address(self, to_address):
        """
        Sets the to_address of this SendAgentlessOutboundMessageRequest.
        The messaging address of the recipient of the message. For an SMS messenger type, the phone number address must be in E.164 format. E.g. +13175555555 or +34234234234.

        :param to_address: The to_address of this SendAgentlessOutboundMessageRequest.
        :type: str
        """
        
        self._to_address = to_address

    @property
    def to_address_messenger_type(self):
        """
        Gets the to_address_messenger_type of this SendAgentlessOutboundMessageRequest.
        The recipient messaging address messenger type. Currently SMS is the only supported type.

        :return: The to_address_messenger_type of this SendAgentlessOutboundMessageRequest.
        :rtype: str
        """
        return self._to_address_messenger_type

    @to_address_messenger_type.setter
    def to_address_messenger_type(self, to_address_messenger_type):
        """
        Sets the to_address_messenger_type of this SendAgentlessOutboundMessageRequest.
        The recipient messaging address messenger type. Currently SMS is the only supported type.

        :param to_address_messenger_type: The to_address_messenger_type of this SendAgentlessOutboundMessageRequest.
        :type: str
        """
        allowed_values = ["sms", "facebook", "twitter", "line", "whatsapp", "webmessaging", "open"]
        if to_address_messenger_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for to_address_messenger_type -> " + to_address_messenger_type)
            self._to_address_messenger_type = "outdated_sdk_version"
        else:
            self._to_address_messenger_type = to_address_messenger_type

    @property
    def text_body(self):
        """
        Gets the text_body of this SendAgentlessOutboundMessageRequest.
        The text of the message to send

        :return: The text_body of this SendAgentlessOutboundMessageRequest.
        :rtype: str
        """
        return self._text_body

    @text_body.setter
    def text_body(self, text_body):
        """
        Sets the text_body of this SendAgentlessOutboundMessageRequest.
        The text of the message to send

        :param text_body: The text_body of this SendAgentlessOutboundMessageRequest.
        :type: str
        """
        
        self._text_body = text_body

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
