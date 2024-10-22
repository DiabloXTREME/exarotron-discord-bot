from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.server_status import ServerStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_players import ServerPlayers
    from ..models.server_software_type_0 import ServerSoftwareType0


T = TypeVar("T", bound="Server")


@_attrs_define
class Server:
    """
    Attributes:
        id (Union[Unset, str]): Unique server ID Example: EwYiY9IAMtQBTb6U.
        name (Union[Unset, str]): Server name Example: example.
        address (Union[Unset, str]): Full server address Example: example.exaroton.me.
        motd (Union[Unset, str]): The MOTD of the server Example: §7Welcome to the server of §aexample!.
        status (Union[Unset, ServerStatus]): Servers can have different numeric status codes. Depending on a server's
            status, only certain features might be available.
            Possible enum values:
             * 0 = OFFLINE
             * 1 = ONLINE
             * 2 = STARTING
             * 3 = STOPPING
             * 4 = RESTARTING
             * 5 = SAVING
             * 6 = LOADING
             * 7 = CRASHED
             * 8 = PENDING
             * 9 = TRANSFERRING
             * 10 = PREPARING
        host (Union[None, Unset, str]): Host machine the server is running on. Only available if the server is online.
        port (Union[Unset, int]): Port the server is listening on. Only available if the server is online.
        players (Union[Unset, ServerPlayers]):
        software (Union['ServerSoftwareType0', None, Unset]): Information about the installed server software
        shared (Union[Unset, bool]): Whether the server is accessed via the Share Access feature
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    motd: Union[Unset, str] = UNSET
    status: Union[Unset, ServerStatus] = UNSET
    host: Union[None, Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    players: Union[Unset, "ServerPlayers"] = UNSET
    software: Union["ServerSoftwareType0", None, Unset] = UNSET
    shared: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.server_software_type_0 import ServerSoftwareType0

        id = self.id

        name = self.name

        address = self.address

        motd = self.motd

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        host: Union[None, Unset, str]
        if isinstance(self.host, Unset):
            host = UNSET
        else:
            host = self.host

        port = self.port

        players: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.players, Unset):
            players = self.players.to_dict()

        software: Union[Dict[str, Any], None, Unset]
        if isinstance(self.software, Unset):
            software = UNSET
        elif isinstance(self.software, ServerSoftwareType0):
            software = self.software.to_dict()
        else:
            software = self.software

        shared = self.shared

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if motd is not UNSET:
            field_dict["motd"] = motd
        if status is not UNSET:
            field_dict["status"] = status
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if players is not UNSET:
            field_dict["players"] = players
        if software is not UNSET:
            field_dict["software"] = software
        if shared is not UNSET:
            field_dict["shared"] = shared

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.server_players import ServerPlayers
        from ..models.server_software_type_0 import ServerSoftwareType0

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        address = d.pop("address", UNSET)

        motd = d.pop("motd", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ServerStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ServerStatus(_status)

        def _parse_host(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        host = _parse_host(d.pop("host", UNSET))

        port = d.pop("port", UNSET)

        _players = d.pop("players", UNSET)
        players: Union[Unset, ServerPlayers]
        if isinstance(_players, Unset):
            players = UNSET
        else:
            players = ServerPlayers.from_dict(_players)

        def _parse_software(data: object) -> Union["ServerSoftwareType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                software_type_0 = ServerSoftwareType0.from_dict(data)

                return software_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ServerSoftwareType0", None, Unset], data)

        software = _parse_software(d.pop("software", UNSET))

        shared = d.pop("shared", UNSET)

        server = cls(
            id=id,
            name=name,
            address=address,
            motd=motd,
            status=status,
            host=host,
            port=port,
            players=players,
            software=software,
            shared=shared,
        )

        server.additional_properties = d
        return server

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
