print("=" * 45)
print("     BUS SEAT RESERVATION LAYOUT SYSTEM")
print("=" * 45)

total_rows = int(input("Enter number of rows in the bus: "))
seats_per_row = int(input("Enter number of seats per row: "))

# Create nested list
bus_layout = []

for r in range(total_rows):
    row = []
    for c in range(seats_per_row):
        row.append("O")
    bus_layout.append(row)

print("\nBus layout created successfully!")
print("O = Open, X = Reserved")

while True:
    print("\n" + "=" * 45)
    print("1. Display Bus Layout")
    print("2. Reserve a Seat")
    print("3. Cancel a Reservation")
    print("4. Check a Specific Seat Status")
    print("5. Count Available / Reserved Seats")
    print("6. Exit")
    print("=" * 45)

    choice = input("Enter your choice (1-6): ")

    # Display Layout
    if choice == "1":
        print("\nCurrent Bus Layout:")

        for r in range(len(bus_layout)):
            print(f"Row {r + 1}: ", end="")

            for c in range(len(bus_layout[r])):
                print(bus_layout[r][c], end=" ")

            print()

    # Reserve Seat
    elif choice == "2":
        row_num = int(input(f"Enter row number (1 to {total_rows}): ")) - 1
        col_num = int(input(f"Enter seat number (1 to {seats_per_row}): ")) - 1

        if 0 <= row_num < total_rows and 0 <= col_num < seats_per_row:

            if bus_layout[row_num][col_num] == "X":
                print("This seat is already reserved!")
            else:
                bus_layout[row_num][col_num] = "X"
                print(f"Seat Row {row_num + 1}, Seat {col_num + 1} reserved successfully!")

        else:
            print("Invalid row or seat number.")

    # Cancel Reservation
    elif choice == "3":
        row_num = int(input(f"Enter row number (1 to {total_rows}): ")) - 1
        col_num = int(input(f"Enter seat number (1 to {seats_per_row}): ")) - 1

        if 0 <= row_num < total_rows and 0 <= col_num < seats_per_row:

            if bus_layout[row_num][col_num] == "O":
                print("This seat is already open.")
            else:
                bus_layout[row_num][col_num] = "O"
                print(f"Reservation cancelled for Row {row_num + 1}, Seat {col_num + 1}.")

        else:
            print("Invalid row or seat number.")

    # Check Specific Seat
    elif choice == "4":
        row_num = int(input(f"Enter row number (1 to {total_rows}): ")) - 1
        col_num = int(input(f"Enter seat number (1 to {seats_per_row}): ")) - 1

        if 0 <= row_num < total_rows and 0 <= col_num < seats_per_row:

            if bus_layout[row_num][col_num] == "O":
                print(f"Seat Row {row_num + 1}, Seat {col_num + 1} is OPEN.")
            else:
                print(f"Seat Row {row_num + 1}, Seat {col_num + 1} is RESERVED.")

        else:
            print("Invalid row or seat number.")

    # Count Seats
    elif choice == "5":
        open_count = 0
        reserved_count = 0

        for r in range(len(bus_layout)):
            for c in range(len(bus_layout[r])):

                if bus_layout[r][c] == "O":
                    open_count += 1
                else:
                    reserved_count += 1

        total_seats = total_rows * seats_per_row

        print("\nTotal Seats   :", total_seats)
        print("Open Seats    :", open_count)
        print("Reserved Seats:", reserved_count)

    # Exit
    elif choice == "6":
        print("Exiting program. Thank you!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")