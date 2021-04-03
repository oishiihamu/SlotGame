import numpy as np



class Slot:

    def bet(self,bet):
        lst = ['○','○','△','△','×','×','×','☆','◇']
        a = np.random.choice(lst)
        b = np.random.choice(lst)
        c = np.random.choice(lst)

        self.ids.label1.text = a
        self.ids.label2.text = b
        self.ids.label3.text = c

        if a == "○" and b == "○" and c == "○":
            self.ids.label4.text = 'あたり！'
            self.counta += 1
            self.text7 = '現在' + str(self.counta) + '回目'
            self.color = 1,1,0,1
            self.coin -= bet
            self.coin += bet * 3
            return self.coin
        elif a == "△" and b == "△" and c == "△":
            self.ids.label4.text = 'あたり！'
            self.counta += 1
            self.text7 = '現在' + str(self.counta) + '回目'
            self.color = 1,1,0,1
            self.coin -= bet
            self.coin += bet * 2
            return self.coin
        elif a == "×" and b == "×" and c == "×":
            self.ids.label4.text = 'あたり！'
            self.counta += 1
            self.text7 = '現在' + str(self.counta) + '回目'
            self.color = 1,1,0,1
            self.coin -= bet
            self.coin += bet * 1
            return self.coin
        if a == "☆" and b == "☆" and c == "☆":
            self.ids.label4.text = 'あたり！'
            self.counta += 1
            self.text7 = '現在' + str(self.counta) + '回目'
            self.color = 1,1,0,1
            self.coin -= bet
            self.coin += bet * 20
            return self.coin
        elif a == "◇" and b == "◇" and c == "◇":
            self.ids.label4.text = 'あたり！'
            self.counta += 1
            self.text7 = '現在' + str(self.counta) + '回目'
            self.color = 1,1,0,1
            self.coin -= bet
            self.coin += bet * 10
            return self.coin
        else:
            self.ids.label4.text = 'はずれ！'
            self.counta += 1
            self.text7 = '現在' + str(self.counta) + '回目'
            self.color = 1,0,1,1
            self.coin -= bet
            return self.coin


    def check(self):
        if self.coin <= 0:
            self.ids.button1.disabled = True
            self.ids.button2.disabled = True
            self.ids.button3.disabled = True
            self.text4 = '終了！'
