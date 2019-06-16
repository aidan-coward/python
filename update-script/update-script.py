import os
import subprocess
import glob

installed_pkg_list = list()

# make list of all pkgs in /home/aidan/abs that could be compilation targets
abs_pkg_list = list()
with os.scandir('/home/aidan/abs') as entries:
    for entry in entries:
        if entry.is_dir():
            abs_pkg_list.append(entry.name)

# create list of all installed pkgs 
installed_pkg_list = subprocess.check_output(['pacman', '-Qqs']).decode('ascii').splitlines()

# create list of installed pkgs that are to checked for updates
update_target_list = list()
for a in abs_pkg_list:
    if a in installed_pkg_list:
        update_target_list.append(a)

# check if any of the packages need to be updated

for target in update_target_list:

    # find current hash 
    current_dir= '/home/aidan/abs/' + target
    print(current_dir)
    current_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd= current_dir ).decode('ascii')
    print(current_hash)
    print('current url: ' + "https://aur.archlinux.org/" + target + ".git")

    # find new hash
    new_hash = subprocess.check_output(['git', 'ls-remote', ('https://aur.archlinux.org/' + target + '.git'), '|', 'grep', 'refs/heads/master', '|', 'cut', '-f', '-1'], cwd='/home/aidan/abs/' + target ).decode('ascii')

    # if hashes differ:
    # add pkg to list of compilation targets 
    # update git repo
    # download source files and dependencies
    if current_hash == new_hash:
        print("package " + target + " is up to date")

    else:
        print("package" + target + " is not up to date")
        compilation_target_list = list()
        compilation_target_list.append(target)
        
        # update here 
 
        # download source files + dependencies
        subprocess.run(['makepkg', '--verifysource', '--syncdeps'], cwd=current_dir)

# for each entry in compilation_target_list, prompt to check certain files with vim
# .install, .patch, PKGBUILD

types = ('PKGBUILD', '*.install', '*.patch')
for target in compilation_target_list:

    files_globbed = list()
    current_dir = '/home/aidan/abs/' + target

    os.chdir(current_dir)
    for files in types:
        files_globbed.append(glob.glob(files))

    print(files_globbed)

    for file in files_globbed:
        print("edit :" + file + " in package " + target + " ?" + " (Y/n)")

