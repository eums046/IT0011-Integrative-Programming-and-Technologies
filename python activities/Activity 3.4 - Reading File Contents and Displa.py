try:
    with open("students.txt", "r") as file:
        contents = file.read()
 
        print("Reading Student Information:")
        print(contents)
except FileNotFoundError:
    print("Error: The file 'students.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")