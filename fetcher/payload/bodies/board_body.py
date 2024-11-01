from __future__ import annotations

from pydantic import BaseModel
from typing_extensions import Required, TypedDict


class ClientInfo(TypedDict):
    CLIENT_ID: Required[str]
    CLIENT_KEY: Required[str]


class GetBoardInfo(TypedDict):
    ID: str
    PAGE: int


class BoardRequestBody(BaseModel):
    common: ClientInfo
    data: GetBoardInfo

    @classmethod
    def create_request_body(
        cls, client_info: ClientInfo, data: GetBoardInfo
    ) -> BoardRequestBody:
        return cls(common=client_info, data=data)
