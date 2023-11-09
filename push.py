#!/usr/bin/python3
from sys import argv
from os  import scandir, system

msg = argv[1]
def main():

    print(f"(*) git add .")
    system("git add .")
    print(f"(*) git commit -m \"{msg}\"")
    system(f"git commit -m \"{msg}\"")
    print("(*) git push")
    system("git push")

if __name__ == "__main__":
    main()
