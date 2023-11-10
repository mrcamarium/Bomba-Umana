import os, threading

def create_large_file(file_path, desired_size_mb):
    desired_size_bytes = desired_size_mb * 1024 * 1024
    content = "A" * 1024
    with open(file_path, 'wb') as file:
        bytes_written = 0
        while bytes_written < desired_size_bytes:
            bytes_to_write = min(desired_size_bytes - bytes_written, len(content.encode()))
            file.write(content.encode()[:bytes_to_write])
            bytes_written += bytes_to_write

def create_files_in_threads(num_files, destination_directory, desired_size_mb):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    num_threads = min(num_files, os.cpu_count())
    files_per_thread = num_files // num_threads
    remainder_files = num_files % num_threads
    threads = []
    for thread_number in range(num_threads):
        num_files_for_thread = files_per_thread + 1 if thread_number < remainder_files else files_per_thread
        thread = threading.Thread(target=create_files, args=(thread_number, destination_directory, num_files_for_thread, desired_size_mb))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    print(f"{num_files} arquivos criados em '{destination_directory}' com {desired_size_mb} MB cada.")

def create_files(thread_number, destination_directory, num_files_for_thread, desired_size_mb):
    for i in range(num_files_for_thread):
        file_path = os.path.join(destination_directory, f"arquivo_thread{thread_number}_file{i + 1}.txt")
        create_large_file(file_path, desired_size_mb)

if __name__ == "__main__":
    num_files_to_create = 5
    destination_directory = "./arquivos_10mb"
    desired_size_mb = 10
    create_files_in_threads(num_files_to_create, destination_directory, desired_size_mb)