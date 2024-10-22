from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerPlayers")


@_attrs_define
class ServerPlayers:
    """
    Attributes:
        max_ (Union[Unset, int]): Maximum player count (slots) Example: 20.
        count (Union[Unset, int]): Current player count
        list_ (Union[Unset, List[str]]): Current player list (not always available)
    """

    max_: Union[Unset, int] = UNSET
    count: Union[Unset, int] = UNSET
    list_: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_ = self.max_

        count = self.count

        list_: Union[Unset, List[str]] = UNSET
        if not isinstance(self.list_, Unset):
            list_ = self.list_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_ is not UNSET:
            field_dict["max"] = max_
        if count is not UNSET:
            field_dict["count"] = count
        if list_ is not UNSET:
            field_dict["list"] = list_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        max_ = d.pop("max", UNSET)

        count = d.pop("count", UNSET)

        list_ = cast(List[str], d.pop("list", UNSET))

        server_players = cls(
            max_=max_,
            count=count,
            list_=list_,
        )

        server_players.additional_properties = d
        return server_players

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
