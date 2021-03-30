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

class ReportSchedule(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ReportSchedule - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'quartz_cron_expression': 'str',
            'next_fire_time': 'datetime',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'description': 'str',
            'time_zone': 'str',
            'time_period': 'str',
            'interval': 'str',
            'report_format': 'str',
            'locale': 'str',
            'enabled': 'bool',
            'report_id': 'str',
            'parameters': 'dict(str, object)',
            'last_run': 'ReportRunEntry',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'quartz_cron_expression': 'quartzCronExpression',
            'next_fire_time': 'nextFireTime',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'description': 'description',
            'time_zone': 'timeZone',
            'time_period': 'timePeriod',
            'interval': 'interval',
            'report_format': 'reportFormat',
            'locale': 'locale',
            'enabled': 'enabled',
            'report_id': 'reportId',
            'parameters': 'parameters',
            'last_run': 'lastRun',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._quartz_cron_expression = None
        self._next_fire_time = None
        self._date_created = None
        self._date_modified = None
        self._description = None
        self._time_zone = None
        self._time_period = None
        self._interval = None
        self._report_format = None
        self._locale = None
        self._enabled = None
        self._report_id = None
        self._parameters = None
        self._last_run = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this ReportSchedule.
        The globally unique identifier for the object.

        :return: The id of this ReportSchedule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ReportSchedule.
        The globally unique identifier for the object.

        :param id: The id of this ReportSchedule.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ReportSchedule.


        :return: The name of this ReportSchedule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ReportSchedule.


        :param name: The name of this ReportSchedule.
        :type: str
        """
        
        self._name = name

    @property
    def quartz_cron_expression(self):
        """
        Gets the quartz_cron_expression of this ReportSchedule.
        Quartz Cron Expression

        :return: The quartz_cron_expression of this ReportSchedule.
        :rtype: str
        """
        return self._quartz_cron_expression

    @quartz_cron_expression.setter
    def quartz_cron_expression(self, quartz_cron_expression):
        """
        Sets the quartz_cron_expression of this ReportSchedule.
        Quartz Cron Expression

        :param quartz_cron_expression: The quartz_cron_expression of this ReportSchedule.
        :type: str
        """
        
        self._quartz_cron_expression = quartz_cron_expression

    @property
    def next_fire_time(self):
        """
        Gets the next_fire_time of this ReportSchedule.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The next_fire_time of this ReportSchedule.
        :rtype: datetime
        """
        return self._next_fire_time

    @next_fire_time.setter
    def next_fire_time(self, next_fire_time):
        """
        Sets the next_fire_time of this ReportSchedule.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param next_fire_time: The next_fire_time of this ReportSchedule.
        :type: datetime
        """
        
        self._next_fire_time = next_fire_time

    @property
    def date_created(self):
        """
        Gets the date_created of this ReportSchedule.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this ReportSchedule.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this ReportSchedule.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this ReportSchedule.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this ReportSchedule.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this ReportSchedule.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this ReportSchedule.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this ReportSchedule.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def description(self):
        """
        Gets the description of this ReportSchedule.


        :return: The description of this ReportSchedule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ReportSchedule.


        :param description: The description of this ReportSchedule.
        :type: str
        """
        
        self._description = description

    @property
    def time_zone(self):
        """
        Gets the time_zone of this ReportSchedule.


        :return: The time_zone of this ReportSchedule.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this ReportSchedule.


        :param time_zone: The time_zone of this ReportSchedule.
        :type: str
        """
        
        self._time_zone = time_zone

    @property
    def time_period(self):
        """
        Gets the time_period of this ReportSchedule.


        :return: The time_period of this ReportSchedule.
        :rtype: str
        """
        return self._time_period

    @time_period.setter
    def time_period(self, time_period):
        """
        Sets the time_period of this ReportSchedule.


        :param time_period: The time_period of this ReportSchedule.
        :type: str
        """
        
        self._time_period = time_period

    @property
    def interval(self):
        """
        Gets the interval of this ReportSchedule.
        Interval. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss

        :return: The interval of this ReportSchedule.
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this ReportSchedule.
        Interval. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss

        :param interval: The interval of this ReportSchedule.
        :type: str
        """
        
        self._interval = interval

    @property
    def report_format(self):
        """
        Gets the report_format of this ReportSchedule.


        :return: The report_format of this ReportSchedule.
        :rtype: str
        """
        return self._report_format

    @report_format.setter
    def report_format(self, report_format):
        """
        Sets the report_format of this ReportSchedule.


        :param report_format: The report_format of this ReportSchedule.
        :type: str
        """
        
        self._report_format = report_format

    @property
    def locale(self):
        """
        Gets the locale of this ReportSchedule.


        :return: The locale of this ReportSchedule.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """
        Sets the locale of this ReportSchedule.


        :param locale: The locale of this ReportSchedule.
        :type: str
        """
        
        self._locale = locale

    @property
    def enabled(self):
        """
        Gets the enabled of this ReportSchedule.


        :return: The enabled of this ReportSchedule.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this ReportSchedule.


        :param enabled: The enabled of this ReportSchedule.
        :type: bool
        """
        
        self._enabled = enabled

    @property
    def report_id(self):
        """
        Gets the report_id of this ReportSchedule.
        Report ID

        :return: The report_id of this ReportSchedule.
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """
        Sets the report_id of this ReportSchedule.
        Report ID

        :param report_id: The report_id of this ReportSchedule.
        :type: str
        """
        
        self._report_id = report_id

    @property
    def parameters(self):
        """
        Gets the parameters of this ReportSchedule.


        :return: The parameters of this ReportSchedule.
        :rtype: dict(str, object)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this ReportSchedule.


        :param parameters: The parameters of this ReportSchedule.
        :type: dict(str, object)
        """
        
        self._parameters = parameters

    @property
    def last_run(self):
        """
        Gets the last_run of this ReportSchedule.


        :return: The last_run of this ReportSchedule.
        :rtype: ReportRunEntry
        """
        return self._last_run

    @last_run.setter
    def last_run(self, last_run):
        """
        Sets the last_run of this ReportSchedule.


        :param last_run: The last_run of this ReportSchedule.
        :type: ReportRunEntry
        """
        
        self._last_run = last_run

    @property
    def self_uri(self):
        """
        Gets the self_uri of this ReportSchedule.
        The URI for this object

        :return: The self_uri of this ReportSchedule.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this ReportSchedule.
        The URI for this object

        :param self_uri: The self_uri of this ReportSchedule.
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
