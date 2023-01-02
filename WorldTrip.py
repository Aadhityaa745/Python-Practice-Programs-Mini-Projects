def trip():
    print('------------------------------------------')
    print(' Welcome To World Trip Tourism Management ')
    print('------------------------------------------')
    print(' Select the country from below\n ')
    print(' 1. Singapore 2. India 3. France ')
    opt = int(input(" Press 1 or 2 or 3 : "))
   
    if opt==1:
        print('Tourist places in Singapore\n')
        sing()
    elif opt==2:
        print('Tourist places in India\n')
        ind()
    elif opt==3:
        print('Tourist places in France\n')
        fra()
    else:
        print("\nInvalid Option")

def sing():
    print('+---------------------+--------------------+')
    print('|Tourist Spot         |       Amount($)    |')
    print('+---------------------+--------------------+')
    print('|1. Universal Studio  |          45        |')
    print('|2. Gardens by the Bay|          15        |')
    print('|3. Singapore Flyer   |          35        |')
    print('|4. Night Safari      |          25        |')
    print('+---------------------+--------------------+')
    places = ['Universal Studio  ','Gardens by the Bay','Singapore Flyer   ','Night Safari      ']    
    money = [45,15,35,25]
    final(places, money)
    
def ind():
    print('+---------------------+--------------------+')
    print('|Tourist Spot         |       Amount($)    |')
    print('+---------------------+--------------------+')
    print('|1. Taj Mahal         |          17        |')
    print('|2. Red Fort          |          16        |')
    print('|3. Qutub Minar       |          28        |')
    print('|4. Fatehpur Sikhri   |          37        |')
    print('+---------------------+--------------------+')
    places = ['Taj Mahal         ','Red Fort          ','Qutub Minar       ','Fatehpur Sikhri   ']    
    money = [17,16,28,37]
    final(places, money)
    
def fra():
    print('+---------------------+--------------------+')
    print('|Tourist Spot         |       Amount($)    |')
    print('+---------------------+--------------------+')
    print('|1. Eiffel Tower      |           27       |')
    print('|2. Louvre Museum     |           20       |')
    print('|3. Cruise            |           17       |')
    print('|4. Toot Bus          |           40       |')
    print('+---------------------+--------------------+')
    places = ['Eiffel Tower      ','Louvre Museum     ','Cruise            ','Toot Bus          ']    
    money = [27,20,17,40]
    final(places, money)

def final(places, money):
    pl = input('Select the Places You want to Visit : ')
    li = pl.split(',')#'1','4' --> 1 4
    mem = int(input('Enter Number of Members :'))
    dic = {}
    for a in li:
        if a=='1':
            dic[places[0]]=money[0]#dic['universal studio']=45
        elif a=='2':
            dic[places[1]]=money[1]
        elif a=='3':
            dic[places[2]]=money[2]
        elif a=='4':
            dic[places[3]]=money[3]
    billing(dic,mem)
    
def billing(dic,mem):
    global fd,acc,ta
    ta=0
    print("\nPlaces You've Selected To Visit\n")
    print('_____________________________________________________________________________\n')
    print('+---------------------+--------------------+-------------+----------------+')
    print('|Tourist Spot         |       Amount($)    |   Members   |   Total Amount |')
    print('+---------------------+--------------------+-------------+----------------+')
    
    for a in dic:
        pl = mem*dic[a]
        ta+=pl
        fd = mem*500
        acc = mem*1000
        print('|',a,' |','       ',dic[a],'       ','|    ',mem,'      |','     ',pl,'      |')
    print('| Food                |         500        |    ',mem,'      |     ',fd,'     |')
    print('| Accomodations       |        1000        |    ',mem,'      |     ',acc,'     |')
    print('|_____________________|____________________|_____________|________________|')
    print('| Total Amount  :                                              ',ta+fd+acc,'     |')
    print('+---------------------+--------------------+-------------+----------------+')

trip()

