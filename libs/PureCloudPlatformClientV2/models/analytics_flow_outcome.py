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

class AnalyticsFlowOutcome(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AnalyticsFlowOutcome - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'flow_outcome_id': 'str',
            'flow_outcome_value': 'str',
            'flow_outcome': 'str',
            'flow_outcome_start_timestamp': 'datetime',
            'flow_outcome_end_timestamp': 'datetime'
        }

        self.attribute_map = {
            'flow_outcome_id': 'flowOutcomeId',
            'flow_outcome_value': 'flowOutcomeValue',
            'flow_outcome': 'flowOutcome',
            'flow_outcome_start_timestamp': 'flowOutcomeStartTimestamp',
            'flow_outcome_end_timestamp': 'flowOutcomeEndTimestamp'
        }

        self._flow_outcome_id = None
        self._flow_outcome_value = None
        self._flow_outcome = None
        self._flow_outcome_start_timestamp = None
        self._flow_outcome_end_timestamp = None

    @property
    def flow_outcome_id(self):
        """
        Gets the flow_outcome_id of this AnalyticsFlowOutcome.
        Unique identifiers of a flow outcome

        :return: The flow_outcome_id of this AnalyticsFlowOutcome.
        :rtype: str
        """
        return self._flow_outcome_id

    @flow_outcome_id.setter
    def flow_outcome_id(self, flow_outcome_id):
        """
        Sets the flow_outcome_id of this AnalyticsFlowOutcome.
        Unique identifiers of a flow outcome

        :param flow_outcome_id: The flow_outcome_id of this AnalyticsFlowOutcome.
        :type: str
        """
        
        self._flow_outcome_id = flow_outcome_id

    @property
    def flow_outcome_value(self):
        """
        Gets the flow_outcome_value of this AnalyticsFlowOutcome.
        Flow outcome value, e.g. SUCCESS

        :return: The flow_outcome_value of this AnalyticsFlowOutcome.
        :rtype: str
        """
        return self._flow_outcome_value

    @flow_outcome_value.setter
    def flow_outcome_value(self, flow_outcome_value):
        """
        Sets the flow_outcome_value of this AnalyticsFlowOutcome.
        Flow outcome value, e.g. SUCCESS

        :param flow_outcome_value: The flow_outcome_value of this AnalyticsFlowOutcome.
        :type: str
        """
        
        self._flow_outcome_value = flow_outcome_value

    @property
    def flow_outcome(self):
        """
        Gets the flow_outcome of this AnalyticsFlowOutcome.
        Colon-separated combinations of unique flow outcome identifier and value

        :return: The flow_outcome of this AnalyticsFlowOutcome.
        :rtype: str
        """
        return self._flow_outcome

    @flow_outcome.setter
    def flow_outcome(self, flow_outcome):
        """
        Sets the flow_outcome of this AnalyticsFlowOutcome.
        Colon-separated combinations of unique flow outcome identifier and value

        :param flow_outcome: The flow_outcome of this AnalyticsFlowOutcome.
        :type: str
        """
        
        self._flow_outcome = flow_outcome

    @property
    def flow_outcome_start_timestamp(self):
        """
        Gets the flow_outcome_start_timestamp of this AnalyticsFlowOutcome.
        Date/time the outcome started. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The flow_outcome_start_timestamp of this AnalyticsFlowOutcome.
        :rtype: datetime
        """
        return self._flow_outcome_start_timestamp

    @flow_outcome_start_timestamp.setter
    def flow_outcome_start_timestamp(self, flow_outcome_start_timestamp):
        """
        Sets the flow_outcome_start_timestamp of this AnalyticsFlowOutcome.
        Date/time the outcome started. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param flow_outcome_start_timestamp: The flow_outcome_start_timestamp of this AnalyticsFlowOutcome.
        :type: datetime
        """
        
        self._flow_outcome_start_timestamp = flow_outcome_start_timestamp

    @property
    def flow_outcome_end_timestamp(self):
        """
        Gets the flow_outcome_end_timestamp of this AnalyticsFlowOutcome.
        Date/time the outcome ended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The flow_outcome_end_timestamp of this AnalyticsFlowOutcome.
        :rtype: datetime
        """
        return self._flow_outcome_end_timestamp

    @flow_outcome_end_timestamp.setter
    def flow_outcome_end_timestamp(self, flow_outcome_end_timestamp):
        """
        Sets the flow_outcome_end_timestamp of this AnalyticsFlowOutcome.
        Date/time the outcome ended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param flow_outcome_end_timestamp: The flow_outcome_end_timestamp of this AnalyticsFlowOutcome.
        :type: datetime
        """
        
        self._flow_outcome_end_timestamp = flow_outcome_end_timestamp

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

