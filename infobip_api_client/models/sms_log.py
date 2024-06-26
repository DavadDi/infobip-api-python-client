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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from infobip_api_client.models.message_error import MessageError
from infobip_api_client.models.message_price import MessagePrice
from infobip_api_client.models.message_status import MessageStatus
from typing import Optional, Set
from typing_extensions import Self


class SmsLog(BaseModel):
    """
    SmsLog
    """  # noqa: E501

    application_id: Optional[StrictStr] = Field(
        default=None,
        description="Application id used to send the message. For more details, see our [documentation](https://www.infobip.com/docs/cpaas-x/application-and-entity-management).",
        alias="applicationId",
    )
    bulk_id: Optional[StrictStr] = Field(
        default=None,
        description="Unique ID assigned to the request if messaging multiple recipients or sending multiple messages via a single API request.",
        alias="bulkId",
    )
    done_at: Optional[datetime] = Field(
        default=None,
        description="Date and time when the Infobip services finished processing the message (i.e. delivered to the destination, delivered to the destination network, etc.). Has the following format: `yyyy-MM-dd'T'HH:mm:ss.SSSZ`.",
        alias="doneAt",
    )
    entity_id: Optional[StrictStr] = Field(
        default=None,
        description="Entity id used to send the message. For more details, see our [documentation](https://www.infobip.com/docs/cpaas-x/application-and-entity-management).",
        alias="entityId",
    )
    error: Optional[MessageError] = None
    var_from: Optional[StrictStr] = Field(
        default=None,
        description="Sender ID that can be alphanumeric or numeric.",
        alias="from",
    )
    mcc_mnc: Optional[StrictStr] = Field(
        default=None, description="Mobile country and network codes.", alias="mccMnc"
    )
    message_id: Optional[StrictStr] = Field(
        default=None, description="Unique message ID.", alias="messageId"
    )
    price: Optional[MessagePrice] = None
    sent_at: Optional[datetime] = Field(
        default=None,
        description="Date and time when the message was [scheduled](https://www.infobip.com/docs/api#channels/sms/get-scheduled-sms-messages) to be sent. Has the following format: `yyyy-MM-dd'T'HH:mm:ss.SSSZ`.",
        alias="sentAt",
    )
    sms_count: Optional[StrictInt] = Field(
        default=None,
        description="The number of parts the message content was split into.",
        alias="smsCount",
    )
    status: Optional[MessageStatus] = None
    text: Optional[StrictStr] = Field(
        default=None, description="Content of the message being sent."
    )
    to: Optional[StrictStr] = Field(
        default=None, description="The destination address of the message."
    )
    __properties: ClassVar[List[str]] = [
        "applicationId",
        "bulkId",
        "doneAt",
        "entityId",
        "error",
        "from",
        "mccMnc",
        "messageId",
        "price",
        "sentAt",
        "smsCount",
        "status",
        "text",
        "to",
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
        """Create an instance of SmsLog from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict["error"] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict["price"] = self.price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict["status"] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SmsLog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "applicationId": obj.get("applicationId"),
                "bulkId": obj.get("bulkId"),
                "doneAt": obj.get("doneAt"),
                "entityId": obj.get("entityId"),
                "error": MessageError.from_dict(obj["error"])
                if obj.get("error") is not None
                else None,
                "from": obj.get("from"),
                "mccMnc": obj.get("mccMnc"),
                "messageId": obj.get("messageId"),
                "price": MessagePrice.from_dict(obj["price"])
                if obj.get("price") is not None
                else None,
                "sentAt": obj.get("sentAt"),
                "smsCount": obj.get("smsCount"),
                "status": MessageStatus.from_dict(obj["status"])
                if obj.get("status") is not None
                else None,
                "text": obj.get("text"),
                "to": obj.get("to"),
            }
        )
        return _obj
