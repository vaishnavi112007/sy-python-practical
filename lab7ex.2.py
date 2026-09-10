
paragraph = input("Enter a paragraph:\n")

count = paragraph.lower().split().count("python")

print(f'The word "python" appears {count} time(s).')