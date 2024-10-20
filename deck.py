import random
from card import Card
class Deck:
    
    def __init__(self):
        self.rank=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.suit=['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards=[]
        for suits in self.suit:
            for ranks in self.rank:
                self.cards.append(Card(suits,ranks))
        random.shuffle(self.cards)
    
    def shuffle(self):
        random.shuffle(self.cards)
    def take_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None
    def canplaceon_tableau(self,card_toplace,target_place):
        if target_place is None: #if there is no card before 
            return False
        if(card_toplace.is_red() != target_place.is_red() and card_toplace.get_rank_value() == target_place.get_rank_value() -1):
            return True
        else:
            return False
        
    def canplaceon_foundation(self,card_toplace,target_place):
        if target_place is None:
            return card_toplace .rank == 'A'
        topcard=target_place[-1]
        if (card_toplace.suit == topcard.suit and card_toplace.get_rank_value() == topcard.get_rank_value()+1):
            return True
        else:
            return False