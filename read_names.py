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