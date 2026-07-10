from parking import ParkingLot

parking = ParkingLot()

while True:

    print("\nSmart Parking Management")
    print("1. Park Vehicle")
    print("2. Show Parked Vehicles")
    print("3. Search Vehicle")
    print("4. Remove Vehicle")
    print("5. Total Collection")
    print("6. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        parking.park_vehicle()

    elif choice == "2":
        parking.show_vehicles()

    elif choice == "3":
        parking.search_vehicle()

    elif choice == "4":
        parking.remove_vehicle()

    elif choice == "5":
        parking.total_collection()

    elif choice == "6":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice")