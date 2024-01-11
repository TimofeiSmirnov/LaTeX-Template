import os, sys

subject = sys.argv[1]
file = sys.argv[2]

os.popen(f"cp {subject}/template.txt {subject}/{file}.tex").read()