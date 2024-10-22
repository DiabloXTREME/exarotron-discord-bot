from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    server_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/servers/{server_id}/playerlists/",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None
    if response.status_code == 400:
        return None
    if response.status_code == 403:
        return None
    if response.status_code == 404:
        return None
    if response.status_code == 500:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Get available player lists

     A player list is a list of players such as the whitelist, ops or bans. Player list entries are
    usually usernames, but might be something else, e.g. IPs in the banned-ips list. All player list
    operations are storage operations that might take a while, so try to reduce the amount of requests
    and combine actions when possible (e.g. adding/deleting multiple entries at once). Player lists are
    also cached and might not immediately return new results when changed through other methods.

    Args:
        server_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    server_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Get available player lists

     A player list is a list of players such as the whitelist, ops or bans. Player list entries are
    usually usernames, but might be something else, e.g. IPs in the banned-ips list. All player list
    operations are storage operations that might take a while, so try to reduce the amount of requests
    and combine actions when possible (e.g. adding/deleting multiple entries at once). Player lists are
    also cached and might not immediately return new results when changed through other methods.

    Args:
        server_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
