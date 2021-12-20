import datetime

### ファイル出力
def output_receipt(text_receipt):
    with open("receipt.txt", "a", encoding="utf-8") as f:
        f.write(text_receipt)

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_item_code(self):
        return self.item_code
    
    def get_price(self):
        return self.price
    
    def get_item_name(self):
        return self.item_name

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list = []
        self.item_number_list = []
        self.amount = 0
        self.money = 0
        self.change = 0
        self.item_master = item_master
    
    def add_item_order(self,item_code):
        self.item_order_list.append(item_code)
        
    def add_item_number(self,item_number):
        self.item_number_list.append(item_number)
        
    def add_money(self, money):
        self.money = money
        
    def output_item_list(self):
        for item, item_master, item_number in zip(self.item_order_list, self.item_master, self.item_number_list):
            output_receipt(f'商品コード:{item}, 商品名:{item_master.get_item_name()}, 価格:{item_master.get_price()}, 個数:{item_number}\n')
    
    def output_items_amount(self):
        for item_master, item_number in zip(self.item_master, self.item_number_list):
            self.amount += int(item_master.get_price()) * int(item_number)
        output_receipt(f'合計金額:{self.amount}\n')
        
    def output_money(self):
        output_receipt(f'お預かり金額:{self.money}\n')
        
    def output_change(self):
        self.change = self.money - self.amount
        output_receipt(f'おつり:{self.change}\n')
    
    
### メイン処理
def main():
    # item_master.csvの読み込み
    with open("item_master.csv", "r", encoding="utf-8") as f:
        item_lines = f.read().splitlines()
    
    # マスタ登録
    item_master=[]  
    for item_line in item_lines:
        item = item_line.split(",")
        item_master.append(Item(item[0], item[1], item[2]))
    
    # オーダー登録
    order=Order(item_master)  
    while True:
        order_yn = input("オーダー登録を行いますか（N:0, Y:1):")
        if not int(order_yn):
            break
        
        # 入力した商品コードを登録
        item_order = input("オーダーを登録する商品コードを入力してください:")
        order.add_item_order(item_order)
        
        # 個数を登録
        item_number = input("商品の個数を入力してください:")
        order.add_item_number(item_number)
        
        print(f'商品コード:{item_order}の商品を{item_number}個オーダー登録しました。\n')
    
    # お預かり金額登録
    money = input("お預かり金額を入力してください:")
    order.add_money(int(money))
    
    # レシートのタイトル出力
    output_receipt("-------------------------------------------------\n")
    now = datetime.datetime.now()
    output_receipt(f'■日時:{now.strftime("%Y年%m月%d日 %H:%M")}のレシート\n')
    output_receipt("-------------------------------------------------\n")
    
    # オーダー出力
    order.output_item_list()
    
    # 合計金額・お預かり金額・おつり出力
    order.output_items_amount()
    order.output_money()
    order.output_change()
    output_receipt("-------------------------------------------------\n")
    
    
    
if __name__ == "__main__":
    main()