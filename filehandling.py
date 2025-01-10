def count_words_in_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
        words = content.split()
        word_count = len(words)
        with open(output_file, 'w') as file:
            file.write(f"The number of words in the file is: {word_count}\n")
        print(f"Word count successfully written to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_file = input("Enter the path of the input text file: ")
output_file = input("Enter the path for the output file: ")
count_words_in_file(input_file, output_file)
