import random
import string

class OTPGenerator:
    def __init__(self, length=6, alphanumeric=False):
        self.length = length
        self.alphanumeric = alphanumeric

    def generate_otp(self):
        if self.alphanumeric:
            characters = string.ascii_letters + string.digits
        else:
            characters = string.digits
        return ''.join(random.choices(characters, k=self.length))

def get_valid_length():
    while True:
        try:
            length = int(input("Enter OTP length (between 4 and 16): "))
            if 4 <= length <= 16:
                return length
            else:
                print("OTP length must be between 4 and 16.")
        except ValueError:
            print("Please enter a valid integer.")

def get_otp_type():
    while True:
        otp_type = input("Alphanumeric OTP? [yes(y)/no(n)]: ").strip().lower()
        if otp_type in ['yes', 'y']:
            return True
        elif otp_type in ['no', 'n']:
            return False
        else:
            print("Please enter a valid response: yes/y or no/n.")

def ask_to_continue():
    while True:
        choice = input("Do you want to generate another OTP? [yes(y)/no(n)]: ").strip().lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("Please enter yes/y or no/n.")

# Main loop
while True:
    length = get_valid_length()
    alphanumeric = get_otp_type()

    otp_gen = OTPGenerator(length=length, alphanumeric=alphanumeric)
    print("Generated OTP:", otp_gen.generate_otp())

    if not ask_to_continue():
        print("Thank you! Exiting OTP Generator.")
        break
