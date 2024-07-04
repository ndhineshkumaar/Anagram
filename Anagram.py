def are_anagrams(str1, str2):
    # Remove any spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)

# Get user input
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

# Check if the input words are anagrams and print the result
if are_anagrams(word1, word2):
    print(f"'{word1}' and '{word2}' are anagrams.")
else:
    print(f"'{word1}' and '{word2}' are not anagrams.")
