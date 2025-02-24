amount = float(input("Enter the purchase amount: "))
location = input("Enter the delivery location (Local/International): ").strip().lower()
payment_method = input("Enter the payment method (CreditCard/DebitCard/UPI/Cash): ").strip().lower()

# Applying discount based on purchase amount
if amount >= 5000:
    discount = amount * 0.20  # 20% discount
elif amount >= 3000:
    discount = amount * 0.15  # 15% discount
elif amount >= 1000:
    discount = amount * 0.10  # 10% discount
else:
    discount = amount * 0.05  # 5% discount

final_amount = amount - discount
print(f"Discount applied: {discount}")
print(f"Final payable amount: {final_amount}")

# Determining delivery charge based on location
if location == "local":
    delivery_charge = 50
elif location == "international":
    delivery_charge = 500
else:
    print("Invalid location entered!")
    delivery_charge = 0  # No delivery charge applied

print(f"Delivery charge: {delivery_charge}")

# Processing payment method
if payment_method == "creditcard":
    print("Payment processed using Credit Card.")
elif payment_method == "debitcard":
    print("Payment processed using Debit Card.")
elif payment_method == "upi":
    print("Payment processed using UPI.")
elif payment_method == "cash":
    print("Cash on delivery selected.")
else:
    print("Invalid payment method!")

# Calculating total payable amount
total_payable = final_amount + delivery_charge
print(f"Total amount to be paid: {total_payable}")

