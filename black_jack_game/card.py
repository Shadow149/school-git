class Card:
    SPADES = "S"
    CLUBS = "C"
    DIAMONDS = "D"
    HEARTS = 'H'
    
    SUITS = [SPADES,CLUBS,DIAMONDS,HEARTS]
    
    SUITS_UNI = {SPADES: '♠',
                 CLUBS: '♣',
                 DIAMONDS: '♦',
                 HEARTS: '♥'}

    VALUES_TO_TRUE = {1: 'A',
                      11: 'J',
                      12: 'Q',
                      13: 'K'}
    
    def __init__(self, val, s):
        self.value = val
        self.suit = s
        
  
    def get_true_value(self):
        return self.value if self.value not in Card.VALUES_TO_TRUE else Card.VALUES_TO_TRUE[self.value] 
    
    def __repr__(self) -> str:
        return f'{self.get_true_value()}{Card.SUITS_UNI[self.suit]}'
    
    def show_back(self):
        return f""" _____
|\ ~ /|
|}}}}:{{{{|
|}}}}:{{{{|
|}}}}:{{{{|
|/_~_\|"""
    
    def render(self):
        if self.value == 1:
            if self.suit == Card.SPADES:
                return f""" _____ 
|A .  |
| /.\ |
|(_._)|
|  |  |
|____V|"""
            if self.suit == Card.DIAMONDS:
                return f""" _____ 
|A ^  |
| / \ |
| \ / |
|  .  |
|____V|"""
            if self.suit == Card.CLUBS:
                return f""" _____ 
|A _  |
| ( ) |
|(_'_)|
|  |  |
|____V|"""
            if self.suit == Card.HEARTS:
                return f""" _____ 
|A_ _ |
|( v )|
| \ / |
|  .  |
|____V|"""
        if self.value == 2:
            return f""" _____ 
|2    |
|  {Card.SUITS_UNI[self.suit]}  |
|     |
|  {Card.SUITS_UNI[self.suit]}  |
|____Z|"""
        
        if self.value == 3:
            return f""" _____ 
|2    |
| {Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]} |
|     |
|  {Card.SUITS_UNI[self.suit]}  |
|____Z|"""
        
        if self.value == 4:
            return f""" _____ 
|4    |
| {Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]} |
|     |
| {Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]} |
|____h|"""
        
        if self.value == 5:
            return f""" _____ 
|5    |
| {Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]} |
|  {Card.SUITS_UNI[self.suit]}  |
| {Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]} |
|____S|"""
        
        if self.value == 6:
            return f""" _____ 
|6    |
| {Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]} |
| {Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]} |
| {Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]} |
|____9|"""
        
        if self.value == 7:
            return f""" _____ 
|7    |
| {Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]} |
|{Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]}|
| {Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]} |
|____L|"""
        
        if self.value == 8:
            return f""" _____ 
|8    |
|{Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]}|
| {Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]} |
|{Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]}|
|____8|"""
        if self.value == 9:
            return f""" _____ 
|9    |
|{Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]}|
|{Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]}|
|{Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]}|
|____6|"""
        if self.value == 10:
            return f""" _____ 
|10 {Card.SUITS_UNI[self.suit]} |
|{Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]}|
|{Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]}|
|{Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]}|
|___0I|"""
        if self.value == 11:
            return f""" _____ 
|J  ww|
| {Card.SUITS_UNI[self.suit]} {{)|
|{Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]}% |
| | % |
|__%%[|"""
        if self.value == 12:
            return f""" _____ 
|Q  ww|
| {Card.SUITS_UNI[self.suit]} {{(|
|{Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]}%%|
| |%%%|
|_%%%O|"""
        if self.value == 13:
            return f""" _____ 
|K  ww|
| {Card.SUITS_UNI[self.suit]} {{)|
|{Card.SUITS_UNI[self.suit]} {Card.SUITS_UNI[self.suit]}%%|
| |%%%|
|_%%%>|"""
        