
def get_order_statistic_from_input(input_string):
    # Remove any '{' and '}' characters from the input string
    clean_string = input_string.replace('{', '').replace('}', '')

    # Split the cleaned string based on ',' to separate the order statistic value and the list of numbers
    parts = clean_string.split(',')

    # The first part of the split string is the order statistic value 'k'
    k = int(parts[0].strip())

    # The remaining parts of the split string represent the numbers in the data set
    numbers = [int(num.strip()) for num in parts[1:]]

    # Sort the list of numbers in ascending order
    numbers.sort()

    # Return the kth smallest number from the sorted list (indexing starts from 0, so subtract 1 from k)
    return numbers[k-1]

def get_order_statistic_from_file(filename):
    # Open the file in read mode
    with open(filename, 'r') as f:
        # Read the file's contents and remove any leading or trailing white spaces
        input_string = f.read().strip()

        # Get the order statistic value using the earlier defined function
        return get_order_statistic_from_input(input_string)

if __name__ == "__main__":
    # Define the filename where our input is stored
    filename = 'input.txt'

    # Get the result by reading the input from the file and calculating the order statistic value
    result = get_order_statistic_from_file(filename)

    # Print the result
    print(result)
