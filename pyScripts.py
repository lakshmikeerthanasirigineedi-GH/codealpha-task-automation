import os
import shutil
source_folder = "source"
destination_folder = "destination"
count = 0
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
files = os.listdir(source_folder)
for file in files:
    if file.endswith((".jpg", ".png")):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)
        try:
            shutil.move(source_path, destination_path)
            count += 1

            print(f"Moved: {file}")

        except Exception as e:
            print(f"Error moving {file}: {e}")

print(f"\nTotal files moved: {count}")
print("Task completed successfully!")