from pathlib import Path
from pythonutils.input_utils import *
from pythonutils.os_utils import *
from shutil import rmtree

# first run this on your upm branch
# git reset --hard master

print("")
input_project_path = stripped_input("Enter/paste the target path: ")
# input_project_path = "/Users/georgekatsaros/Projects/UnityFramework"
print("")

names_to_ignore = {
    ".git",
    ".gitattributes",
    ".DS_Store",
    "Assets",
    "package.json",
    "package.json.meta",
}

top_level_project_files = get_all_in_dir(input_project_path)
for top_level_project_file in top_level_project_files:
    top_level_project_file_name = os.path.basename(top_level_project_file)

    # delete the file if its not to be destroyed
    if top_level_project_file_name not in names_to_ignore:
        print(f"deleted: {top_level_project_file_name}")

        if os.path.isdir(top_level_project_file):
            rmtree(top_level_project_file)
        else:
            os.remove(top_level_project_file)

# move contents of assets to dir above
assets_path = Path(input_project_path) / "Assets"
assets_sub_paths = get_all_in_dir(assets_path)

for assets_sub_path in assets_sub_paths:
    assets_sub_path_name = os.path.basename(assets_sub_path)
    print(f"moving: {assets_sub_path_name}")

    assets_sub_path_new_path = Path(assets_sub_path)
    assets_sub_path_new_path = assets_sub_path_new_path.parent
    assets_sub_path_new_path = assets_sub_path_new_path.parent
    assets_sub_path_new_path = assets_sub_path_new_path / os.path.basename(assets_sub_path)
    # print(f"{assets_sub_path} -> {assets_sub_path_new_path}\n")
    os.rename(assets_sub_path, assets_sub_path_new_path)

os.rmdir(assets_path)

print("")
print("Done!")
