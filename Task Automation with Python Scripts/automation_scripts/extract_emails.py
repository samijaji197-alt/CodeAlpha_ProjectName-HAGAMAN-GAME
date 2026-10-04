import os
import re

# --- Configuration ---
INPUT_FILE = "input.txt"          # the .txt file to scan
OUTPUT_FILE = "emails_found.txt"  # where found emails are saved

# Regex pattern that matches most standard email addresses
EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


def read_file(filepath):
    """Read and return the contents of a text file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def extract_emails(text):
    """Return a sorted list of unique email addresses found in the text."""
    found = re.findall(EMAIL_PATTERN, text)
    unique_sorted = sorted(set(found))  # remove duplicates, sort alphabetically
    return unique_sorted


def save_emails(emails, filepath):
    """Write each email address on its own line in the output file."""
    with open(filepath, "w", encoding="utf-8") as f:
        for email in emails:
            f.write(email + "\n")


def main():
    print("=== Email Extractor ===\n")

    if not os.path.exists(INPUT_FILE):
        print(f"Input file '{INPUT_FILE}' not found in this folder.")
        print("Create a text file with that name (or change INPUT_FILE in the script) and try again.")
        return

    text = read_file(INPUT_FILE)
    emails = extract_emails(text)

    if not emails:
        print(f"No email addresses were found in '{INPUT_FILE}'.")
        return

    save_emails(emails, OUTPUT_FILE)

    print(f"Found {len(emails)} unique email address(es):")
    for email in emails:
        print(f"  - {email}")
    print(f"\nSaved to '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    main()
