# Exercise 1 : Call History
# Instructions

#     Create a class called Phone. This class takes a parameter called phone_number. When instantiating an object create an attribute called call_history which value is an empty list.

#     Add a method called call that takes both self and other_phone (i.e another Phone object) as parameters. The method should print a string stating who called who, and add this string to the phone’s call_history.

#     Add a method called show_call_history. This method should print the call_history.

#     Add another attribute called messages to your __init__() method which value is an empty list.

#     Create a method called send_message which is similar to the call method. Each message should be saved as a dictionary with the following keys:
#         to : the number of another Phone object
#         from : your phone number (also a Phone object)
#         content

#     Create the following methods: show_outgoing_messages(self), show_incoming_messages(self), show_messages_from(self)

#     Test your code !!!


class Phone:

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []


    def call(self,other_phone):
        print(f"{self.phone_number} has called {other_phone.phone_number}")
        self.call_history.append(other_phone.phone_number)
        other_phone.call_history.append(self.phone_number)


    def show_call_history(self):
        print(*self.call_history ,sep=" -> ")


    def send_message(self,other_phone,umessage):
        dict_messages = {}
        dict_messages["to"] = other_phone.phone_number
        dict_messages["from"] = self.phone_number
        dict_messages["message"] = umessage
        self.messages.append(dict_messages)
        other_phone.messages.append(dict_messages)

    def show_outgoing_messages(self):
        return [x["message"] + " -> "+ x["to"] for x in self.messages if x["to"]!=self.phone_number]


    def show_incoming_messages(self):
        return [x["from"] + " -> "+ x["message"] for x in self.messages if x["from"]!=self.phone_number]


    def show_messages_from(self,num):
        return [x for x in self.messages if x["from"]==num]

Dekel = Phone("0502163020")
Nadav = Phone("0501242354")
Dekel.call(Nadav)
Dekel.call(Nadav)
Dekel.call(Nadav)
Dekel.call(Nadav)
Dekel.show_call_history()
Dekel.send_message(Nadav, "Hey")
Dekel.send_message(Nadav, "How")
Dekel.send_message(Nadav, "Are")
Dekel.send_message(Nadav, "You")
Nadav.send_message(Dekel, "Hey!, I'm great how are you?")
print(Dekel.show_outgoing_messages())
print(Dekel.show_incoming_messages())

print(Nadav.show_messages_from("0501242354"))