import random

def coder():
    
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    

    message = input("ENTER YOUR MESSAGE: ")
    
    
    words = message.split()
    

    encoded_words = []
    for word in words:
        if len(word) < 3:
            
            encoded_words.append(word[::-1])
        else:
            
            pre = ''.join(random.choice(alpha) for _ in range(3))
            post = ''.join(random.choice(alpha) for _ in range(3))
            
        
            transformed_word = word[1:] + word[0]
            
        
            encoded_word = pre + transformed_word + post
            encoded_words.append(encoded_word)
    
    
    print("Encoded Message:", " ".join(encoded_words))

def decode():
    
    message = input("ENTER THE ENCODED MESSAGE: ")
    

    words = message.split()
    

    decoded_words = []
    for word in words:
        if len(word) < 3:
            
            decoded_words.append(word[::-1])
        else:
            
            core_word = word[3:-3]
            
            original_word = core_word[-1] + core_word[:-1]
            decoded_words.append(original_word)
    
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
