from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditPoolMember")


@_attrs_define
class CreditPoolMember:
    """
    Attributes:
        account (Union[Unset, str]): Unique account ID of the pool member Example: EwYiY9IAMtQBTb6s.
        name (Union[Unset, str]): Account name of the pool member Example: example.
        share (Union[Unset, float]): Share of the credits in this pool that are owned by the account Example: 0.5.
        credits_ (Union[Unset, float]): Number of credits in the pool that are owned by the account Example: 21.
        is_owner (Union[Unset, bool]): Whether the account is the owner of this credit pool
    """

    account: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    share: Union[Unset, float] = UNSET
    credits_: Union[Unset, float] = UNSET
    is_owner: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account = self.account

        name = self.name

        share = self.share

        credits_ = self.credits_

        is_owner = self.is_owner

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if name is not UNSET:
            field_dict["name"] = name
        if share is not UNSET:
            field_dict["share"] = share
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if is_owner is not UNSET:
            field_dict["isOwner"] = is_owner

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account = d.pop("account", UNSET)

        name = d.pop("name", UNSET)

        share = d.pop("share", UNSET)

        credits_ = d.pop("credits", UNSET)

        is_owner = d.pop("isOwner", UNSET)

        credit_pool_member = cls(
            account=account,
            name=name,
            share=share,
            credits_=credits_,
            is_owner=is_owner,
        )

        credit_pool_member.additional_properties = d
        return credit_pool_member

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
