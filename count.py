import os

def count_ext(folder_path, extension):
    count = 0
    for filename in os.listdir(folder_path):
        if filename.endswith(extension):
            count += 1
    return count

folder_path = "C:\\Users\\DEEPIKA LAKSHMI\\Desktop"

csv_count = count_ext(folder_path, ".csv")
txt_count = count_ext(folder_path, ".txt")

print(f"Number of .csv files: {csv_count}")
print(f"Number of .txt files: {txt_count}")
