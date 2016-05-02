"""
Example usage of flamegraph.

To view a flamegraph run these commands:
$ python example.py
$ flamegraph.pl perf.log > perf.svg
$ inkview perf.svg
"""

import time
import sys
import flamegraph

def foo():
    time.sleep(.1)
    bar()

def bar():
    time.sleep(.05)

if __name__ == "__main__":
    flamegraph.start_profile_thread(fd=open("./perf.log", "w"))

    N = 10
    for x in xrange(N):
        print "{}/{}".format(x, N)
        foo()
