import inflect

def number_to_words(number):
    p = inflect.engine()
   
    # Convert the number to words
    words = p.number_to_words(number)

        # Print the result
    print(f"The words representation of {number} is: {words}")   
n=input()
number_to_words(n)

