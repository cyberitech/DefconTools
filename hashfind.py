import subprocess
import os
import sys


if __name__=="__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python3 {sys.argv[0]} [n_defcon] [date]\n\tExample: python3 {sys.argv[0]} 30 2023-08-15")
        print("\tThis will parse submodules at the path 30/uncategorized and checkout the latest commit hash as of date 2023-08-15")
        sys.exit(0)
    target = sys.argv[2]
    p = os.path.join(sys.argv[1],"uncategorized")
    print(f"moving into {p}")
    os.chdir(p)
    pkgs = os.listdir()
    for pkg in pkgs:
        print(f"Switching to {pkg}")
        os.chdir(pkg)
        process = subprocess.Popen(['git', 'log','--format=format:"%H"', f'--before={target}', '-1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        if process.returncode != 0:
            print(err.decode())
            print("exiting...")
            sys.exit(1)
        hash=out.decode().replace("\"",'')
        print(f"Package: {pkg} using hash {hash}")
        process = subprocess.Popen(['git', 'checkout', hash], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        if process.returncode != 0:
            print(err.decode())
            print("exiting...")
            sys.exit(1)
        print(out.decode())
        os.chdir("../")
        print(f"Backing out of {pkg}")
