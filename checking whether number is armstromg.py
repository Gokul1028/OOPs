#checking whether the given no is armstrong or not

num=input("enter the number")
sum =0
for a in num:
    sum+=int(a)**3
if sum==int(num):
    print("Armstrong")

else:
    print("not")(a)**3