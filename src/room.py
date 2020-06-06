# Implement a class to hold room information. This should have name and
# description attributes.
from dataclasses import dataclass, field
from typing import Optional, List
from item import Item

@dataclass
class Room:
    name: str
    description: str
    n_to: Optional[str] = None
    s_to: Optional[str] = None
    e_to: Optional[str] = None
    w_to: Optional[str] = None
    items: List[Item] = field(default_factory=list)
