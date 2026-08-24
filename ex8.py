#======================================================
# CUSTOMER FEEDBACK FORMATOR 
#Teaching:  Built- in string Methods & String Formationg 
#======================================================

# Step 1: Input raw customer data (often messy with extra spaces or bad casing )
raw_name = input("Enter customer name: ")
raw_feedback = input("Enter feedback message: ")
rating = input("Enter rating (1 to 5): ")

#======================================================
# CONCEPT 1: BUILT - IN STRING METHODS 
#======================================================

# 1. .strip() removes unwanted spaces from the start and end 
clean_name = raw_name.strip()
clean_feedback = raw_feedback.strip()

# 2. .title() capatalizes the first letter of each word ( e.g.,"john doe" ->"john doe")
formatted_feedback = clean_name.title()

# 3. .capatalize() makes only the very first letter of the message uppercase
formatted_feedback = clean_feedback.capitalize()

# 4. .replace() replaces specifies words or characters (e.g., fixing common abbreviations)
formatted_feedback = clean_feedback.replace(" u ", " you ").replace(" r "," are ")

# 5. .count() counts occurrenses of a specifies words or character (e.g., checking exclamation marks)
exclamation_count = formatted_feedback.count("!")

# 6. .upper() converts tyext to ALL CAPS for important tags
while True:
    if (rating>=1 and rating<=5):
        if int(rating) >= 4:
            category = "POSITOVE".upper()
        else:
            category = "NEEDS REVIEW".upper()
        break    
    else:
        rating = int(input("Invalid rating provided. Enter rating (1 to 5): "))
# -------------------------------------------------------
# CONCEPT 2: STRING FORMATTING (f.strings)
# -------------------------------------------------------

# Displays formatted report using f-strings and text alignment
print("\n " + "=" * 45)
# :^45 centers the text within a 45-character wide block
print(f"{'PROFESSIONAL FEEDBACK REPORT':^45}")
print("-" * 45)

# Standard f-string variable interpolation
print(f"Customer Name : {formatted_name}")
print(f"Rating        : {rating} / 5 stars")
print(f"Category      : [{category}]")
print(f"Excitement    :{exclamation_count} exclamation mark(s)")
print("." * 45)
print("Formatted Message:")
print(f'"{formatted_feedback}"')
print("-" * 45)
