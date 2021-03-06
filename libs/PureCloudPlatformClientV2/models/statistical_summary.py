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

class StatisticalSummary(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        StatisticalSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'max': 'float',
            'min': 'float',
            'count': 'int',
            'count_negative': 'int',
            'count_positive': 'int',
            'sum': 'float',
            'current': 'float',
            'ratio': 'float',
            'numerator': 'float',
            'denominator': 'float',
            'target': 'float'
        }

        self.attribute_map = {
            'max': 'max',
            'min': 'min',
            'count': 'count',
            'count_negative': 'countNegative',
            'count_positive': 'countPositive',
            'sum': 'sum',
            'current': 'current',
            'ratio': 'ratio',
            'numerator': 'numerator',
            'denominator': 'denominator',
            'target': 'target'
        }

        self._max = None
        self._min = None
        self._count = None
        self._count_negative = None
        self._count_positive = None
        self._sum = None
        self._current = None
        self._ratio = None
        self._numerator = None
        self._denominator = None
        self._target = None

    @property
    def max(self):
        """
        Gets the max of this StatisticalSummary.


        :return: The max of this StatisticalSummary.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """
        Sets the max of this StatisticalSummary.


        :param max: The max of this StatisticalSummary.
        :type: float
        """
        
        self._max = max

    @property
    def min(self):
        """
        Gets the min of this StatisticalSummary.


        :return: The min of this StatisticalSummary.
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this StatisticalSummary.


        :param min: The min of this StatisticalSummary.
        :type: float
        """
        
        self._min = min

    @property
    def count(self):
        """
        Gets the count of this StatisticalSummary.


        :return: The count of this StatisticalSummary.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this StatisticalSummary.


        :param count: The count of this StatisticalSummary.
        :type: int
        """
        
        self._count = count

    @property
    def count_negative(self):
        """
        Gets the count_negative of this StatisticalSummary.


        :return: The count_negative of this StatisticalSummary.
        :rtype: int
        """
        return self._count_negative

    @count_negative.setter
    def count_negative(self, count_negative):
        """
        Sets the count_negative of this StatisticalSummary.


        :param count_negative: The count_negative of this StatisticalSummary.
        :type: int
        """
        
        self._count_negative = count_negative

    @property
    def count_positive(self):
        """
        Gets the count_positive of this StatisticalSummary.


        :return: The count_positive of this StatisticalSummary.
        :rtype: int
        """
        return self._count_positive

    @count_positive.setter
    def count_positive(self, count_positive):
        """
        Sets the count_positive of this StatisticalSummary.


        :param count_positive: The count_positive of this StatisticalSummary.
        :type: int
        """
        
        self._count_positive = count_positive

    @property
    def sum(self):
        """
        Gets the sum of this StatisticalSummary.


        :return: The sum of this StatisticalSummary.
        :rtype: float
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """
        Sets the sum of this StatisticalSummary.


        :param sum: The sum of this StatisticalSummary.
        :type: float
        """
        
        self._sum = sum

    @property
    def current(self):
        """
        Gets the current of this StatisticalSummary.


        :return: The current of this StatisticalSummary.
        :rtype: float
        """
        return self._current

    @current.setter
    def current(self, current):
        """
        Sets the current of this StatisticalSummary.


        :param current: The current of this StatisticalSummary.
        :type: float
        """
        
        self._current = current

    @property
    def ratio(self):
        """
        Gets the ratio of this StatisticalSummary.


        :return: The ratio of this StatisticalSummary.
        :rtype: float
        """
        return self._ratio

    @ratio.setter
    def ratio(self, ratio):
        """
        Sets the ratio of this StatisticalSummary.


        :param ratio: The ratio of this StatisticalSummary.
        :type: float
        """
        
        self._ratio = ratio

    @property
    def numerator(self):
        """
        Gets the numerator of this StatisticalSummary.


        :return: The numerator of this StatisticalSummary.
        :rtype: float
        """
        return self._numerator

    @numerator.setter
    def numerator(self, numerator):
        """
        Sets the numerator of this StatisticalSummary.


        :param numerator: The numerator of this StatisticalSummary.
        :type: float
        """
        
        self._numerator = numerator

    @property
    def denominator(self):
        """
        Gets the denominator of this StatisticalSummary.


        :return: The denominator of this StatisticalSummary.
        :rtype: float
        """
        return self._denominator

    @denominator.setter
    def denominator(self, denominator):
        """
        Sets the denominator of this StatisticalSummary.


        :param denominator: The denominator of this StatisticalSummary.
        :type: float
        """
        
        self._denominator = denominator

    @property
    def target(self):
        """
        Gets the target of this StatisticalSummary.


        :return: The target of this StatisticalSummary.
        :rtype: float
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this StatisticalSummary.


        :param target: The target of this StatisticalSummary.
        :type: float
        """
        
        self._target = target

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

