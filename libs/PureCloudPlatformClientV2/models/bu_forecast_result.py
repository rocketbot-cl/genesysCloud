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

class BuForecastResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BuForecastResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'reference_start_date': 'datetime',
            'planning_groups': 'list[ForecastPlanningGroupData]',
            'week_number': 'int',
            'week_count': 'int'
        }

        self.attribute_map = {
            'reference_start_date': 'referenceStartDate',
            'planning_groups': 'planningGroups',
            'week_number': 'weekNumber',
            'week_count': 'weekCount'
        }

        self._reference_start_date = None
        self._planning_groups = None
        self._week_number = None
        self._week_count = None

    @property
    def reference_start_date(self):
        """
        Gets the reference_start_date of this BuForecastResult.
        The reference start date for interval-based data for this forecast. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The reference_start_date of this BuForecastResult.
        :rtype: datetime
        """
        return self._reference_start_date

    @reference_start_date.setter
    def reference_start_date(self, reference_start_date):
        """
        Sets the reference_start_date of this BuForecastResult.
        The reference start date for interval-based data for this forecast. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param reference_start_date: The reference_start_date of this BuForecastResult.
        :type: datetime
        """
        
        self._reference_start_date = reference_start_date

    @property
    def planning_groups(self):
        """
        Gets the planning_groups of this BuForecastResult.
        The forecast data broken up by planning group

        :return: The planning_groups of this BuForecastResult.
        :rtype: list[ForecastPlanningGroupData]
        """
        return self._planning_groups

    @planning_groups.setter
    def planning_groups(self, planning_groups):
        """
        Sets the planning_groups of this BuForecastResult.
        The forecast data broken up by planning group

        :param planning_groups: The planning_groups of this BuForecastResult.
        :type: list[ForecastPlanningGroupData]
        """
        
        self._planning_groups = planning_groups

    @property
    def week_number(self):
        """
        Gets the week_number of this BuForecastResult.
        The week number represented by this response

        :return: The week_number of this BuForecastResult.
        :rtype: int
        """
        return self._week_number

    @week_number.setter
    def week_number(self, week_number):
        """
        Sets the week_number of this BuForecastResult.
        The week number represented by this response

        :param week_number: The week_number of this BuForecastResult.
        :type: int
        """
        
        self._week_number = week_number

    @property
    def week_count(self):
        """
        Gets the week_count of this BuForecastResult.
        The number of weeks in this forecast

        :return: The week_count of this BuForecastResult.
        :rtype: int
        """
        return self._week_count

    @week_count.setter
    def week_count(self, week_count):
        """
        Sets the week_count of this BuForecastResult.
        The number of weeks in this forecast

        :param week_count: The week_count of this BuForecastResult.
        :type: int
        """
        
        self._week_count = week_count

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
