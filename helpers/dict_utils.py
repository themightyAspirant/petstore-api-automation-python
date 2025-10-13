from typing import Any, Optional


def get_nested_value(data: dict, key_path: str, default: Any = None) -> Any:
    if not isinstance(data, dict):
        return default
    
    if not key_path:
        return default
    
    keys = key_path.split('.')
    current = data
    
    try:
        for key in keys:
            if not isinstance(current, dict) or key not in current:
                return default
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default


def set_nested_value(data: dict, key_path: str, value: Any) -> bool:
    if not isinstance(data, dict):
        return False
    
    if not key_path:
        return False
    
    keys = key_path.split('.')
    current = data
    
    try:
        # Navigate to the parent of the target key
        for key in keys[:-1]:
            if key not in current:
                current[key] = {}
            elif not isinstance(current[key], dict):
                return False
            current = current[key]
        
        # Set the final value
        current[keys[-1]] = value
        return True
    except (KeyError, TypeError):
        return False


def has_nested_key(data: dict, key_path: str) -> bool:
    if not isinstance(data, dict):
        return False
    
    if not key_path:
        return False
    
    keys = key_path.split('.')
    current = data
    
    try:
        for key in keys:
            if not isinstance(current, dict) or key not in current:
                return False
            current = current[key]
        return True
    except (KeyError, TypeError):
        return False


def delete_nested_key(data: dict, key_path: str) -> bool:
    if not isinstance(data, dict):
        return False
    
    if not key_path:
        return False
    
    keys = key_path.split('.')
    current = data
    
    try:
        # Navigate to the parent of the target key
        for key in keys[:-1]:
            if not isinstance(current, dict) or key not in current:
                return False
            current = current[key]
        
        # Delete the final key
        if isinstance(current, dict) and keys[-1] in current:
            del current[keys[-1]]
            return True
        return False
    except (KeyError, TypeError):
        return False
