import os
import re
import sys

for filenameOld in os.listdir(sys.argv[1]):
    m = re.match(r"(?P<pid>[a-zA-Z0-9]*)-(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})(?P<time>\d{4}).log", filenameOld)
    filenameNew =  m.group('year') + "-" + m.group('month') + "-" + m.group('day') + "_"+ m.group('time') + "_" + m.group('pid') + ".log"
    os.rename(os.path.join(sys.argv[1], filenameOld), os.path.join(sys.argv[1], filenameNew))
