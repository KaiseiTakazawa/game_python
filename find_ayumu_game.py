#main4の方が新しい
from random import randint, sample

#オープニング無しにしてる

def main():
    #Opening()
    #ここにプレイヤークラスを入れて実行する
    Floor()
    #Floor__init__の中に、Player ()が入っている
    #floor = Floor()

class Opening:
#仮で作った、あとでガチで作ること
    #ここでplaye_nameをクラス変数にして、OPNEINGがインスタンス化するたびに、リセットするようにすればいいんじゃね？？？
    def __init__(self):
        player_name = input('あなたの名前を教えてください。もう準備はすぐです：')
        opening = [
        f'ようこそ、{player_name}、さあ、あゆむを探す旅に出ましょう',
        'あなたはハウスマスターから、あゆむを探すことを任されました',
        'あなたはこれからWISH6Fにある25の部屋からあゆむを見つけることになりました',
        'あゆむは25室の部屋のどこかに潜んでいます。彼はあなたが彼を見つけることを待っています',
        'あなたは、あゆむに会うまでに、さまざまな困難にぶつかるでしょう',
        'そして、あなたは、さまざまな人との友情を築くでしょう',
        '最後に、必要なものは、情熱と忍耐です。早速、あゆむを探しにいきましょうか'
    ]

        for i in opening:
            input(i)

class Player:
    money = 0
    items = []
    weapon = []
    friends = []
    heart = 1
    #プレイヤーは1回しぬとデータが飛ぶ,Player.heartで条件管理すべき

    def __init__(self):
        Player.money = 0
        Player.items = []
        Player.weapon = []
        Player.friends = []
        Player.heart = 1
        #self.show_data()  これはなくていい
        #これはなくてもいいかもしれないけど
        
    """
    def reset(self):
    
    #これをセットすることを忘れちゃだめ！！！ゲームの最後に
    #問題はこれをどうやって呼び出すか、、、
        if Player.heart == 0:
            
    """
    #表記がこれであってるかわからない 
    @classmethod
    def show_data(cls):
    #こいつをクラスメソッドにしてしまおう
        print('')
        line = ''
        for _ in range(85):
            line += '-'
        print(line)
        print('●所持品')
        print('　　持っているお金　:',Player.money)

        """エラーの原因なってる

        string1 = ''
        #items_string
        for i in Player.items:
            string1 += Player.items[i]

        string2 = ''
        #items_string
        for i in Player.weapon:
            string2 += Player.weapon[i]

        string3 = ''
        #items_string
        for i in Player.friends:
            string3 += Player.friends[i]

        """

        
        print('持っているアイテム　:',Player.items)
        print('　　　　　　　武器　:',Player.weapon)
        print('　　　　　　　仲間　:',Player.friends)
        print('　　　　　残りの命　:',Player.heart)
        print(line)

class Battle:
    def __init__(self):
        print('\n~バトルイベント~\n')
        print('寮生とのバトル発生')
        input('enterを押して、寮生を倒せ')
        #下に簡単にバトルイベントを作る
        while True:
            if 'バット' in Player.weapon:     #'バット','包丁'
            #違う条件を考えよう
                Player.weapon.remove(' バット ')         
                input('enterを押して、バットを装備しよう、一撃で決めよう')

                y = randint(1,2)
                if y == 1:
                    print('戦いに勝利した\n')
                    m = randint(0,2500)
                    Player.money += m
                    print(f'{m}円ゲットした')
                    break
                
                if y == 2:
                    print('やり損ねた')
                    input('まだ相手はダウンしてない。もう一度enterで殴れ!')  
            
            x = randint(1,3)
            if x == 1:
                input('まだ相手はダウンしてない。もう一度enterで殴れ!')
            if x == 2:
                print('戦いに勝利した\n')
                m = randint(0,2500)
                Player.money += m
                print(f'{m}円ゲットした')
                break
            if x == 3:
                if Player.heart > 1:
                    Player.heart -= 1
                    print('寮生のパンチで死にかけた')
                    print('1の命が減少')
                    input('寮生の命のおかげでかろうじて助かった,enterでもう一撃')
                    continue
                print('君は殺された\n')
                Floor.win_lose = False
                break

        
class Friends:
    def __init__(self):
        print('\n~仲間イベント~\n')
        print('\n友達ゲット\n')


"""
class ItemTotal:
    def __init__(self):
        x = randint(1,10)
        if x <= 2:
            Money()

        elif x <= 4:
            Weapon()

        elif x <= 6:
            Alcohol()

        elif x <= 8:
            Drug()

        else:
            Heart()
"""


"""        
        print('\nアイテムイベント発生\n')
        input('enterを押して、アイテムを確認')
        
        #これがあると説明が重複するかも
        
        self.event()

    def event(self):
        
"""     
        

class Money:
    def __init__(self):
        print('\n~アイテムイベント~\n')
        input('enterを押して、アイテムを確認')
        money_event_list = [self.good, self.normal, self.bad]
        x = randint(0,2)
        money_event = money_event_list[x]
        money_event()
        """
        if x == 0:
            self.good()
        if x == 1:
            self.noraml()
        if x == 2:
            self.bad()
        """
        
    def good(self):
        money = randint(1000,1500)
        Player.money += money
        print(f'あなたは{money}円ゲットした')

    def normal(self):
        money = randint(500,1000)
        Player.money += money
        print(f'あなたは{money}円ゲットした')

    def bad(self):
        money = randint(0,500)
        Player.money += money
        print(f'あなたは{money}円ゲットした')

class Weapon:
    def __init__(self):
        print('\n~アイテムイベント~\n')
        input('enterを押して、アイテムを確認')
        weapon_event_list = [self.bat,self.bat,self.bat,self.bat, self.houtyou]
        x = randint(0,4)
        weapon_event = weapon_event_list[x]
        weapon_event()       
    
    def bat(self):
        print('あなたはバットを手に入れた')
        print('これを使えば、寮生を倒しやすそうだ')
        Player.weapon.append(' バット ')  

    def houtyou(self):
        print('あなたは包丁を手に入れた')
        print('これを使えば、簡単に寮生を倒しやすそうだ')
        Player.weapon.append(' 包丁 ')

class Alcohol:
    def __init__(self):
        print('\n~アイテムイベント~\n')
        input('enterを押して、アイテムを確認')
        alcohol_event_list = [self.beer,self.beer,self.beer,self.emptybeer]
        x = randint(0,3)
        alcohol_event = alcohol_event_list[x]
        alcohol_event()       
    
    def beer(self):
        print('あなたはビールを手に入れた')
        print('これをある人に見られると、、、')
        #お金没収か、バトル、退寮（負け確定）
        Player.items.append(' ビール ')

    def emptybeer(self):
        print('あなたはあゆむがのんだビールを手に入れた')
        print('この瓶を持ってあの人に渡せば、、、')
        Player.items.append(' あゆむのビール空びん ')

class Heart:
    def __init__(self):
        print('\n~アイテムイベント~\n')
        self.get_heart()

    def get_heart(self):
        input('ここに寮生の命が落ちていた、enterで盗む')
        x = randint(0,1)
        if x == 0:
            print('寮生の心を盗んだ、残りの命が一つ増えた')
            Player.heart += 1
        else:
            print('寮生の心を盗むことに失敗した')



class Drug:
#このイベントが発生したら、フロアデータをリセットするから、
    def __init__(self):
        print('\n~アイテムイベント~\n')
        input('enterを押して、アイテムを確認')
        while True:
            yes_no = input('ハッシシが落ちていた、使うか、使わないか選べ、yes or noを入力')          
            if yes_no == 'no':
                print('あなたは使わなかった')
                break
            elif yes_no == 'yes':
                input('あたまがくらくらしてきた、enterでもう一息')
                x =0
                #x = randint(0,1)
                if x == 0:
                    #天才だ！！！全て部屋のイベントが終わったあとにはっししイベントが発生するようにすれば良いのだ！！！
                    Floor.hassisi = True
                    input('「.......」(enterで次へ）')
                    print('特にこれ以上なさそうだ')

                    """
                    input('...')
                    print('記憶がない')
                    print('ハッシシがうまく効いたようだ、あゆむのいる場所が大体わかる')
                    """
                    """
                    self.floor[select_room_num].generate_ev()を強制終了させるように仕込まないといけない...
                    """
                    break

                else:
                    print('あなたは死んだ')

                    Floor.win_lose = False
                    #これでループが終わる、event.nt
                    Player.heart = 0
                    break

            else:
                print('エラー、yes or no　でもう一度入力してください')


class Ayumu:
    def __init__(self):
        print('\n~あゆむイベント~\n')
        print('あゆむに遭遇')
        input('enterを押してあゆむに話かけよう')
        
        x = randint(1,10)

        if '　あゆむ　' in Player.friends:
            input('enterを押して、あゆむを紹介しよう')
            print('あゆむ「！！！」')
            print('あゆむは驚いて身動きを取れていない')
            #ゲームクリアの条件変数を作ろう

        elif x <= 3 :
            print('あゆむは殴ってきた')
            input('あゆむを倒せ、enterで殴ろう')
            while True:
                if '包丁' in Player.weapon:
                #包丁を持っているとき
                    Player.weapon.remove(' 包丁 ')
                    input('enterを押して、包丁を装備して、あゆむを倒そう、チャンスは一度だけ')
                    z = randint(1,5)
                    if z == 1:
                        print('君は殺された\n')
                        Floor.win_lose = False
                        break

                    elif z == 2 or z == 3:
                        print('あゆむに勝利した\n')
                        Floor.win_lose = True
                        break

                    elif z == 4:
                        input('まだ相手はダウンしてない。包丁がないから、enterで殴れ!')

                    else:
                        print('あゆむは逃げ出した')
                        print('あゆむは他の部屋にいる。もう一度探しに行こう\n')
                        Floor.escape = True
                        break

                y = randint(1,10)
                if y >= 6:
                    input('まだ相手はダウンしてない。もう一度enterで殴れ!')

                if y == 5:
                    print('あゆむは逃げ出した')
                    print('あゆむは他の部屋にいる。もう一度探しに行こう\n')
                    Floor.escape = True
                    break

                if y <= 2:
                    print('あゆむに勝利した\n')
                    Floor.win_lose = True
                    break

                if 3 <= y <= 4:
                    if Player.heart > 1:
                        Player.heart -= 1
                        print('1の命が減少')
                        input('寮生の命のおかげでかろうじて助かった,enterでもう一撃')
                        continue
                    print('君は殺された\n')
                    Floor.win_lose = False
                    break

        elif 9 >= x >= 4 :
            print('あゆむは逃げ出した')
            print('あゆむは他の部屋にいる。もう一度探しに行こう\n')
            Floor.escape = True

        elif x == 10 :
            print('あゆむは寝ている')
            input('enterを押してあゆむを捕まえよう')
            y = randint(1,2)
            if y == 1:
                print('あゆむを捕まえた\n')
                print('あゆむが仲間に加わった')
                print('...あゆむは寝ている')
                print('あゆむが起きるまで待とう')
                
                #隠しイベントあゆむがあゆむの居場所を教える
                Player.friends.append('　あゆむ　')
                #あゆむを仲間に入れてもいいかもね、、、笑、ゲームは続く的な、、、わろた。。。あゆむ遭遇イベントとかおもろい
                Floor.win_lose = True
            if y == 2:
                print('あゆむは逃げ出した')
                print('あゆむは他の部屋にいる。もう一度探しに行こう\n')
                Floor.escape = True
            
class AyumuStrong(Ayumu):
    def __init__(self):
        print('\n~あゆむイベント~\n')
        print('あゆむに遭遇')
        input('あゆむが一人佇んでいる。enterで話しかけよう')
        input('あゆむ「....]')
        input('あゆむ「一騎討ちや！」')
        input('あゆむはいつもよりつよそうだ')        
        input('あゆむを倒せ、enterで殴ろう')
        while True:
            x = randint(1,10)
            if x <= 8 :
                if Player.heart > 1:
                    Player.heart -= 1
                    print('1の命が減少')
                    input('寮生の命のおかげでかろうじて助かった,enterでもう一撃')
                    continue
                
                print('あゆむからの痛恨の一撃、君は殺された')
                Floor.win_lose = False
                break
            else:
                if x >= 9:
                    print('あゆむは弱ってきている。あと一息')
                    x =randint(1,2,3)
                    if x == 1:
                        print('あゆむに勝った')
                        Floor.win_lose = True
                        break
                    if x == 2:
                        if Player.heart > 1:
                            Player.heart -= 1
                            print('1の命が減少')
                            input('寮生の命のおかげでかろうじて助かった,enterでもう一撃')
                            continue
                        print('君は殺された\n')
                        Floor.win_lose = False
                        break                

                    if x == 3:
                        print('あゆむは命かながら、逃げ出した')
                        print('あゆむは他の部屋にいる。もう一度探しに行こう\n')
                        Floor.escape = True
                             
        """
        if 9 >= x > 5 :
            print('あゆむは逃げ出した')
            print('あゆむは他の部屋にいる。もう一度探しに行こう\n')
            Floor.escape = True

        if x == 10 :
            print('あゆむは寝ている')
            input('enterを押してあゆむを捕まえよう')
            print('あゆむを捕まえた\n')
            Floor.win_lose = True
        """
            

class Room:
    #ここに部屋の状態に関する変数をリストとして設定して、ランダムに決定させるのがいいかも！
    def __init__(self,room_num):
        self.room_num = room_num
        self.room_name = f'□room{self.room_num+600}    '
        self.empty = False

    #def __repr__(self):
        #return f'room{self.room_num}'
        
    def generate_ev(self):
        print('ルームイベント開始')
        for i in range(4):
            print(f'\n◆ルームイベント{i+1}') 
            x = randint(1,3)
            #イベントが始まる
            if x == 1:
                Battle()
            if x == 2:
                #一旦仲間イベント消した
                y = randint(1,10)
                if y <= 2:
                    Money()
                elif 3 <= y <= 4:
                    Weapon()
                elif 5 <= y <= 6:
                    Heart()
                elif 7 <= y <= 8:
                    Alcohol()
                elif 10 >= y > 9:
                    Drug()
                
                #Friends()
            if x == 3 :
            #ランダムにアイテムイベントを発生させる
                y = randint(1,10)
                if y <= 2:
                    Money()
                elif 3 <= y <= 4:
                    Weapon()
                elif 5 <= y <= 6:
                    Heart()
                elif 7 <= y <= 8:
                    Alcohol()
                elif 10 >= y > 9:
                    Drug()
            if Floor.win_lose == False :
            #イベントで負けると、Falseにして、イベントがストップするようにした
                break

        else:
            print('ルームイベント終了')

class RoomAyumu(Room):
    def __init__(self,room_num):
        self.room_num = room_num
        self.room_name = f'□room{self.room_num+600}    ' #▲であゆむがいることがわかる、デモ用
        self.empty = False

    def generate_ev(self):
        print('ルームイベント開始')
        self.ayumu_num = randint(0,3)
        #ayumuが呼び出される順番を決定するための変数

        for i in range(4):
            print(f'\n◆ルームイベント{i+1}') 
            if self.ayumu_num == i:
                Ayumu()
                break
            else:
                x = randint(1,3)
                if x == 1:
                    Battle()
                if x == 2:
                    y = randint(1,10)
                    if y <= 2:
                        Money()
                    elif 3 <= y <= 4:
                        Weapon()
                    elif 5 <= y <= 6:
                        Heart()
                    elif 7 <= y <= 8:
                        Alcohol()
                    elif 10 >= y > 9:
                        Drug()
                    #Friends()
                if x == 3:
                    y = randint(1,10)
                    if y <= 2:
                        Money()
                    elif 3 <= y <= 4:
                        Weapon()
                    elif 5 <= y <= 6:
                        Heart()
                    elif 7 <= y <= 8:
                        Alcohol()
                    elif 10 >= y > 9:
                        Drug()

                
                    
                if Floor.win_lose == False :
                #イベントで負けると、Falseにして、イベントがストップするようにした
                    break
                

    #def __repr__(self):
        #return f'room{self.room_num}'
        #return f'room{self.room_num}(あゆむがいる)'

class RoomEmpty(Room):
    def __init__(self,room_num):
        self.room_num = room_num
        self.room_name = f'■room{self.room_num+600}    '
        self.empty = True
    
    def generate_ev(self):
        print('ルームイベント開始\n\nこの部屋はすでにきた部屋だ\n')
        print('ルームイベント終了')



        # def generate_ev(self):
        #print('ルームイベント開始\n\nこの部屋はすでにきた部屋だ\n')
           
        #

    #def __repr__(self):
        #return f'room{self.room_num}（空）'

    #特殊イベント用のメソッドを作る。特殊イベントは空部屋に発生するようにする

    

class RoomAyumuEmpty(RoomAyumu):
    def __init__(self,room_num):
        self.room_num = room_num
        self.room_name = f'■room{self.room_num+600}    '#▲であゆむがいることをわかりやすく、デモ用
        self.empty = True
    
    def generate_ev(self):
        print('ルームイベント開始')
        AyumuStrong()

#Hatena系全てを下に書く

class RoomHatena(Room):
    def __init__(self,room_num):
        self.room_num = room_num
        self.room_name = f'❔room{self.room_num+600}    '
        self.empty = False

class RoomAyumuHatena(RoomAyumu):
    def __init__(self,room_num):
        self.room_num = room_num
        self.room_name = f'❔room{self.room_num+600}    ' #▲であゆむがいることがわかる、デモ用
        self.empty = False

class RoomEmptyHatena(RoomEmpty):
    def __init__(self,room_num):
        self.room_num = room_num
        self.room_name = f'❔■room{self.room_num+600}   '
        self.empty = True

class RoomAyumuEmptyHatena(RoomAyumuEmpty):
    def __init__(self,room_num):
        self.room_num = room_num
        self.room_name = f'❔■room{self.room_num+600}   '#▲であゆむがいることをわかりやすく、デモ用
        self.empty = True


   

class Floor:
    win_lose = None
    #ゲームに勝利したかの判定に使う
    escape = False
    #あゆむが逃げたかの判定に使う
    ayumu_room = 0
    #あゆむのいる部屋を保持する
    hassisi = False
    #drugイベントが起動するようにするため
    round = 1
    #何ラウンド耐えたか示す

    def __init__(self):
        Player()
        #ここでplayerデータの消去(作成とも言える）を行うべき
        #特殊技能　と　かたがきをつけても面白いかもね
        self.floor = []
        #floorリストは、ゲームの初めに一度だけ作成される。ゲームが始まると削除のみおけ
        for i in range(26):
        #floorをあゆむ抜きで作成
            if i == 0:
                self.floor.append(None)
            else:
                self.floor.append(Room(i))

        self.ayumu_room_num = randint(1,25)
        #Floor.ayumu_roomに関して、毎回Floorが作成されるたびにリセットされるから、気にしなくて良い

        Floor.ayumu_room = self.ayumu_room_num
        #ayumuが入った部屋をクラス変数に残した、ハッシシイベントで使う

        #ayumuが入る部屋を決定する
        self.floor[self.ayumu_room_num] = RoomAyumu(self.ayumu_room_num)
        #ここでfloorの初期データは完成
        print('loading...')
        print('loading...')
        print('loading...')
        print('')  
        print('\nフロア作成完了')
        self.select_room()

        #エンディングがない、、、実は謎解きゲームにすると面白いかもね、、、
        
    def select_room(self):
        print('')
        string1 = '              '
        string2 = '              '
        string3 = '              '
        string4 = '              '
        string5 = '              '
        for i, name in enumerate(self.floor):
            if i == 0:
                continue
            else:
                if i <= 5:
                    string1 += name.room_name
                elif i <= 10:
                    string2 += name.room_name
                elif i <= 15:
                    string3 += name.room_name
                elif i <= 20:
                    string4 += name.room_name
                elif i <= 25:
                    string5 += name.room_name
        line = ''
        for _ in range(85):
            line += '-'
        print(f'第{Floor.round}ラウンド')
        print(line)
        print(string1)
        print(string2)
        print(string3)
        print(string4)
        print(string5)
        print(line)
        print('□：入室してない    ■：入室済み    ❔あゆむがいるかもしれない部屋    ▲あゆむのいる部屋')
                
        #print(self.floor)
        #ルーム表示を文字列表示にして、あとNoneを無くして！

        Player.show_data()
        print('')
        while True:
            try:
                select_room_num = input('601から625で入る部屋を番号で選んでください,下二桁で:')

                #ステータス表示
                select_room_num = int(select_room_num) 
                if not 0 < select_room_num < 26 :
                    print('エラー、もう一度入力してください')
                    continue
                break
                #例外処理を作ること
            except:
                print('エラー、もう一度入力してください')
        print('')
        print(line)
        print(f'room{select_room_num + 600}\n')

        self.floor[select_room_num].generate_ev()
        #選んだ部屋のイベントが発生

        
        if Floor.win_lose == False:
        #負けたとき（あゆむに負けたとき　or 同級生に負けたとき）
            Floor.win_lose = None
            Floor.round = 1
            Player()
            #データを消去している

        elif Floor.win_lose :
        #elifからifに変えた
        #あゆむを倒したとき（あゆむと戦う　or あゆむ　を捕まえたとき)
            Floor.win_lose = None
            Floor.round = 1


        elif Floor.escape:
            Floor.round += 1
        #あゆむが逃げ出したとき
            #self.floor.pop(select_room_num)
            #選んだ部屋を消した
            #self.floor.pop(0)
            #Noneの部屋を消した
            #x = len(self.floor)
            #y = randint(1,x-1)
            #self.floor[y] = RoomAyumu(y)
            #多分ここであゆむの逃走が完了

            self.floor[select_room_num] = RoomEmpty(select_room_num)
            #入った部屋をemptyにした
            x = randint(1,25)
            #あゆむが逃げる部屋を決めている
            Floor.ayumu_room = x
            #あゆむがいる部屋を保存した

            
            if self.floor[x].empty :
                self.floor[x] = RoomAyumuEmpty(x)
            elif not self.floor[x].empty :
                self.floor[x] = RoomAyumu(x)
            #あゆむが逃げる部屋がfilled か　emptyかを判定する

            Floor.escape = False

            if '　あゆむ　' in Player.friends:
            #隠しイベント、ドッペルゲンガーイベントを起こす
                #ステートを戻した
                print('..........ファーーー')
                print('あゆむがめを覚ました')
                input('enterを押して、あゆむから、あゆむの居場所を聞こう')
                print(f'あゆむ「俺は{Floor.ayumu_room}におるよ！」')
                print('マップにあゆむがいるかもしれない場所に表示される')
                list = [i for i in range(1,26)]

                
                change_room = self.floor[Floor.ayumu_room]
                                     
                if type(change_room) == type(RoomAyumu(0)):
                        self.floor[Floor.ayumu_room] = RoomAyumuHatena(i)
                   
                elif type(change_room) == type(RoomAyumuEmpty(0)):
                        self.floor[Floor.ayumu_room] = RoomAyumuEmptyHatena(i)

            if Floor.hassisi:
            #ハッシシイベントを起こす
                Floor.hassisi = False
                #ステートを戻した
                print('..........っつ！！！！')
                input('突然のめまい、記憶が薄れていく、、、enterで目を覚ます')
                print('ハッシシが、後になってきいたようだ、あゆむのいるばしょがなんとなくわかる')
                list = [i for i in range(1,26)]

                change_list = sample(list,randint(3,6))
                num = Floor.ayumu_num
                if not num in change_list:
                    change_list.append(num)
                for i in change_list:
                    change_room = self.floor[i]
                    if type(change_room) == type(Room(0)):
                        self.floor[i] = RoomHatena(i)        
                    elif type(change_room) == type(RoomAyumu(0)):
                        self.floor[i] = RoomAyumuHatena(i)
                    elif type(change_room) == type(RoomEmpty(0)):
                        self.floor[i] = RoomEmptyHatena(i)
                    elif type(change_room) == type(RoomAyumuEmpty(0)):
                        self.floor[i] = RoomAyumuEmptyHatena(i)
    
            self.select_room()
            #このメソッドが離れているのは仕方がない

        


        
        else:
            Floor.round += 1
        #あゆむが部屋にいないとき
            self.floor[select_room_num] = RoomEmpty(select_room_num)
            #選んだ部屋の要素をリストから削除
            #選んだ部屋は削除ではなくて、部屋に入れるが４つのイベントが発生しないようにすればいいのでは？？？　→特殊イベント作れる
            #ここはpopさせないで、からのroomという選択肢を作っていいかも、イベントの幅が増える

            #このように条件分岐させないと

            if '　あゆむ　' in Player.friends:
            #隠しイベント、ドッペルゲンガーイベントを起こす
                #ステートを戻した
                print('..........ファーーー')
                print('あゆむがめを覚ました')
                input('enterを押して、あゆむから、あゆむの居場所を聞こう')
                print(f'あゆむ「俺は{Floor.ayumu_room}におるよ！」')
                print('マップにあゆむがいるかもしれない場所に表示される')
                list = [i for i in range(1,26)]

                
                change_room = self.floor[Floor.ayumu_room]
                                     
                if type(change_room) == type(RoomAyumu(0)):
                        self.floor[Floor.ayumu_room] = RoomAyumuHatena(i)
                   
                elif type(change_room) == type(RoomAyumuEmpty(0)):
                        self.floor[Floor.ayumu_room] = RoomAyumuEmptyHatena(i)

                self.select_room()

            if Floor.hassisi:
            #ハッシシイベントを起こす
                Floor.hassisi = False
                #ステートを戻した
                print('..........っつ！！！！')
                input('突然のめまい、記憶が薄れていく、、、enterで目を覚ます')
                print('ハッシシが、後になってきいたようだ、あゆむのいるばしょがなんとなくわかる')
                list = [i for i in range(1,26)]

                change_list = sample(list,randint(3,6))
                num = Floor.ayumu_room
                if not num in change_list:
                    change_list.append(num)
                for i in change_list:
                    change_room = self.floor[i]
                    if type(change_room) == type(Room(0)):
                        self.floor[i] = RoomHatena(i)        
                    elif type(change_room) == type(RoomAyumu(0)):
                        self.floor[i] = RoomAyumuHatena(i)
                    elif type(change_room) == type(RoomEmpty(0)):
                        self.floor[i] = RoomEmptyHatena(i)
                    elif type(change_room) == type(RoomAyumuEmpty(0)):
                        self.floor[i] = RoomAyumuEmptyHatena(i)

                self.select_room()
        
        
        #Floor()
        #死んだ時読み込んでもらいたい
        #self.select_room()
        #↑これがあったからデータがリセットされなかった？？？
            
            #もう一度部屋選択に移行       
      

        #リストの要素を削除する処理を書くこと
        #↑は解決済み
        print('...loadin...')
        print('...loadin...')
        print('...loadin...')
        print('')
        print('所持品がリセットされました')
        print('生き返りに成功しました')

        Floor()
        #しぬとこれにたどり着く？？？そうwin_lose == Falseの時
        
if __name__ == '__main__':
    main()

"""
ルームがから部屋になるように設定する
　番号調整

ルーム番号を６００台にする

条件管理のクラスを作る

あゆむがランダムで逃げるイベントを作ろう

アイテム設定
　お金
　お酒
　　戦闘イベントを回避
　からの酒びん
　復活の水
　お風呂セット
　クラブチケット
　バット
　女装
　
仲間設定　　　ゲームのヒントをくれるキャラを作る（から部屋、特殊イベント、クリアの条件等々
　だいち
　　（通常）あゆむがいるばしょのヒント　
　　（特殊）死ぬ　（ひかりがいると）
　れお
　　（通常）ご飯を作る（命が１復活）
　　（特殊）
　太陽
　　（通常）
　　（特殊）太　か　陽をくれる（水があると）
　ちゃん
　　（通常）敵を倒す
　　（特殊）クリアのヒント
　ハウスマスター
　　（通常）おかねをくれる
　　からの酒瓶を持ってると、、、
　しょうい
　　（通常）ビートボックス
　　（特殊）お金（低確率）
　　（特殊）手を繋ぐイベント （もえのがいると）　→ 痛い思い出
　　（特殊）インターン
　女の子
　　（通常）
　　（特殊）ようだとわかる（ようを手に入れると）
　もえの
　フカヒレ
　　もえのとだいちがいると手に入る
　たけだ
　　しょういともえのがいると
　ひかる
　

イベント
　もえのとだいち
　復活の水をある部屋に持っていくと、、、ちゃん復活イベント
　たけだとふかひれ
　ハウスマスター
　隠しステージ
　　セントラルパーク（野球）
　　風呂（お風呂セット）
　　　水がゲットできる
　　クラブ（クラブのチケット）
　　女子フロア

プレイヤーデータが何回でリセットされるか
　3回まで死ねる
　　一回死ぬごとに、フロアデータはリセットされるが、プレイヤーデータ（アイテム）は消えない
 3回後データはリセット
 　プレイヤーデータが消える

あゆむ
　寝てる
　　捕まえると　お金ゲット
　戦う
　　倒すと　→ お金ゲット　強くなったあゆむ
　仲間がいると
　　よう
　　↓
　　真のあゆむ（真のあゆむを倒すとクリア）




ストーリを作る
　深夜を徘徊するあゆむを見つける
　
クリア条件
"""