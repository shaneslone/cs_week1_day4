def csRaindrops(number):
    result = ""
    raindrop = False
    if number % 3 == 0:
        result += "Pling"
        raindrop = True
    if number % 5 == 0:
        result += "Plang"
        raindrop = True
    if number % 7 == 0:
        result += "Plong"
        raindrop = True
    if not raindrop:
        result = str(number)
    return result
        
    

