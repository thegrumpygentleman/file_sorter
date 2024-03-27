# File Sorter

File Sorter is a Python script designed to organize files in a specified directory based on their file types. It categorizes files into different folders such as Pictures, Documents, Videos, Audio, Applications, Coding, and Other.

## Features
- Automatically sorts files into appropriate folders based on their file extensions.
- Handles common file types for images, documents, videos, audio, applications, and coding files.
- Creates destination directories if they don't exist.

## Requirements
- Python 3.x
- `os` module
- `shutil` module

## Usage
1. Clone the repository or download the `file_sorter.py` script.
2. Customize the `source_directory` variable to specify the directory containing the files you want to sort.
3. Run the script using Python: `python file_sorter.py`.
4. The script will organize the files into respective folders within the source directory.

## Configuration
- Modify the `destination_directories` dictionary to add or remove file types and corresponding destination folders as needed.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
