import os
def make_bird_dirs():
    print("creating dirs according to info...")
    file_path = './info.txt'
    observations = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line: continue
            bird_name, habit = line.split()
            observations.append((bird_name, habit))

    for obs in observations:
        name,_=obs
        dir=f"./birds/{name}"
        if not os.path.exists(dir):
            os.makedirs(dir)
            print(f"created {dir}")

    print("bird image dir check done.")
            