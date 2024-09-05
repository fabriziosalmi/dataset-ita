import re
from collections import defaultdict

def process_data(file_path):
    # Define a regex pattern to match lines containing only alphabetical characters
    pattern = re.compile(r'^[a-zA-Z]+$')

    # Read data and filter lines based on the regex
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip() and pattern.match(line.strip())]

    # Remove duplicates and sort the lines case-sensitively
    unique_lines = sorted(set(lines), key=str)

    # Write back to dataset.txt
    with open(file_path, 'w') as file:
        file.writelines(f"{line}\n" for line in unique_lines)

    # Initialize dictionaries for stats using defaultdict
    starts_with_count = defaultdict(int)
    ends_with_count = defaultdict(int)
    longest_words_start = {}
    first_words = {}
    last_words = {}

    # Collect statistics
    for line in unique_lines:
        if line:
            start_letter = line[0]
            end_letter = line[-1]

            # Count items starting with each letter
            starts_with_count[start_letter] += 1

            # Count items ending with each letter
            ends_with_count[end_letter] += 1

            # Track longest word starting with each letter
            if start_letter not in longest_words_start or len(line) > len(longest_words_start[start_letter]):
                longest_words_start[start_letter] = line

            # Track first word starting with each letter
            if start_letter not in first_words or line < first_words[start_letter]:
                first_words[start_letter] = line

            # Track last word starting with each letter
            if start_letter not in last_words or line > last_words[start_letter]:
                last_words[start_letter] = line

    # Write statistics to boundaries.log
    with open('boundaries.log', 'w') as log:
        log.write(f"Total rows: {len(unique_lines)}\n")
        for letter in sorted(set(starts_with_count) | set(ends_with_count)):
            log.write(
                f"{letter}: Starts {starts_with_count[letter]}, "
                f"Ends {ends_with_count[letter]}, "
                f"Longest {longest_words_start.get(letter, 'N/A')}, "
                f"First {first_words.get(letter, 'N/A')}, "
                f"Last {last_words.get(letter, 'N/A')}\n"
            )

if __name__ == '__main__':
    process_data('dataset.txt')
