contacts ={
    "Alice":"555-1234",
    "Bob":"555-5678",
    "Charlie":"555-9999"
}


print(f"Alice's number:{contacts["Alice"]}")
contacts["Diana"]="555-4567"
print(f"Contacts after adding a new person:{contacts}")
contacts["Bob"]="567-9087"
print(f"Contacts after updating Bob:{contacts}")
del contacts["Charlie"]
print(f"Contacts after deleting Charlie:{contacts}")
print(f"All names:{contacts.keys()}")
print(f"All numbers:{contacts.values()}")
print(f"Total contacts:{len(contacts)}")


