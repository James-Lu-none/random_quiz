import os

def rename_files(directory_path, old_extension, new_extension):
    for filename in os.listdir(directory_path):
        if filename.endswith(old_extension):
            old_filepath = os.path.join(directory_path, filename)
            new_filename = os.path.splitext(filename)[0] + new_extension
            new_filepath = os.path.join(directory_path, new_filename)
            os.rename(old_filepath, new_filepath)
            print(f"Renamed: {old_filepath} -> {new_filepath}")

def rename_files_extension():
    print("unifing image file extension...")
    image_dir= './birds'
    file_path = './info.txt'
    observations = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line: continue
            bird_name, habit = line.split()
            observations.append((bird_name, habit))

    for obs in observations:
        name,_= obs
        try:
            directory_path = os.path.join(image_dir,name)
            old_extension = '.jfif'
            new_extension = '.jpg'

            rename_files(directory_path, old_extension, new_extension)
        except:
            print(f"{directory_path} not found")
            continue
    print("extension modification done.")