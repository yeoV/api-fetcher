# For request body
from __future__ import annotations

from pydantic import BaseModel
from typing_extensions import Required, TypedDict


class ClientInfo(TypedDict):
    CLIENT_ID: Required[str]
    CLIENT_KEY: Required[str]


class GetBoardBody(TypedDict):
    ID: str
    PAGE: int


class BoardRequestBody(BaseModel):
    common: ClientInfo
    data: GetBoardBody

    @classmethod
    def create_board_request_body(
        cls, client_info: ClientInfo, data: GetBoardBody
    ) -> BoardRequestBody:
        return cls(common=client_info, data=data)
