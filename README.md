# goit-pythonweb-hw-04

# Async File Sorter

An asynchronous Python application that sorts files by their extensions into organized subdirectories. This tool efficiently processes large numbers of files concurrently, making file organization fast and reliable.

## Features

- **Asynchronous Processing**: Uses Python's `asyncio` for concurrent file operations
- **Extension-based Sorting**: Automatically organizes files into folders based on their file extensions
- **Conflict Resolution**: Handles duplicate filenames by adding numeric suffixes
- **Comprehensive Logging**: Logs operations to both file and console
- **Error Handling**: Robust error handling for file operations and edge cases
- **Recursive Processing**: Processes all files in subdirectories recursively

## Installation

1. Clone or download this repository
2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

```bash
python3 main.py <source_folder> <output_folder>
```

### Examples

1. **Sort files from Documents to SortedFiles:**

   ```bash
   python3 main.py ~/Desktop/m-power ~/Desktop/sorted-files
   ```

2. **Sort files with absolute paths:**

   ```bash
   python3 main.py /path/to/messy/folder /path/to/organized/folder
   ```

3. **Sort current directory files:**
   ```bash
   python3 main.py . ./sorted_files
   ```

### Arguments

- `source`: Path to the source folder containing files to sort
- `output`: Path to the output folder where sorted files will be placed

## How It Works

1. **Scanning**: The application recursively scans the source folder for all files
2. **Extension Detection**: Each file's extension is extracted (files without extensions go to 'no_extension' folder)
3. **Directory Creation**: Creates subdirectories in the output folder based on file extensions
4. **Asynchronous Copying**: Files are copied concurrently using async operations
5. **Conflict Resolution**: If files with the same name exist, numeric suffixes are added (e.g., `file_1.txt`, `file_2.txt`)

## Output Structure

The application organizes files into the following structure:

```
output_folder/
├── txt/
│   ├── document1.txt
│   └── document2.txt
├── jpg/
│   ├── photo1.jpg
│   └── photo2.jpg
├── pdf/
│   ├── manual.pdf
│   └── report.pdf
├── no_extension/
│   └── README
└── ...
```

## Logging

The application creates detailed logs in two locations:

- **Console output**: Real-time progress and status updates
- **Log file**: `file_sorter.log` in the current directory with detailed operation history

Log entries include:

- Successful file copies with source and destination paths
- Error messages for failed operations
- Process start and completion notifications

## Error Handling

The application handles various error scenarios:

- Non-existent source folders
- Permission issues
- File access errors during copying
- Invalid path specifications

## Performance

The async implementation allows for:

- Concurrent file operations
- Efficient processing of large file collections
- Non-blocking I/O operations
- Scalable performance based on system resources

## Example Output

```
2025-06-07 17:01:49,876 - INFO - Starting file sorting from /Users/admin/Desktop/m-power to /Users/admin/Desktop/sorted-files
2025-06-07 17:01:49,881 - INFO - Copied /Users/admin/Desktop/m-power/other/Ковальчук_РА.zip to /Users/admin/Desktop/sorted-files/zip/Ковальчук_РА.zip
2025-06-07 17:01:49,882 - INFO - Copied /Users/admin/Desktop/m-power/other/Одноразова рада.txt to /Users/admin/Desktop/sorted-files/txt/Одноразова рада.txt
2025-06-07 17:01:49,882 - INFO - Copied /Users/admin/Desktop/m-power/Ковальчук_РА.zip to /Users/admin/Desktop/sorted-files/zip/Ковальчук_РА.zip
2025-06-07 17:01:49,882 - INFO - Copied /Users/admin/Desktop/m-power/.DS_Store to /Users/admin/Desktop/sorted-files/no_extension/.DS_Store
2025-06-07 17:01:49,882 - INFO - Copied /Users/admin/Desktop/m-power/Знімок екрана 2025-04-05 о 17.20.06.png to /Users/admin/Desktop/sorted-files/png/Знімок екрана 2025-04-05 о 17.20.06.png
2025-06-07 17:01:49,883 - INFO - File sorting completed
```

## Troubleshooting

### Common Issues

1. **Permission Denied**

   - Ensure you have read permissions for the source folder
   - Ensure you have write permissions for the output folder

2. **Module Not Found Error**

   - Install the required dependencies: `pip install -r requirements.txt`

3. **Source Folder Not Found**
   - Verify the source folder path exists and is accessible
   - Use absolute paths if relative paths cause issues

### Getting Help

If you encounter issues:

1. Check the `file_sorter.log` file for detailed error messages
2. Ensure all file paths are valid and accessible
3. Verify Python version compatibility (3.7+)

## License

This project is open source and available under the MIT License.
