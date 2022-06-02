class HTTPConnection:

    def __init__(self, address):
        self.address = address

    def __enter__(self): #executed first
        print(f"Connected to {self.address}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb): #executed last
        print(f"Closing the connection....")
        # TODO the logic for closing
        print(f"Connection Closed...")

    def send(self): #executed middle
        print("sending data....")





if __name__ == '__main__':
    with HTTPConnection("127.0.0.1") as connection:
        connection.send()
        connection.send()
        connection.send()

    print("Out of the Context Manager")