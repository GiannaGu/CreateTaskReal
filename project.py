
temp = input("What is the weather in your area? Sunny, Rainy, Snowy, or Cloudy?")

if temp != "Sunny" or " Rainy" or "Snowy" or "Cloudy":
    print("Invalid response, please type in again")



clothing = ["Sunny", "Rainy", "Snowy", "Cloudy"]

weathers = {

"Sunny" : ["Shorts", "Flip-Flops", "Tank Top", "Short-Sleeve Shirt","Sunglasses"],

"Rainy" : ["Pants", "Closed Toe Shoes", "Rain-Jacket", "Umbrella","Long-Sleeve Shirt"],

"Snowy" : ["Thermals", "Boots", "Gloves", "OverCoat","Layers of Long Sleeves"],

"Cloudy" : ["Jeans", "Sweater", "Fluffy Socks", "Leggings","Hoodie"]

}

def choose_clothes(temp):

    for i in clothing:
        
        if i == temp:
            return i    
        
         

outfit = weathers[(choose_clothes(temp))]
print("Here are some clothes to wear for your type of weather!", outfit)
