import subprocess
converteps = subprocess.call(["command", "-v", "epstopdf"]) != 0

info = {
    "wpmunu_minnlo_photos" : {
        "Name" : r'W^{-}(\mu\nu)+\text{jets} \,\mathrm{MiNNLO}' if not converteps else "W(#mu#nu)+jets MiNNLO",
        "Style" : "qual12_green",
        "Members" : [
            "wpmunu_minnlo__photos"
        ]
    },
    "wpmunu_minnlo_nnlopslike_photos" : {
        "Name" : "W^{+}(#mu#nu)+jets MiNNLO",
        "Style" : "qual12_red",
        "Members" : [
            "wpmunu_minnlo_nnlopslike__photos"
        ]
    },
    "wpmunu_nnlops_photos" : {
        "Name" : "W^{+}(#mu#nu)+jets NNLOPS",
        "Style" : "qual12_lightblue",
        "Members" : [
            "wpmunu_nnlops__photos"
        ]
    },
    "wpmunu_nnlops_nlow" : {
        "Name" : "W^{+}(#mu#nu)+jets MiNLO (via NNLOPS)",
        "Style" : "qual12_green_dash",
        "Members" : [
            "wpmunu_nnlops__nloOnly_photos"
        ]
    },
    "wpmunu_matrix" : {
        "Name" : "W^{+}(#mu#nu)+jets MATRIX (FO)",
        "Style" : "qual12_purple_dotdash",
        "Members" : [
            "wpmunu_matrix"
        ]
    },
    "wpmunu_dynnlo" : {
        "Name" : "W^{+}(e#nu)+jets DYNNLO (FO)",
        "Style" : "qual12_brown_dash",
        "Members" : [
            "wpmunu_dynnlo"
        ]
    },
    "wpmunu_fewz" : {
        "Name" : "W^{+}(e#nu)+jets FEWZ (FO)",
        "Style" : "qual12_orange_dotdash",
        "Members" : [
            "wpmunu_fewz"
        ]
    },
    "wpmunu_nnlops" : {
        "Name" : r'W^{+}(\ell\nu)+\text{jets} \,\mathrm{NNLOPS}' if not converteps else "W(l#nu)+jets NNLOPS",
        "Style" : "nofill-grey",
        "Members" : [
            "wpmunu_nnlops"
        ]
    },
    "wpenu_nloew_photos" : {
        "Name" : "W(e#nu)+jets NLO QCD+EW (photos)",
        "Style" : "qual12_green",
        "Members" : [
            "wpenu_nloew__photos"
        ],
        "Scale" : 0.5,
    },
    "wpenu_nloew" : {
        "Name" : "W(e#nu)+jets NLO QCD+EW",
        "Style" : "qual12_brown",
        "Members" : [
            "wpenu_nloew"
        ]
    },
    "wpenu_nloewConf_noew" : {
        "Name" : "W(e#nu)+jets NLO QCD",
        "Style" : "qual12_burntorange_dotdash",
        "Members" : [
            "wpenu_nloewConf_noew"
        ]
    },
    "wlnu_lo" : {
        "Name" : r'W(\ell\nu)+\text{jets} \,\mathrm{(LO)}',
        "Style" : "nofill-darkred",
        "Members" : [
            "wlnu_lo"
        ]
    },
    "wlnu_lo_cp5" : {
        "Name" : r'W(\ell\nu)+\text{jets} \,\mathrm{CP5 \, (LO)}',
        "Style" : "nofill-darkred",
        "Members" : [
            "wlnu_lo_cp5"
        ]
    },
    "wlnu_nlo" : {
        "Name" : r'W(\ell\nu)+\text{jets} \,\mathrm{(NLO)}' if not converteps else "W(l#nu)+jets MG5_aMC NLO",
        "Style" : "qual12_blue",
        "Members" : [
            "wlnu_nlo"
        ]
    },
    "wlnu_jetbinned_nlo" : {
        "Name" : r'W(\ell\nu)\,\text{jet binned} \,\mathrm{(NLO)}',
        "Style" : "nofill-grey",
        "Members" : [
            "wlnu_0j_nlo",
            "wlnu_1j_nlo",
            "wlnu_2j_nlo",
        ]
    },
    "wlnu_jetbinned_nlo_cp5" : {
        "Name" : r'W(\ell\nu)\,\text{jet binned} \,\mathrm{CP5 \, (NLO)}',
        "Style" : "nofill-darkpurple-dash",
        "Members" : [
            "wlnu_0j_nlo_cp5",
            "wlnu_1j_nlo_cp5",
            "wlnu_2j_nlo_cp5",
        ]
    },
}
