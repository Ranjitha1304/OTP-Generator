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

        otp = ''.join(random.choices(characters, k=self.length))
        return otp

# CLI input usage
try:
    length = int(input("Enter OTP length (between 4 and 16): "))
    if length < 4 or length > 16:
        raise ValueError("OTP length must be between 4 and 16.")

    while True:
        otp_type = input("Alphanumeric OTP? (yes/no): ").strip().lower()
        if otp_type in ['yes', 'y']:
            alphanumeric = True
            break
        elif otp_type in ['no', 'n']:
            alphanumeric = False
            break
        else:
            print("Please enter a valid response: yes/y or no/n.")

    otp_gen = OTPGenerator(length=length, alphanumeric=alphanumeric)
    print("Generated OTP:", otp_gen.generate_otp())

except ValueError as e:
    print("Invalid input:", e)
