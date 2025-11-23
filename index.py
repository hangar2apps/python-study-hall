# making shopping cart

# dictionary for inventory 
# shopping cart will be a list
# need functions 
    # - add item to cart
    # - remove from cart
    # - calculate total
    # - display cart
    # - display inventory
    
# initalize an empty cart
# see what's in inventory
# add item to cart
# remove item from cart
# calculate total 
# check out



inventory = [
    {"ID": 1, "name": "banana", "price": 1.45},
    {"ID": 2, "name": "apple", "price": 3.45},
    {"ID": 3, "name": "cheese", "price": 8.45},
    {"ID": 4, "name": "egg", "price": 16.45},
]

cart = []

def calculate_total():
    total = 0
    for id in cart:
        for item in inventory:
            if(item["ID"] == id):
                total += item["price"]
    print(f'Total: ${total}')

def get_item_id(name):
    print(f'Name: {name}')
    id_to_return = None
    for item in inventory:
        if(item["name"] == name):
            id_to_return = item["ID"]
            break
    return id_to_return


def show_inventory():
    for item in inventory:
        print(f'Name: {item["name"]}, Price: {item["price"]}')

def add_to_cart(id):
    print(f'ID: {id}')
    cart.append(id)
    print(f'Cart: {cart}')

def remove_from_cart(id):
    print(id)
    cart.remove(id)
    print(f'Cart: {cart}')



def main():
    print('walk into store')

    show_inventory()

    selected_item = input('What item would you like to add? apple, banana, cheese, or egg? ')

    print('selected_item: ', selected_item)

    item_id = get_item_id(selected_item)
    
    add_to_cart(item_id)

    selected_item = input('What other item would you like to add? apple, banana, cheese, or egg? ')

    print('selected_item: ', selected_item)

    item_id = get_item_id(selected_item)
    
    add_to_cart(item_id)

    selected_item = input('What other item would you like to add? apple, banana, cheese, or egg? ')

    print('selected_item: ', selected_item)

    item_id = get_item_id(selected_item)
    
    add_to_cart(item_id)

    selected_item = input('What item would you like to remove? apple, banana, cheese, or egg? ')

    print('selected_item: ', selected_item)

    item_id = get_item_id(selected_item)
    
    remove_from_cart(item_id)

    calculate_total()

main()

