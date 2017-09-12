amount = int(input("Enter the Amount Please! :  "))
if amount<1000:discount = (amount*0.05) 
print("You are presented with 5 % Discount.And the discount amount is :-",discount)
else
	if amount>1000:
		discount = (amount*0.10)
print("You are presented with the 10% Discount.And the discount is :-",discount)
print("And the Net Payable amount is :- ", amount-discount)
print("Thank you for Shopping with Us!! ")