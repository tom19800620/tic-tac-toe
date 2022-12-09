from __future__ import annotations
import enum
# https://realpython.com/tic-tac-toe-ai-python/
#
# https://realpython.com/tutorials/projects/

class Mark(str,enum.Enum):
    CROSS = "X"
    NAUGHT = "O"

    @property
    def other(self) -> "Mark":
        return Mark.CROSS if self is Mark.NAUGHT else Mark.NAUGHT
