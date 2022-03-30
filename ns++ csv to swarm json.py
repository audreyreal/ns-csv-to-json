# this is so bad but it works and only a few people will ever use it
from sys import path
import os

def main() -> None:
    csv_files = get_all_csv_files(path[0])
    json_file_list = [process_csv(file) for file in csv_files]
    json_file_list = sum(json_file_list, [])
    json_file_list = remove_duplicate_lines(json_file_list)
    json_file_list[-1] = json_file_list[-1].replace(",", "")  # remove trailing comma

    with open("config.json", "w", encoding="utf-8") as json_file:
        json_file.write("{")
        json_file.write('\n    "nations": {\n')
        json_file.write("\n".join(json_file_list))
        json_file.write("\n    }")
        json_file.write("\n}\n")

def remove_duplicate_lines(json_file_list: list) -> list:
    print("\n".join(json_file_list))
    lines_seen = set()
    for line in json_file_list:
        if line in lines_seen:
            json_file_list.remove(line)
        else:
            lines_seen.add(line)
    return json_file_list


def get_all_csv_files(root) -> list:
    # shamelessly stolen from geeksforgeeks
    # traverse whole directory
    csv_files = []
    for root, _, files in os.walk(root):
        # select file name
        csv_files.extend(
            os.path.join(file) for file in files if file.endswith('.csv')
        )
    return csv_files

def process_csv(file_name: str) -> list:
    with open(file_name, "r", encoding="utf-8") as csv_file:
        gay = csv_file.read()
    gay = gay.replace('Nation," ""Password"""', "")
    gay = gay.split("\n")
    json_file_list = []
    for line in gay:
        sanitized_line = (
            line.replace(',"', '":').replace('"""', '",').replace('""', '"')
        )
        if len(sanitized_line) > 6:
            json_file_list.append(f'        "{sanitized_line}')
    return json_file_list


if __name__ == "__main__":
    main()
