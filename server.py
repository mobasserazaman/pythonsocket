import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):

    database = {

    }

    def setup(self):
        # Load database
        f = open("data.txt","r")
        for line in f:
            record = line.rstrip('\n').split('|')
            for i in range(4):
                record[i] = record[i].strip()
        
            if record[0] is not None:
                MyTCPHandler.database[record[0]] = record
        f.close()
        

    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):

        def print_report():
            keylist =  MyTCPHandler.database.keys()
            sorted_keylist = sorted(keylist)
        
            result =  "\n** Python DB contents **\n"
            for key in sorted_keylist:
                result = result + "|".join(MyTCPHandler.database.get(key)) + "\n"

            return result

        def process_request(request):
            try:
                command = int(request[0])
                arguments = request.split('|')
                if command == 1:
                    record = MyTCPHandler.database.get(arguments[1])
                    if record is not None:
                        return "|".join(record)
                    else:
                        return arguments[1] + " not found in database" 
                elif command == 2:
                    record = MyTCPHandler.database.get(arguments[1])
                    if record is None:
                        MyTCPHandler.database[arguments[1]] = [arguments[1],arguments[2],arguments[3],arguments[4]]
                        return "Customer added"
                    else:
                        return "Customer already exists"
                elif command == 3:
                    record = MyTCPHandler.database.get(arguments[1])
                    if record is not None:
                        MyTCPHandler.database.pop(arguments[1])
                        return "Customer deleted"
                    else:
                        return "Customer does not exist"
                elif command == 4:
                    record = MyTCPHandler.database.get(arguments[1])
                    if record is not None:
                        record[1] = arguments[2]
                        return "Customer age updated"
                    else:
                        return "Customer not found"
                elif command == 5:
                    record = MyTCPHandler.database.get(arguments[1])
                    if record is not None:
                        record[2] = arguments[2]
                        return "Customer address updated"
                    else:
                        return "Customer not found"
                elif command == 6:
                    record = MyTCPHandler.database.get(arguments[1])
                    if record is not None:
                        record[3] = arguments[2]
                        return "Customer phone updated"
                    else:
                        return "Customer not found"
                elif command == 7:
                    return print_report()
            except:
                return "Client disconnected"

        while True:  
            self.data = self.request.recv(1024)
            request = self.data.decode()
            result = process_request(request)
            self.request.sendall(result.encode()) 


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()