#Write a Python program that reads a text file named numbers.txt that contains 20 integers
with open('numbers.txt','r') as rawinput_text, open('even.txt','a') as output_even, open('odd.txt','a') as output_odd:
#The program will create two other text file the first text file will be named even.txt
# It will contains all even numbers extracted from the numbers.txt
    raw_numbers=rawinput_text.readlines()

    for line in raw_numbers:
        if int(line) % 2 == 0:
            output_even.write(line)
#The second text file will be named odd.txt that will
#It will contain all odd numbers extracted from the numbers.txt