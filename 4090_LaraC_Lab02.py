#Christian Lara
#000983220
#Jun/24/2021
#Jun/24/2021
#The purpose of this project is to automate a calculation of loss or profits while trading stocks.
print('\nPURCHASE OF STOCK')
nameOfInvestor = input('Enter name of investor: ')
numberOfSharesPurchased = input('Enter number of shares purchased (as a whole amount): ')
costPerSharePurchased = input('Enter the cost per share (in dollars): ')
purchaseAmount = int(numberOfSharesPurchased) * float(costPerSharePurchased)
commissioForPurchase = float(purchaseAmount) * 0.03
print('Purchase amount is $' + str(format(purchaseAmount, ',.2f')))
print('Commission for the purchase is $' + str(format(commissioForPurchase, ',.2f')))

print('\nSALE OF STOCK')
nameOfInvestor = input('Enter name of investor: ')
numberOfSharesSold = input('Enter number of shares sold (as a whole amount): ')
costPerShareSold = input('Enter the cost per share (in dollars): ')
saleAmount = int(numberOfSharesSold) * float(costPerShareSold)
commissioForSale = float(saleAmount) * 0.03
print('Sale amount is $' + str(format(saleAmount, ',.2f')))
print('Commission for the sale is $' + str(format(commissioForSale, ',.2f')))

print('\nSUMMARY OF TRANSACTIONS')
print('Invertor name is ' + nameOfInvestor)
totalCommission = commissioForPurchase + commissioForSale
valueOfRestOfShares = (int(numberOfSharesPurchased )- int(numberOfSharesSold)) * float(costPerSharePurchased)
print('Total commission is $' + str(format(totalCommission, ',.2f')))
profitLossAmount = saleAmount - purchaseAmount - totalCommission + valueOfRestOfShares
print('Profit/Loss amount is $' + str(format(profitLossAmount, ',.2f')))
 
