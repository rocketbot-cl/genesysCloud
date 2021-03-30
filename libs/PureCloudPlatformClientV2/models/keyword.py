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

class Keyword(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Keyword - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'phrase': 'str',
            'confidence': 'int',
            'agent_score_modifier': 'int',
            'customer_score_modifier': 'int',
            'alternate_spellings': 'list[str]',
            'pronunciations': 'list[str]',
            'anti_words': 'list[str]',
            'anti_pronunciations': 'list[str]',
            'spotability_index': 'float',
            'margin_of_error': 'float',
            'pronunciation': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'phrase': 'phrase',
            'confidence': 'confidence',
            'agent_score_modifier': 'agentScoreModifier',
            'customer_score_modifier': 'customerScoreModifier',
            'alternate_spellings': 'alternateSpellings',
            'pronunciations': 'pronunciations',
            'anti_words': 'antiWords',
            'anti_pronunciations': 'antiPronunciations',
            'spotability_index': 'spotabilityIndex',
            'margin_of_error': 'marginOfError',
            'pronunciation': 'pronunciation'
        }

        self._id = None
        self._name = None
        self._phrase = None
        self._confidence = None
        self._agent_score_modifier = None
        self._customer_score_modifier = None
        self._alternate_spellings = None
        self._pronunciations = None
        self._anti_words = None
        self._anti_pronunciations = None
        self._spotability_index = None
        self._margin_of_error = None
        self._pronunciation = None

    @property
    def id(self):
        """
        Gets the id of this Keyword.


        :return: The id of this Keyword.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Keyword.


        :param id: The id of this Keyword.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Keyword.


        :return: The name of this Keyword.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Keyword.


        :param name: The name of this Keyword.
        :type: str
        """
        
        self._name = name

    @property
    def phrase(self):
        """
        Gets the phrase of this Keyword.
        The word or phrase which is being looked for with speech recognition.

        :return: The phrase of this Keyword.
        :rtype: str
        """
        return self._phrase

    @phrase.setter
    def phrase(self, phrase):
        """
        Sets the phrase of this Keyword.
        The word or phrase which is being looked for with speech recognition.

        :param phrase: The phrase of this Keyword.
        :type: str
        """
        
        self._phrase = phrase

    @property
    def confidence(self):
        """
        Gets the confidence of this Keyword.
        A sensitivity threshold that can be increased to lower false positives or decreased to reduce false negatives.

        :return: The confidence of this Keyword.
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this Keyword.
        A sensitivity threshold that can be increased to lower false positives or decreased to reduce false negatives.

        :param confidence: The confidence of this Keyword.
        :type: int
        """
        
        self._confidence = confidence

    @property
    def agent_score_modifier(self):
        """
        Gets the agent_score_modifier of this Keyword.
        A modifier to the evaluation score when the phrase is spotted in the agent channel

        :return: The agent_score_modifier of this Keyword.
        :rtype: int
        """
        return self._agent_score_modifier

    @agent_score_modifier.setter
    def agent_score_modifier(self, agent_score_modifier):
        """
        Sets the agent_score_modifier of this Keyword.
        A modifier to the evaluation score when the phrase is spotted in the agent channel

        :param agent_score_modifier: The agent_score_modifier of this Keyword.
        :type: int
        """
        
        self._agent_score_modifier = agent_score_modifier

    @property
    def customer_score_modifier(self):
        """
        Gets the customer_score_modifier of this Keyword.
        A modifier to the evaluation score when the phrase is spotted in the customer channel

        :return: The customer_score_modifier of this Keyword.
        :rtype: int
        """
        return self._customer_score_modifier

    @customer_score_modifier.setter
    def customer_score_modifier(self, customer_score_modifier):
        """
        Sets the customer_score_modifier of this Keyword.
        A modifier to the evaluation score when the phrase is spotted in the customer channel

        :param customer_score_modifier: The customer_score_modifier of this Keyword.
        :type: int
        """
        
        self._customer_score_modifier = customer_score_modifier

    @property
    def alternate_spellings(self):
        """
        Gets the alternate_spellings of this Keyword.
        Other spellings of the phrase that can be added to reduce missed spots (false negatives).

        :return: The alternate_spellings of this Keyword.
        :rtype: list[str]
        """
        return self._alternate_spellings

    @alternate_spellings.setter
    def alternate_spellings(self, alternate_spellings):
        """
        Sets the alternate_spellings of this Keyword.
        Other spellings of the phrase that can be added to reduce missed spots (false negatives).

        :param alternate_spellings: The alternate_spellings of this Keyword.
        :type: list[str]
        """
        
        self._alternate_spellings = alternate_spellings

    @property
    def pronunciations(self):
        """
        Gets the pronunciations of this Keyword.
        The phonetic spellings for the phrase and alternate spellings.

        :return: The pronunciations of this Keyword.
        :rtype: list[str]
        """
        return self._pronunciations

    @pronunciations.setter
    def pronunciations(self, pronunciations):
        """
        Sets the pronunciations of this Keyword.
        The phonetic spellings for the phrase and alternate spellings.

        :param pronunciations: The pronunciations of this Keyword.
        :type: list[str]
        """
        
        self._pronunciations = pronunciations

    @property
    def anti_words(self):
        """
        Gets the anti_words of this Keyword.
        Words that are similar to the phrase but not desired. Added to reduce incorrect spots (false positives).

        :return: The anti_words of this Keyword.
        :rtype: list[str]
        """
        return self._anti_words

    @anti_words.setter
    def anti_words(self, anti_words):
        """
        Sets the anti_words of this Keyword.
        Words that are similar to the phrase but not desired. Added to reduce incorrect spots (false positives).

        :param anti_words: The anti_words of this Keyword.
        :type: list[str]
        """
        
        self._anti_words = anti_words

    @property
    def anti_pronunciations(self):
        """
        Gets the anti_pronunciations of this Keyword.
        The phonetic spellings for the antiWords.

        :return: The anti_pronunciations of this Keyword.
        :rtype: list[str]
        """
        return self._anti_pronunciations

    @anti_pronunciations.setter
    def anti_pronunciations(self, anti_pronunciations):
        """
        Sets the anti_pronunciations of this Keyword.
        The phonetic spellings for the antiWords.

        :param anti_pronunciations: The anti_pronunciations of this Keyword.
        :type: list[str]
        """
        
        self._anti_pronunciations = anti_pronunciations

    @property
    def spotability_index(self):
        """
        Gets the spotability_index of this Keyword.
        A prediction of how easy it is to unambiguously spot the keyword within its language based on spelling.

        :return: The spotability_index of this Keyword.
        :rtype: float
        """
        return self._spotability_index

    @spotability_index.setter
    def spotability_index(self, spotability_index):
        """
        Sets the spotability_index of this Keyword.
        A prediction of how easy it is to unambiguously spot the keyword within its language based on spelling.

        :param spotability_index: The spotability_index of this Keyword.
        :type: float
        """
        
        self._spotability_index = spotability_index

    @property
    def margin_of_error(self):
        """
        Gets the margin_of_error of this Keyword.


        :return: The margin_of_error of this Keyword.
        :rtype: float
        """
        return self._margin_of_error

    @margin_of_error.setter
    def margin_of_error(self, margin_of_error):
        """
        Sets the margin_of_error of this Keyword.


        :param margin_of_error: The margin_of_error of this Keyword.
        :type: float
        """
        
        self._margin_of_error = margin_of_error

    @property
    def pronunciation(self):
        """
        Gets the pronunciation of this Keyword.


        :return: The pronunciation of this Keyword.
        :rtype: str
        """
        return self._pronunciation

    @pronunciation.setter
    def pronunciation(self, pronunciation):
        """
        Sets the pronunciation of this Keyword.


        :param pronunciation: The pronunciation of this Keyword.
        :type: str
        """
        
        self._pronunciation = pronunciation

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
