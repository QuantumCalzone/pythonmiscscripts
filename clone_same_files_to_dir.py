from pythonutils.os_utils import *
import sys
import hashlib


# def return_str_array_stripped(str_array, to_strip):
#     index = 0
#     for str_array_entry in str_array:
#         str_array[index] = str_array_entry.replace(to_strip, '')
#         index += 1
#
#     return str_array


def file_to_hash(file_path):
    h = hashlib.sha256()
    b = bytearray(128 * 1024)
    mv = memoryview(b)
    with open(file_path, 'rb', buffering=0) as f:
        for n in iter(lambda: f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()


def get_paths_and_hashes(target_dir):
    paths = get_all_in_dir(target_dir, full_path=True, recursive=True, include_dirs=False, include_files=True)
    paths_and_hashes = []
    for entry in paths:
        if not entry.endswith('meta'):
            paths_and_hashes.append({'path': entry, 'hash': file_to_hash(entry)})

    return paths_and_hashes

path_a = '/Users/georgekatsaros/Projects/UnityFramework/ToProcess/zzzzzzInProg/V1'
path_b = '/Users/georgekatsaros/Projects/UnityFramework/ToProcess/zzzzzzInProg/V2/First'
path_same = '/Users/georgekatsaros/Desktop/Same'

a_paths_and_hashes = get_paths_and_hashes(path_a)
b_paths_and_hashes = get_paths_and_hashes(path_b)
longest_paths_and_hashes = []
shortest_paths_and_hashes = []

if len(a_paths_and_hashes) > len(b_paths_and_hashes):
    longest_paths_and_hashes = a_paths_and_hashes
    shortest_paths_and_hashes = b_paths_and_hashes
else:
    longest_paths_and_hashes = b_paths_and_hashes
    shortest_paths_and_hashes = a_paths_and_hashes

same_file_hashes = []
for path_and_hash_l in longest_paths_and_hashes:
    for path_and_hash_s in shortest_paths_and_hashes:
        if path_and_hash_l['hash'] == path_and_hash_s['hash']:
            same_file_hashes.append({'path': path_and_hash_l['path'], 'hash': path_and_hash_l['hash']})

for same_file_hash in same_file_hashes:
    sub_path = same_file_hash['path'].replace('/Users/georgekatsaros/Projects/UnityFramework/ToProcess/zzzzzzInProg/V2/First/', '')
    print(sub_path)

# a_file_paths = return_str_array_stripped(a_file_paths, path_a)
# b_file_paths = return_str_array_stripped(b_file_paths, path_b)

# same_file_paths = []

# for a_file_path in a_file_paths:
#     for b_file_path in b_file_paths:
#         if a_file_path == b_file_path and a_file_path not in same_file_paths:
#             same_file_paths.append(a_file_path)


# for same_file_path in same_file_paths:
#     print(same_file_path)