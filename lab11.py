print("-" * 45)
print("    BUS SEAT RESERVATION LAYOUT SYSTEM")
print("-" * 45)

total_rows = int(input("Enter number of rows in the bus: "))
seats_per_row = int(input("Enter number of seats per row: "))

# ----------- Create the Nested List (Bus Layout) -----------
bus_layout = []
for r in range(total_rows):
    row = []
    for c in range(seats_per_row):
        row.append("O")  # every seat starts as Open
    bus_layout.append(row)  # add this row into the main nested list

print(f"\nBus layout created: {total_rows} rows x {seats_per_row} seats per row.")
print("All seats are currently Open (O).\n")

while True:
    print("-" * 45)
    print("1. Display Bus Layout")
    print("2. Reserve a Seat")
    print("3. Cancel a Reservation")
    print("4. Check a Specific Seat Status")
    print("5. Count Available / Reserved Seats")
    print("6. Exit")
    print("-" * 45)

    choice = input("Enter your choice (1-6): ").strip()

    # ------------ DISPLAY LAYOUT (Traversal) ------------
    if choice == "1":
        print("\nCurrent Bus Layout:")
        print("Rows top to bottom - Row 1 to Row", total_rows, "\n")

        for r in range(len(bus_layout)):
            print(f"Row {r + 1}: ", end="")  # traverse outer list (rows)
            for c in range(len(bus_layout[r])):
                print(bus_layout[r][c], end=" ")  # traverse inner list (seats)
            print()

        print()

    # ------------ RESERVE SEAT ------------
    elif choice == "2":
        row_num = int(input(f"Enter row number (1 to {total_rows}): ")) - 1
        col_num = int(input(f"Enter seat number (1 to {seats_per_row}): ")) - 1

        if 0 <= row_num < total_rows and 0 <= col_num < seats_per_row:
            if bus_layout[row_num][col_num] == "X":
                print("This seat is already reserved.\n")
            else:
                bus_layout[row_num][col_num] = "X"  # indexing into nested list
                print(f"Seat at Row {row_num + 1}, Seat {col_num + 1} reserved successfully.\n")
        else:
            print("Invalid row or seat number.\n")

    # ------------ CANCEL RESERVATION ------------
    elif choice == "3":
        row_num = int(input(f"Enter row number (1 to {total_rows}): ")) - 1
        col_num = int(input(f"Enter seat number (1 to {seats_per_row}): ")) - 1

        if 0 <= row_num < total_rows and 0 <= col_num < seats_per_row:
            if bus_layout[row_num][col_num] == "O":
                print("This seat is already open (not reserved).\n")
            else:
                bus_layout[row_num][col_num] = "O"
                print(f"Reservation cancelled for Row {row_num + 1}, Seat {col_num + 1}.\n")
        else:
            print("Invalid row or seat number.\n")

    # ------------ CHECK SPECIFIC SEAT ------------
    elif choice == "4":
        row_num = int(input(f"Enter row number (1 to {total_rows}): ")) - 1
        col_num = int(input(f"Enter seat number (1 to {seats_per_row}): ")) - 1

        if 0 <= row_num < total_rows and 0 <= col_num < seats_per_row:
            status = bus_layout[row_num][col_num]

            if status == "O":
                print(f"Seat Row {row_num + 1}, Seat {col_num + 1} is OPEN.\n")
            else:
                print(f"Seat Row {row_num + 1}, Seat {col_num + 1} is RESERVED.\n")
        else:
            print("Invalid row or seat number.\n")

    # ------------ COUNT SEATS ------------
    elif choice == "5":
        open_count = 0
        reserved_count = 0

        for r in range(len(bus_layout)):
            for c in range(len(bus_layout[r])):
                if bus_layout[r][c] == "O":
                    open_count += 1
                else:
                    reserved_count += 1

        print(f"Total Seats   : {total_rows * seats_per_row}")
        print(f"Open Seats    : {open_count}")
        print(f"Reserved Seats: {reserved_count}")

    # ------------ EXIT ------------
    elif choice == "6":
        print("Exiting program. Thank you!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.\n")