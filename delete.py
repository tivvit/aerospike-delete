#!/usr/bin/env python

import aerospike
from aerospike.exception import *
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    add = parser.add_argument

    add('namespace', type=str, help="aerospike namespace")
    add('-a', '--hosts', nargs='+', type=str, default=['localhost'],
        help="[localhost] list of hosts")
    add('-p', '--port', type=int, default=3000, help="[3000] aerospike port")
    add('-s', '--set', type=str, help="aerospike set")

    args = parser.parse_args()

    cli = aerospike.client(
        {
            "hosts": [(host, 3000) for host in args.hosts],
        }
    )

    aeros_client = cli.connect()

    def delEntry((key, metadata, record)):
        print "deleting record - key: %s, val: %s" % (str(key), str(record))
        try:
            aeros_client.remove(key)
        except Exception as e:
            print str(e)

    scan = aeros_client.scan(args.namespace)
    if args.set:
        scan = aeros_client.scan(args.namespace, args.set)
    scan.foreach(delEntry)

