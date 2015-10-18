#!/usr/bin/env python

# Register datasets with proof to avoid loading files each time
# Only needs to be done once, valied until the file is modified
#
# Taken (almost verbatim) from Nick Smith, U. Wisconsin
# https://github.com/nsmith-/ZHinvAnalysis/blob/master/register_proof_datasets.py

import ROOT
ROOT.gROOT.SetBatch(True)
import argparse
import os
import json
import sys

def getComLineArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--selection", type=str,
                        required=True, help="Specify the selection level "
                        "of the dataset. Used to form a unique name")
    parser.add_argument("-d", "--is_data", action='store_true',
                        help="Is CMS data, not Monte Carlo (default = false)")
    parser.add_argument("-n", "--names", 
                        type=lambda x: [i.strip() for i in x.split(",")],
                        required=False, help="List of datasets to register "
                        "(separated by commas).")
    return parser.parse_args()
def readJson(json_file_name):
    json_info = {}
    with open(json_file_name) as json_file:
        try:
            json_info = json.load(json_file)
        except ValueError as err:
            print "Error reading JSON file %s. The error message was:" % json_file_name 
            print(err)
    return json_info
def getFilePath(name, selection):
    datafile = "FileInfo"
    if "wz_" in selection:
        datafile += "/wz_analysis/%s.json" % selection.strip("wz_")
    dataset_info = readJson(datafile)
    if name not in dataset_info.keys():
        print "Failed to find %s in %s" % (name, dataset_info)
        return ""
    return dataset_info[name]["file_path"]
args = getComLineArgs()
reRegister = True

ROOT.TProof.Open('workers=8')
# TProof::Open returns pointer to proof-lite and messes with pyroot's
# inability to call virtual base class members
# gProof is base class type, so no issues
proof = ROOT.gProof
current_path = os.getcwd()
os.chdir(sys.path[0])
dataset_file = "/".join(["FileInfo", "data.json" if args.is_data else "montecarlo.json"])
datasets = readJson(dataset_file)

for name in args.names:
    if name not in datasets.keys():
        print "%s is not a valid file! Skipping." % name
        print "File names must be defined in data.json or montecarlo.json"
        continue
    proof_name = '-'.join([name, args.selection])
    if proof.GetDataSet(proof_name) == None or reRegister :
        filelist = ROOT.TFileCollection(proof_name, proof_name)
        num_files = filelist.Add(getFilePath(name, args.selection))
        print "num_files is %i file path is %s" % (num_files, getFilePath(name, args.selection))
        #proof.RegisterDataSet(proof_name, filelist, 'OVnostagedcheck:')
os.chdir(current_path)

