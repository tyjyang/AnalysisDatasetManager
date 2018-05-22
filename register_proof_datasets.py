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
import glob
import sys
import fnmatch

def getComLineArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--selection", type=str,
                        required=True, help="Specify the selection level "
                        "of the dataset. Used to form a unique name")
    parser.add_argument("-f", "--filelist", 
                        type=lambda x: [i.strip() for i in x.split(",")],
                        required=False, help="List of datasets to register "
                        "(separated by commas).")
    return parser.parse_args()
def readAllJson(json_file_path):
    json_info = {}
    for json_file in glob.glob(json_file_path):
        json_info.update(readJson(json_file))
    return json_info
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
    datafile = "FileInfo/%s.json" % selection
    dataset_info = readJson(datafile)
    if name not in dataset_info.keys():
        print "Failed to find %s for %s" % (name, selection)
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
data_info = readAllJson("FileInfo/data/*.json")
mc_info = readAllJson("FileInfo/montecarlo/*.json")
valid_names = mc_info.keys() + data_info.keys()

if args.filelist in [[""], None]:
    args.filelist = readJson("FileInfo/%s.json" % args.selection)

names = []
log = ""
for name in args.filelist:
    names += fnmatch.filter(valid_names, name) if "*" in name else [name]

registerTogether=False
proof_name_all = '_'.join(args.selection.split("/"))
filelist_all = ROOT.TFileCollection(proof_name_all, proof_name_all)
for name in names:
    if name.split("__")[0] not in valid_names:
        log += "%s is not a valid file! Skipping." % name
        log += "\nFile names must be defined in data.json or montecarlo.json\n"
        continue
    proof_name = '_'.join([name] + args.selection.split("/"))
    print "Proof name is", proof_name
    if proof.GetDataSet(proof_name) == None or reRegister :
        filename = getFilePath(name, args.selection)
        if registerTogether:
            filelist_all.Add(filename)
        else:
            filelist = ROOT.TFileCollection(proof_name, proof_name)
            num_files = filelist.Add(filename)
            if filelist.GetNFiles() == 0:
                log += "\n%s does not point to a valid file! Skipping" % name
                log += "\nFile name was %s\n" % filename
                continue
            proof.RegisterDataSet(proof_name, filelist, 'OVnostagedcheck:')
if registerTogether:
    if filelist_all.GetNFiles() == 0:
        log += "\n%s does not point to a valid file! Skipping" % name
        log += "\nFile name was %s\n" % filename
    else:
        proof.RegisterDataSet(proof_name_all, filelist_all, 'OVnostagedcheck:')

os.chdir(current_path)
print log
