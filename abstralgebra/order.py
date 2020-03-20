from .Element import Element
from .Group import Group

def O(value):
    if isinstance(value, Group):
        return len(value)
    
    order = 1
    current_value = value
    while (current_value != value.group.eye):
        current_value *= value
        order += 1
    return order
