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

class CreateBusinessUnitSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CreateBusinessUnitSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'start_day_of_week': 'str',
            'time_zone': 'str',
            'short_term_forecasting': 'BuShortTermForecastingSettings'
        }

        self.attribute_map = {
            'start_day_of_week': 'startDayOfWeek',
            'time_zone': 'timeZone',
            'short_term_forecasting': 'shortTermForecasting'
        }

        self._start_day_of_week = None
        self._time_zone = None
        self._short_term_forecasting = None

    @property
    def start_day_of_week(self):
        """
        Gets the start_day_of_week of this CreateBusinessUnitSettings.
        The start day of week for this business unit

        :return: The start_day_of_week of this CreateBusinessUnitSettings.
        :rtype: str
        """
        return self._start_day_of_week

    @start_day_of_week.setter
    def start_day_of_week(self, start_day_of_week):
        """
        Sets the start_day_of_week of this CreateBusinessUnitSettings.
        The start day of week for this business unit

        :param start_day_of_week: The start_day_of_week of this CreateBusinessUnitSettings.
        :type: str
        """
        allowed_values = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        if start_day_of_week.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for start_day_of_week -> " + start_day_of_week)
            self._start_day_of_week = "outdated_sdk_version"
        else:
            self._start_day_of_week = start_day_of_week

    @property
    def time_zone(self):
        """
        Gets the time_zone of this CreateBusinessUnitSettings.
        The time zone for this business unit, using the Olsen tz database format

        :return: The time_zone of this CreateBusinessUnitSettings.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this CreateBusinessUnitSettings.
        The time zone for this business unit, using the Olsen tz database format

        :param time_zone: The time_zone of this CreateBusinessUnitSettings.
        :type: str
        """
        
        self._time_zone = time_zone

    @property
    def short_term_forecasting(self):
        """
        Gets the short_term_forecasting of this CreateBusinessUnitSettings.
        Short term forecasting settings

        :return: The short_term_forecasting of this CreateBusinessUnitSettings.
        :rtype: BuShortTermForecastingSettings
        """
        return self._short_term_forecasting

    @short_term_forecasting.setter
    def short_term_forecasting(self, short_term_forecasting):
        """
        Sets the short_term_forecasting of this CreateBusinessUnitSettings.
        Short term forecasting settings

        :param short_term_forecasting: The short_term_forecasting of this CreateBusinessUnitSettings.
        :type: BuShortTermForecastingSettings
        """
        
        self._short_term_forecasting = short_term_forecasting

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
