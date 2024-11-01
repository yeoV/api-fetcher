from typing import Any, Dict, TypeVar

T = TypeVar("T")


class RequestBody:
    """
    API 요청의 바디 정보를 생성하는 추상화 class

    Attributes:
        request_body (T): API 요청 Body 정보를 담는 변수
    """

    def __init__(self, request_body: T = None):
        if request_body is None or not isinstance(request_body, object):
            raise TypeError("request_body is not None or must be object.")
        self.request_body = request_body

    def create_request_body(self, *args) -> Dict[str, Any]:
        # params 순서가 중요
        return self.request_body.create_request_body(*args).dict()
