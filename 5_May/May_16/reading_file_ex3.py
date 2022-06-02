if __name__ == '__main__':

    with open("csv_values.txt") as file:
        content = file.read()
        print(content)

        #do not need file.close() to close file because this uses managers