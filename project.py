#What should you wear depending on the weather? Prompt the user for what kind of weather they have 
#maybe hot, cold, or warm, then once getting the answer give them an idea of they may want to wear. 

#Start with a variable that can hold the input of the weather
weather = input("What is the weather like in your area? a)Sunny b) Rainy c)Snowy d)Cloudy")

#Make lists and dictonaries that hold different clothing apperals

clothing = {

"Sunny":["Shorts", "Flip-Flops", "Tank Top", "Short-Sleeve Shirt","Sunglasses"],

"Rainy":["Pants", "Closed Toe Shoes", "Rain-Jacket", "Umbrella","Long-Sleeve Shirt"],

"Snowy":["Thermals", "Boots", "Gloves", "OverCoat","Layers of Long Sleeves"],

"Cloudy":["Jeans", "Sweater", "Fluffy Socks", "Leggings","Hoodie"]

}

#Make a Function that holds your input
def choose_clothes(weather,clothing):

    if weather == "a":
        

