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

class VoicemailOrganizationPolicy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        VoicemailOrganizationPolicy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'enabled': 'bool',
            'alert_timeout_seconds': 'int',
            'pin_configuration': 'PINConfiguration',
            'voicemail_extension': 'str',
            'pin_required': 'bool',
            'send_email_notifications': 'bool',
            'modified_date': 'datetime'
        }

        self.attribute_map = {
            'enabled': 'enabled',
            'alert_timeout_seconds': 'alertTimeoutSeconds',
            'pin_configuration': 'pinConfiguration',
            'voicemail_extension': 'voicemailExtension',
            'pin_required': 'pinRequired',
            'send_email_notifications': 'sendEmailNotifications',
            'modified_date': 'modifiedDate'
        }

        self._enabled = None
        self._alert_timeout_seconds = None
        self._pin_configuration = None
        self._voicemail_extension = None
        self._pin_required = None
        self._send_email_notifications = None
        self._modified_date = None

    @property
    def enabled(self):
        """
        Gets the enabled of this VoicemailOrganizationPolicy.
        Whether voicemail is enable for this organization

        :return: The enabled of this VoicemailOrganizationPolicy.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this VoicemailOrganizationPolicy.
        Whether voicemail is enable for this organization

        :param enabled: The enabled of this VoicemailOrganizationPolicy.
        :type: bool
        """
        
        self._enabled = enabled

    @property
    def alert_timeout_seconds(self):
        """
        Gets the alert_timeout_seconds of this VoicemailOrganizationPolicy.
        The organization's default number of seconds to ring a user's phone before a call is transfered to voicemail

        :return: The alert_timeout_seconds of this VoicemailOrganizationPolicy.
        :rtype: int
        """
        return self._alert_timeout_seconds

    @alert_timeout_seconds.setter
    def alert_timeout_seconds(self, alert_timeout_seconds):
        """
        Sets the alert_timeout_seconds of this VoicemailOrganizationPolicy.
        The organization's default number of seconds to ring a user's phone before a call is transfered to voicemail

        :param alert_timeout_seconds: The alert_timeout_seconds of this VoicemailOrganizationPolicy.
        :type: int
        """
        
        self._alert_timeout_seconds = alert_timeout_seconds

    @property
    def pin_configuration(self):
        """
        Gets the pin_configuration of this VoicemailOrganizationPolicy.
        The configuration for user PINs to access their voicemail from a phone

        :return: The pin_configuration of this VoicemailOrganizationPolicy.
        :rtype: PINConfiguration
        """
        return self._pin_configuration

    @pin_configuration.setter
    def pin_configuration(self, pin_configuration):
        """
        Sets the pin_configuration of this VoicemailOrganizationPolicy.
        The configuration for user PINs to access their voicemail from a phone

        :param pin_configuration: The pin_configuration of this VoicemailOrganizationPolicy.
        :type: PINConfiguration
        """
        
        self._pin_configuration = pin_configuration

    @property
    def voicemail_extension(self):
        """
        Gets the voicemail_extension of this VoicemailOrganizationPolicy.
        The extension for voicemail retrieval.  The default value is *86.

        :return: The voicemail_extension of this VoicemailOrganizationPolicy.
        :rtype: str
        """
        return self._voicemail_extension

    @voicemail_extension.setter
    def voicemail_extension(self, voicemail_extension):
        """
        Sets the voicemail_extension of this VoicemailOrganizationPolicy.
        The extension for voicemail retrieval.  The default value is *86.

        :param voicemail_extension: The voicemail_extension of this VoicemailOrganizationPolicy.
        :type: str
        """
        
        self._voicemail_extension = voicemail_extension

    @property
    def pin_required(self):
        """
        Gets the pin_required of this VoicemailOrganizationPolicy.
        If this is true, a PIN is required when accessing a user's voicemail from a phone.

        :return: The pin_required of this VoicemailOrganizationPolicy.
        :rtype: bool
        """
        return self._pin_required

    @pin_required.setter
    def pin_required(self, pin_required):
        """
        Sets the pin_required of this VoicemailOrganizationPolicy.
        If this is true, a PIN is required when accessing a user's voicemail from a phone.

        :param pin_required: The pin_required of this VoicemailOrganizationPolicy.
        :type: bool
        """
        
        self._pin_required = pin_required

    @property
    def send_email_notifications(self):
        """
        Gets the send_email_notifications of this VoicemailOrganizationPolicy.
        Whether email notifications are sent for new voicemails in the organization. If false, new voicemail email notifications are not be sent for the organization overriding any user or group setting.

        :return: The send_email_notifications of this VoicemailOrganizationPolicy.
        :rtype: bool
        """
        return self._send_email_notifications

    @send_email_notifications.setter
    def send_email_notifications(self, send_email_notifications):
        """
        Sets the send_email_notifications of this VoicemailOrganizationPolicy.
        Whether email notifications are sent for new voicemails in the organization. If false, new voicemail email notifications are not be sent for the organization overriding any user or group setting.

        :param send_email_notifications: The send_email_notifications of this VoicemailOrganizationPolicy.
        :type: bool
        """
        
        self._send_email_notifications = send_email_notifications

    @property
    def modified_date(self):
        """
        Gets the modified_date of this VoicemailOrganizationPolicy.
        The date the policy was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The modified_date of this VoicemailOrganizationPolicy.
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """
        Sets the modified_date of this VoicemailOrganizationPolicy.
        The date the policy was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param modified_date: The modified_date of this VoicemailOrganizationPolicy.
        :type: datetime
        """
        
        self._modified_date = modified_date

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
