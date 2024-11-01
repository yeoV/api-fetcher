from typing import Any, Dict


def flatten_dict(d: dict) -> Dict[str, Any]:
    flatten = []
    for k, v in d.items():
        if isinstance(v, dict):
            flatten.extend(flatten_dict(v).items())
        else:
            flatten.append((k, v))
    return dict(flatten)
