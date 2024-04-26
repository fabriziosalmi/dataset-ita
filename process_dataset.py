def process_data(file_path):
    # Reading data and removing duplicates
    with open(file_path, 'r') as file:
        unique_lines = sorted(set(file.readlines()), key=str)

    # Sorting lines case-sensitively
    unique_lines.sort()

    # Writing back to dataset.txt
    with open(file_path, 'w') as file:
        file.writelines(unique_lines)

    # Prepare boundaries.log content and stats
    boundaries = {}
    starts_with_count = {}
    total_rows = len(unique_lines)

    for line in unique_lines:
        line_clean = line.strip()
        start_letter = line_clean[0]
        end_letter = line_clean[-1]

        # Update starts_with_count dictionary
        if start_letter in starts_with_count:
            starts_with_count[start_letter] += 1
        else:
            starts_with_count[start_letter] = 1

        # Update boundaries dictionary
        if start_letter not in boundaries:
            boundaries[start_letter] = {'first': line_clean, 'last': line_clean}
        else:
            boundaries[start_letter]['last'] = line_clean

        if end_letter not in boundaries:
            boundaries[end_letter] = {'first': line_clean, 'last': line_clean}
        else:
            boundaries[end_letter]['last'] = line_clean

    # Writing boundaries.log with additional stats
    with open('boundaries.log', 'w') as log:
        log.write(f"Total rows: {total_rows}\n")
        for letter, info in sorted(boundaries.items()):
            starts_with = starts_with_count.get(letter, 0)
            log.write(f"{letter}: First starts {info['first']}, Last starts {info['last']}, Total starts {starts_with}\n")

if __name__ == '__main__':
    process_data('dataset.txt')
