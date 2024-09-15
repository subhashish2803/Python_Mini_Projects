import random

def coder():
    # Define the alphabet for encoding
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Get user input
    message = input("ENTER YOUR MESSAGE: ")
    
    # Split the message into words
    words = message.split()
    
    # Process each word
    encoded_words = []
    for word in words:
        if len(word) < 3:
            # Reverse short words
            encoded_words.append(word[::-1])
        else:
            # Generate random prefixes and suffixes
            pre = ''.join(random.choice(alpha) for _ in range(3))
            post = ''.join(random.choice(alpha) for _ in range(3))
            
            # Transform the word (move the first letter to the end)
            transformed_word = word[1:] + word[0]
            
            # Create the encoded word
            encoded_word = pre + transformed_word + post
            encoded_words.append(encoded_word)
    
    # Print the encoded message
    print("Encoded Message:", " ".join(encoded_words))

def decode():
    # Get user input
    message = input("ENTER THE ENCODED MESSAGE: ")
    
    # Split the message into words
    words = message.split()
    
    # Process each word
    decoded_words = []
    for word in words:
        if len(word) < 3:
            # Reverse short words
            decoded_words.append(word[::-1])
        else:
            # Remove random prefixes and suffixes
            core_word = word[3:-3]
            
            # Transform the word (move the last letter to the front)
            original_word = core_word[-1] + core_word[:-1]
            decoded_words.append(original_word)
    
    # Print the decoded message
    print("Decoded Message:", " ".join(decoded_words))

def main():
    print("WHAT DO YOU WANT TO DO?")
    print("1. ENCODE")
    print("2. DECODE")
    print("3. QUIT")
    
    while True:
        try:
            choice = int(input("\nENTER YOUR CHOICE: "))
            if choice == 1:
                coder()
            elif choice == 2:
                decode()
            elif choice == 3:
                break
            else:
                print("SORRY, YOU HAVE ENTERED THE WRONG VALUE. PLEASE TRY AGAIN.")
        except ValueError:
            print("INVALID INPUT. PLEASE ENTER A NUMBER.")
    
    print("THANK YOU FOR USING OUR MESSAGING SERVICE")

if __name__ == "__main__":
    main()
