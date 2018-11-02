bk_name = input("enter name of the book:")
bk_code = int(input("enter book code:"))
bk_price = int(input("enter book price:"))
if (bk_name=="python_programing") and (bk_price>800):
    d_price= 20/100*bk_price
    print("the total price of the book is :",float(bk_price)-float(d_price))
elif (bk_name=="linux_shell_scripting")  and (500<bk_price>800):
    d_price = 15/100*bk_price
    print("the total price of the book is :",float(bk_price)-float(d_price))
elif (bk_price<500):
    d_price = 15/100*bk_price
    print("the total price of the book is :", float(bk_price) - float(d_price))
else :
    d_price=5/100*bk_price
    print("the total price of the book is :", float(bk_price) - float(d_price))

