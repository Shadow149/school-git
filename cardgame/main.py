from deck import Deck
from player import Player
from dealer import Dealer
import time

def get_starting_deck() -> Deck:
    d = Deck()
    d.build()
    d.shuffle()
    return d

def get_player_hand(deck, hand_size):
    hand = Deck()
    for _ in range(hand_size):
        hand.put_on_top(deck.get_card_from_top())
    return hand

def show_board(player, dealer, up = False):
    print(chr(27) + "[2J")
    dealer.show_hand(not up)
    print('-'*max([player.hand.size(),dealer.hand.size()]) * 7)
    player.show_hand()


def main():
    playing = True
    while playing:
        d = get_starting_deck()
        # d.simple_show()
        
        p_h = get_player_hand(d, 2)
        p = Player(p_h)
        
        d_h = get_player_hand(d, 2)
        # p.show_hand()
        dealer = Dealer(d_h)
        
        players = [p,dealer]
        
        
        any_playing = any([player.playing for player in players])
        
        show_board(p,dealer)
        while any_playing:
            any_playing = any([player.playing for player in players])
            
            for player in players:
                if not player.playing:
                    continue
                move = player.get_player_move(d)
                player.update_score()
                time.sleep(1.5)
                show_board(p,dealer)
                if player.isBust() or move == Player.FOLD:
                    if player.isBust():
                        print(player.bust_message())
                        player.score = [999,999]
                    player.playing = False
            
            # show_board(p,dealer)
        
        show_board(p,dealer, True)
        # print((dealer.calculate_21_diff()) , (p.calculate_21_diff()))
        if min(dealer.calculate_21_diff()) < min(p.calculate_21_diff()):
            print('Dealer wins')
        elif min(dealer.calculate_21_diff()) > min(p.calculate_21_diff()):
            print('You win!')
        else:
            print('Draw!')
        
        again = input('Play again [y]? > ')
        if again not in ['y','Y']:
            playing = False


if __name__ == '__main__':
    main()