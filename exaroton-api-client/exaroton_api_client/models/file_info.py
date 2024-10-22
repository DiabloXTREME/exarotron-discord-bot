from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileInfo")


@_attrs_define
class FileInfo:
    """
    Attributes:
        path (Union[Unset, str]):  Example: world/playerdata.
        name (Union[Unset, str]):  Example: playerdata.
        is_text_file (Union[Unset, bool]):
        is_config_file (Union[Unset, bool]):
        is_directory (Union[Unset, bool]):  Example: True.
        is_log (Union[Unset, bool]):
        is_readable (Union[Unset, bool]):
        is_writable (Union[Unset, bool]):
        size (Union[Unset, int]):  Example: 4096.
        children (Union[List['FileInfo'], None, Unset]):
    """

    path: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    is_text_file: Union[Unset, bool] = UNSET
    is_config_file: Union[Unset, bool] = UNSET
    is_directory: Union[Unset, bool] = UNSET
    is_log: Union[Unset, bool] = UNSET
    is_readable: Union[Unset, bool] = UNSET
    is_writable: Union[Unset, bool] = UNSET
    size: Union[Unset, int] = UNSET
    children: Union[List["FileInfo"], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path

        name = self.name

        is_text_file = self.is_text_file

        is_config_file = self.is_config_file

        is_directory = self.is_directory

        is_log = self.is_log

        is_readable = self.is_readable

        is_writable = self.is_writable

        size = self.size

        children: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.children, Unset):
            children = UNSET
        elif isinstance(self.children, list):
            children = []
            for children_type_0_item_data in self.children:
                children_type_0_item = children_type_0_item_data.to_dict()
                children.append(children_type_0_item)

        else:
            children = self.children

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if name is not UNSET:
            field_dict["name"] = name
        if is_text_file is not UNSET:
            field_dict["isTextFile"] = is_text_file
        if is_config_file is not UNSET:
            field_dict["isConfigFile"] = is_config_file
        if is_directory is not UNSET:
            field_dict["isDirectory"] = is_directory
        if is_log is not UNSET:
            field_dict["isLog"] = is_log
        if is_readable is not UNSET:
            field_dict["isReadable"] = is_readable
        if is_writable is not UNSET:
            field_dict["isWritable"] = is_writable
        if size is not UNSET:
            field_dict["size"] = size
        if children is not UNSET:
            field_dict["children"] = children

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path", UNSET)

        name = d.pop("name", UNSET)

        is_text_file = d.pop("isTextFile", UNSET)

        is_config_file = d.pop("isConfigFile", UNSET)

        is_directory = d.pop("isDirectory", UNSET)

        is_log = d.pop("isLog", UNSET)

        is_readable = d.pop("isReadable", UNSET)

        is_writable = d.pop("isWritable", UNSET)

        size = d.pop("size", UNSET)

        def _parse_children(data: object) -> Union[List["FileInfo"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                children_type_0 = []
                _children_type_0 = data
                for children_type_0_item_data in _children_type_0:
                    children_type_0_item = FileInfo.from_dict(children_type_0_item_data)

                    children_type_0.append(children_type_0_item)

                return children_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["FileInfo"], None, Unset], data)

        children = _parse_children(d.pop("children", UNSET))

        file_info = cls(
            path=path,
            name=name,
            is_text_file=is_text_file,
            is_config_file=is_config_file,
            is_directory=is_directory,
            is_log=is_log,
            is_readable=is_readable,
            is_writable=is_writable,
            size=size,
            children=children,
        )

        file_info.additional_properties = d
        return file_info

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
