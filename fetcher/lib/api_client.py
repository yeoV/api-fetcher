import json
import logging
import requests
from typing import Dict, Any

from requests.exceptions import RequestException, ConnectionError

logger = logging.getLogger(__name__)


def get_data(url: str, headers: Dict[str, Any] = None):
    _headers = {"Content-Type": "application/json"} if headers is None else headers
    try:
        response = requests.get(url=url, headers=_headers, timeout=20)
        response.raise_for_status()
        return response.json()
    except (RequestException, ConnectionError) as e:
        logger.error("GET Request Error. %s", e)
        raise e


def post_data(url: str, headers: Dict[str, Any] = None, data: json = None):
    _headers = {"Content-Type": "application/json"} if headers is None else headers
    if data is None:
        raise EmptyBodyException("RequestBody data is empty")
    try:
        response = requests.post(url=url, data=data, headers=_headers)
        response.raise_for_status()
        return response.json()
    except (RequestException, ConnectionError) as e:
        logger.error("POST Request Error. %s", e)
        raise e


class EmptyBodyException(Exception):
    def __init__(self, *args):
        super().__init__(*args)
