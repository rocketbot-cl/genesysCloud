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

class EvaluationQualityV2TopicEvaluationV2(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EvaluationQualityV2TopicEvaluationV2 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'conversation_id': 'str',
            'agent': 'EvaluationQualityV2TopicUser',
            'evaluator': 'EvaluationQualityV2TopicUser',
            'event_time': 'datetime',
            'evaluation_form_id': 'str',
            'form_name': 'str',
            'scoring_set': 'EvaluationQualityV2TopicEvaluationScoringSet',
            'context_id': 'str',
            'status': 'str',
            'agent_has_read': 'bool',
            'release_date': 'datetime',
            'assigned_date': 'datetime',
            'changed_date': 'datetime',
            'event_type': 'str',
            'resource_id': 'str',
            'resource_type': 'str',
            'division_ids': 'list[str]',
            'rescore': 'bool',
            'conversation_date': 'datetime',
            'media_type': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'conversation_id': 'conversationId',
            'agent': 'agent',
            'evaluator': 'evaluator',
            'event_time': 'eventTime',
            'evaluation_form_id': 'evaluationFormId',
            'form_name': 'formName',
            'scoring_set': 'scoringSet',
            'context_id': 'contextId',
            'status': 'status',
            'agent_has_read': 'agentHasRead',
            'release_date': 'releaseDate',
            'assigned_date': 'assignedDate',
            'changed_date': 'changedDate',
            'event_type': 'eventType',
            'resource_id': 'resourceId',
            'resource_type': 'resourceType',
            'division_ids': 'divisionIds',
            'rescore': 'rescore',
            'conversation_date': 'conversationDate',
            'media_type': 'mediaType'
        }

        self._id = None
        self._conversation_id = None
        self._agent = None
        self._evaluator = None
        self._event_time = None
        self._evaluation_form_id = None
        self._form_name = None
        self._scoring_set = None
        self._context_id = None
        self._status = None
        self._agent_has_read = None
        self._release_date = None
        self._assigned_date = None
        self._changed_date = None
        self._event_type = None
        self._resource_id = None
        self._resource_type = None
        self._division_ids = None
        self._rescore = None
        self._conversation_date = None
        self._media_type = None

    @property
    def id(self):
        """
        Gets the id of this EvaluationQualityV2TopicEvaluationV2.


        :return: The id of this EvaluationQualityV2TopicEvaluationV2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EvaluationQualityV2TopicEvaluationV2.


        :param id: The id of this EvaluationQualityV2TopicEvaluationV2.
        :type: str
        """
        
        self._id = id

    @property
    def conversation_id(self):
        """
        Gets the conversation_id of this EvaluationQualityV2TopicEvaluationV2.


        :return: The conversation_id of this EvaluationQualityV2TopicEvaluationV2.
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id):
        """
        Sets the conversation_id of this EvaluationQualityV2TopicEvaluationV2.


        :param conversation_id: The conversation_id of this EvaluationQualityV2TopicEvaluationV2.
        :type: str
        """
        
        self._conversation_id = conversation_id

    @property
    def agent(self):
        """
        Gets the agent of this EvaluationQualityV2TopicEvaluationV2.


        :return: The agent of this EvaluationQualityV2TopicEvaluationV2.
        :rtype: EvaluationQualityV2TopicUser
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """
        Sets the agent of this EvaluationQualityV2TopicEvaluationV2.


        :param agent: The agent of this EvaluationQualityV2TopicEvaluationV2.
        :type: EvaluationQualityV2TopicUser
        """
        
        self._agent = agent

    @property
    def evaluator(self):
        """
        Gets the evaluator of this EvaluationQualityV2TopicEvaluationV2.


        :return: The evaluator of this EvaluationQualityV2TopicEvaluationV2.
        :rtype: EvaluationQualityV2TopicUser
        """
        return self._evaluator

    @evaluator.setter
    def evaluator(self, evaluator):
        """
        Sets the evaluator of this EvaluationQualityV2TopicEvaluationV2.


        :param evaluator: The evaluator of this EvaluationQualityV2TopicEvaluationV2.
        :type: EvaluationQualityV2TopicUser
        """
        
        self._evaluator = evaluator

    @property
    def event_time(self):
        """
        Gets the event_time of this EvaluationQualityV2TopicEvaluationV2.


        :return: The event_time of this EvaluationQualityV2TopicEvaluationV2.
        :rtype: datetime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """
        Sets the event_time of this EvaluationQualityV2TopicEvaluationV2.


        :param event_time: The event_time of this EvaluationQualityV2TopicEvaluationV2.
        :type: datetime
        """
        
        self._event_time = event_time

    @property
    def evaluation_form_id(self):
        """
        Gets the evaluation_form_id of this EvaluationQualityV2TopicEvaluationV2.


        :return: The evaluation_form_id of this EvaluationQualityV2TopicEvaluationV2.
        :rtype: str
        """
        return self._evaluation_form_id

    @evaluation_form_id.setter
    def evaluation_form_id(self, evaluation_form_id):
        """
        Sets the evaluation_form_id of this EvaluationQualityV2TopicEvaluationV2.


        :param evaluation_form_id: The evaluation_form_id of this EvaluationQualityV2TopicEvaluationV2.
        :type: str
        """
        
        self._evaluation_form_id = evaluation_form_id

    @property
    def form_name(self):
        """
        Gets the form_name of this EvaluationQualityV2TopicEvaluationV2.


        :return: The form_name of this EvaluationQualityV2TopicEvaluationV2.
        :rtype: str
        """
        return self._form_name

    @form_name.setter
    def form_name(self, form_name):
        """
        Sets the form_name of this EvaluationQualityV2TopicEvaluationV2.


        :param form_name: The form_name of this EvaluationQualityV2TopicEvaluationV2.
        :type: str
        """
        
        self._form_name = form_name

    @property
    def scoring_set(self):
        """
        Gets the scoring_set of this EvaluationQualityV2TopicEvaluationV2.


        :return: The scoring_set of this EvaluationQualityV2TopicEvaluationV2.
        :rtype: EvaluationQualityV2TopicEvaluationScoringSet
        """
        return self._scoring_set

    @scoring_set.setter
    def scoring_set(self, scoring_set):
        """
        Sets the scoring_set of this EvaluationQualityV2TopicEvaluationV2.


        :param scoring_set: The scoring_set of this EvaluationQualityV2TopicEvaluationV2.
        :type: EvaluationQualityV2TopicEvaluationScoringSet
        """
        
        self._scoring_set = scoring_set

    @property
    def context_id(self):
        """
        Gets the context_id of this EvaluationQualityV2TopicEvaluationV2.


        :return: The context_id of this EvaluationQualityV2TopicEvaluationV2.
        :rtype: str
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id):
        """
        Sets the context_id of this EvaluationQualityV2TopicEvaluationV2.


        :param context_id: The context_id of this EvaluationQualityV2TopicEvaluationV2.
        :type: str
        """
        
        self._context_id = context_id

    @property
    def status(self):
        """
        Gets the status of this EvaluationQualityV2TopicEvaluationV2.


        :return: The status of this EvaluationQualityV2TopicEvaluationV2.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this EvaluationQualityV2TopicEvaluationV2.


        :param status: The status of this EvaluationQualityV2TopicEvaluationV2.
        :type: str
        """
        allowed_values = ["Pending", "InProgress", "Finished"]
        if status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status -> " + status)
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def agent_has_read(self):
        """
        Gets the agent_has_read of this EvaluationQualityV2TopicEvaluationV2.


        :return: The agent_has_read of this EvaluationQualityV2TopicEvaluationV2.
        :rtype: bool
        """
        return self._agent_has_read

    @agent_has_read.setter
    def agent_has_read(self, agent_has_read):
        """
        Sets the agent_has_read of this EvaluationQualityV2TopicEvaluationV2.


        :param agent_has_read: The agent_has_read of this EvaluationQualityV2TopicEvaluationV2.
        :type: bool
        """
        
        self._agent_has_read = agent_has_read

    @property
    def release_date(self):
        """
        Gets the release_date of this EvaluationQualityV2TopicEvaluationV2.


        :return: The release_date of this EvaluationQualityV2TopicEvaluationV2.
        :rtype: datetime
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """
        Sets the release_date of this EvaluationQualityV2TopicEvaluationV2.


        :param release_date: The release_date of this EvaluationQualityV2TopicEvaluationV2.
        :type: datetime
        """
        
        self._release_date = release_date

    @property
    def assigned_date(self):
        """
        Gets the assigned_date of this EvaluationQualityV2TopicEvaluationV2.


        :return: The assigned_date of this EvaluationQualityV2TopicEvaluationV2.
        :rtype: datetime
        """
        return self._assigned_date

    @assigned_date.setter
    def assigned_date(self, assigned_date):
        """
        Sets the assigned_date of this EvaluationQualityV2TopicEvaluationV2.


        :param assigned_date: The assigned_date of this EvaluationQualityV2TopicEvaluationV2.
        :type: datetime
        """
        
        self._assigned_date = assigned_date

    @property
    def changed_date(self):
        """
        Gets the changed_date of this EvaluationQualityV2TopicEvaluationV2.


        :return: The changed_date of this EvaluationQualityV2TopicEvaluationV2.
        :rtype: datetime
        """
        return self._changed_date

    @changed_date.setter
    def changed_date(self, changed_date):
        """
        Sets the changed_date of this EvaluationQualityV2TopicEvaluationV2.


        :param changed_date: The changed_date of this EvaluationQualityV2TopicEvaluationV2.
        :type: datetime
        """
        
        self._changed_date = changed_date

    @property
    def event_type(self):
        """
        Gets the event_type of this EvaluationQualityV2TopicEvaluationV2.


        :return: The event_type of this EvaluationQualityV2TopicEvaluationV2.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """
        Sets the event_type of this EvaluationQualityV2TopicEvaluationV2.


        :param event_type: The event_type of this EvaluationQualityV2TopicEvaluationV2.
        :type: str
        """
        
        self._event_type = event_type

    @property
    def resource_id(self):
        """
        Gets the resource_id of this EvaluationQualityV2TopicEvaluationV2.


        :return: The resource_id of this EvaluationQualityV2TopicEvaluationV2.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this EvaluationQualityV2TopicEvaluationV2.


        :param resource_id: The resource_id of this EvaluationQualityV2TopicEvaluationV2.
        :type: str
        """
        
        self._resource_id = resource_id

    @property
    def resource_type(self):
        """
        Gets the resource_type of this EvaluationQualityV2TopicEvaluationV2.


        :return: The resource_type of this EvaluationQualityV2TopicEvaluationV2.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this EvaluationQualityV2TopicEvaluationV2.


        :param resource_type: The resource_type of this EvaluationQualityV2TopicEvaluationV2.
        :type: str
        """
        
        self._resource_type = resource_type

    @property
    def division_ids(self):
        """
        Gets the division_ids of this EvaluationQualityV2TopicEvaluationV2.


        :return: The division_ids of this EvaluationQualityV2TopicEvaluationV2.
        :rtype: list[str]
        """
        return self._division_ids

    @division_ids.setter
    def division_ids(self, division_ids):
        """
        Sets the division_ids of this EvaluationQualityV2TopicEvaluationV2.


        :param division_ids: The division_ids of this EvaluationQualityV2TopicEvaluationV2.
        :type: list[str]
        """
        
        self._division_ids = division_ids

    @property
    def rescore(self):
        """
        Gets the rescore of this EvaluationQualityV2TopicEvaluationV2.


        :return: The rescore of this EvaluationQualityV2TopicEvaluationV2.
        :rtype: bool
        """
        return self._rescore

    @rescore.setter
    def rescore(self, rescore):
        """
        Sets the rescore of this EvaluationQualityV2TopicEvaluationV2.


        :param rescore: The rescore of this EvaluationQualityV2TopicEvaluationV2.
        :type: bool
        """
        
        self._rescore = rescore

    @property
    def conversation_date(self):
        """
        Gets the conversation_date of this EvaluationQualityV2TopicEvaluationV2.


        :return: The conversation_date of this EvaluationQualityV2TopicEvaluationV2.
        :rtype: datetime
        """
        return self._conversation_date

    @conversation_date.setter
    def conversation_date(self, conversation_date):
        """
        Sets the conversation_date of this EvaluationQualityV2TopicEvaluationV2.


        :param conversation_date: The conversation_date of this EvaluationQualityV2TopicEvaluationV2.
        :type: datetime
        """
        
        self._conversation_date = conversation_date

    @property
    def media_type(self):
        """
        Gets the media_type of this EvaluationQualityV2TopicEvaluationV2.


        :return: The media_type of this EvaluationQualityV2TopicEvaluationV2.
        :rtype: list[str]
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """
        Sets the media_type of this EvaluationQualityV2TopicEvaluationV2.


        :param media_type: The media_type of this EvaluationQualityV2TopicEvaluationV2.
        :type: list[str]
        """
        
        self._media_type = media_type

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

