import socket
import sys

HOST, PORT = "localhost", 9999


def print_menu():
    print("""
    Python DB Menu
    1. Find customer
    2. Add customer
    3. Delete customer
    4. Update customer age
    5. Update customer address
    6. Update customer phone
    7. Print report
    8. Exit
    """)

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    while True:
        print_menu()
        user_input = input("Select: ")
        if user_input.isdigit() and 1 <= int(user_input) <= 8:

            command = int(user_input)
            if command == 1:
                name = input("Customer name: ")
                sock.sendall(bytes("1|" + name, "utf-8"))  
            if command == 2:
                name = input("Customer name: ")
                age = input("Age: ")
                street = input("Street address: ")
                phone = input("Phone: ")
                sock.sendall(bytes("2|" + name + "|" + age + "|" + street + "|" + phone, "utf-8"))  
            if command == 3:
                name = input("Customer name: ")
                sock.sendall(bytes("3|" + name, "utf-8"))
            if command == 4:
                name = input("Customer name: ")
                age = input("Age: ")
                sock.sendall(bytes("4|" + name + "|" + age, "utf-8"))
            if command == 5:
                name = input("Customer name: ")
                street = input("Street address: ")
                sock.sendall(bytes("5|" + name+ "|" + street, "utf-8"))  
            if command == 6:
                name = input("Customer name: ")
                phone = input("Phone: ")
                sock.sendall(bytes("6|" + name + "|" + phone, "utf-8"))                              
            if command == 7:
                sock.sendall(bytes("7", "utf-8"))                              
            if command == 8:
                print("Good bye")
                sys.exit()

            received = str(sock.recv(1024), "utf-8")   
            print("Server response: {}".format(received)) 
    
        else:
            print("Please provide a valid menu option.")

  

   



