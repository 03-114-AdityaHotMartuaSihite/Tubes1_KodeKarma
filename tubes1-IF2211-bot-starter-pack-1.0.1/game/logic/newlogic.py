import random
from typing import Optional, List

from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction


class GreedyDiamondLogic(BaseLogic):
    def __init__(self):
        super().__init__()
        # Pilihan arah gerak: kanan, bawah, kiri, atas
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.current_target: Optional[Position] = None
        self.active_direction_index = 0

    def _find_best_diamond(self, bot_pos: Position, diamonds: List[GameObject]) -> Optional[Position]:
        if not diamonds:
            return None

        best_ratio = float('-inf')
        best_position = None

        for diamond in diamonds:
            diamond_value = getattr(diamond.properties, "value", 1)
            dist = abs(bot_pos.x - diamond.position.x) + abs(bot_pos.y - diamond.position.y)

            if dist == 0:
                # Jangan hitung berlian yang posisinya sama dengan bot
                continue

            ratio = diamond_value / dist
            if ratio > best_ratio:
                best_ratio = ratio
                best_position = diamond.position

        return best_position

    def next_move(self, bot: GameObject, board: Board):
        props = bot.properties
        pos = bot.position

        # Tentukan target: kalau sudah dapat 4 berlian atau lebih, kembali ke base
        if props.diamonds >= 4:
            if (self.current_target is None or 
                self.current_target.x != props.base.x or 
                self.current_target.y != props.base.y):
                self.current_target = props.base
        else:
            diamond_objs = [obj for obj in board.game_objects if obj.type == "DiamondGameObject"]
            if diamond_objs:
                best_target = self._find_best_diamond(pos, diamond_objs)
                if best_target:
                    if (self.current_target is None or
                        self.current_target.x != best_target.x or
                        self.current_target.y != best_target.y):
                        self.current_target = best_target
                else:
                    self.current_target = None
            else:
                self.current_target = None

        # Reset target jika sudah sampai tujuan
        if (self.current_target and pos.x == self.current_target.x and pos.y == self.current_target.y):
            self.current_target = None

        move_x, move_y = 0, 0

        if self.current_target:
            move_x, move_y = get_direction(pos.x, pos.y, self.current_target.x, self.current_target.y)
        else:
            # Kalau tidak ada target, pilih arah gerak secara acak dengan probabilitas tertentu
            rand_val = random.random()
            if rand_val < 0.25:
                self.active_direction_index = random.randrange(len(self.directions))
            elif rand_val < 0.85:
                # Kadang-kadang ubah arah secara sedikit bergantian
                if random.random() < 0.3:
                    shift = random.choice([-1, 1])
                    self.active_direction_index = (self.active_direction_index + shift) % len(self.directions)

            chosen_direction = self.directions[self.active_direction_index]
            move_x, move_y = chosen_direction

            # Tambahan rotasi arah secara berkala
            if random.random() > 0.7:
                self.active_direction_index = (self.active_direction_index + 1) % len(self.directions)

        return move_x, move_y
