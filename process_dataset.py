import re

def process_data(file_path):
    # Define a regex pattern to match lines containing only alphabetical characters
    pattern = re.compile(r'^[a-zA-Z]+$')

    # Read data and filter lines based on the regex
    with open(file_path, 'r') as file:
        lines = file.readlines()
    filtered_lines = [line.strip() for line in lines if line.strip() and pattern.match(line.strip())]

    # Remove duplicates and sort the lines case-sensitively
    unique_lines = sorted(set(filtered_lines), key=str)

    # Writing back to dataset.txt
    with open(file_path, 'w') as file:
        file.writelines(line + '\n' for line in unique_lines)

    # Initialize dictionaries for stats
    starts_with_count = {}
    ends_with_count = {}
    longest_words_start = {}

    # Collect statistics
    for line in unique_lines:
        if line:  # Ensure line is not empty
            start_letter = line[0]
            end_letter = line[-1]

            # Count items starting with each letter
            starts_with_count[start_letter] = starts_with_count.get(start_letter, 0) + 1

            # Count items ending with each letter
            ends_with_count[end_letter] = ends_with_count.get(end_letter, 0) + 1

            # Track longest word starting with each letter
            if start_letter not in longest_words_start or len(line) > len(longest_words_start[start_letter]):
                longest_words_start[start_letter] = line

    # Write to boundaries.log with additional stats
    with open('boundaries.log', 'w') as log:
        log.write(f"Total rows: {len(unique_lines)}\n")
        for letter in sorted(set(starts_with_count.keys()).union(ends_with_count.keys())):
            starts = starts_with_count.get(letter, 0)
            ends = ends_with_count.get(letter, 0)
            longest_word = longest_words_start.get(letter, 'N/A')
            log.write(f"{letter}: Starts {starts}, Ends {ends}, Longest {longest_word}\n")

if __name__ == '__main__':
    process_data('dataset.txt')
