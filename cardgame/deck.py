from card import Card
import random

class Deck:    
    def __init__(self) -> None:
        self.cards = []
        
    def build(self):
        self.cards = []
        for suit in Card.SUITS:
            for value in range(1, 14):
                self.cards.append(Card(value,suit))
                
    def shuffle(self):
        random.shuffle(self.cards)
        
    def get_card_from_top(self):
        return self.cards.pop()

    def put_on_top(self, card):
        self.cards.append(card)
                
    def show(self, back=False):
        if not back:
            print(*[''.join(x) for x in zip(*[[x.ljust(len(max(s.render().split('\n'), key=len))) for x in s.render().split('\n')] for s in self.cards])], sep='\n')
        else:
            print(*[''.join(x) for x in zip(*[[x.ljust(len(max(s.show_back().split('\n'), key=len))) for x in s.show_back().split('\n')] for s in self.cards])], sep='\n') 
        print('')
    
    def simple_show(self):
        for card in self.cards:
            print(card)
        
    def calculate_value(self):
        min_value = 0
        max_value = 0
        value = 0
        for card in self.cards:
            if card.value == 1:
                min_value += 1
                max_value += 11
            elif card.value > 10:
                value += 10
            else:
                value += card.value
        min_value += value
        max_value += value
        return min_value,max_value

    def is_bust(self):
        values = self.calculate_value()
        return min(values) > 21
    
    def size(self):
        return len(self.cards)