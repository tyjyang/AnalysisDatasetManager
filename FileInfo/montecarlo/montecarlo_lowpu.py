info = {
    "zz" : {
        "cross_section" : 1.15,
        "Source of cross section" : "POWHEG tarball",
        "DAS Name" : ""
    },
    "wz" : {
        "cross_section" : 4.43,
        "Source of cross section" : "POWHEG tarball",
        "DAS Name" : "WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8"
    },
    "tt_had" : {
        "cross_section" : 2,
        "Source of cross section" : "placeholder",
        "DAS Name" : ""
    },
    "tt_semilep" : {
        "cross_section" : 2,
        "Source of cross section" : "placeholder",
        "DAS Name" : ""
    },
    "tt_lep" : {
        "cross_section" : 87.31,
        "Source of cross section" : "https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#TTbar",
        "DAS Name" : "TTJets_DiLept_TuneCUETP8M1_13TeUETP8M2_ttHtranche3_13TeV-powheg-pythia8"
    },
    "ww" : {
        "cross_section" : 12.178,
        "Source of cross section" : "https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson",
        "DAS Name" : "WWTo2L2Nu_13TeV-powheg"
    },
}

ptbins = [0.0, 13.0, 26.0, 38.0, 50.0, 62.0, 75.0, 100.0]
regions = ["GenPtW_%i_%i" % (ptbins[i], ptbins[i+1]) for i in range(len(ptbins)-1)]
ptbins = [0, 5, 10, 15, 20, 25, 30, 40, 50, 60, 75, 100]
regions += ["GenPtW_%i_%i" % (ptbins[i], ptbins[i+1]) for i in range(len(ptbins)-1)]
regions = ["GenPtW_%i_%i" % (ptbins[i], ptbins[i+1]) for i in range(len(ptbins)-1)]
regions.append("GenPtW_100")

for proc in ["wlnu_%ij_nlo" % i for i in [0, 1, 2] ]:
    for region in regions:
        name = proc + "_" + region
        info[name] = { "cross_section" : 2 }
