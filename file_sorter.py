import os
import shutil

# Directory Information
source_directory = "Downloads"
destination_directories = {
    "Pictures": [".jpeg", ".png", ".jpg", ".gif"],
    "Documents": [".doc", ".txt", ".pdf", ".xlsx", ".docx", ".xls", ".rtf"],
    "Videos": [".mp4", ".mkv"],
    "Audio": [".mp3", ".wav", ".m4a"],
    "Applications": [".exe"],
    "Coding": [".c", ".py", ".java", ".cpp", ".js", ".html", ".css", ".php"],
}

# Create destination directories if they don't exist
for directory in destination_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Start sorting
print("Files being sorted")

for filename in os.listdir(source_directory):
    source_path = os.path.join(source_directory, filename)
    if os.path.isfile(source_path):
        for destination, extensions in destination_directories.items():
            for ext in extensions:
                if filename.endswith(ext):
                    destination_path = os.path.join(destination, filename)
                    shutil.move(source_path, destination_path)
                    break
        else:
            # If file type not recognized, move to 'Other' directory
            other_path = os.path.join("Other", filename)
            shutil.move(source_path, other_path)

print("Finished sorting")
