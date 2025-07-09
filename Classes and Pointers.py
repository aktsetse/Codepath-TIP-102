# class Cookie:
#     def __init__(self, color):
#         self.color = color

#     def get_color(self):
#         return self.color
    
#     def set_color(self, color):
#         self.color = color



# cookie_one = Cookie('green')
# cookie_two = Cookie('blue')

# print('Cookie one is', cookie_one.get_color())
# print('Cookie two is', cookie_two.get_color())

# num1 = 11
# num2 = num1

# print('Before num2 value is updated:')
# print("num1 =", num1)
# print("num2 =", num2)

# print("\nnum1 points to:", id(num1))
# print("num2 points to:", id(num2))

# from array import *

# arr1 = array('i',[1,2,3,4,5,6])
# arr2 = array('d', [1.3,1.5,1.6])
# print(arr1)


# from twilio.rest import Client

# Twilio credentials
# account_sid = "your_account_sid"
# auth_token = "your_auth_token"
# client = Client(account_sid, auth_token)

# # List of recipient numbers
# numbers = ["+13187507542", "+12405841268"]

# # Sending messages
# for number in numbers:
#     message = client.messages.create(
#         body="Hello! This is a bulk SMS test.",
#         from_="+your_twilio_number",
#         to=number
#     )
#     print(f"Message sent to {number}: {message.sid}")


