# super market billing

name = input("enter my name:")
# list of iteams
lists = '''
        Rice  = Rs 30/kg
        Oil   = Rs 170/liter
        sugar = Rs 50/kg
        salt  = Rs 20/kg
        '''
# Declaration
ptice = 0
pricelist = []
totalprice = 0
finalamount = 0
ilist = []
qlist = []
plist = []
#rate for items
items= {'rice':30,'oil':170,'sugar':50,'salt':20}
option = int(input("for list of items press 1:"))
if option == 1:
    print(lists)
for i in range (len(items)):
    inp1 = int(input("if you want to buy press 1 or 2 exist:"))
    if inp1 == 2:
       break
    if inp1 == 1:
       item = input ("enter your iteams:")
       quality = int(input("enter quality"))
       if item in items.keys():
        price = quality*(items[item])
        pricelist.append((item,quality,items,price))
        totalprice = price
        qlist.append(quality)
        ilist.append(item)
        plist.append(price)
        gst = (totalprice*5)/100
        finalamount = gst+totalprice
inp = input("can i bill the iteams yes or no:")
if finalamount!=0:
    print(30* "=","srjun",30*"=")
    print(30* " ","medak")
    print("Name:",name,40*"","date")
    print(50*"-")
    print("sno",5*" ", 'iteam',5*" ",'quality',4*" ",'price')
    for i in range(len(pricelist)):
        print(i,5*' ',ilist[i],5*' ',5*' ',qlist[i],5*' ',plist[i])
        print(60*"-")
        print(30*" ",'totalAmount:','Rs',totalprice)
        print("gst amount",30*" ",'Rs', gst)
        print(60*"-")
        print(30*" ",'finalAmount:','Rs',finalamount)
        print(60*"-")
        print(20*" ","Thanks for visiting")
        print(60*"-")



