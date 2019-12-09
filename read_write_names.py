# Read the file

def reading_names(names):
    try:
        with open(names, 'r') as name_reading:
            lines = name_reading.readlines()
            for line in lines:
                print(line.strip('\n'))

    except FileNotFoundError as error:
        print('Check your file')
        print(error)

    finally:
        print('Execution done!')

reading_names('names.txt')

# Write in the file

def writing_names(names, item):
    try:
        with open(names, 'a') as names_to_write:
            names_to_write.write(item + '\n')

    except FileNotFoundError as error:
        print('Check your file')
        print(error)

    finally:
        print('Execution done!')

