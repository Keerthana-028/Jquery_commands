#  The python script reads a JSON file, extracts the data, and
#  prints its output.
import json


def process_json_data(json_data):
    """

    Processes student data from a JSON object and prints each students data.

    """
    print("Processing the Students Data:\n")
    for student in json_data['students']:
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Department: {student['department']}\n")


def load_json_file(file_path):
    """
    Loads JSON data from the specified file.

    """
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' is not valid JSON.")
        return None


if __name__ == "__main__":
    file_path = 'student_data.json'

    json_data = load_json_file(file_path)

    if json_data:
        process_json_data(json_data)
