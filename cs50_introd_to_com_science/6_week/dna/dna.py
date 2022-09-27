import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py databases/FILENAME.csv sequences/FILENAME.txt")
        sys.exit(1)
    try:
        file = open(f"{sys.argv[1]}")
        file1 = open(f"{sys.argv[2]}")
        file.close()
        file1.close()
    except:
        sys.exit("File not found")

    # TODO: Read database file into a variable
    database = []
    with open(f"{sys.argv[1]}", 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        subsequences = reader.fieldnames[1:]
        for row in reader:
            database.append(row)
    # TODO: Read DNA sequence file into a variable
    txtfile = open(f"{sys.argv[2]}")
    dna = txtfile.read()
    # TODO: Find longest match of each STR in DNA sequence
    longest_run = {}
    for seq in subsequences:
        longest_run[seq] = longest_match(dna, seq)
    # TODO: Check database for matching profiles
    for person in database:
        if match(subsequences, longest_run, person):
            print(person['name'])
            return
    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


def match(subsequences, strs_dna, person):
    for subsequence in subsequences:
        if strs_dna[subsequence] != int(person[subsequence]):
            return False
    return True


main()

