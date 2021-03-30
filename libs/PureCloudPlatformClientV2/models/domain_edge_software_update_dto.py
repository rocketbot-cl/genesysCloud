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

class DomainEdgeSoftwareUpdateDto(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DomainEdgeSoftwareUpdateDto - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'version': 'DomainEdgeSoftwareVersionDto',
            'max_download_rate': 'int',
            'download_start_time': 'datetime',
            'execute_start_time': 'datetime',
            'execute_stop_time': 'datetime',
            'execute_on_idle': 'bool',
            'status': 'str',
            'edge_uri': 'str',
            'call_draining_wait_time_seconds': 'int',
            'current': 'bool'
        }

        self.attribute_map = {
            'version': 'version',
            'max_download_rate': 'maxDownloadRate',
            'download_start_time': 'downloadStartTime',
            'execute_start_time': 'executeStartTime',
            'execute_stop_time': 'executeStopTime',
            'execute_on_idle': 'executeOnIdle',
            'status': 'status',
            'edge_uri': 'edgeUri',
            'call_draining_wait_time_seconds': 'callDrainingWaitTimeSeconds',
            'current': 'current'
        }

        self._version = None
        self._max_download_rate = None
        self._download_start_time = None
        self._execute_start_time = None
        self._execute_stop_time = None
        self._execute_on_idle = None
        self._status = None
        self._edge_uri = None
        self._call_draining_wait_time_seconds = None
        self._current = None

    @property
    def version(self):
        """
        Gets the version of this DomainEdgeSoftwareUpdateDto.
        Version

        :return: The version of this DomainEdgeSoftwareUpdateDto.
        :rtype: DomainEdgeSoftwareVersionDto
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this DomainEdgeSoftwareUpdateDto.
        Version

        :param version: The version of this DomainEdgeSoftwareUpdateDto.
        :type: DomainEdgeSoftwareVersionDto
        """
        
        self._version = version

    @property
    def max_download_rate(self):
        """
        Gets the max_download_rate of this DomainEdgeSoftwareUpdateDto.


        :return: The max_download_rate of this DomainEdgeSoftwareUpdateDto.
        :rtype: int
        """
        return self._max_download_rate

    @max_download_rate.setter
    def max_download_rate(self, max_download_rate):
        """
        Sets the max_download_rate of this DomainEdgeSoftwareUpdateDto.


        :param max_download_rate: The max_download_rate of this DomainEdgeSoftwareUpdateDto.
        :type: int
        """
        
        self._max_download_rate = max_download_rate

    @property
    def download_start_time(self):
        """
        Gets the download_start_time of this DomainEdgeSoftwareUpdateDto.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The download_start_time of this DomainEdgeSoftwareUpdateDto.
        :rtype: datetime
        """
        return self._download_start_time

    @download_start_time.setter
    def download_start_time(self, download_start_time):
        """
        Sets the download_start_time of this DomainEdgeSoftwareUpdateDto.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param download_start_time: The download_start_time of this DomainEdgeSoftwareUpdateDto.
        :type: datetime
        """
        
        self._download_start_time = download_start_time

    @property
    def execute_start_time(self):
        """
        Gets the execute_start_time of this DomainEdgeSoftwareUpdateDto.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The execute_start_time of this DomainEdgeSoftwareUpdateDto.
        :rtype: datetime
        """
        return self._execute_start_time

    @execute_start_time.setter
    def execute_start_time(self, execute_start_time):
        """
        Sets the execute_start_time of this DomainEdgeSoftwareUpdateDto.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param execute_start_time: The execute_start_time of this DomainEdgeSoftwareUpdateDto.
        :type: datetime
        """
        
        self._execute_start_time = execute_start_time

    @property
    def execute_stop_time(self):
        """
        Gets the execute_stop_time of this DomainEdgeSoftwareUpdateDto.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The execute_stop_time of this DomainEdgeSoftwareUpdateDto.
        :rtype: datetime
        """
        return self._execute_stop_time

    @execute_stop_time.setter
    def execute_stop_time(self, execute_stop_time):
        """
        Sets the execute_stop_time of this DomainEdgeSoftwareUpdateDto.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param execute_stop_time: The execute_stop_time of this DomainEdgeSoftwareUpdateDto.
        :type: datetime
        """
        
        self._execute_stop_time = execute_stop_time

    @property
    def execute_on_idle(self):
        """
        Gets the execute_on_idle of this DomainEdgeSoftwareUpdateDto.


        :return: The execute_on_idle of this DomainEdgeSoftwareUpdateDto.
        :rtype: bool
        """
        return self._execute_on_idle

    @execute_on_idle.setter
    def execute_on_idle(self, execute_on_idle):
        """
        Sets the execute_on_idle of this DomainEdgeSoftwareUpdateDto.


        :param execute_on_idle: The execute_on_idle of this DomainEdgeSoftwareUpdateDto.
        :type: bool
        """
        
        self._execute_on_idle = execute_on_idle

    @property
    def status(self):
        """
        Gets the status of this DomainEdgeSoftwareUpdateDto.


        :return: The status of this DomainEdgeSoftwareUpdateDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DomainEdgeSoftwareUpdateDto.


        :param status: The status of this DomainEdgeSoftwareUpdateDto.
        :type: str
        """
        allowed_values = ["NONE", "INIT", "IN_PROGRESS", "EXPIRED", "EXCEPTION", "ABORTED", "FAILED", "SUCCEEDED", "DELETE"]
        if status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status -> " + status)
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def edge_uri(self):
        """
        Gets the edge_uri of this DomainEdgeSoftwareUpdateDto.


        :return: The edge_uri of this DomainEdgeSoftwareUpdateDto.
        :rtype: str
        """
        return self._edge_uri

    @edge_uri.setter
    def edge_uri(self, edge_uri):
        """
        Sets the edge_uri of this DomainEdgeSoftwareUpdateDto.


        :param edge_uri: The edge_uri of this DomainEdgeSoftwareUpdateDto.
        :type: str
        """
        
        self._edge_uri = edge_uri

    @property
    def call_draining_wait_time_seconds(self):
        """
        Gets the call_draining_wait_time_seconds of this DomainEdgeSoftwareUpdateDto.


        :return: The call_draining_wait_time_seconds of this DomainEdgeSoftwareUpdateDto.
        :rtype: int
        """
        return self._call_draining_wait_time_seconds

    @call_draining_wait_time_seconds.setter
    def call_draining_wait_time_seconds(self, call_draining_wait_time_seconds):
        """
        Sets the call_draining_wait_time_seconds of this DomainEdgeSoftwareUpdateDto.


        :param call_draining_wait_time_seconds: The call_draining_wait_time_seconds of this DomainEdgeSoftwareUpdateDto.
        :type: int
        """
        
        self._call_draining_wait_time_seconds = call_draining_wait_time_seconds

    @property
    def current(self):
        """
        Gets the current of this DomainEdgeSoftwareUpdateDto.


        :return: The current of this DomainEdgeSoftwareUpdateDto.
        :rtype: bool
        """
        return self._current

    @current.setter
    def current(self, current):
        """
        Sets the current of this DomainEdgeSoftwareUpdateDto.


        :param current: The current of this DomainEdgeSoftwareUpdateDto.
        :type: bool
        """
        
        self._current = current

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
