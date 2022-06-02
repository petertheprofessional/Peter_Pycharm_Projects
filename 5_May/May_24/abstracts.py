from abc import ABC, abstractmethod

class Sender(ABC): #abstracts can

    @abstractmethod
    def send(self, message):
        pass


class PlainTextSender(Sender):

    def send(self, message):
        print(f"Message Sent! >>> {message}")


class EncryptSender(Sender):

    def send(self, message):
        result = str()
        for char in message:
           enc_message += 'A'
        print(f"Message Sent {enc_sender}")

class ReverseSender(Sender):
    def send(self, message):
        print(f"Message Sent {message.reverse()}")

class Chat:
    def __init__(self, sender):
        self.sender = sender

    def send_message(self, message):
        self.sender.send(message)


if __name__ == '__main__':
    sender_object = PlainTextSender()
    chat = Chat(sender_object)
    chat.send_message("Hi Peter...")

    enc_sender = EncryptSender()
    chat = Chat(enc_sender)
    chat.send_message("Hi Peter")

    rev_sender = ReverseSender()
    chat
