from cardstock import CardStock

MAX_HAND_SUM = 21

class Hand:
    def __init__(self):
        self._hand = []
    
    def draw(self, cardstock):
        """山札から１枚引き手札に加える"""
        self._hand.append(cardstock.draw())
        return (self)
    
    def myprint(self, title=""):
        """手札を簡易形式で出力する"""
        display = title #　表示のタイトル
        
        for suit, number in self._hand:
            # 数字を絵札記号に変換
            if number == 1:
                snum = 'A'
            elif number > 10:
                coat = ['J','Q','K']
                snum = coat[number-11]
            else:
                snum = str(number)
            # [S-J]形式で文字列に追加
            display += '[' + suit[0:1] + '-' + snum + ']'
        print(display)

    def sum(self):
        """手札の合計を出す"""
        hand_sum = 0
        nace = 0
        for suit, number in self._hand:
            if number == 1:
                nace += 1
                hand_sum += 11 
            elif number > 10:
                hand_sum += 10
            else:
                hand_sum += number
        while nace > 0:
            if hand_sum > MAX_HAND_SUM:
                hand_sum -= 10
                nace -= 1
            else:
                break
        return hand_sum
    
    def isBurst(self):
        """バーストの判定"""
        return self.sum() > MAX_HAND_SUM

# Test Program
#stock = CardStock()
#stock.cut()
#hand = Hand()
#hand.draw(stock).draw(stock).draw(stock)
#hand.myprint()
#print(hand.sum(), hand.isBurst())

                    
    
