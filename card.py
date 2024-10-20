class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.card_faceup=False

    def flip(self):
        if self.card_faceup:
            self.card_faceup=False
        else:
            self.card_faceup=True
    def __repr__(self):
        if self.card_faceup:
            return f"{self.rank} of {self.suit}"
        else:
            return "Card face down"
    def is_red(self):
        if self.suit=='Hearts' or self.suit =='Diamonds':
            return True
        else:
            return False
    def is_black(self):
        if self.suit == 'Clubs' or self.suit =='Spades':
            return True
        else:
            return False        


    def get_rank_value(self):
        if self.rank == 'A':
            return 1
        elif self.rank == '2':
            return 2
        elif self.rank == '3':
            return 3
        elif self.rank == '4':
            return 4
        elif self.rank == '5':
            return 5
        elif self.rank == '6':
            return 6
        elif self.rank == '7':
            return 7
        elif self.rank == '8':
            return 8
        elif self.rank == '9':
            return 9
        elif self.rank == '10':
            return 10
        elif self.rank == 'J':
            return 11
        elif self.rank == 'Q':
            return 12
        elif self.rank == 'K':
            return 13
