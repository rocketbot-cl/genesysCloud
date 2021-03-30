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

class SmsPhoneNumber(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SmsPhoneNumber - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'phone_number': 'str',
            'phone_number_type': 'str',
            'provisioned_through_pure_cloud': 'bool',
            'phone_number_status': 'str',
            'capabilities': 'list[str]',
            'country_code': 'str',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'created_by': 'User',
            'modified_by': 'User',
            'version': 'int',
            'purchase_date': 'datetime',
            'cancellation_date': 'datetime',
            'renewal_date': 'datetime',
            'auto_renewable': 'str',
            'address_id': 'SmsAddress',
            'short_code_billing_type': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'phone_number': 'phoneNumber',
            'phone_number_type': 'phoneNumberType',
            'provisioned_through_pure_cloud': 'provisionedThroughPureCloud',
            'phone_number_status': 'phoneNumberStatus',
            'capabilities': 'capabilities',
            'country_code': 'countryCode',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'created_by': 'createdBy',
            'modified_by': 'modifiedBy',
            'version': 'version',
            'purchase_date': 'purchaseDate',
            'cancellation_date': 'cancellationDate',
            'renewal_date': 'renewalDate',
            'auto_renewable': 'autoRenewable',
            'address_id': 'addressId',
            'short_code_billing_type': 'shortCodeBillingType',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._phone_number = None
        self._phone_number_type = None
        self._provisioned_through_pure_cloud = None
        self._phone_number_status = None
        self._capabilities = None
        self._country_code = None
        self._date_created = None
        self._date_modified = None
        self._created_by = None
        self._modified_by = None
        self._version = None
        self._purchase_date = None
        self._cancellation_date = None
        self._renewal_date = None
        self._auto_renewable = None
        self._address_id = None
        self._short_code_billing_type = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this SmsPhoneNumber.
        The globally unique identifier for the object.

        :return: The id of this SmsPhoneNumber.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SmsPhoneNumber.
        The globally unique identifier for the object.

        :param id: The id of this SmsPhoneNumber.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this SmsPhoneNumber.


        :return: The name of this SmsPhoneNumber.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SmsPhoneNumber.


        :param name: The name of this SmsPhoneNumber.
        :type: str
        """
        
        self._name = name

    @property
    def phone_number(self):
        """
        Gets the phone_number of this SmsPhoneNumber.
        A phone number provisioned for SMS communications in E.164 format. E.g. +13175555555 or +34234234234

        :return: The phone_number of this SmsPhoneNumber.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this SmsPhoneNumber.
        A phone number provisioned for SMS communications in E.164 format. E.g. +13175555555 or +34234234234

        :param phone_number: The phone_number of this SmsPhoneNumber.
        :type: str
        """
        
        self._phone_number = phone_number

    @property
    def phone_number_type(self):
        """
        Gets the phone_number_type of this SmsPhoneNumber.
        Type of the phone number provisioned.

        :return: The phone_number_type of this SmsPhoneNumber.
        :rtype: str
        """
        return self._phone_number_type

    @phone_number_type.setter
    def phone_number_type(self, phone_number_type):
        """
        Sets the phone_number_type of this SmsPhoneNumber.
        Type of the phone number provisioned.

        :param phone_number_type: The phone_number_type of this SmsPhoneNumber.
        :type: str
        """
        allowed_values = ["local", "mobile", "tollfree", "shortcode"]
        if phone_number_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for phone_number_type -> " + phone_number_type)
            self._phone_number_type = "outdated_sdk_version"
        else:
            self._phone_number_type = phone_number_type

    @property
    def provisioned_through_pure_cloud(self):
        """
        Gets the provisioned_through_pure_cloud of this SmsPhoneNumber.
        Is set to false, if the phone number is provisioned through a SMS provider, outside of PureCloud

        :return: The provisioned_through_pure_cloud of this SmsPhoneNumber.
        :rtype: bool
        """
        return self._provisioned_through_pure_cloud

    @provisioned_through_pure_cloud.setter
    def provisioned_through_pure_cloud(self, provisioned_through_pure_cloud):
        """
        Sets the provisioned_through_pure_cloud of this SmsPhoneNumber.
        Is set to false, if the phone number is provisioned through a SMS provider, outside of PureCloud

        :param provisioned_through_pure_cloud: The provisioned_through_pure_cloud of this SmsPhoneNumber.
        :type: bool
        """
        
        self._provisioned_through_pure_cloud = provisioned_through_pure_cloud

    @property
    def phone_number_status(self):
        """
        Gets the phone_number_status of this SmsPhoneNumber.
        Status of the provisioned phone number.

        :return: The phone_number_status of this SmsPhoneNumber.
        :rtype: str
        """
        return self._phone_number_status

    @phone_number_status.setter
    def phone_number_status(self, phone_number_status):
        """
        Sets the phone_number_status of this SmsPhoneNumber.
        Status of the provisioned phone number.

        :param phone_number_status: The phone_number_status of this SmsPhoneNumber.
        :type: str
        """
        allowed_values = ["INVALID", "ACTIVE", "PORTING", "PENDING", "PENDING_CANCELLATION"]
        if phone_number_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for phone_number_status -> " + phone_number_status)
            self._phone_number_status = "outdated_sdk_version"
        else:
            self._phone_number_status = phone_number_status

    @property
    def capabilities(self):
        """
        Gets the capabilities of this SmsPhoneNumber.
        The capabilities of the phone number available for provisioning.

        :return: The capabilities of this SmsPhoneNumber.
        :rtype: list[str]
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """
        Sets the capabilities of this SmsPhoneNumber.
        The capabilities of the phone number available for provisioning.

        :param capabilities: The capabilities of this SmsPhoneNumber.
        :type: list[str]
        """
        
        self._capabilities = capabilities

    @property
    def country_code(self):
        """
        Gets the country_code of this SmsPhoneNumber.
        The ISO 3166-1 alpha-2 country code of the country this phone number is associated with.

        :return: The country_code of this SmsPhoneNumber.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """
        Sets the country_code of this SmsPhoneNumber.
        The ISO 3166-1 alpha-2 country code of the country this phone number is associated with.

        :param country_code: The country_code of this SmsPhoneNumber.
        :type: str
        """
        
        self._country_code = country_code

    @property
    def date_created(self):
        """
        Gets the date_created of this SmsPhoneNumber.
        Date this phone number was provisioned. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this SmsPhoneNumber.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this SmsPhoneNumber.
        Date this phone number was provisioned. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this SmsPhoneNumber.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this SmsPhoneNumber.
        Date this phone number was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this SmsPhoneNumber.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this SmsPhoneNumber.
        Date this phone number was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this SmsPhoneNumber.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def created_by(self):
        """
        Gets the created_by of this SmsPhoneNumber.
        User that provisioned this phone number

        :return: The created_by of this SmsPhoneNumber.
        :rtype: User
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this SmsPhoneNumber.
        User that provisioned this phone number

        :param created_by: The created_by of this SmsPhoneNumber.
        :type: User
        """
        
        self._created_by = created_by

    @property
    def modified_by(self):
        """
        Gets the modified_by of this SmsPhoneNumber.
        User that last modified this phone number

        :return: The modified_by of this SmsPhoneNumber.
        :rtype: User
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """
        Sets the modified_by of this SmsPhoneNumber.
        User that last modified this phone number

        :param modified_by: The modified_by of this SmsPhoneNumber.
        :type: User
        """
        
        self._modified_by = modified_by

    @property
    def version(self):
        """
        Gets the version of this SmsPhoneNumber.
        Version number required for updates.

        :return: The version of this SmsPhoneNumber.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this SmsPhoneNumber.
        Version number required for updates.

        :param version: The version of this SmsPhoneNumber.
        :type: int
        """
        
        self._version = version

    @property
    def purchase_date(self):
        """
        Gets the purchase_date of this SmsPhoneNumber.
        Date this phone number was purchased, if the phoneNumberType is shortcode. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The purchase_date of this SmsPhoneNumber.
        :rtype: datetime
        """
        return self._purchase_date

    @purchase_date.setter
    def purchase_date(self, purchase_date):
        """
        Sets the purchase_date of this SmsPhoneNumber.
        Date this phone number was purchased, if the phoneNumberType is shortcode. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param purchase_date: The purchase_date of this SmsPhoneNumber.
        :type: datetime
        """
        
        self._purchase_date = purchase_date

    @property
    def cancellation_date(self):
        """
        Gets the cancellation_date of this SmsPhoneNumber.
        Contract end date of this phone number, if the phoneNumberType is shortcode. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The cancellation_date of this SmsPhoneNumber.
        :rtype: datetime
        """
        return self._cancellation_date

    @cancellation_date.setter
    def cancellation_date(self, cancellation_date):
        """
        Sets the cancellation_date of this SmsPhoneNumber.
        Contract end date of this phone number, if the phoneNumberType is shortcode. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param cancellation_date: The cancellation_date of this SmsPhoneNumber.
        :type: datetime
        """
        
        self._cancellation_date = cancellation_date

    @property
    def renewal_date(self):
        """
        Gets the renewal_date of this SmsPhoneNumber.
        Contract renewal date of this phone number, if the phoneNumberType is shortcode. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The renewal_date of this SmsPhoneNumber.
        :rtype: datetime
        """
        return self._renewal_date

    @renewal_date.setter
    def renewal_date(self, renewal_date):
        """
        Sets the renewal_date of this SmsPhoneNumber.
        Contract renewal date of this phone number, if the phoneNumberType is shortcode. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param renewal_date: The renewal_date of this SmsPhoneNumber.
        :type: datetime
        """
        
        self._renewal_date = renewal_date

    @property
    def auto_renewable(self):
        """
        Gets the auto_renewable of this SmsPhoneNumber.
        Renewal time period of this phone number, if the phoneNumberType is shortcode.

        :return: The auto_renewable of this SmsPhoneNumber.
        :rtype: str
        """
        return self._auto_renewable

    @auto_renewable.setter
    def auto_renewable(self, auto_renewable):
        """
        Sets the auto_renewable of this SmsPhoneNumber.
        Renewal time period of this phone number, if the phoneNumberType is shortcode.

        :param auto_renewable: The auto_renewable of this SmsPhoneNumber.
        :type: str
        """
        allowed_values = ["Quarterly"]
        if auto_renewable.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for auto_renewable -> " + auto_renewable)
            self._auto_renewable = "outdated_sdk_version"
        else:
            self._auto_renewable = auto_renewable

    @property
    def address_id(self):
        """
        Gets the address_id of this SmsPhoneNumber.
        The id of an address attached to this phone number.

        :return: The address_id of this SmsPhoneNumber.
        :rtype: SmsAddress
        """
        return self._address_id

    @address_id.setter
    def address_id(self, address_id):
        """
        Sets the address_id of this SmsPhoneNumber.
        The id of an address attached to this phone number.

        :param address_id: The address_id of this SmsPhoneNumber.
        :type: SmsAddress
        """
        
        self._address_id = address_id

    @property
    def short_code_billing_type(self):
        """
        Gets the short_code_billing_type of this SmsPhoneNumber.
        BillingType of this phone number, if the phoneNumberType is shortcode.

        :return: The short_code_billing_type of this SmsPhoneNumber.
        :rtype: str
        """
        return self._short_code_billing_type

    @short_code_billing_type.setter
    def short_code_billing_type(self, short_code_billing_type):
        """
        Sets the short_code_billing_type of this SmsPhoneNumber.
        BillingType of this phone number, if the phoneNumberType is shortcode.

        :param short_code_billing_type: The short_code_billing_type of this SmsPhoneNumber.
        :type: str
        """
        allowed_values = ["Basic", "Vanity"]
        if short_code_billing_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for short_code_billing_type -> " + short_code_billing_type)
            self._short_code_billing_type = "outdated_sdk_version"
        else:
            self._short_code_billing_type = short_code_billing_type

    @property
    def self_uri(self):
        """
        Gets the self_uri of this SmsPhoneNumber.
        The URI for this object

        :return: The self_uri of this SmsPhoneNumber.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this SmsPhoneNumber.
        The URI for this object

        :param self_uri: The self_uri of this SmsPhoneNumber.
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
