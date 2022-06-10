from enum import Enum


class Action(Enum):
    PATROL = 1
    CHASE = 2
    RETURN = 3
    LOCKED_MOVEMENT = 4
    UNLOCKED_MOVEMENT = 5
