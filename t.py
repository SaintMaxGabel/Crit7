class Item:
    def __init__(self):
        self.name = 'none'
        self.price = 0.0
        self.quantity = 0
        self.description = 'none'
    def set_attributes(self):
        self.name = str(input('Set a name: '))
        self.price = float(input('Set a price: '))
        self.quantity = int(input('Set a quantity: '))
        self.description = str(input('Set a description: ')) 
    def printItem(self):
        print(self.name +' '+ str(self.quantity) + ' @ $'+ str(self.price) + '= $' + str(self.quantity * self.price))
    def modQuan(self):
        self.quantity = int(input('Enter quantity: '))
    def printD(self):
        print(self.description)
class ShoppingCart:
    def __init__(self, name , date): 
        self.customer_name = name;
        self.current_date = date;
        self.cart_items = [];
    def add_item(self,ItemToPurchase):
        self.cart_items.append(ItemToPurchase);
    def remove_item(self, anItemsName):
        self.cart_items.remove(anItemsName);
    def get_num_items_in_cart(self):
        return len(self.cart_items)
    def modify_item(self, ItemToPurchase):
        found = 'no'
        for item in self.cart_items:
            if item.name == ItemToPurchase.name:
                 found = 'yes'
                 if item.price != 0.0 and item.quantity != 0 and item.description != 'none':
                     item.printItem()
                     item.price = float(input('Input a price to modify'))
                     item.quantity = int(input('input a quantity to modify'))
                     item.description = str(input('input a new discription'))
                     item.printItem()
                     print('Item motified')
        if found == 'yes':
           print('Item found')
        else:
                print('Item not found in cart. Nothing modified.')
    def get_cost_of_cart(self):
        cost = 0.0
        for item in self.cart_items:
            cost = cost + (item.price * item.quantity)
        return cost
    def print_total(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        if self.get_num_items_in_cart() >0:
            print('Number of Items: '+ str(self.get_num_items_in_cart()))
            for item in self.cart_items:
                item.printItem()
            print('Total: $' +str(self.get_cost_of_cart()))
        else:
            print('SHOPPING CART IS EMPTY')
    def print_descriptions(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print('Items description')
        for item in self.cart_items:
            print(item.name + ': ' + item.description)
    def print_menu(self,cartMENUIn):
        
        cartMENU = cartMENUIn
        

        while True:
            print('')
            print('MENU')
            print('a - add item to cart')
            print('r - Remove item from cart')
            print('c - Change item quantity')
            print("i - Output items' descriptions")
            print('o - Output shopping cart')
            print('q - Quit')
            print('Choose an option:')
            letter = input()

            if letter == 'a':
                print('ADD ITEM TO CART')
                item = Item()
                item.set_attributes()
                cartMENU.add_item(item)
            elif letter == 'c':
                print('CHANGE ITEM QUANTITY')
                itemTM = str(input(' Item name to modify quantity: '))
                for item in cartMENU.cart_items:
                    if itemTM == item.name:
                        item.modQuan()
            
            elif letter == 'r':
                print("REMOVE ITEM FROM CART")
                itemTM = str(input(' Item name to remove: '))
                for item in cartMENU.cart_items:
                    if itemTM == item.name:
                        cartMENU.remove_item(item)
            
            elif letter == 'i':
                print("OUTPUT ITEMS' DESCRIPTIONS")
                cartMENU.print_descriptions()            
            elif letter == 'o':
                print('OUTPUT SHOPPING CART')
                cartMENU.print_total()

            elif letter == 'q':
                 break
            else:
                print(" ")
                

            

"""

Step 4:

"""










cart = ShoppingCart('CustomerOne','4/7/2024')

print(cart.customer_name + ' date: ' + cart.current_date)
item1t = Item()
item1t.set_attributes()

item2t = Item()
item2t.set_attributes()


cart.add_item(item1t)
cart.add_item(item2t)
print(str(cart.get_num_items_in_cart())+ ' items in cart')
print('price of cart is: '+ str(cart.get_cost_of_cart()))
cart.print_total()

cart.modify_item(item2t)

cart.remove_item(item1t)
print(str(cart.get_num_items_in_cart()))

print('price of cart is: '+ str(cart.get_cost_of_cart()))

cart.print_total()
cart.print_descriptions()






cartMENUIn = ShoppingCart('CustomerOne','4/7/2024')

cartMENUIn.print_menu(cartMENUIn)



AName = str(input('enter a name: '))
ADate = str(input('write  a date: '))
print("Customer's name: " + AName)
print("Today's date: " + ADate)

cartMENUIn1 = ShoppingCart(AName,ADate)

cartMENUIn1.print_menu(cartMENUIn1)