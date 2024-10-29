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

    def calculate_score(self) -> int:
        last_frame = len(self._frames) - 1
        score = 0
        for i, frame in enumerate(self._frames):
            if frame.is_spare():
                if i == last_frame:
                    frame.set_bonus(self._first_bonus_throw)
                else:
                    frame.set_bonus(self.get_frame_at(i + 1).get_first_throw())

            score += frame.score()
        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
