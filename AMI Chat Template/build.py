import os, sys, re

filename = sys.argv[1]
subject, file = filename.split('/')[-2:]
file, ext = file.split('.')

if ext != 'tex': exit()

depends = []
log = open("log.txt", "w")
with open(filename, 'r') as input_file:
    log.write(f"preprocessing {filename}...\n")
    content = input_file.read()
    depends = re.findall(r'(?<=\\input\{)py/.*?(?=\})', content)
    for sss in depends:
        os.popen(f"python3 ./{sss}.py > ./{sss}.tex").read()
    input_file.close()

output_file = f"{subject}-{file}"
output_dir = "build"

log.write(output_file + "\n")

LATEX_CMD = "pdflatex --shell-escape"
LATEX_CMD += f" -output-directory={output_dir}/"
LATEX_CMD += f" -jobname={output_file}"
LATEX_CMD += f" {filename} < /dev/null > {output_dir}/{subject}.log"

TEXINPUTS = "TEXINPUTS=.:tex/:"
BUILD_CMD = f"{TEXINPUTS} {LATEX_CMD}"
TRASH_PREFIX = f"{output_dir}/{output_file}"

TRASH_SUFFIX = [".aux", ".log", ".out", ".snm", ".nav", ".toc"]
TRASH = " ".join([TRASH_PREFIX + suf for suf in TRASH_SUFFIX])
#TRASH += " " + " ".join([f"./py/{x}.tex" for x in depends])
log.write(f"{BUILD_CMD}\n")

os.popen(BUILD_CMD).read()
os.popen(f"rm {TRASH}")