import random
from player import Player
import numpy as np

class Dealer(Player):
    def __init__(self, hand) -> None:
        super().__init__(hand=hand)
        self.player = 'Dealer'
        
    def show_hand(self, back=True):
        return super().show_hand(back=back)
        
    def get_player_move(self,deck):
        self.update_score()
        if self.score[0] <= 17 or self.score[1] <= 17:
            return self.hit(deck)
        return self.fold()
        