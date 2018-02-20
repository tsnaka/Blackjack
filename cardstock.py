import random

class CardStock:
    """カードの山"""
    def __init__(self):
        self._current = 0
        self._deck = []
        for suit in ["Heart", "Spade", "Club", "Diamond"]:
            for number in range(1,14):
                self._deck.append([suit, number])
    
    def draw(self):
        """カードの山から１枚引く"""
        if self._current < len(self._deck):
            result = self._deck[self._current]
            self._current += 1
        return result
    
    def cut(self):
        """カードを切る"""
        self._current = 0
        random.shuffle(self._deck)
        return (self)
    
    def myprint(self):
        print(self._deck)
        
    
#Test Program
#stock = CardStock().cut()
#stock.myprint()
  
