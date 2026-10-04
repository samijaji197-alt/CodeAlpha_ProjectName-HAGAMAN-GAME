import os
import shutil

# --- Configuration ---
SOURCE_FOLDER = "source_folder"        # folder to scan for .jpg files
DESTINATION_FOLDER = "jpg_files"       # folder where .jpg files will be moved


def ensure_destination_exists(folder):
    """Create the destination folder if it doesn't already exist."""
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Created destination folder: '{folder}'")


def find_jpg_files(folder):
    """Return a list of .jpg / .jpeg filenames found directly in the folder."""
    jpg_files = []
    for filename in os.listdir(folder):
        full_path = os.path.join(folder, filename)
        if os.path.isfile(full_path) and filename.lower().endswith((".jpg", ".jpeg")):
            jpg_files.append(filename)
    return jpg_files


def move_files(filenames, source_folder, destination_folder):
    """Move each file from source_folder to destination_folder."""
    moved_count = 0
    for filename in filenames:
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(destination_folder, filename)

        # Avoid overwriting a file that already exists at the destination
        if os.path.exists(dst_path):
            print(f"Skipped '{filename}' (already exists in destination).")
            continue

        shutil.move(src_path, dst_path)
        print(f"Moved: {filename}")
        moved_count += 1
    return moved_count


def main():
    print("=== JPG File Mover ===\n")

    if not os.path.exists(SOURCE_FOLDER):
        print(f"Source folder '{SOURCE_FOLDER}' not found.")
        print("Create it (or change SOURCE_FOLDER in the script) and add some .jpg files, then try again.")
        return

    ensure_destination_exists(DESTINATION_FOLDER)

    jpg_files = find_jpg_files(SOURCE_FOLDER)

    if not jpg_files:
        print(f"No .jpg files found in '{SOURCE_FOLDER}'.")
        return

    print(f"Found {len(jpg_files)} .jpg file(s). Moving now...\n")
    moved_count = move_files(jpg_files, SOURCE_FOLDER, DESTINATION_FOLDER)

    print(f"\nDone. Moved {moved_count} file(s) to '{DESTINATION_FOLDER}'.")


if __name__ == "__main__":
    main()
