
available_product = ["Carrots", "Onions", "Broccoli", "Egg plants", "Cabbages"]
information = input("Press Y to order product or N to see the available products: ")


if information == "Y":

    def get_information():

        product_name = input("Choose product of your choice: ")
        for items in available_product:
            if product_name in items:
                quantity = input("Enter the product quantity: ")
                payment_mode = input("Choose the means of payment: ")

                print('''
                Product_name: {}
                Quantity:{}
                Payment Mode:{}
                '''.format(product_name, quantity, payment_mode))
                print("The order has been successfully recieved")
                break
            else:
                print("Product not available")
                print("Choose another")
                break
    get_information()

elif information == "N":

    my_product = {
        "Carrots": {
            "price": 500,
            "quantity": "100 kg"
        },
        "Onions": {
            "price": 800,
            "quantity": "60 kg",
        },
        "Broccoli": {
            "price": 800,
            "quantity": "60 kg",
        }
    }
    for keys, values in my_product.items():
        print(f"{keys}:{values}")
    print("Pick product of your choice")
else:
    print("Order denied")