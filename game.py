# -*- coding: utf-8 -*-
from cardstock import CardStock
from hand import Hand

MAX_DRAW_NUMBER = 16

def game():
    """
    ゲームをコントロールする関数
    戻り値　True: 勝ち　False: ドローまたは負け
    """
    playerHand = Hand()
    dealerHand = Hand()
    
    # 山札の準備
    stock = CardStock()
    stock.cut()
    
    # 最初の2枚とその表示
    playerHand.draw(stock).draw(stock).myprint("Player's hand: ")
    dealerHand.draw(stock).draw(stock).myprint("Dealer's hand: ")
    
    # PlayerのHit/Stand
    while True:
        if input('もう1枚カードを引く？[y/n]: ') == "y":
            playerHand.draw(stock).myprint("Player's hand: ")
            print ("合計: ", playerHand.sum());
            if playerHand.isBurst() == True:
                print ("Burst! Game over")
                return False
        else:
            break
    
    # DealerのHit/Stand
    while dealerHand.sum() < MAX_DRAW_NUMBER:
        dealerHand.draw(stock).myprint("Dealer's hand: ")
    
    # 勝敗の決定
    if dealerHand.isBurst() == True or dealerHand.sum() < playerHand.sum():
        print ("あなたの勝ちです")
        return True
    elif dealerHand.sum() == playerHand.sum():
        print("引き分けです")
        return False
    else:
        print("あなたの負けです")
        return False

game()
