from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigFileOption")


@_attrs_define
class ConfigFileOption:
    """
    Attributes:
        key (Union[Unset, str]):  Example: max-players.
        label (Union[Unset, str]):  Example: Max Players.
        type (Union[Unset, str]):  Example: integer.
        value (Union[Unset, bool, int, str]):  Example: 20.
        options (Union[List[str], None, Unset]):
    """

    key: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    value: Union[Unset, bool, int, str] = UNSET
    options: Union[List[str], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key

        label = self.label

        type = self.type

        value: Union[Unset, bool, int, str]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        options: Union[List[str], None, Unset]
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, list):
            options = self.options

        else:
            options = self.options

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if label is not UNSET:
            field_dict["label"] = label
        if type is not UNSET:
            field_dict["type"] = type
        if value is not UNSET:
            field_dict["value"] = value
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key", UNSET)

        label = d.pop("label", UNSET)

        type = d.pop("type", UNSET)

        def _parse_value(data: object) -> Union[Unset, bool, int, str]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, bool, int, str], data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_options(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_type_0 = cast(List[str], data)

                return options_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        options = _parse_options(d.pop("options", UNSET))

        config_file_option = cls(
            key=key,
            label=label,
            type=type,
            value=value,
            options=options,
        )

        config_file_option.additional_properties = d
        return config_file_option

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
