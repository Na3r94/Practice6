def read_from_database():

    try:
        products = []

        f = open("naser_store/database.csv" )

        big_text = f.read()

        product_list = big_text.split('\n')

        for i in range(len(product_list)):
            info = product_list[i].split(',')

            products.append({'id':info[0] , 'name':info[1] , 'price' : info[2] , 'count':info[3]})


    except Exception as e:
        print(e)
        products = []

    return products

def add():
    id = input('enter id: ')
    name = input('enter name: ')
    price = input('enter price:')
    count = input('enter cpunt:')
    products.append({'id':id , 'name':name , 'price': price , 'count' : count})


def search():
    user_input = input('enter a text to search...')

    for product in products:
        if product['id'] == user_input or product['name'] == user_input:
            print(product)
            break
    else:
        print('not found')

def edit():
    user_input = input('enter a product name or code to edit : ')
    for product in products:
        if product['id'] == user_input or product['name'] == user_input:
            print(product)
            products.remove(product)
            add()

    else:
        print('not found')

def remove():
    user_input = input('enter a product name or code to remove : ')
    for product in products:
        if product['id'] == user_input or product['name'] == user_input:
            products.remove(product)
            print('your pruduct removed successfully')
            break
    else:
        print('not found')  

def buy():

    factor = []
    cost = 0
    
    while True:

        print('1 - select products')
        print('2 - exit and print factor')
        a = int(input('1 or 2? '))

        if a == 1:
            user_input = input('enter a product name or code: ')


            for product in products:
                if product['id'] == user_input or product['name'] == user_input:
                    print(product)
                    user_count = int(input('enter the number of product : '))
                    n = int(product['count'])
                    if user_count <= n :
                        count = n - user_count
                        factor.append({'name' : product['name'] , 'price' : product['price'] , 'count' : str(user_count)})
                        
                        products.remove(product)
                        products.append({'id' : product['id'] , 'name' : product['name'] , 'price' : product['price'] , 'count' : str(count)})
                        cost += user_count * int(product['price'])

                        break


                    else:
                        print('The number of products you want,doesnt exist')
                        break

            else:
                print('Sorry,This product doesnt available now')



        if a == 2 :
            print(factor)
            print('cost = ', cost)
            break

def show_all():
    for product in products:
        print(product)



def myExit():
    save = input('Do you want to save data? 1 - yes , 2 - no')
    if save == 1:
        f = open('naser_store/database.csv',mood ='w')
        for product in products:
            f.write(str(product['id'] + ',' + product['name'] + ',' + product['price'] + ',' + product['count'] + '\n'))
            #man in ghesmat ru motasefane harcheghad talash kardam movafagh nashodam
            #va ghesmate akhare code ru ham az code  sayere dustan copy kardam ama hamchenan ham bartaraf nashod
            #  har code moshabehi ke dar stackoverflow ham donbal kardam baz ham faghat ta ghabl az exit data save mishe
            #va dar seri jadid dobare liste ghadimi namayesh dade mishe

    
    exit()

def show_menu():
    print('Welcome to naser store')
    print('1 - add new product')
    print('2 - search')
    print('3 - edit')
    print('4 - remove')
    print('5 - buy')
    print('6- show all')
    print('7 - exit')

products =  read_from_database()


while True:
    show_menu()
    choice = input('enter your choice: ')

    if choice == '1':
        add()

    elif choice == '2':
        search()

    elif choice == '3':
        edit()

    elif choice == '4':
        remove()

    elif choice == '5':
        buy()

    elif choice == '6':
        show_all()

    elif choice == '7':
        myExit()
