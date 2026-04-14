buying=float(input("Enter the buying price:"))
selling=float(input("Enter the selling price:"))
if(selling>buying):
    profit=selling-buying
    print("You made a profit of:",profit)
else:
    loss=selling-buying
    print("you lost:",loss)