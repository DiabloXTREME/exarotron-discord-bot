from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditPool")


@_attrs_define
class CreditPool:
    """
    Attributes:
        id (Union[Unset, str]): Unique credit pool ID Example: X4iJREgqBGFSBtn0.
        name (Union[Unset, str]): Credit pool name Example: example.
        credits_ (Union[Unset, float]): Credits in this credit pool Example: 100.05.
        servers (Union[Unset, int]): Number of servers in this credit pool Example: 1.
        owner (Union[Unset, str]): Unique account ID of the pool owner Example: EwYiY9IAMtQBTb6s.
        is_owner (Union[Unset, bool]): Whether the current user is the owner of this credit pool
        members (Union[Unset, int]): Number of members in this credit pool Example: 2.
        own_share (Union[Unset, float]): Share of the credits in this pool that are owned by the current user Example:
            0.5.
        own_credits (Union[Unset, float]): Number of credits in the pool that are owned by the current user Example: 21.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    credits_: Union[Unset, float] = UNSET
    servers: Union[Unset, int] = UNSET
    owner: Union[Unset, str] = UNSET
    is_owner: Union[Unset, bool] = UNSET
    members: Union[Unset, int] = UNSET
    own_share: Union[Unset, float] = UNSET
    own_credits: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        credits_ = self.credits_

        servers = self.servers

        owner = self.owner

        is_owner = self.is_owner

        members = self.members

        own_share = self.own_share

        own_credits = self.own_credits

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if servers is not UNSET:
            field_dict["servers"] = servers
        if owner is not UNSET:
            field_dict["owner"] = owner
        if is_owner is not UNSET:
            field_dict["isOwner"] = is_owner
        if members is not UNSET:
            field_dict["members"] = members
        if own_share is not UNSET:
            field_dict["ownShare"] = own_share
        if own_credits is not UNSET:
            field_dict["ownCredits"] = own_credits

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        credits_ = d.pop("credits", UNSET)

        servers = d.pop("servers", UNSET)

        owner = d.pop("owner", UNSET)

        is_owner = d.pop("isOwner", UNSET)

        members = d.pop("members", UNSET)

        own_share = d.pop("ownShare", UNSET)

        own_credits = d.pop("ownCredits", UNSET)

        credit_pool = cls(
            id=id,
            name=name,
            credits_=credits_,
            servers=servers,
            owner=owner,
            is_owner=is_owner,
            members=members,
            own_share=own_share,
            own_credits=own_credits,
        )

        credit_pool.additional_properties = d
        return credit_pool

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
