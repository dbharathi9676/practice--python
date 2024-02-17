import os
import threading


def list_files_and_folders(directory):
    print("Listing all folders, subfolders, text files, and CSV files in:", directory)
    for dirpath , _, filenames in os.walk(directory):
        for folder_name in _:
            fold_path = os.path.join(dirpath, folder_name)
            print(fold_path)
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            print(file_path)



def count_word_frequency(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
        word_frequency = {}
        for word in words:
            word = word.lower()
            word_frequency[word] = word_frequency.get(word, 0) + 1
        return word_frequency


def encrypt_capital_letters(file_path, encryption_value):
    with open(file_path, 'r') as file:
        content = file.read()
        encrypted_content = ''.join([chr((ord(char) - ord('A') + encryption_value) % 26 + ord('A'))
                                     if 'A' <= char <= 'Z' else char for char in content])

    encrypted_file_path = file_path.replace('.txt', '_encrypted.txt')
    with open(encrypted_file_path, 'w') as encrypted_file:
        encrypted_file.write(encrypted_content)

    print(f"Encryption completed for {file_path}. Encrypted file saved at {encrypted_file_path}")


def main():
    directory_path = input("Enter the directory path: ")
    list_files_and_folders(directory_path)

    word_frequency_dict = {}
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(('.txt', '.csv')):
                file_path = os.path.join(root, file)
                word_frequency_dict[file_path] = count_word_frequency(file_path)

    for file_path, word_frequency in word_frequency_dict.items():
        print(f"Word frequency in {file_path}: {word_frequency}")

    encryption_value = int(input("Enter the encryption value: "))

    threads = []
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                thread = threading.Thread(target=encrypt_capital_letters, args=(file_path, encryption_value))
                thread.start()
                threads.append(thread)

    for thread in threads:
        thread.join()

    print("Encryption performed successfully.")


if __name__ == "__main__":
    main()

