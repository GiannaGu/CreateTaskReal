weathers = {

"Sunny" : ["A tank top, shorts, sunglasses, and tennis shoes", "A Short-sleeve shirt, skirt, flip-flops, and a hat"],

"Rainy" : ["Jeans, closed toe shoes, a rain-jacket and a long-sleeve shirt", "A hoodie, Coat, Umbrella, and Rain Boots"],

"Snowy" : ["Thermals,a sweater, gloves and an over-coat!", "Snow-pants,a puffer jacket, goggles, and a long sleeve shirt"],

"Cloudy" : ["Jeans, a Sweater and fluffy socks", "Leggings, hoodies, and warm slippers"]

}

def choose(weathers):

    temp = input("What is the weather in your area? Sunny, Rainy, Snowy, or Cloudy?")

    while temp not in weathers.keys():
        temp = input("Input Invlaid, Please Pick: Sunny, Rainy, Snowy, or Cloudy?")
    
    print("Heres an outfit you can wear for ", temp , " weather!", weathers[temp][0])
    like = input("Do you want to see another outfit that would fit the weather? Yes or No?" )
    if like == "Yes":
        print("Here is another outfit for ", temp, "weather!", weathers[temp][1])
    else:
        print("Glad you like your outfit! Thank You!")
    

start = input("Do you need outfit suggestions? Yes or No?")
while start == "Yes":
    choose(weathers)
    end = input("Do you need to choose another Outfit for a a different weather? Yes or No?")
    if end == "No":
        break



