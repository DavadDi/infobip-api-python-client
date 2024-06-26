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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class SmsTurkeyIysOptions(BaseModel):
    """
    IYS regulations specific parameters required for sending promotional SMS to phone numbers registered in Turkey.
    """  # noqa: E501

    brand_code: Optional[StrictInt] = Field(
        default=None,
        description="Brand code is an ID of the company based on a company VAT number. If not provided in request, default value is used from your Infobip account.",
        alias="brandCode",
    )
    recipient_type: StrictStr = Field(
        description="Recipient Type must be `TACIR` or `BIREYSEL`.",
        alias="recipientType",
    )
    __properties: ClassVar[List[str]] = ["brandCode", "recipientType"]

    @field_validator("recipient_type")
    def recipient_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["BIREYSEL", "TACIR"]):
            raise ValueError("must be one of enum values ('BIREYSEL', 'TACIR')")
        return value

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
        """Create an instance of SmsTurkeyIysOptions from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SmsTurkeyIysOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "brandCode": obj.get("brandCode"),
                "recipientType": obj.get("recipientType"),
            }
        )
        return _obj
