from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self._frames = []
        self._first_bonus_throw = 0
        self._second_bonus_throw = 0
    
    def add_frame(self, frame: Frame) -> None:
        if len(self._frames) > 9:
            raise BowlingError
        self._frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        if i < 0 or i >= len(self._frames):
            raise BowlingError
        return self._frames[i]

    def get_next_throw(self, i: int):
        last_frame = len(self._frames) - 1
        if i == last_frame:
            return self._first_bonus_throw
        else:
            return self.get_frame_at(i + 1).get_first_throw()

    def get_next_two_throws(self, i: int):
        last_frame = len(self._frames) - 1
        if i == last_frame:
            return self._first_bonus_throw + self._second_bonus_throw
        elif self.get_frame_at(i + 1).is_strike():
            return 10 + self.get_next_throw(i + 1)
        else:
            return self.get_frame_at(i + 1).get_first_throw() + self.get_frame_at(i + 1).get_second_throw()

    def calculate_score(self) -> int:
        score = 0
        for i, frame in enumerate(self._frames):
            if frame.is_spare():
                frame.set_bonus(self.get_next_throw(i))
            if frame.is_strike():
                frame.set_bonus(self.get_next_two_throws(i))
            score += frame.score()
        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        if bonus_throw < 0 or bonus_throw > 10:
            raise BowlingError
        self._first_bonus_throw = bonus_throw

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        if bonus_throw < 0 or bonus_throw > 10:
            raise BowlingError
        self._second_bonus_throw = bonus_throw
