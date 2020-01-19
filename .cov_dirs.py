from typing import List
import subprocess

IGNORED_DIRS: List[str] = [
    ".circleci/",
    # "sql_homework/",
    # "sql_homework/homeworks/",
]

git_output: List[str] = subprocess.check_output([
    "/usr/bin/git",
    "diff",
    "--dirstat=files",
    "@..origin/master"
]).decode().strip().split("\n")

cov_folder_list = []
for changed_dir in git_output:
    if changed_dir:
        folder = changed_dir.split()[1]
        if folder not in IGNORED_DIRS:
            cov_folder_list.append(f"--cov={folder}")

cov_folder_str: str = " ".join(cov_folder_list)
if cov_folder_str:
    print(cov_folder_str + " --no-cov-on-fail --cov-fail-under=80")
