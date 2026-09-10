email_text = input("Enter the email text:\n")


symbols = ['@', '.', '!']

print("\nSpecial Symbol Count:")
for symbol in symbols:
    count = email_text.count(symbol)
    print(f"{symbol} : {count}")