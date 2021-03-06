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

class CreateActivityCodeRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CreateActivityCodeRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'category': 'str',
            'length_in_minutes': 'int',
            'counts_as_paid_time': 'bool',
            'counts_as_work_time': 'bool',
            'agent_time_off_selectable': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'category': 'category',
            'length_in_minutes': 'lengthInMinutes',
            'counts_as_paid_time': 'countsAsPaidTime',
            'counts_as_work_time': 'countsAsWorkTime',
            'agent_time_off_selectable': 'agentTimeOffSelectable'
        }

        self._name = None
        self._category = None
        self._length_in_minutes = None
        self._counts_as_paid_time = None
        self._counts_as_work_time = None
        self._agent_time_off_selectable = None

    @property
    def name(self):
        """
        Gets the name of this CreateActivityCodeRequest.
        The name of the activity code

        :return: The name of this CreateActivityCodeRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateActivityCodeRequest.
        The name of the activity code

        :param name: The name of this CreateActivityCodeRequest.
        :type: str
        """
        
        self._name = name

    @property
    def category(self):
        """
        Gets the category of this CreateActivityCodeRequest.
        The activity code's category

        :return: The category of this CreateActivityCodeRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this CreateActivityCodeRequest.
        The activity code's category

        :param category: The category of this CreateActivityCodeRequest.
        :type: str
        """
        allowed_values = ["OnQueueWork", "Break", "Meal", "Meeting", "OffQueueWork", "TimeOff", "Training", "Unavailable", "Unscheduled"]
        if category.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for category -> " + category)
            self._category = "outdated_sdk_version"
        else:
            self._category = category

    @property
    def length_in_minutes(self):
        """
        Gets the length_in_minutes of this CreateActivityCodeRequest.
        The default length of the activity in minutes

        :return: The length_in_minutes of this CreateActivityCodeRequest.
        :rtype: int
        """
        return self._length_in_minutes

    @length_in_minutes.setter
    def length_in_minutes(self, length_in_minutes):
        """
        Sets the length_in_minutes of this CreateActivityCodeRequest.
        The default length of the activity in minutes

        :param length_in_minutes: The length_in_minutes of this CreateActivityCodeRequest.
        :type: int
        """
        
        self._length_in_minutes = length_in_minutes

    @property
    def counts_as_paid_time(self):
        """
        Gets the counts_as_paid_time of this CreateActivityCodeRequest.
        Whether an agent is paid while performing this activity

        :return: The counts_as_paid_time of this CreateActivityCodeRequest.
        :rtype: bool
        """
        return self._counts_as_paid_time

    @counts_as_paid_time.setter
    def counts_as_paid_time(self, counts_as_paid_time):
        """
        Sets the counts_as_paid_time of this CreateActivityCodeRequest.
        Whether an agent is paid while performing this activity

        :param counts_as_paid_time: The counts_as_paid_time of this CreateActivityCodeRequest.
        :type: bool
        """
        
        self._counts_as_paid_time = counts_as_paid_time

    @property
    def counts_as_work_time(self):
        """
        Gets the counts_as_work_time of this CreateActivityCodeRequest.
        Indicates whether or not the activity should be counted as work time

        :return: The counts_as_work_time of this CreateActivityCodeRequest.
        :rtype: bool
        """
        return self._counts_as_work_time

    @counts_as_work_time.setter
    def counts_as_work_time(self, counts_as_work_time):
        """
        Sets the counts_as_work_time of this CreateActivityCodeRequest.
        Indicates whether or not the activity should be counted as work time

        :param counts_as_work_time: The counts_as_work_time of this CreateActivityCodeRequest.
        :type: bool
        """
        
        self._counts_as_work_time = counts_as_work_time

    @property
    def agent_time_off_selectable(self):
        """
        Gets the agent_time_off_selectable of this CreateActivityCodeRequest.
        Whether an agent can select this activity code when creating or editing a time off request

        :return: The agent_time_off_selectable of this CreateActivityCodeRequest.
        :rtype: bool
        """
        return self._agent_time_off_selectable

    @agent_time_off_selectable.setter
    def agent_time_off_selectable(self, agent_time_off_selectable):
        """
        Sets the agent_time_off_selectable of this CreateActivityCodeRequest.
        Whether an agent can select this activity code when creating or editing a time off request

        :param agent_time_off_selectable: The agent_time_off_selectable of this CreateActivityCodeRequest.
        :type: bool
        """
        
        self._agent_time_off_selectable = agent_time_off_selectable

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

