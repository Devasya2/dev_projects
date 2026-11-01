import random



print('what time are u visiting')
time=int(input("enter time 0-23\n"))
time_whole=round(time)
         
if 0<=time_whole <= 6:
    print('sry we are closed.')
else:
    print('Welcome. Have food in this restaurant')
    menu1=["pancake","waffle","paratha","burger","sandwich"]
    price1=['30','35','50','100','14']
    print('ITEM', 'PRICE (INR), excl. Tax', sep='\t\t\t')
    for kk in range(len(menu1)):
     print(str(kk+1)+'. '+menu1[kk], price1[kk], sep='\t\t')
     shopping_cart = [] 
     shopping_quant= []
     shopping_complete = 0
    while shopping_complete==0:
        order = int(input('Enter 1 to 5 to select an item, 6 to proceed to checkout.\n')) 
        if order <= 5:
             print('You selected', menu1[order-1])
             quant = int(input('How many units do you wish to purchase?'))
             if menu1[order-1] in shopping_cart:
                idx = shopping_cart.index(menu1[order-1])
                shopping_quant[idx]+=quant
             else:
                shopping_cart.append(menu1[order-1])        
                shopping_quant.append(quant)        
        
                print('Added to shopping cart:', quant, 'units of', menu1[order-1])
        elif order == 6:
           shopping_complete = 1
        else: 
            print("Sorry that was not a valid input.")
        
    print()
    print('Your Shopping Cart:')

    grand_tot=0


    print('ITEM', 'QUANT', 'TOTAL', sep='\t\t\t')    
    for kk in range(len(shopping_cart)):
       idx = menu1.index(shopping_cart[kk])
      
   
       tot_price=(int(price1[idx])*shopping_quant[kk])
    
       grand_tot += tot_price
       print(shopping_cart[kk], shopping_quant[kk],tot_price, sep='\t\t\t')
    print()

    random_number = random.randint(1, 10)
    guess=int(input('enter guess'))
    if guess==random_number:
       print('congrats. you got 50% off')

       print('Your total order is (INR)', grand_tot*0.5)
    else:
       print('better luck next time. pay full price')
       print('Your total order is (INR)', grand_tot)


