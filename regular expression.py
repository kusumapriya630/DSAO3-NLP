import re

def main():
    # Sample text
    text = "Hello, my email addresses are john@example.com and jane@gmail.com. Feel free to contact me!"

    # Define a pattern for matching email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Use re.findall to find all matches in the text
    email_addresses = re.findall(email_pattern, text)

    # Print the matched email addresses
    print("Found email addresses:")
    for email in email_addresses:
        print(email)

    # Use re.search to search for the first occurrence of the pattern
    search_result = re.search(email_pattern, text)
    
    # Print the first found email address
    if search_result:
        print("\nFirst email address found:", search_result.group())
    else:
        print("\nNo email address found in the text.")

if __name__ == "__main__":
    main()
