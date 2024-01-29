#Nate Eikom
#Date: Jan 29

#variables inputted by user
price = float(input('Price: '))
discountRate = float(input('Discount: '))

#calculated variables from input
discountAmt = price * discountRate
salesPrice = price - discountAmt

print('The original price was 'f'${price: ,.2f}')
print('The discount amount is 'f'${discountAmt: ,.2f}')
print('The discounted price is 'f'${salesPrice: ,.2f}')