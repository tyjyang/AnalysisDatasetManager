#!/usr/bin/env python

import argparse
import glob
import os
import subprocess
import multiprocessing

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="path to files in hdfs")
parser.add_argument("--eos", action='store_true', help="Store files on eos instead of /data")
parser.add_argument("-s", "--selection", type=str, default="Dilepton",
        help="Selection tier (default Dilepton)")
parser.add_argument("-d", "--data_name", type=str, default="DibosonAnalysisData",
        help="Data name")
args = parser.parse_args()

if "store" in args.path[:7]:
    args.path = "/hdfs" + args.path
for directory in glob.glob(args.path):
    print "Copying directory", directory
    if not os.path.isdir(directory):
        print "Invalid filename: %s" % directory
        exit(1)
    dirs = directory.split("/")
    dir_name = dirs[-1]
    if dir_name[:3] == "000" and len(dirs)>= 5:
        if "/hdfs" in directory:
            indices = (6,8)
        else:
            indices = (5,7)
        dir_name = dirs[indices[0]]
        if any(y in dir_name for y in ["Muon", "EG", "Electron"]):
            dir_name = "_".join(dirs[indices[0]:indices[1]])
    new_dir = "/".join(["/data", os.getlogin(), args.data_name, args.selection.strip("/"), dir_name])
    if args.eos:
        new_dir = "/".join(["/eos/user", os.getlogin()[0], os.getlogin(), args.selection, dir_name])
    try:
        os.makedirs(new_dir)
    except OSError as e:
        print e
        continue
    filenames = [f if "hdfs" not in f else f[5:] for f in glob.glob(directory + "/*.root")]
    p = multiprocessing.Pool(processes=10)
    p.map(subprocess.call, [["xrdcp", 
            "root://cmsxrootd.hep.wisc.edu/%s" % filename, 
            new_dir] for filename in filenames]
        )
