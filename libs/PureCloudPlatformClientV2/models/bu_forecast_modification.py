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

class BuForecastModification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BuForecastModification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'start_interval_index': 'int',
            'end_interval_index': 'int',
            'metric': 'str',
            'legacy_metric': 'str',
            'value': 'float',
            'values': 'list[WfmForecastModificationIntervalOffsetValue]',
            'display_granularity': 'str',
            'granularity': 'str',
            'enabled': 'bool',
            'planning_group_ids': 'list[str]'
        }

        self.attribute_map = {
            'type': 'type',
            'start_interval_index': 'startIntervalIndex',
            'end_interval_index': 'endIntervalIndex',
            'metric': 'metric',
            'legacy_metric': 'legacyMetric',
            'value': 'value',
            'values': 'values',
            'display_granularity': 'displayGranularity',
            'granularity': 'granularity',
            'enabled': 'enabled',
            'planning_group_ids': 'planningGroupIds'
        }

        self._type = None
        self._start_interval_index = None
        self._end_interval_index = None
        self._metric = None
        self._legacy_metric = None
        self._value = None
        self._values = None
        self._display_granularity = None
        self._granularity = None
        self._enabled = None
        self._planning_group_ids = None

    @property
    def type(self):
        """
        Gets the type of this BuForecastModification.
        The type of the modification

        :return: The type of this BuForecastModification.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this BuForecastModification.
        The type of the modification

        :param type: The type of this BuForecastModification.
        :type: str
        """
        allowed_values = ["MinimumPerInterval", "MaximumPerInterval", "SetValuePerInterval", "ChangeValuePerInterval", "ChangePercentPerInterval", "SetValueOverRange", "ChangeValueOverRange", "SetValuesForIntervalSet"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def start_interval_index(self):
        """
        Gets the start_interval_index of this BuForecastModification.
        The number of 15 minute intervals past referenceStartDate representing the first interval to which to apply this modification. Must be null if values is populated

        :return: The start_interval_index of this BuForecastModification.
        :rtype: int
        """
        return self._start_interval_index

    @start_interval_index.setter
    def start_interval_index(self, start_interval_index):
        """
        Sets the start_interval_index of this BuForecastModification.
        The number of 15 minute intervals past referenceStartDate representing the first interval to which to apply this modification. Must be null if values is populated

        :param start_interval_index: The start_interval_index of this BuForecastModification.
        :type: int
        """
        
        self._start_interval_index = start_interval_index

    @property
    def end_interval_index(self):
        """
        Gets the end_interval_index of this BuForecastModification.
        The number of 15 minute intervals past referenceStartDate representing the last interval to which to apply this modification.  Must be null if values is populated

        :return: The end_interval_index of this BuForecastModification.
        :rtype: int
        """
        return self._end_interval_index

    @end_interval_index.setter
    def end_interval_index(self, end_interval_index):
        """
        Sets the end_interval_index of this BuForecastModification.
        The number of 15 minute intervals past referenceStartDate representing the last interval to which to apply this modification.  Must be null if values is populated

        :param end_interval_index: The end_interval_index of this BuForecastModification.
        :type: int
        """
        
        self._end_interval_index = end_interval_index

    @property
    def metric(self):
        """
        Gets the metric of this BuForecastModification.
        The metric to which this modification applies

        :return: The metric of this BuForecastModification.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """
        Sets the metric of this BuForecastModification.
        The metric to which this modification applies

        :param metric: The metric of this BuForecastModification.
        :type: str
        """
        allowed_values = ["Offered", "AverageHandleTimeSeconds"]
        if metric.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for metric -> " + metric)
            self._metric = "outdated_sdk_version"
        else:
            self._metric = metric

    @property
    def legacy_metric(self):
        """
        Gets the legacy_metric of this BuForecastModification.
        The legacy metric to which this modification applies if applicable

        :return: The legacy_metric of this BuForecastModification.
        :rtype: str
        """
        return self._legacy_metric

    @legacy_metric.setter
    def legacy_metric(self, legacy_metric):
        """
        Sets the legacy_metric of this BuForecastModification.
        The legacy metric to which this modification applies if applicable

        :param legacy_metric: The legacy_metric of this BuForecastModification.
        :type: str
        """
        allowed_values = ["AverageAfterCallWorkTimeSeconds", "AverageHandleTimeSeconds", "AverageTalkTimeSeconds", "Offered"]
        if legacy_metric.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for legacy_metric -> " + legacy_metric)
            self._legacy_metric = "outdated_sdk_version"
        else:
            self._legacy_metric = legacy_metric

    @property
    def value(self):
        """
        Gets the value of this BuForecastModification.
        The value of the modification.  Must be null if \"values\" is populated

        :return: The value of this BuForecastModification.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this BuForecastModification.
        The value of the modification.  Must be null if \"values\" is populated

        :param value: The value of this BuForecastModification.
        :type: float
        """
        
        self._value = value

    @property
    def values(self):
        """
        Gets the values of this BuForecastModification.
        The list of values to update.  Only applicable for grid-type modifications. Must be null if \"value\" is populated

        :return: The values of this BuForecastModification.
        :rtype: list[WfmForecastModificationIntervalOffsetValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this BuForecastModification.
        The list of values to update.  Only applicable for grid-type modifications. Must be null if \"value\" is populated

        :param values: The values of this BuForecastModification.
        :type: list[WfmForecastModificationIntervalOffsetValue]
        """
        
        self._values = values

    @property
    def display_granularity(self):
        """
        Gets the display_granularity of this BuForecastModification.
        The client side display granularity of the modification, expressed in the ISO-8601 duration format. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H

        :return: The display_granularity of this BuForecastModification.
        :rtype: str
        """
        return self._display_granularity

    @display_granularity.setter
    def display_granularity(self, display_granularity):
        """
        Sets the display_granularity of this BuForecastModification.
        The client side display granularity of the modification, expressed in the ISO-8601 duration format. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H

        :param display_granularity: The display_granularity of this BuForecastModification.
        :type: str
        """
        
        self._display_granularity = display_granularity

    @property
    def granularity(self):
        """
        Gets the granularity of this BuForecastModification.
        The actual granularity of the modification as stored behind the scenes, expressed in the ISO-8601 duration format. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H

        :return: The granularity of this BuForecastModification.
        :rtype: str
        """
        return self._granularity

    @granularity.setter
    def granularity(self, granularity):
        """
        Sets the granularity of this BuForecastModification.
        The actual granularity of the modification as stored behind the scenes, expressed in the ISO-8601 duration format. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H

        :param granularity: The granularity of this BuForecastModification.
        :type: str
        """
        
        self._granularity = granularity

    @property
    def enabled(self):
        """
        Gets the enabled of this BuForecastModification.
        Whether the modification is enabled for the forecast

        :return: The enabled of this BuForecastModification.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this BuForecastModification.
        Whether the modification is enabled for the forecast

        :param enabled: The enabled of this BuForecastModification.
        :type: bool
        """
        
        self._enabled = enabled

    @property
    def planning_group_ids(self):
        """
        Gets the planning_group_ids of this BuForecastModification.
        The IDs of the planning groups to which this forecast modification applies.  Leave empty to apply to all

        :return: The planning_group_ids of this BuForecastModification.
        :rtype: list[str]
        """
        return self._planning_group_ids

    @planning_group_ids.setter
    def planning_group_ids(self, planning_group_ids):
        """
        Sets the planning_group_ids of this BuForecastModification.
        The IDs of the planning groups to which this forecast modification applies.  Leave empty to apply to all

        :param planning_group_ids: The planning_group_ids of this BuForecastModification.
        :type: list[str]
        """
        
        self._planning_group_ids = planning_group_ids

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
