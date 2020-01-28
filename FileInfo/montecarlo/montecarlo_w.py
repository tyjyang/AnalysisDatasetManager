info = {
    "wmv_0j_nlo" : {
        "cross_section" : 54601,
        "kfactor" : 0.9,
        "DAS name" : ""
    },
    "wmv_1j_nlo" : {
        "cross_section" : 8939,
        "kfactor" : 0.9,
        "DAS name" : ""
    },
    "wmv_2j_nlo" : {
        "cross_section" : 3511,
        "kfactor" : 0.9,
        "DAS name" : ""
    },
    "wlnu_nlo" : {
        "cross_section" : 61526.7,
        "DAS Name" : "",
        "Generator" : "MadGraph5_aMC@NLO NLO",
        "Cards" : ""
    },
    "wlnu_lo" : {
        "cross_section" : 61526.7,
        "Source of cross section" : "MadGraph LO",
        "DAS Name" : "",
        "Generator" : "MadGraph5_aMC@NLO LO",
        "Cards" : ""
    },
    "wlnu_lo_cp5" : {
        "cross_section" : 61526.7,
        "DAS Name" : "WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8",
        "Generator" : "MadGraph5_aMC@NLO LO",
        "Cards" : ""
    },
    "wlnu_mgnlo" : {
        "cross_section" : 61526.7,
        "Source of cross section" : "MadGraph NLO",
        "DAS Name" : "",
        "Generator" : "MadGraph5_aMC@NLO NLO",
        "Cards" : ""
    },
    "wlnu_mglo" : {
        "cross_section" : 61526.7,
        "Source of cross section" : "MadGraph LO",
        "DAS Name" : "WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8",
        "Generator" : "MadGraph5_aMC@NLO LO",
        "Cards" : ""
    },
    "wlnu_0j_nlo_cp5" : {
        "cross_section" : 54416.25,
    },
    "wlnu_1j_nlo_cp5" : {
        "cross_section" : 8677.5,
    },
    "wlnu_2j_nlo_cp5" : {
        "cross_section" : 3034.72,
    },
    "wlnu_0j_nlo" : {
        "cross_section" : 49264.92,
    },
    "wlnu_1j_nlo" : {
        "cross_section" : 8280.36,
    },
    "wlnu_2j_nlo" : {
        "cross_section" : 3118.08,
    },
    "wmenu_nloew_photos" : {
        "cross_section" : 11638.57,
        "DAS Name" : "",
        "Generator" : "POWHEG + Photos",
        "Cards" : ""
    },
    "wpmunu_minnlo" : {
        "cross_section" : 11170.4,
        "DAS Name" : "",
        "Generator" : "POWHEG NNLOPS",
        "Cards" : "",
    },
    "wpmunu_minnlo_nnlopslike" : {
        "cross_section" : 11436.6,
        "DAS Name" : "",
        "Generator" : "POWHEG NNLOPS",
        "Cards" : "",
    },
    "wpmunu_nnlops" : {
        "cross_section" : 10670,
        "DAS Name" : "",
        "Generator" : "POWHEG NNLOPS",
        "Cards" : "",
    },
}

ptbins = [0.0, 13.0, 26.0, 38.0, 50.0, 62.0, 75.0, 100.0]
regions = ["GenPtW_%i_%i" % (ptbins[i], ptbins[i+1]) for i in range(len(ptbins)-1)]
ptbins = [0, 5, 10, 15, 20, 25, 30, 40, 50, 60, 75, 100]
regions += ["GenPtW_%i_%i" % (ptbins[i], ptbins[i+1]) for i in range(len(ptbins)-1)]
regions.append("GenPtW_100")
for i in [0, 1, 2]:
    for region in regions:
        info[region] = info["wmv_%ij_nlo" % i]
        # Don't want to accidentally process these files
        info[region]["file_path"] = ""
        info["wmv_%ij_nlo_%s" % (i, region)] = info["wmv_%ij_nlo" % i]
