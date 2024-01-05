import os
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def choose_bird_image_file(directory, bird_name):
    dir=os.path.join(directory, bird_name)
    files = [f for f in os.listdir(dir)]
    if(files):
        return os.path.join(dir, random.choice(files))
    else:
        None

image_dir= './birds'
file_path = './info.txt'

observations = []
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if not line: continue
        bird_name, habit = line.split()
        try:
            result=choose_bird_image_file(image_dir, bird_name)
            # print(result)
            observations.append((bird_name, habit, result))
        except:
            print(f"dir for {bird_name} not found")

plt.ion()
correct=0
random.shuffle(observations)
print(f"loaded {len(observations)} questions")
for obs in observations:
    name,habit,image_file = obs
    img = mpimg.imread(image_file)
    imgplot = plt.imshow(img)
    plt.show()
    guess=input("name and habit? ")
    answer=" ".join([name, habit])
    if(guess=='stop'): break
    if(answer==guess):
        print("correct")
        correct+=1
    else:
        print(f"wrong! the correct answer is {answer}")
plt.ioff()
plt.close()
print(f"quiz done, you got {correct}/{len(observations)}")