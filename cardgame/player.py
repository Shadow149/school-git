from deck import Deck
class Player:
    
    FOLD = 'f'
    HIT = 'h'
    
    def __init__(self, hand = Deck()) -> None:
        self.hand = hand
        self.playing = True
        self.score = [0,0]
        self.player = 'Player'
        
    def show_hand(self, back=False):
        self.hand.show(back)
    
    def get_player_move(self,deck):
        move = input("Hit [h] or fold [f] > ")
        if move in [Player.HIT,'H']:
            self.hit(deck)
            # value = player.hand.calculate_value()
            return Player.HIT
        return Player.FOLD
    
    def hit(self, deck):
        self.hand.put_on_top(deck.get_card_from_top())
        print(f'{self.player}: Hit!')
        return Player.HIT

    def fold(self):
        print(f'{self.player}: I Fold!')
        return Player.FOLD
        
    def isBust(self):
        return self.hand.is_bust()

    def bust_message(self):
        return f'{self.player} went bust!'
    
    def update_score(self):
        self.score = self.hand.calculate_value()
    
    def calculate_21_diff(self):
        # print([x for x in self.score])
        return [abs(21 - x) for x in self.score]