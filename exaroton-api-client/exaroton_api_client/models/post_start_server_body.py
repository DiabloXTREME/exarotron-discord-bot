from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostStartServerBody")


@_attrs_define
class PostStartServerBody:
    """
    Attributes:
        use_own_credits (Union[Unset, bool]):
    """

    use_own_credits: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        use_own_credits = self.use_own_credits

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if use_own_credits is not UNSET:
            field_dict["useOwnCredits"] = use_own_credits

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        use_own_credits = d.pop("useOwnCredits", UNSET)

        post_start_server_body = cls(
            use_own_credits=use_own_credits,
        )

        post_start_server_body.additional_properties = d
        return post_start_server_body

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
