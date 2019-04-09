#!/usr/bin/env python2

import sys
import struct


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])
curr = 0;
if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
curr += 8
time = struct.unpack("<L", data[curr:curr+4])[0]
print("timestamp: %s" % int(time))
curr+= 4
a1,a2,a3,a4,a5,a6,a7,a8 = struct.unpack("<cccccccc", data[curr:curr+8])
print("author: %s" % a1)
print("author: %s" % a2)
print("author: %s" % a3)
print("author: %s" % a4)
print("author: %s" % a5)
print("author: %s" % a6)
curr += 8
sectionCount = struct.unpack("<L", data[curr:curr+4])[0]
print("section count: %s" % int(sectionCount))
curr += 4

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
s1t = struct.unpack("<L", data[curr:curr+4])[0]
print("stype1: %s" % hex(s1t))
curr += 4
s1l = struct.unpack("<L", data[curr:curr+4])[0]
print("slen1: %s" % s1l)
curr += 4
s1v = struct.unpack("<LLLLLL", data[curr:curr+24])[0]
print("sval1: %s" % s1v)
curr += 24
s2t = struct.unpack("<L", data[curr:curr+4])[0]
print("stype2: %s" % hex(s2t))
curr += 4
s2l = struct.unpack("<L", data[curr:curr+4])[0]
print("slen2: %s" % s2l)
curr += 4
s2vlat, s2vlong = struct.unpack("<dd", data[curr:curr+16])
print("sval2lat: %s" % float(s2vlat))
print("sval2long: %s" % float(s2vlong))
curr += 16
s3t = struct.unpack("<L", data[curr:curr+4])[0]
print("stype3: %s" % hex(s3t))
curr += 4
s3l = struct.unpack("<L", data[curr:curr+4])[0]
print("slen3: %s" % s3l)
curr += 4
s3v = struct.unpack("<L", data[curr:curr+4])[0]
print("sval3: %s" % int(s3v))
curr += 202776
s4t = struct.unpack("<L", data[curr:curr+4])[0]
print("stype4: %s" % hex(s4t))
curr += 4
s4l = struct.unpack("<L", data[curr:curr+4])[0]
print("slen4: %s" % s4l)
curr += 4
s4v = struct.unpack("<LLLLLLLLLLL", data[curr:curr+44]) [0]
print("sval4: %s" % s4v)
curr += 44
s5t = struct.unpack("<L", data[curr:curr+4])[0]
print("stype5: %s" % hex(s5t))
curr += 4
s5l = struct.unpack("<L", data[curr:curr+4])[0]
print("slen5: %s" % s5l)
curr += 4