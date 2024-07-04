'''CREATING PAYMENT RECEIPT

Creating payment receipts is a pretty common task, be it an e-commerce website or any local store for that matter.

Here, you have to create our own transaction receipts just by using python. We would be using reportlab to generate the PDFs. Generally, it comes as a built-in package but sometimes it might not be present too. 
If it’s not present, then simply type the following in your terminal'''

from datetime import datetime 

name = input("Enter Customer Name: ")

price = 0
plist = []
totalprice = 0
finalprice = 0
itemlist = []
quantitylist = []
pricelist =[]

items = { 'rice':200 , 'wheat flour': 90 ,'panner' :120,'termaric' :170, 'sugar':80 , 'potatoes':80, 'tomatoes': 100 ,'onions': 120, 
         'carrots': 60, 'apples': 200, 'bananas':90, 'chicken': 270 ,'milk': 80, 'butter': 150, 'eggs': 70 }

for i in range(len(items)):
    inp = int(input("Enter 1 for bill generation OR Enter 2 for exit:  "))
    if inp == 2:
        break
    elif inp == 1 :
        item = input("Enter items: ")
        quantity = int(input("Enter quantity: "))
        if item in items.keys():
            price = quantity * (items[item])
            plist.append( (item, quantity, items, price) ) 
            totalprice += price 
            itemlist.append(item)
            quantitylist.append(quantity)
            pricelist.append(price)
            gst = ( totalprice * 5)/100 
            finalprice = gst + totalprice
        else:
            print("Enter item is not found")  
    else:
        print("you entered invalid number ")

status = input("start billing yes/no:  ")
if status == 'yes' :
    pass
    if finalprice != 0 :
            print("")
            print("")
            print(27*"*" , "CSK local store" , 30*"*" )
            print(30*"-", "Hyderabad" , 34*"-")
            print("")
            print("")
            print("Customer Name: ", name , 10*" ", "Date: ", datetime.now())
            print(75 *"-")
            print("sno", 10*" ", "items" , 10*" ", 'quantity' , 10*" ", "price" )
            for i in range(len(pricelist)):
                 print( i, 10*" ", itemlist[i], 15*" ", quantitylist[i], 15*" ",pricelist[i])
            print(75*"-")
            print('Total Amount: ', 'RS', totalprice)
            print("gst amount: ", "RS" , gst)
            print(75*"-")
            print(" ")
            print("Final Amount:", "RS", finalprice)
            print(" ")
            
            print(25*"*", "Thank you for visiting", 27*"*")
            print("")
            print(30*" ", "visit again!")
    
    else:
         print("thank you")

              

















