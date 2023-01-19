import json
import unittest

class Item:
    def __init__(self, name, price, is_taxable):
        self.name = name
        self.price = price
        self.is_taxable = is_taxable

class Coupon:
    def __init__(self, code, discount, applicable_items):
        self.code = code
        self.discount = discount
        self.applicable_items = applicable_items

class ShoppingCart:
    def __init__(self, items, coupons, tax_rate):
        self.items = items
        self.coupons = coupons
        self.tax_rate = tax_rate

    def calculate_total(self):
        subtotal = 0
        taxable_subtotal = 0
        for item in self.items:
            subtotal += item.price
            if item.is_taxable:
                taxable_subtotal += item.price
        tax_total = taxable_subtotal * self.tax_rate
        grand_total = subtotal + tax_total
        if grand_total < 0:
            grand_total = 0
        return subtotal, tax_total, grand_total

    def apply_coupons(self):
        for item in self.items:
            for coupon in self.coupons:
                if item.name in coupon.applicable_items:
                    item.price -= item.price * coupon.discount

    def get_items(self):
        return self.items

    def get_coupons(self):
        return self.coupons

    def get_tax_rate(self):
        return self.tax_rate

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        with open('items.json') as json_file:
            items_data = json.load(json_file)
            items = []
            for item_data in items_data:
                item_name = item_data['name']
                item_price = item_data['price']

                with open('is_taxable.json') as json_file:
                    is_taxable_data = json.load(json_file)
                    for taxable_item_data in is_taxable_data:
                        if taxable_item_data['name'] == item_name:
                            item_is_taxable = taxable_item_data['is_taxable']
                item = Item(item_name, item_price, item_is_taxable)
                items.append(item)
        self.items=items

# Read coupons from a JSON file
        with open('coupon.json') as json_file:
            coupons_data = json.load(json_file)
            coupons = []
            for coupon_data in coupons_data:
                coupon = Coupon(coupon_data['code'], coupon_data['discount'], coupon_data['applicable_items'])
                coupons.append(coupon)
            self.coupons = coupons
            self.tax_rate = 0.0825
            self.shopping_cart = ShoppingCart(self.items, self.coupons, self.tax_rate)

    def test_calculate_total(self):
        subtotal, tax_total, grand_total = self.shopping_cart.calculate_total()
        self.assertEqual(subtotal, 80)
        self.assertEqual(tax_total, 6.6)
        self.assertEqual(grand_total, 86.6)

    def test_apply_coupons(self):
        self.shopping_cart.apply_coupons()
        items = self.shopping_cart.get_items
        self.assertEqual(items, [{"name": "item1", "price": 27, "is_taxable": True},{"name": "item2", "price": 50, "is_taxable": False}, {"name": "item3", "price": 20, "is_taxable": True} ])
    
    def test_get_items(self):
        items = self.shopping_cart.get_items()
        self.assertEqual(items, [{"name": "item1", "price": 27, "is_taxable": True},{"name": "item2", "price": 50, "is_taxable": False}, {"name": "item3", "price": 20, "is_taxable": True} ])

    def test_get_coupons(self):
        coupons = self.shopping_cart.get_coupons()
        self.assertEqual(coupons, [{"code": "coupon1", "discount": 0.1, "applicable_items":["item 1"]}])

    def test_get_tax_rate(self):
        tax_rate = self.shopping_cart.get_tax_rate()
        self.assertEqual(tax_rate, 0.0825)

unittest.main()








#without classes below 
#Calculated Feature 1 and Feature 2
# def calculate_total(shopping_cart):
#     subtotal = 0
#     for item in shopping_cart:
#         subtotal += item['price']
#     tax_rate = 0.0825
#     tax_amount = subtotal * tax_rate
#     grand_total = subtotal + tax_amount
#     #Makes sure grand total isn't negative
#     if grand_total < 0:
#         grand_total = 0
#         print(grand_total)

#     return {'subtotal': subtotal, 'tax_amount': tax_amount, 'grand_total': grand_total}

# shopping_cart = [{'name': 'item1', 'price': 10.00}, {'name': 'item2', 'price': 15.00}, {'name': 'item3', 'price': 20.00}]
# total = calculate_total(shopping_cart)

# #print(total)
# #Test cases
# #print('Subtotal: $' + str(total['subtotal']) + ' USD')
# #print('Tax amount: $' + str(total['tax_amount']) +  ' USD')
# #print('Grand total: $' + str(total['grand_total']) + ' USD')

# #Calculated Feature 3
# def check_taxable(shopping_cart):
#     taxable_subtotal = 0
#     non_taxable_subtotal = 0

#     tax = {"isTaxable": True}
    
#     temp_file = json.dumps(tax)
#     with open("isTaxable.json", "w") as file:
#         file.write(temp_file)

#     for item in shopping_cart:
#         if item["isTaxable"]:
#             taxable_subtotal += item['price']
#         else:
#             non_taxable_subtotal += item['price']
#     tax_rate = 0.0825
#     tax_amount = taxable_subtotal * tax_rate
#     grand_total = taxable_subtotal + non_taxable_subtotal + tax_amount
#     return {'subtotal': taxable_subtotal + non_taxable_subtotal, 'tax_amount': tax_amount, 'grand_total': grand_total}

# #Testcases
# # print('Subtotal: $' + str(total['subtotal']) + ' USD')
# # print('Tax amount: $' + str(total['tax_amount']) +  ' USD')
# # print('Grand total: $' + str(total['grand_total']) + ' USD')


# #Calculate Feature 4
# def apply_coupon(shopping_cart, coupon_code):
#     data = [{"coupon1": {"valid": True, "items": ["item1, item2"], "discount": 5.00}}, {"coupon2": {"valid": True, "items": ["item3"], "discount": 10.00}},{"coupon3": {"valid": False,  "items": ["item4"], "discount": 15.00}}]

#     #temp_file = json.dumps(data, indent = 3)
#     #with open("coupon.json", "w") as file:
#         #file.write(temp_file)

#     with open('coupon.json', 'r') as file:
#         coupons = json.load(file)
#         for coup in coupons:
#             for i in coup:
#         #for coupon_code in coupons:
#                 coupon = coup[i] #i is coupons1, 2, 3
#                 valid = coupon['valid'] #access valid items and discount
#                 if valid:
#         #checking to see if any of the coupons applies to the items in the cart.
#                     for item in shopping_cart:
#                         if item['name'] in coupon['items']:
#                             item['price'] -= coupon['discount']
#                             if item['price'] >= 0:
#                                 print(f"{coupon['discount']} discount has been applied to the total")
#                                 return item['price']

#                     else:
#                         print(f"{coupon_code} is not a valid coupon")

# coup = apply_coupon(shopping_cart, "coupon1")

# total = calculate_total(shopping_cart)
# print('Subtotal: $' + str(total['subtotal']) + ' USD')
# print('Tax amount: $' + str(total['tax_amount']) +  ' USD')
# print('Grand total: $' + str(total['grand_total']) + ' USD')
