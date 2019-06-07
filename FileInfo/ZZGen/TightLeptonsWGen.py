import os
uw = "hep.wisc.edu" in os.environ["HOSTNAME"] 
info = {
    "zz4l-powheg" : {
        "file_path" : "/data/uhussain/ZZSkimmedFiles/ZZ2018AnalysisTightWGen_2019-04-16/TightLeptons/2019-04-16-zz4l-powheg-ZZ4l2018-TightSIPToZZSelection-v1/*" if uw else \
            "",
        "plot_group" : "zz"
    },
}
