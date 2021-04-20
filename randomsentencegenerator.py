import random as rd

def senGen():

    subject1 = ["I", "We", "They"]

    subject2 = ["He", "She", "Ahmed", "Bob", "Alice", "Wang", "Rafee"]

    verb1 = ["eat", "go", "speak", "like", "play", "drink"]

    verb2 = ["eats", "goes", "speaks", "likes", "plays", "drinks"]

    food = ["pasta", "pizzas", "fried chicken", "sandwiches", "burgers"]

    drinks = ["coffee", "tea", "fizzy drinks", "lemonade", "strawberry shake"]

    games = ["chess", "cricket", "football", "tennis", "golf", "basketball", "rugby"]

    places = ["school", "work", "the beach", "the countryside", "Neverland"]

    spoken = ["English", "Spanish", "French", "German", "nonsense", "the truth"]

    preposition = ["to", "at", "in"]
               

    sentence = ""

    r = rd.randint(0, 1)

    if r==0:          #Plural pronoun
           r1 = rd.randint(0, len(subject1)-1)   # I, We, They...
           w1 = subject1[r1]       
           sentence = sentence + " " + w1

           r2 = rd.randint(0, len(verb1)-1)   #verb
           w2 = verb1[r2]           #eat, go, speak...
           sentence = sentence + " " + w2
           if r2 == 0:    # eat
               r3 = rd.randint(0, len(food)-1)  #chooses food item
               w3 = food[r3]       #pasta, pizza, etc.
               sentence = sentence + " " + w3 
           elif r2 == 1:   #go
               w3 = preposition[0] #to
               sentence = sentence + " " + w3
               r3 = rd.randint(0, len(places)-1)
               w4 = places[r3]  #place
               sentence = sentence + " " + w4
           elif r2 == 2:   #speak
               r3 = rd.randint(0, len(spoken)-1)
               w3 = spoken[r3]
               sentence = sentence + " " + w3
           elif r2 == 3:           #like
                r3 = rd.randint(0,2)  # choose one of 3 options
                if r3 == 0: # food
                    r4 = rd.randint(0, len(food)-1)
                    w3 = food[r4]
                    sentence = sentence + " " + w3
                elif r3 ==1: #games
                    r4 = rd.randint(0, len(games)-1)
                    w3 = games[r4]
                    sentence = sentence + " " + w3
                elif r3 ==2: #places
                    r4 = rd.randint(0, len(places)-1)
                    w3 = places[r4]
                    sentence = sentence + " " + w3
           elif r2 == 4:  #play
                r3 = rd.randint(0, len(games)-1)
                w3 = games[r3]
                sentence = sentence + " " + w3
           elif r2 == 5:  #drink
                r3 = rd.randint(0, len(drinks)-1)
                w3 = drinks[r3]
                sentence = sentence + " " + w3

               
    elif r==1:        
        r1 = rd.randint(0, len(subject2)-1)  # He, She, ...
        w1 = subject2[r1]
        sentence = sentence + " " + w1

            

        r2 = rd.randint(0, (len(verb2))-1)   #verb
        w2 = verb2[r2]           #eats, goes, speaks...
        sentence = sentence + " " + w2
        if r2 == 0:    # eats
            r3 = rd.randint(0, len(food)-1)  #chooses food item
            w3 = food[r3]       #pasta, pizza, etc.
            sentence = sentence + " " + w3 
        elif r2 == 1:   #goes
            w3 = preposition[0] #to
            sentence = sentence + " " + w3
            r3 = rd.randint(0, len(places)-1)
            w4 = places[r3]  #place
            sentence = sentence + " " + w4
        elif r2 == 2:   #speaks
            r3 = rd.randint(0, len(spoken)-1)
            w3 = spoken[r3]
            sentence = sentence + " " + w3
        elif r2 == 3: #likes
            r3 = rd.randint(0,2)  # choose one of 3 options
            if r3 == 0: # food
                r4 = rd.randint(0, len(food)-1)
                w3 = food[r4]
                sentence = sentence + " " + w3
            elif r3 ==1: #games
                r4 = rd.randint(0, len(games)-1)
                w3 = games[r4]
                sentence = sentence + " " + w3
            elif r3 ==2: #places
                r4 = rd.randint(0, len(places)-1)
                w3 = places[r4]
                sentence = sentence + " " + w3
        elif r2 == 4:  #plays
            r3 = rd.randint(0, len(games)-1)
            w3 = games[r3]
            sentence = sentence + " " + w3

        elif r2 == 5:  #drink
            r3 = rd.randint(0, len(drinks)-1)
            w3 = drinks[r3]
            sentence = sentence + " " + w3


    print(sentence)

for i in range(10):
    senGen()
