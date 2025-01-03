def find_anagrams(dictionary_file):
    # Initialize the HashMap
    anagrams = {}

    # Read all words from the dictionary
    with open(dictionary_file, 'r') as file:
        for word in file:
            word = word.strip()  # Remove extra spaces/newlines
            # Sort the characters in the word to form the key
            key = ''.join(sorted(word))
            # Add the word to the appropriate group in the HashMap
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)

    return anagrams

# Example usage to find the largest anagram group
anagrams = find_anagrams("Dictionary.txt")

# Find the key with the largest group of anagrams
largest_group_key = max(anagrams, key=lambda k: len(anagrams[k]))
largest_group = sorted(anagrams[largest_group_key])

# Output the results
print(f"Largest anagram group ({len(largest_group)} words): {', '.join(largest_group)}")


anagrams = find_anagrams("Dictionary.txt")
result = sorted(anagrams['eilnst'])
print(", ".join(result))  # Output in alphabetical order

