import os
import sys

def print_tree(directory, indent=''):
    """Print directory tree recursively"""
    items = os.listdir(directory)
    for item in items:
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            print(indent + item + '/')
            print_tree(item_path, indent + '  ')
        else:
            print(indent + item)

def main():
    if len(sys.argv) != 2:
        print("Usage: python dir_tree.py <directory_path>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.exists(directory) or not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory path.")
        sys.exit(1)

    print_tree(directory)

if __name__ == "__main__":
    main()