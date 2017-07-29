#!/usr/bin/env python

import sys
import collections
import argparse

IGNORED = ("MAINTAINER", "FROM")
def nextline(deq):
    s = deq.popleft()
    return s


def parse_multiline(deq, prefix=""):
    s = nextline(deq)
    while True:
        if s.endswith("\\"):
            prefix = prefix + "\n" + s
            s = nextline(deq)
        else:
            return prefix + s


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert Dockerfile into shell script')
    parser.add_argument('--copy-prefix-url', dest="copy_prefix", action="store")
    parser.add_argument('--fail-on-unknown', dest="failfast", action="store_true", default=True)
    opts = parser.parse_args()
    print opts

    with open('Dockerfile', 'r') as df:
        cur_cmd = ""
        lines = collections.deque(map(lambda l: l.rstrip(), df.readlines()))

        while len(lines) > 0:
            line = nextline(lines)
            if not line:
                print ("#")
                continue

            skip = False
            for ign in IGNORED:
                if line and line.startswith(ign + " "):
                    print ("# ignored. %s" % line)
                    skip = True
                    break

            if skip:
                continue

            if line.startswith("#"):
                print (line)
            elif line.startswith("RUN "):
                args = line.split("RUN ")[1]
                if args.endswith("\\"):
                    cmd = parse_multiline(lines, args)
                else:
                    cmd = args
                print (cmd)
            elif line.startswith("WORKDIR "):
                args = line.split("WORKDIR ")[1]
                cmd = "cd %s" % args
                print (cmd)
            elif line.startswith("COPY "):
                args = line.split("COPY ")[1]
                args = args.split(" ")

                if not opts.copy_prefix:
                    parser.print_help()
                    raise ValueError("COPY command does not have URL prefix")
                if len(args) == 2:
                    cmd = "curl %s/%s > %s" % (opts.copy_prefix, args[0], args[1])
                    print ("# %s" % line)
                    print (cmd)
                else:
                    raise ValueError("COPY multiple files does not supported. TODO")
            else:
                if opts.failfast:
                    raise ValueError("Unknown command: %s" % line)
                else:
                    print "# XXX Unknown ignored: %s" % line
            #sys.stdin.readline()

