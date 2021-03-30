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

class TimeOffRequestResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TimeOffRequestResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'user': 'UserReference',
            'is_full_day_request': 'bool',
            'marked_as_read': 'bool',
            'activity_code_id': 'str',
            'status': 'str',
            'partial_day_start_date_times': 'list[datetime]',
            'full_day_management_unit_dates': 'list[str]',
            'daily_duration_minutes': 'int',
            'notes': 'str',
            'submitted_by': 'UserReference',
            'submitted_date': 'datetime',
            'reviewed_by': 'UserReference',
            'reviewed_date': 'datetime',
            'modified_by': 'UserReference',
            'modified_date': 'datetime',
            'metadata': 'WfmVersionedEntityMetadata',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'user': 'user',
            'is_full_day_request': 'isFullDayRequest',
            'marked_as_read': 'markedAsRead',
            'activity_code_id': 'activityCodeId',
            'status': 'status',
            'partial_day_start_date_times': 'partialDayStartDateTimes',
            'full_day_management_unit_dates': 'fullDayManagementUnitDates',
            'daily_duration_minutes': 'dailyDurationMinutes',
            'notes': 'notes',
            'submitted_by': 'submittedBy',
            'submitted_date': 'submittedDate',
            'reviewed_by': 'reviewedBy',
            'reviewed_date': 'reviewedDate',
            'modified_by': 'modifiedBy',
            'modified_date': 'modifiedDate',
            'metadata': 'metadata',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._user = None
        self._is_full_day_request = None
        self._marked_as_read = None
        self._activity_code_id = None
        self._status = None
        self._partial_day_start_date_times = None
        self._full_day_management_unit_dates = None
        self._daily_duration_minutes = None
        self._notes = None
        self._submitted_by = None
        self._submitted_date = None
        self._reviewed_by = None
        self._reviewed_date = None
        self._modified_by = None
        self._modified_date = None
        self._metadata = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this TimeOffRequestResponse.
        The globally unique identifier for the object.

        :return: The id of this TimeOffRequestResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TimeOffRequestResponse.
        The globally unique identifier for the object.

        :param id: The id of this TimeOffRequestResponse.
        :type: str
        """
        
        self._id = id

    @property
    def user(self):
        """
        Gets the user of this TimeOffRequestResponse.
        The user associated with this time off request

        :return: The user of this TimeOffRequestResponse.
        :rtype: UserReference
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this TimeOffRequestResponse.
        The user associated with this time off request

        :param user: The user of this TimeOffRequestResponse.
        :type: UserReference
        """
        
        self._user = user

    @property
    def is_full_day_request(self):
        """
        Gets the is_full_day_request of this TimeOffRequestResponse.
        Whether this is a full day request (false means partial day)

        :return: The is_full_day_request of this TimeOffRequestResponse.
        :rtype: bool
        """
        return self._is_full_day_request

    @is_full_day_request.setter
    def is_full_day_request(self, is_full_day_request):
        """
        Sets the is_full_day_request of this TimeOffRequestResponse.
        Whether this is a full day request (false means partial day)

        :param is_full_day_request: The is_full_day_request of this TimeOffRequestResponse.
        :type: bool
        """
        
        self._is_full_day_request = is_full_day_request

    @property
    def marked_as_read(self):
        """
        Gets the marked_as_read of this TimeOffRequestResponse.
        Whether this request has been marked as read by the agent

        :return: The marked_as_read of this TimeOffRequestResponse.
        :rtype: bool
        """
        return self._marked_as_read

    @marked_as_read.setter
    def marked_as_read(self, marked_as_read):
        """
        Sets the marked_as_read of this TimeOffRequestResponse.
        Whether this request has been marked as read by the agent

        :param marked_as_read: The marked_as_read of this TimeOffRequestResponse.
        :type: bool
        """
        
        self._marked_as_read = marked_as_read

    @property
    def activity_code_id(self):
        """
        Gets the activity_code_id of this TimeOffRequestResponse.
        The ID of the activity code associated with this time off request. Activity code must be of the TimeOff category

        :return: The activity_code_id of this TimeOffRequestResponse.
        :rtype: str
        """
        return self._activity_code_id

    @activity_code_id.setter
    def activity_code_id(self, activity_code_id):
        """
        Sets the activity_code_id of this TimeOffRequestResponse.
        The ID of the activity code associated with this time off request. Activity code must be of the TimeOff category

        :param activity_code_id: The activity_code_id of this TimeOffRequestResponse.
        :type: str
        """
        
        self._activity_code_id = activity_code_id

    @property
    def status(self):
        """
        Gets the status of this TimeOffRequestResponse.
        The status of this time off request

        :return: The status of this TimeOffRequestResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TimeOffRequestResponse.
        The status of this time off request

        :param status: The status of this TimeOffRequestResponse.
        :type: str
        """
        allowed_values = ["PENDING", "APPROVED", "DENIED", "CANCELED"]
        if status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status -> " + status)
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def partial_day_start_date_times(self):
        """
        Gets the partial_day_start_date_times of this TimeOffRequestResponse.
        A set of start date-times in ISO-8601 format for partial day requests.  Will be not empty if isFullDayRequest == false

        :return: The partial_day_start_date_times of this TimeOffRequestResponse.
        :rtype: list[datetime]
        """
        return self._partial_day_start_date_times

    @partial_day_start_date_times.setter
    def partial_day_start_date_times(self, partial_day_start_date_times):
        """
        Sets the partial_day_start_date_times of this TimeOffRequestResponse.
        A set of start date-times in ISO-8601 format for partial day requests.  Will be not empty if isFullDayRequest == false

        :param partial_day_start_date_times: The partial_day_start_date_times of this TimeOffRequestResponse.
        :type: list[datetime]
        """
        
        self._partial_day_start_date_times = partial_day_start_date_times

    @property
    def full_day_management_unit_dates(self):
        """
        Gets the full_day_management_unit_dates of this TimeOffRequestResponse.
        A set of dates in yyyy-MM-dd format.  Should be interpreted in the management unit's configured time zone.  Will be not empty if isFullDayRequest == true

        :return: The full_day_management_unit_dates of this TimeOffRequestResponse.
        :rtype: list[str]
        """
        return self._full_day_management_unit_dates

    @full_day_management_unit_dates.setter
    def full_day_management_unit_dates(self, full_day_management_unit_dates):
        """
        Sets the full_day_management_unit_dates of this TimeOffRequestResponse.
        A set of dates in yyyy-MM-dd format.  Should be interpreted in the management unit's configured time zone.  Will be not empty if isFullDayRequest == true

        :param full_day_management_unit_dates: The full_day_management_unit_dates of this TimeOffRequestResponse.
        :type: list[str]
        """
        
        self._full_day_management_unit_dates = full_day_management_unit_dates

    @property
    def daily_duration_minutes(self):
        """
        Gets the daily_duration_minutes of this TimeOffRequestResponse.
        The daily duration of this time off request in minutes

        :return: The daily_duration_minutes of this TimeOffRequestResponse.
        :rtype: int
        """
        return self._daily_duration_minutes

    @daily_duration_minutes.setter
    def daily_duration_minutes(self, daily_duration_minutes):
        """
        Sets the daily_duration_minutes of this TimeOffRequestResponse.
        The daily duration of this time off request in minutes

        :param daily_duration_minutes: The daily_duration_minutes of this TimeOffRequestResponse.
        :type: int
        """
        
        self._daily_duration_minutes = daily_duration_minutes

    @property
    def notes(self):
        """
        Gets the notes of this TimeOffRequestResponse.
        Notes about the time off request

        :return: The notes of this TimeOffRequestResponse.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this TimeOffRequestResponse.
        Notes about the time off request

        :param notes: The notes of this TimeOffRequestResponse.
        :type: str
        """
        
        self._notes = notes

    @property
    def submitted_by(self):
        """
        Gets the submitted_by of this TimeOffRequestResponse.
        The user who submitted this time off request

        :return: The submitted_by of this TimeOffRequestResponse.
        :rtype: UserReference
        """
        return self._submitted_by

    @submitted_by.setter
    def submitted_by(self, submitted_by):
        """
        Sets the submitted_by of this TimeOffRequestResponse.
        The user who submitted this time off request

        :param submitted_by: The submitted_by of this TimeOffRequestResponse.
        :type: UserReference
        """
        
        self._submitted_by = submitted_by

    @property
    def submitted_date(self):
        """
        Gets the submitted_date of this TimeOffRequestResponse.
        The timestamp when this request was submitted. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The submitted_date of this TimeOffRequestResponse.
        :rtype: datetime
        """
        return self._submitted_date

    @submitted_date.setter
    def submitted_date(self, submitted_date):
        """
        Sets the submitted_date of this TimeOffRequestResponse.
        The timestamp when this request was submitted. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param submitted_date: The submitted_date of this TimeOffRequestResponse.
        :type: datetime
        """
        
        self._submitted_date = submitted_date

    @property
    def reviewed_by(self):
        """
        Gets the reviewed_by of this TimeOffRequestResponse.
        The user who reviewed this time off request

        :return: The reviewed_by of this TimeOffRequestResponse.
        :rtype: UserReference
        """
        return self._reviewed_by

    @reviewed_by.setter
    def reviewed_by(self, reviewed_by):
        """
        Sets the reviewed_by of this TimeOffRequestResponse.
        The user who reviewed this time off request

        :param reviewed_by: The reviewed_by of this TimeOffRequestResponse.
        :type: UserReference
        """
        
        self._reviewed_by = reviewed_by

    @property
    def reviewed_date(self):
        """
        Gets the reviewed_date of this TimeOffRequestResponse.
        The timestamp when this request was reviewed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The reviewed_date of this TimeOffRequestResponse.
        :rtype: datetime
        """
        return self._reviewed_date

    @reviewed_date.setter
    def reviewed_date(self, reviewed_date):
        """
        Sets the reviewed_date of this TimeOffRequestResponse.
        The timestamp when this request was reviewed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param reviewed_date: The reviewed_date of this TimeOffRequestResponse.
        :type: datetime
        """
        
        self._reviewed_date = reviewed_date

    @property
    def modified_by(self):
        """
        Gets the modified_by of this TimeOffRequestResponse.
        The user who last modified this TimeOffRequestResponse

        :return: The modified_by of this TimeOffRequestResponse.
        :rtype: UserReference
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """
        Sets the modified_by of this TimeOffRequestResponse.
        The user who last modified this TimeOffRequestResponse

        :param modified_by: The modified_by of this TimeOffRequestResponse.
        :type: UserReference
        """
        
        self._modified_by = modified_by

    @property
    def modified_date(self):
        """
        Gets the modified_date of this TimeOffRequestResponse.
        The timestamp when this request was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The modified_date of this TimeOffRequestResponse.
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """
        Sets the modified_date of this TimeOffRequestResponse.
        The timestamp when this request was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param modified_date: The modified_date of this TimeOffRequestResponse.
        :type: datetime
        """
        
        self._modified_date = modified_date

    @property
    def metadata(self):
        """
        Gets the metadata of this TimeOffRequestResponse.
        The version metadata of the time off request

        :return: The metadata of this TimeOffRequestResponse.
        :rtype: WfmVersionedEntityMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this TimeOffRequestResponse.
        The version metadata of the time off request

        :param metadata: The metadata of this TimeOffRequestResponse.
        :type: WfmVersionedEntityMetadata
        """
        
        self._metadata = metadata

    @property
    def self_uri(self):
        """
        Gets the self_uri of this TimeOffRequestResponse.
        The URI for this object

        :return: The self_uri of this TimeOffRequestResponse.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this TimeOffRequestResponse.
        The URI for this object

        :param self_uri: The self_uri of this TimeOffRequestResponse.
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
