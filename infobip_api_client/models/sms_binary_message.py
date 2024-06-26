# coding: utf-8

"""
    Infobip Client API Libraries OpenAPI Specification

    OpenAPI specification containing public endpoints supported in client API libraries.

    The version of the OpenAPI document: 1.0.0
    Contact: support@infobip.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from infobip_api_client.models.sms_binary_content import SmsBinaryContent
from infobip_api_client.models.sms_delivery_time_window import SmsDeliveryTimeWindow
from infobip_api_client.models.sms_destination import SmsDestination
from infobip_api_client.models.sms_regional_options import SmsRegionalOptions
from typing import Optional, Set
from typing_extensions import Self


class SmsBinaryMessage(BaseModel):
    """
    An array of message objects of a single message or multiple messages sent under one bulk ID.
    """  # noqa: E501

    binary: Optional[SmsBinaryContent] = None
    callback_data: Optional[
        Annotated[str, Field(min_length=0, strict=True, max_length=4000)]
    ] = Field(
        default=None,
        description="Additional client data that will be sent on the notifyUrl. The maximum value is 4000 characters.",
        alias="callbackData",
    )
    delivery_time_window: Optional[SmsDeliveryTimeWindow] = Field(
        default=None, alias="deliveryTimeWindow"
    )
    destinations: List[SmsDestination] = Field(
        description="An array of destination objects for where messages are being sent. A valid destination is required."
    )
    flash: Optional[StrictBool] = Field(
        default=None,
        description="Allows for sending a [flash SMS](https://www.infobip.com/docs/sms/message-types#flash-sms) to automatically appear on recipient devices without interaction. Set to `true` to enable flash SMS, or leave the default value, `false` to send a standard SMS.",
    )
    var_from: Optional[StrictStr] = Field(
        default=None,
        description="The sender ID which can be alphanumeric or numeric (e.g., `CompanyName`). Make sure you don't exceed [character limit](https://www.infobip.com/docs/sms/get-started#sender-names).",
        alias="from",
    )
    intermediate_report: Optional[StrictBool] = Field(
        default=None,
        description="The [real-time intermediate delivery report](https://www.infobip.com/docs/api#channels/sms/receive-outbound-sms-message-report) containing GSM error codes, messages status, pricing, network and country codes, etc., which will be sent on your callback server. Defaults to `false`.",
        alias="intermediateReport",
    )
    notify_content_type: Optional[StrictStr] = Field(
        default=None,
        description="Preferred delivery report content type, `application/json` or `application/xml`.",
        alias="notifyContentType",
    )
    notify_url: Optional[StrictStr] = Field(
        default=None,
        description="The URL on your call back server on which the Delivery report will be sent.",
        alias="notifyUrl",
    )
    regional: Optional[SmsRegionalOptions] = None
    send_at: Optional[datetime] = Field(
        default=None,
        description="Date and time when the message is to be sent. Used for [scheduled SMS](https://www.infobip.com/docs/api#channels/sms/get-scheduled-sms-messages). Has the following format: `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, and can only be scheduled for no later than 180 days in advance.",
        alias="sendAt",
    )
    validity_period: Optional[StrictInt] = Field(
        default=None,
        description="The message validity period in minutes. When the period expires, it will not be allowed for the message to be sent. Validity period longer than 48h is not supported (in this case, it will be automatically set to 48h).",
        alias="validityPeriod",
    )
    entity_id: Optional[
        Annotated[str, Field(min_length=0, strict=True, max_length=66)]
    ] = Field(
        default=None,
        description="Required for entity use in a send request for outbound traffic. Returned in notification events. For more details, see our [documentation](https://www.infobip.com/docs/cpaas-x/application-and-entity-management).",
        alias="entityId",
    )
    application_id: Optional[
        Annotated[str, Field(min_length=0, strict=True, max_length=66)]
    ] = Field(
        default=None,
        description="Required for application use in a send request for outbound traffic. Returned in notification events. For more details, see our [documentation](https://www.infobip.com/docs/cpaas-x/application-and-entity-management).",
        alias="applicationId",
    )
    __properties: ClassVar[List[str]] = [
        "binary",
        "callbackData",
        "deliveryTimeWindow",
        "destinations",
        "flash",
        "from",
        "intermediateReport",
        "notifyContentType",
        "notifyUrl",
        "regional",
        "sendAt",
        "validityPeriod",
        "entityId",
        "applicationId",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SmsBinaryMessage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of binary
        if self.binary:
            _dict["binary"] = self.binary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of delivery_time_window
        if self.delivery_time_window:
            _dict["deliveryTimeWindow"] = self.delivery_time_window.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in destinations (list)
        _items = []
        if self.destinations:
            for _item in self.destinations:
                if _item:
                    _items.append(_item.to_dict())
            _dict["destinations"] = _items
        # override the default output from pydantic by calling `to_dict()` of regional
        if self.regional:
            _dict["regional"] = self.regional.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SmsBinaryMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "binary": SmsBinaryContent.from_dict(obj["binary"])
                if obj.get("binary") is not None
                else None,
                "callbackData": obj.get("callbackData"),
                "deliveryTimeWindow": SmsDeliveryTimeWindow.from_dict(
                    obj["deliveryTimeWindow"]
                )
                if obj.get("deliveryTimeWindow") is not None
                else None,
                "destinations": [
                    SmsDestination.from_dict(_item) for _item in obj["destinations"]
                ]
                if obj.get("destinations") is not None
                else None,
                "flash": obj.get("flash"),
                "from": obj.get("from"),
                "intermediateReport": obj.get("intermediateReport"),
                "notifyContentType": obj.get("notifyContentType"),
                "notifyUrl": obj.get("notifyUrl"),
                "regional": SmsRegionalOptions.from_dict(obj["regional"])
                if obj.get("regional") is not None
                else None,
                "sendAt": obj.get("sendAt"),
                "validityPeriod": obj.get("validityPeriod"),
                "entityId": obj.get("entityId"),
                "applicationId": obj.get("applicationId"),
            }
        )
        return _obj
