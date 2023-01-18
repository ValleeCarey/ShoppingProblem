import json

#Calculated Feature 1 and Feature 2
def calculate_total(shopping_cart):
    subtotal = 0
    for item in shopping_cart:
        subtotal += item['price']
    tax_rate = 0.0825
    tax_amount = subtotal * tax_rate
    grand_total = subtotal + tax_amount
    return {'subtotal': subtotal, 'tax_amount': tax_amount, 'grand_total': grand_total}

shopping_cart = [{'name': 'item1', 'price': 10.00}, {'name': 'item2', 'price': 15.00}, {'name': 'item3', 'price': 20.00}]
total = calculate_total(shopping_cart)

#print(total)
#Test cases
#print('Subtotal: $' + str(total['subtotal']) + ' USD')
#print('Tax amount: $' + str(total['tax_amount']) +  ' USD')
#print('Grand total: $' + str(total['grand_total']) + ' USD')

#Calculated Feature 3
def check_taxable(shopping_cart):
    taxable_subtotal = 0
    non_taxable_subtotal = 0

    tax = {"isTaxable": True}
    
    temp_file = json.dumps(tax)
    with open("isTaxable.json", "w") as file:
        file.write(temp_file)

    for item in shopping_cart:
        if item["isTaxable"]:
            taxable_subtotal += item['price']
        else:
            non_taxable_subtotal += item['price']
    tax_rate = 0.0825
    tax_amount = taxable_subtotal * tax_rate
    grand_total = taxable_subtotal + non_taxable_subtotal + tax_amount
    return {'subtotal': taxable_subtotal + non_taxable_subtotal, 'tax_amount': tax_amount, 'grand_total': grand_total}

#Testcases
print('Subtotal: $' + str(total['subtotal']) + ' USD')
print('Tax amount: $' + str(total['tax_amount']) +  ' USD')
print('Grand total: $' + str(total['grand_total']) + ' USD')


#Calculate Feature 4
def apply_coupon(shopping_cart, coupon_code):
    shopping_cart = [{'name': 'item1', 'price': 10.00}, {'name': 'item2', 'price': 15.00}, {'name': 'item3', 'price': 20.00}]

    data = {"coupon1": {"valid": True, "items": ["item1, item2"], "discount": 5.00}}, {"coupon2": {"valid": True, "items": ["item3"], "discount": 10.00}},{"coupon3": {"valid": False,  "items": ["item4"], "discount": 15.00}}

    temp_file = json.dumps(data, indent = 3)
    with open("coupon.json", "w") as file:
        file.write(temp_file)

    with open('coupon.json', 'r') as file:
        coupons = json.load(file)
        #print(type(coupons))
        if coupon_code in coupons:
            print(coupon_code)
            coupon = coupons[coupon_code]
            valid = coupon['valid'] 
            if valid:
        #checking to see if any of the coupons applies to the items in the cart.
                for item in shopping_cart:
                    if item['name'] in coupon['items']:
                        item['price'] -= coupon['discount']
                        print(item['price'])
                        break
                else:
                    print(f"{coupon_code} is not applied to any items in the cart.")
            else:
                print(f"{coupon_code} is not a valid coupon")

apply_coupon(shopping_cart, 'coupon1')
total = calculate_total(shopping_cart)
# print('Subtotal: $' + str(total['subtotal']) + ' USD')
# print('Tax amount: $' + str(total['tax_amount']) +  ' USD')
# print('Grand total: $' + str(total['grand_total']) + ' USD')