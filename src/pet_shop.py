# WRITE YOUR FUNCTIONS HERE

# 1
def get_pet_shop_name(shop):
    return shop["name"]

# 2
def get_total_cash(amount):
    return amount["admin"]["total_cash"]

# 3,4
def add_or_remove_cash(shop, sale):
    shop["admin"]["total_cash"] += sale

# 5  
def get_pets_sold(shop):
    return shop["admin"]["pets_sold"] 

# 6
def increase_pets_sold(sale, pets):
    sale["admin"]["pets_sold"] += pets

# 7
def get_stock_count(shop):
    return len(shop["pets"])

# 8,9
def get_pets_by_breed(shop, breed):
    pets = []
    for pet in shop['pets']:
      if pet['breed'] == breed:
          pets.append(pet)
 
    return pets
   

# # 10
def find_pet_by_name(shop, name):
    for pet in shop['pets']:
      if pet['name'] == name:
        return pet

    return None



# # 11
def remove_pet_by_name(shop, name):
    dictionary_key = 0
    for pet in shop['pets']:
      if pet['name'] == name:
        shop['pets'].pop(dictionary_key)
      dictionary_key += 1
 

# # 12
def add_pet_to_stock(shop, new_pet):
    shop['pets'].append(new_pet)
        
# 13
def get_customer_cash(customer):
    return customer['cash']

# 14
def remove_customer_cash(customer, amount):
    customer['cash'] -= amount
    
# 15
def get_customer_pet_count(customer):
    return len(customer['pets'])

# 16
def add_pet_to_customer(customer, new_pet):
    customer['pets'].append(new_pet)