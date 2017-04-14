#!/usr/bin/env python2


__author__ = 'Taylor Lee'
__email__  = 'tdlee2@wisc.edu'


import os
import sys
import time

# Assumptions from looking at the example output, I am assuming we should only print out the data of regular files, and hence only directories that have regular files


def recursive_ls(dir_name, relative_path = ''):

    os.chdir(dir_name)
    file_list = os.listdir(os.getcwd())
    dir_list = []
    for file_name in file_list:
        if not os.path.isfile(file_name):
            if os.path.isdir(file_name):
                dir_list.append(file_name)
            else:
                print 'Dectected file that is neither regular nor a directory'
                print 'Terminating...'
                sys.exit(1)

    if len(dir_list) < len(file_list):  # If our current directory has regular files, create output

        print 'Directory <' + str(os.path.join(relative_path, dir_name)) + '>'

        file_list = sorted(file_list, key = lambda file_name: os.path.getsize(os.getcwd() +'/'+ file_name), reverse = True)
        for file_name in file_list:
            if file_name not in dir_list:
                time_struct = time.gmtime(os.path.getmtime(file_name))
                time_string = time.strftime('%Y-%m-%d %H:%M:%S', time_struct)
                print '{:>12}'.format(str(os.path.getsize(file_name))) + ' ' * 3 + time_string + ' ' * 3 + file_name

        print ''

    for directory in dir_list:
        recursive_ls(directory, os.path.join(relative_path, dir_name)) # Recursive call
    os.chdir('..')

def main():
    recursive_ls(sys.argv[1])

if __name__ == '__main__':
    main()
