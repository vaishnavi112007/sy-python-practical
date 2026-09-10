product_names = []
product_prices = []
product_qty = []

while True:     


    
    print( "=" * 45 )
    print( "  PRODUCT INVENTORY SYSTEM" )
    print( "=" * 45 )
    print( "1. Add Product" )
    print( "2. Delete Product" )
    print( "3. Update Product Price" )
    print( "4. Display All Products (Traverse)" )
    print( "5. Search Product (by name)" )
    print( "6. Sort Products by Price (Ascending)" )
    print( "7. Sort Products by Price (Descending)" )
    print( "8. Sort Products by Name (Alphabetical)" )
    print( "9. Show Costliest / Cheapest Product" )
    print( "10. Exit" )
    print( "=" * 45 )

    choice = input( "Enter your choice(1-10): " ).strip()

    #-----------------ADD PRODUCT----------------

    if choice == '1':
        name = input( "Enter product name: " ).strip()

        if name in product_names:
            print( f"Product '{name}' already exists! Use update option instead.\n" )
        else:
            price = float(input( f"Enter price for {name}: " ))
            qty = int(input( f"Enter quantity for {name}: " ))
            product_names.append(name)
            product_prices.append(price)
            product_qty.append(qty)
            print( f"Product '{name}' added successfully.\n" )

    #----------------DELETE PRODUCT--------------------

    elif choice == '2':
        name = input( "Enter productt name to delete: " ).strip()

        if name in product_names:
            index = product_names.index(name)
            product_names.pop(index)
            product_prices.pop(index)
            product_qty.pop(index)
            print( f"Product '{name}' deleted successfully.\n" )
        else:
            print( f"Product '{name}' not found.\n" )

    #------------------UPDATE PRICE--------------------

    elif choice == '3':
        name = input( "Enter Product name to update: " ).strip()

        if name in product_names:
            index = product_names.index(name)
            new_price = float( input( f"Enter new price for {name}: " ) )
            product_prices[index] = new_price
            print( f"Price for '{name}' updated successfully.\n" )
        else:
            print( f"Product '{name}' not found.\n" )

    #-------------------DISPLAY / TRAVERSE------------------
    elif choice == '4':
        if len( product_names ) == 0:
            print( "No products to display.\n" )
        else:
            print( "\n{:<5} {:<20} {:<10} {:<10}".format("No.", "Name", "Price", "Qty"))
            print("-" * 45)
            for i in range(len(product_names)):
                print("{:<5} {:<20} {:<10} {:<10}".format(i + 1, product_names[i], product_prices[i], product_qty[i]))   #i+1 is for representing 1
                                          
                print()
            
    #--------------------SEARCH-------------------
    elif choice == '5':
        name = input( "Enter product name to search: " ).strip()

        if name in product_names:
            index = product_names.index(name)
            print( f"Found -> Name: {product_names[index]},"   
                   f"Price: {product_prices[index]}, Qty: {product_qty[index]}\n")
        else:
            print( f"Productt '{name}' not found.\n" )

    #------------------SORT BY PRICE ASCENDING------------------
    elif choice == '6':
        if len(product_names) == 0:
            print( "No products to sort.\n" )
        else:
            combined = list(zip(product_prices, product_names, product_qty))
            combined.sort()       

            product_prices = [item[0] for item in combined]
            product_names = [item[1] for item in combined]
            product_qty = [item[2] for item in combined]
            print("Products sorted by price (ascending).\n")

    #--------------------SORT BY PRICE DESCENDING------------------
    elif choice == '7':
            if len(product_names) == 0:
                print( "No products to sort.\n" )
            else:
                combined = list(zip(product_prices, product_names, product_qty))
                combined.sort(reverse=True)           
    
                product_prices = [item[0] for item in combined]
                product_names = [item[1] for item in combined]
                product_qty = [item[2] for item in combined]
                print("Products sorted by price (descending).\n")

    #----------------------SORT BY NAME------------------------------
    elif choice == '8':
            if len(product_names) == 0:
                print( "No products to sort.\n" )
            else:
                combined = list(zip(product_prices, product_names, product_qty))
                combined.sort()
    
                product_names = [item[0] for item in combined]
                product_prices = [item[1] for item in combined]
                product_qty = [item[2] for item in combined]
                print("Products sorted alphabetically by name.\n")

    #------------------------COSTLIEST / CHEAPEST---------------------
    elif choice == '9':
        if len(product_prices) == 0:
            print("No products available.\n")
        else:
            highest = max(product_prices)
            lowest = min(product_prices)

            costliest_index = product_prices.index(highest)
            cheapest_index = product_prices.index(lowest)

            print("\n-------Price Summary-------")
            print(f"Cosrliest Product : {product_names[costliest_index]} (Price: {highest})")
            print(f"Cheapest Product : {product_names[cheapest_index]} (Price: {lowest})")
            
    #-------------------EXIT------------------------ 
    elif choice == '10':
        print( "Exiting program. Thank you!" )
        break

    else:
        print( "Invalid choice. Please enter a number between 1 and 10.\n" )