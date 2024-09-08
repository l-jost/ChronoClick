import subprocess
import os
import sys

def get_modified_files(extension):
    """Get list of files modified in the last commit with a specific extension."""
    try:
        result = subprocess.check_output(
            ['git', 'diff', '--name-only', 'main', 'HEAD', f'*.{extension}']
        )
        return result.decode('utf-8').splitlines()
    except subprocess.CalledProcessError:
        print(f"Error: Failed to get modified {extension} files.")
        sys.exit(1)

def get_last_modified_time(file_path):
    """Get the last commit timestamp for a specific file."""
    try:
        result = subprocess.check_output(
            ['git', 'log', '-1', '--format=%at', '--', file_path]
        )
        return int(result.decode('utf-8').strip())
    except subprocess.CalledProcessError:
        print(f"Error: Failed to get last modified time for {file_path}.")
        sys.exit(1)

def check_pdf_updates():
    # Get modified .schdoc and .pdf files
    schdoc_files = get_modified_files('SchDoc')
    pdf_files = get_modified_files('pdf')

    if not schdoc_files:
        print("No .schdoc files were modified. Skipping check.")
        sys.exit(0)

    print(f"Modified .schdoc files: {schdoc_files}")

    for schdoc in schdoc_files:
        folder = os.path.dirname(schdoc)

        # Find corresponding .pdf file in the same folder
        corresponding_pdf = None
        for pdf in pdf_files:
            if os.path.dirname(pdf) == folder:
                corresponding_pdf = pdf
                break

        if not corresponding_pdf:
            print(f"Error: No .pdf file found in the folder for {schdoc}.")
            sys.exit(1)

        # Compare last modification times
        schdoc_mod_time = get_last_modified_time(schdoc)
        pdf_mod_time = get_last_modified_time(corresponding_pdf)

        if pdf_mod_time < schdoc_mod_time:
            print(f"Error: {corresponding_pdf} has not been updated after {schdoc}.")
            sys.exit(1)

    print("Success: All .pdf files are updated after their corresponding .schdoc files.")

if __name__ == "__main__":
    check_pdf_updates()
