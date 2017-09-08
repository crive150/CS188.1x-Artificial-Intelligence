fruitPrices = {'apples' : 2.0, 'oranges' : 1.5, 'pears' : 1.75 }

def buyFruit(fruit, numPounds):
    if fruit not in fruitPrices:
        print "Sorry but we don't have %s" % (fruit)
    else:
        cost = fruitPrices[fruit] * numPounds
        print "That'll be %f please" % (cost)

# Main Function
if __name__ == '__main__':
    buyFruit('apples', 2.4)
    buyFruit('coconut',2)