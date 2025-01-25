# input sentence
user_input = input("Enter sentence of your choice: ")

# output sentence details
print(len(user_input))
word_count = len(user_input.split())
print(word_count)
first_word = user_input.split()[0]
last_word = user_input.split()[-1]
print(f"first word: {first_word}, last word: {last_word}")

# indexing and splicing
first_three_chars = user_input[:3]
last_three_chars = user_input[-3:]
print(first_three_chars, last_three_chars)
input_reversed = user_input[::-1]
print(input_reversed)

# modify the sentence
print(user_input.upper())
print(user_input.lower())
print(user_input.replace(" ", "-"))