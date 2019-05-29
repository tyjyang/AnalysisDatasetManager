import json

def readAllInfo(file_path):
    info = {}
    for info_file in glob.glob(file_path):
        json_info.update(readInfo(info_file))
    return json_info

def readInfo(file_path):
    try:
        file_info = imp.load_source("info_file", file_path)
        info = file_info.info
    except IOError:
        info = readJson(file_path)
    return info

def readJson(json_file_name):
    json_info = {}
    with open(json_file_name) as json_file:
        try:
            json_info = json.load(json_file)
        except ValueError as err:
            print "Error reading JSON file %s. The error message was:" % json_file_name 
            print(err)
    return json_info

def getHistType(manager_path, selection, hist_name):
    hist_file = "/".join([manager_path, 
        "AnalysisDatasetManager", "PlotObjects", selection + ".json"]) 
    all_hist_info = readJson(hist_file)
    if hist_name not in all_hist_info.keys():
        print all_hist_info
        raise ValueError("Invalid hist name '%s'. Must be defined in %s"
                % (hist_name, hist_file))
    hist_info = all_hist_info[hist_name]["Initialize"]
    return hist_info["type"]

def getHistBinInfo(manager_path, selection, hist_name):
    bin_info = {}
    hist_file = "/".join([manager_path, 
        "AnalysisDatasetManager", "PlotObjects", selection + ".json"]) 
    all_hist_info = readJson(hist_file)
    if hist_name not in all_hist_info.keys():
        print all_hist_info
        raise ValueError("Invalid hist name '%s'. Must be defined in %s"
                % (hist_name, hist_file))
    hist_info = all_hist_info[hist_name]["Initialize"]
    if "TH1" in hist_info["type"]:
        args = ['nbins', 'xmin', 'xmax']
    elif "TH2" in hist_info["type"]:
        args = ['nbinsx', 'xmin', 'xmax', 'nbinsy', 'ymin', 'ymax']
    else:
        raise ValueError("Invalid histogram type %s" % hist_info['type'])
        
    for key in args:
        bin_info.update({key : hist_info[key]})
    return bin_info

def getAllHistNames(manager_path, selection):
    bin_info = {}
    hist_file = "/".join([manager_path, 
        "AnalysisDatasetManager", "PlotObjects", selection + ".json"]) 
    all_hist_names = readJson(hist_file).keys()
    return all_hist_names
