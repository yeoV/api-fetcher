import logging
import requests

from typing import Any, Dict
from requests.exceptions import ConnectionError, RequestException

logger = logging.getLogger(__name__)


def get_data(url: str, headers: Dict[str, Any] = None, verify=True):
    _headers = {"Content-Type": "application/json"} if headers is None else headers
    try:
        response = requests.get(url=url, headers=_headers, timeout=20, verify=verify)
        response.raise_for_status()
        return response.json()
    except (RequestException, ConnectionError) as e:
        logger.error("GET Request Error. %s", e)
        raise e


def post_data(url: str, headers: Dict[str, Any] = None, data=None, verify=True):
    _headers = {"Content-Type": "application/json"} if headers is None else headers
    if not data:
        raise EmptyBodyException("RequestBody data is empty")
    try:
        response = requests.post(
            url=url, data=data, headers=_headers, timeout=20, verify=verify
        )
        response.raise_for_status()
        return response.json()
    except (RequestException, ConnectionError) as e:
        logger.error("POST request error. %s", e)
        raise e
    except AttributeError as e:
        logger.error("invaild header's 'key' data type. %s", e)
        raise e


class EmptyBodyException(Exception):
    def __init__(self, *args):
        super().__init__(*args)
