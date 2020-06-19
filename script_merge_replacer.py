from pythonutils.input_utils import *
from pythonutils.os_utils import *


def filter_for_scripts(all_paths):
    for target_path in all_paths:
        if not target_path.endswith(".cs"):
            all_paths.remove(target_path)
    return all_paths


def get_all_project_scripts_and_times(project_path):
    project_path_editor = os.path.join(project_path, "Editor")
    project_path_base = os.path.join(project_path, "Scripts")
    all_project_scripts = []
    all_project_editor_scripts = get_all_in_dir(target_dir=project_path_editor, full_path=True, recursive=True,
                                                include_dirs=False, include_files=True)
    project_base_scripts = get_all_in_dir(target_dir=project_path_base, full_path=True, recursive=True,
                                          include_dirs=False, include_files=True)
    all_project_scripts.extend(all_project_editor_scripts)
    all_project_scripts.extend(project_base_scripts)
    all_project_scripts = filter_for_scripts(all_project_scripts)

    all_project_scripts_and_times = {}
    all_project_script_names = []
    for all_project_script in all_project_scripts:
        all_project_script_time = os.path.getmtime(all_project_script)
        all_project_script_name = os.path.splitext(os.path.basename(all_project_script))[0]
        if all_project_script_name.endswith(".cs"):
            all_project_script_names.append(all_project_script_name)
            all_project_scripts_and_times[all_project_script_name] = {
                "path": all_project_script,
                "time": all_project_script_time,
            }
            # print("%s: %s" % (all_project_script_name, all_project_script_time))

    all_project_scripts_and_times_dict = {
        "scripts_and_times": all_project_scripts_and_times,
        "scripts": all_project_scripts,
        "names": all_project_script_names,
    }

    return all_project_scripts_and_times_dict


def get_duplicates(list_a, list_b):
    duplicates = []
    for entry in list_a:
        if entry in list_b:
            duplicates.append(entry)
    return duplicates


# project_a = stripped_input("Enter/paste the Assets path for Project A: ")
project_a = "C:\\Users\\georg\\Projects\\GlobalGameJam2020\\Assets"
# project_b = stripped_input("Enter/paste the Project B path: ")
project_b = "C:\\Users\\georg\\Projects\\UnityFramework\\Assets"

all_project_a_scripts_and_times = get_all_project_scripts_and_times(project_a)
all_project_b_scripts_and_times = get_all_project_scripts_and_times(project_b)
matching_script_names = get_duplicates(all_project_a_scripts_and_times["names"],
                                       all_project_b_scripts_and_times["names"])

for matching_script_name in matching_script_names:
    matching_script_a = all_project_a_scripts_and_times["scripts_and_times"][matching_script_name]
    matching_script_b = all_project_b_scripts_and_times["scripts_and_times"][matching_script_name]
    matching_script_a_time = matching_script_a["time"]
    matching_script_b_time = matching_script_b["time"]

    if matching_script_a_time > matching_script_b_time:
        print("%s is more recent than %s" % (matching_script_a["path"], matching_script_b["path"]))
    elif matching_script_b_time > matching_script_a_time:
        print("%s is more recent than %s" % (matching_script_b["path"], matching_script_a["path"]))
    else:
        print("idk about %s and %s" % (matching_script_a["path"], matching_script_b["path"]))


# if project A script is newer, replace, project, b
# vice versa
