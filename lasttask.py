from kivy.core.window import Window
Window.fullscreen = False
Window.size = (1000,600)

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ListProperty
import japanize_kivy
from kivy.lang import Builder
import numpy as np
import lasttask_module




Builder.load_string('''
<TextWidget>:
    BoxLayout:
        orientation:'vertical'
        size: root.size

        BoxLayout:
            orientation:'horizontal'

            Label:
                id: label1
                font_size:100
                text: root.text1
                size_hint_x: 1.5
                color: 1,0,0,1
            Label:
                id: label2
                font_size:100
                text: root.text2
                size_hint_x: 1.5
                color: 0,1,0,1
            Label:
                id: label3
                font_size:100
                text: root.text3
                size_hint_x: 1.5
                color: 0,0,1,1

            BoxLayout:
                orientation:'vertical'
                size: root.size

                Button:
                    id: button1
                    text: "3Bet!"
                    font_size: 45
                    size_hint_y: 0.3
                    on_press: root.buttonClicked1()
                Button:
                    id: button2
                    text: "5Bet!"
                    font_size: 45
                    size_hint_y: 0.3
                    on_press: root.buttonClicked2()
                Button:
                    id: button3
                    text: "10Bet!"
                    font_size: 45
                    size_hint_y: 0.3
                    on_press: root.buttonClicked3()
                Label:
                    id: label7
                    font_size:30
                    text: root.text7
                    size_hint_y: 0.3
                    color: 1,1,1,1


        BoxLayout:
            size_hint_y: 0.5
            padding: 20,30,20,10

            Label:
                id: label5
                text_size: self.size
                text: "【説明】これはスロットゲームです。最初の持ち金は200です。それぞれ3コインBET、5コインBET、10コインBETの掛け金でスロットを回します。。コインが無くなれば終了です。×が揃えば1倍、△が揃えば2倍、○が揃えば3倍、◇が揃えば10倍、☆が揃えば20倍の掛け金が戻ってきます。"
                color: 1,1,1,1
                halign: 'left'
                valign: 'middle'
            Label:
                id: label6
                font_size:30
                text: root.text6
                color: 1,1,1,1
            Label:
                id: label4
                font_size: 50
                text: root.text4
                color: root.color




''')


class TextWidget(Widget):
    text1 = StringProperty()
    text2 = StringProperty()
    text3 = StringProperty()
    text4 = StringProperty()
    text6 = StringProperty()
    text7 = StringProperty()
    color = ListProperty([1,1,1,1])

    coin = 200
    counta = 0
    bet3 = 3
    bet5 = 5
    bet10 = 10

    def __init__(self, **kwargs):
        super(TextWidget,self).__init__(**kwargs)
        self.text1 = '1'
        self.text2 = '2'
        self.text3 = '3'
        self.text6 = '持ち金' + str(self.coin) + 'coin'
        self.text7 = '現在' + str(self.counta) + '回目'

    def buttonClicked1(self):
        lasttask_module.Slot.bet(self,self.bet3)
        self.text6 = '持ち金' + str(self.coin) + 'coin'
        lasttask_module.Slot.check(self)
    def buttonClicked2(self):
        lasttask_module.Slot.bet(self,self.bet5)
        self.text6 = '持ち金' + str(self.coin) + 'coin'
        lasttask_module.Slot.check(self)
    def buttonClicked3(self):
        lasttask_module.Slot.bet(self,self.bet10)
        self.text6 = '持ち金' + str(self.coin) + 'coin'
        lasttask_module.Slot.check(self)


class TestApp(App):
    def build(self):
        self.title = 'スロットゲーム'
        return TextWidget()



TestApp().run()
