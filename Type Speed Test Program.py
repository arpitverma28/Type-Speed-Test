#TYPING SPEED TEST PROGRAM

import time
def main():
    # Define the text for the typing test.
    text = "Type a few lines of code, You create an Organism."
    print("Type something about yourself as fast you can!")
    print("Test your typing skills ")
    print(text)
 # Record the start time.
    start_time = time.time()
# Get user input.
    user_input = input("Type the text and press Enter: ")
 # Record the end time.
    end_time = time.time()
 # Calculate the time taken to type.
    typing_time = end_time - start_time
 # Calculate the length of the sample text.
    text_length = len(text)
 # Calculate typing speed (characters per minute).
    typing_speed = (text_length / typing_time) * 60
 # Compare the user input to the original text.
    correct_characters = 0
    for s1, s2 in zip(user_input, text):
        if s1 == s2:
            correct_characters += 1
 # Calculate accuracy as a percentage.
    accuracy = (correct_characters / text_length) * 100
# Provide feedback.
    print("\nYou typed {} characters in {:.2f} seconds.".format(len(user_input), typing_time))
    print("Your typing speed is {:.2f} characters per minute.".format(typing_speed))
    print("Your accuracy is = {:.2f}".format(accuracy))

    if accuracy >= 85:
        print("You are an excellent typist.")
    elif accuracy >= 65:
        print("You have room for improvement.")
    else:
        print("Type the given text correctly to boost your accuracy.")


# Call the function
main()