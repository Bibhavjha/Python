# a
price=50
txt="price is {} rupees"
print(txt.format(price))
# b
item="noodles"
price=25
txt="price of {} is {} rupees"
print(txt.format(item,price))
# c(indexing can also be used)
item="noodles"
price=25
txt="{1} is a flat food. price of {1} is {0} rupees"
print(txt.format(price,item)) 
# d we can use named indexing
txt="{item} is a flat food. it costs {price} rupees"
print(txt.format(item="noodles",price=25))
