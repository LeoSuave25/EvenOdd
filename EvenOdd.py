#Write a Python program that reads a text file named numbers.txt that contains 20 integers
with open('numbers.txt','r') as rawinput_text, open('even.txt','w') as output_even, open('odd.txt','w') as output_odd:
#The program will create two other text file the first text file will be named even.txt
# It will contains all even numbers extracted from the numbers.txt
    raw_numbers=rawinput_text.readlines()

    for line in raw_numbers:
        number = int(line.strip())
        if number % 2 == 0:
            output_even.write(str(number)+'\n')
#The second text file will be named odd.txt that will
#It will contain all odd numbers extracted from the numbers.txt
        else:
            output_odd.write(str(number)+'\n')