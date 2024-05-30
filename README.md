# FuckParsing
Offensive Security Tools

Created by Krypt0n https://offensivesec.blogspot.com/

This repository contains a Python script designed to parse logs containing `url:user:pass` information. These logs can be used for advanced attacks on applications. The extracted data is stored using Google Drive for easy access and management.

Disclaimer: This information is provided solely for educational purposes. The author is not responsible for any misuse of this knowledge.

How to Use
Clone the repository:
   ```bash
   git clone https://github.com/OffSec30/FuckParsing.git
   cd FuckParsing
   ```

Install dependencies:
   Ensure you have Python installed. Install any required dependencies if necessary.

Run the script:
   ```bash
   python FuckParsing.py
   ```

Script Overview

The script performs the following tasks:

Lists all `.txt` files in a specified directory.
Reads lines from these files randomly without repetition.
Extracts URLs using regex patterns.
Saves the extracted results to a designated file.

Functions

list_txt_files(directory): Lists all `.txt` files in the specified directory.
read_random_file(files, directory): Reads lines from a randomly selected `.txt` file.
find_pattern(line, pattern): Finds all occurrences of a given pattern in a line.
save_results(destination_file, results, file_name): Saves the found results to the specified file.

Example Usage

See the script for detailed implementation.

Download Logs

You can download the relevant logs [here](https://github.com/fastfire/deepdarkCTI/blob/main/telegram_infostealer.md).

