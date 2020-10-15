import subprocess
converteps = subprocess.call(["command", "-v", "epstopdf"]) != 0

info = {
    "wpmunu_minnlo_photos" : {
        "Name" : r'W^{-}(\mu\nu)+\text{jets} \,\mathrm{MiNNLO}' if not converteps else "W(#mu#nu) MiNNLO",
        "Style" : "qual12_green",
        "Members" : [
            "wpmunu_minnlo__photos"
        ]
    },
    "wpmunu_minnlo_nnlopslike_photos" : {
        "Name" : "W^{+}(#mu#nu) MiNNLO (old)",
        "Style" : "qual12_red",
        "Members" : [
            "wpmunu_minnlo_nnlopslike__photos"
        ]
    },
    "wpmunu_nnlops" : {
        "Name" : "W^{+}(#mu#nu) NNLOPS",
        "Style" : "qual12_lightblue",
        "Members" : [
            "wpmunu_nnlops__photos"
        ]
    },
    "wpmunu_nnlops_photos" : {
        "Name" : "W^{+}(#mu#nu) NNLOPS",
        "Style" : "qual12_lightblue",
        "Members" : [
            "wpmunu_nnlops__photos"
        ]
    },
    "wmmunu_nnlops" : {
        "Name" : "W^{-}(#mu#nu) NNLOPS",
        "Style" : "qual12_lightblue",
        "Members" : [
            "wmmunu_nnlops"
        ]
    },
    "wmunu_nnlops" : {
        "Name" : "W^{#pm}(#mu#nu) NNLOPS",
        "Style" : "qual12_lightblue",
        "Members" : [
            "wmmunu_nnlops",
            "wpmunu_nnlops__photos",
        ]
    },
    "wpmunu_minnlo_ewweights" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (auth. update)",
        "Style" : "qual12_purple_dotdash",
        "Members" : [
            "wpmunu_minnlo_ewweights__photos"
        ]
    },
    "wpmunu_minnlo_gridfix" : {
        "Name" : "W^{+}(#mu#nu) MiNNLO (update, grid fix)",
        "Style" : "qual12_blue_dotdash",
        "Members" : [
            "wpmunu_minnlo_gridfix"
        ]
    },
    "wmunu_minnlo_svn3756_hoppet" : {
        "Name" : "W(#mu#nu) MiNNLO (svn 3756 Hoppet)",
        "Style" : "qual12_blue",
        "Members" : [
            "wpmunu_minnlo_svn3756_hoppet",
            "wmmunu_minnlo_svn3756_hoppet"
        ]
    },
    "wmunu_minnlo_prod" : {
        "Name" : "W(#mu#nu) MiNNLO (arXiv:2006.04133)",
        "Style" : "qual12_orange",
        "Members" : [
            "wpmunu_minnlo_svn3756_hoppet",
            "wmmunu_minnlo_svn3756_hoppet"
        ]
    },
    "wmmunu_minnlo_svn3756_hoppet" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (arXiv:2006.04133)",
        "Style" : "qual12_orange",
        "Members" : [
            "wmmunu_minnlo_svn3756_hoppet"
        ]
    },
    "wpmunu_minnlo_svn3756_hoppet" : {
        "Name" : "W^{+}(#mu#nu) MiNNLO (arXiv:2006.04133)",
        "Style" : "qual12_orange",
        "Members" : [
            "wpmunu_minnlo_svn3756_hoppet"
        ]
    },
    "wmmunu_minnlo_prod" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (arXiv:2006.04133)",
        "Style" : "qual12_orange",
        "Members" : [
            "wmmunu_minnlo_svn3756_hoppet"
        ]
    },
    "wpmunu_minnlo_prod" : {
        "Name" : "W^{+}(#mu#nu) MiNNLO (arXiv:2006.04133)",
        "Style" : "qual12_orange",
        "Members" : [
            "wpmunu_minnlo_svn3756_hoppet"
        ]
    },
    "wmmunu_minnlo_svn3756_hoppet_lhe" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (LHE, svn 3756 Hoppet)",
        "Style" : "qual12_green",
        "Members" : [
            "wmmunu_minnlo_svn3756_hoppet"
        ]
    },
    "wmmunu_minnlo_svn3756_hoppet" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (svn 3756 Hoppet)",
        "Style" : "qual12_blue",
        "Members" : [
            "wmmunu_minnlo_svn3756_hoppet"
        ]
    },
    "wmmunu_minnlo_svn3756" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (svn 3756)",
        "Style" : "qual12_lightblue",
        "Members" : [
            "wmmunu_minnlo_svn3756"
        ]
    },
    "wmmunu_minnlo_svn3756_lhe" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (svn 3756, LHE-level)",
        "Style" : "qual12_lightblue",
        "Members" : [
            "wmmunu_minnlo_svn3756"
        ]
    },
    "wmmunu_minnlo_svn3741" : {
        #"Name" : "W^{-}(#mu#nu) MiNNLO (svn 3741, LHE-level)",
        "Name" : "W^{-}(#mu#nu) MiNNLO (svn 3741)",
        "Style" : "qual12_blue",
        "Members" : [
            "wmmunu_minnlo_svn3741"
        ]
    },
    "wmmunu_minnlo_primktOff" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (svn 3741, no primKt)",
        "Style" : "qual12_pink",
        "Members" : [
            "wmmunu_minnlo_svn3741__primktOff"
        ]
    },
    "wmmunu_minnlo_primktOffWimpy_prefsr" : {
        #"Name" : "W^{-}(#mu#nu) MiNNLO (svn3741, primKtOff+wimpyPS, pre-FSR)",
        "Name" : "W^{-}(#mu#nu) MiNNLO (svn3741)",
        "Style" : "qual12_lightgreen",
        "Members" : [
            "wmmunu_minnlo_svn3741__primktOffWimpy"
        ]
    },
    "wmmunu_minnlo_primktOffWimpy" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (svn3741, primKtOff, wimpyPS)",
        "Style" : "qual12_green",
        "Members" : [
            "wmmunu_minnlo_svn3741__primktOffWimpy"
        ]
    },
    "wmmunu_minnlo_primktOffWimpyDipole_prefsr" : {
        #"Name" : "W^{-}(#mu#nu) MiNNLO (svn3741, primKtOff+dipole+wimpyPS, prefsr)",
        "Name" : "W^{-}(#mu#nu) MiNNLO (svn3741)",
        "Style" : "qual12_blue",
        "Members" : [
            "wmmunu_minnlo_svn3741__primktOffWimpyDipole"
        ]
    },
    "wmmunu_minnlo_primktOffWimpyDipole_lhe" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (svn3741, primKtOff+dipole+wimpyPS, LHE)",
        "Style" : "qual12_lightblue",
        "Members" : [
            "wmmunu_minnlo_svn3741__primktOffWimpyDipole"
        ]
    },
    "wmmunu_minnlo_primktOffWimpyDipole" : {
        #"Name" : "W^{-}(#mu#nu) MiNNLO (svn3741, primKtOff+dipole+wimpyPS)",
        "Name" : "W^{-}(#mu#nu) MiNNLO (svn3741)",
        "Style" : "qual12_red",
        "Members" : [
            "wmmunu_minnlo_svn3741__primktOffWimpyDipole"
        ]
    },
    "wmmunu_minnlo_primktOff_bare" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (svn 3741, no primKt, bare)",
        "Style" : "qual12_orange_dash",
        "Members" : [
            "wmmunu_minnlo_svn3741__primktOff"
        ]
    },
    "wmmunu_minnlo_primktOff_prefsr" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (svn 3741, no primKt, pre-FSR)",
        "Style" : "qual12_brown",
        "Members" : [
            "wmmunu_minnlo_svn3741__primktOff"
        ]
    },
    "wmmunu_minnlo_primktOff_dress" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (svn 3741, no primKt, dressed)",
        "Style" : "qual12_red_dash",
        "Members" : [
            "wmmunu_minnlo_svn3741__primktOff"
        ]
    },
    "wmmunu_minnlo_dress" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (svn 3741, dressed)",
        "Style" : "qual12_blue_dotdash",
        "Members" : [
            "wmmunu_minnlo_svn3741"
        ]
    },
    "wmmunu_minnlo_prefsr" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (svn 3741, pre-FSR)",
        "Style" : "qual12_lightblue",
        "Members" : [
            "wmmunu_minnlo_svn3741"
        ]
    },
    "wmmunu_minnlo_bare" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (svn 3741, bare)",
        "Style" : "qual12_orange_dash",
        "Members" : [
            "wmmunu_minnlo_svn3741"
        ]
    },
    "wpmunu_minnlo_svn3741" : {
        "Name" : "W^{+}(#mu#nu) MiNNLO (svn 3741)",
        "Style" : "qual12_pink",
        "Members" : [
            "wpmunu_minnlo_svn3741"
        ]
    },
    "wpmunu_minnlo_gridfix_wFac1000" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (grid fix, w < 1000 w_{0})",
        "Style" : "qual12_purple_dash",
        "Members" : [
            "wpmunu_minnlo_gridfix__wFac1000"
        ]
    },
    "wpmunu_minnlo_gridfix_wFac100" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (grid fix, w < 100 w_{0})",
        "Style" : "qual12_brown_dash",
        "Members" : [
            "wpmunu_minnlo_gridfix__wFac100"
        ]
    },
    "wpmunu_minnlo_gridfix_wFac10" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (grid fix, w < 10 w_{0})",
        "Style" : "qual12_orange",
        "Members" : [
            "wpmunu_minnlo_gridfix__wFac100"
        ]
    },
    "wpmunu_minnlo_gridfix_wSignOnly" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (grid fix, w #in {0, 1})",
        "Style" : "qual12_pink_dotdash",
        "Members" : [
            "wpmunu_minnlo_gridfix__wSignOnly"
        ]
    },
    "wpmunu_minnlo_update_doublefsr" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (update, double fsr, NNPDF31)",
        "Style" : "qual12_brown_dash",
        "Members" : [
            "wpmunu_minnlo_update_doublefsr"
        ]
    },
    "wmmunu_minnlo_update_ubound" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (update, grid fix1, NNPDF31)",
        "Style" : "qual12_purple_dotdash",
        "Members" : [
            "wmmunu_minnlo_update_ubound"
        ]
    },
    "wmmunu_minnlo_gridfix_wFac1000" : {
        "Name" : "W^{-}(#mu#nu) MiNNLO (update, grid fix, w > 1000 w_{0})",
        "Style" : "qual12_purple_dotdash",
        "Members" : [
            "wmmunu_minnlo_gridfix__wFac1000"
        ]
    },
    "wpmunu_minnlo_update_uboundonly" : {
        "Name" : "W^{+}(#mu#nu) MiNNLO (update, ubound only, NNPDF31)",
        "Style" : "qual12_blue",
        "Members" : [
            "wpmunu_minnlo_update_uboundonly"
        ]
    },
    "wpmunu_minnlo_update_storemintupb" : {
        "Name" : "W^{+}(#mu#nu) MiNNLO (update, storemintupb, NNPDF31)",
        "Style" : "qual12_green_dotdash",
        "Members" : [
            "wpmunu_minnlo_update_storemintupb"
        ]
    },
    "wpmunu_minnlo_update" : {
        "Name" : "W^{+}(#mu#nu) MiNNLO (update, ref., NNPDF31)",
        "Style" : "qual12_pink",
        "Members" : [
            "wpmunu_minnlo_update"
        ]
    },
    "wpmunu_minnlo_update_ubound" : {
        "Name" : "W^{+}(#mu#nu) MiNNLO (update, grid fix, NNPDF31)",
        "Style" : "qual12_purple_dotdash",
        "Members" : [
            "wpmunu_minnlo_update_ubound"
        ]
    },
    "wpmunu_nnlops_nlow" : {
        "Name" : "W^{+}(#mu#nu) MiNLO'",
        "Style" : "qual12_green_dash",
        "Members" : [
            "wpmunu_nnlops__nloOnly_photos"
        ]
    },
    "wmunu_matrix" : {
        "Name" : "W(#mu#nu) MATRIX",
        "Style" : "qual12_green",
        "Members" : [
            "wpmunu_matrix",
            "wmmunu_matrix",
        ]
    },
    "wpmunu_matrix_marius" : {
        "Name" : "W^{+}(#mu#nu) MATRIX (Marius)",
        "Style" : "qual12_green",
        "Members" : [
            "wpmunu_matrix__marius"
        ]
    },
    "wpmunu_matrix" : {
        "Name" : "W^{+}(#mu#nu) MATRIX",
        "Style" : "qual12_green",
        "Members" : [
            "wpmunu_matrix"
        ]
    },
    "wmmunu_matrix" : {
        "Name" : "W^{-}(#mu#nu) MATRIX",
        "Style" : "qual12_green",
        "Members" : [
            "wmmunu_matrix"
        ]
    },
    "wpmunu_matrix_lhe" : {
        "Name" : "W^{+}(#mu#nu) MATRIX",
        "Style" : "qual12_green",
        "Members" : [
            "wpmunu_matrix"
        ]
    },
    "wmmunu_matrix_lhe" : {
        "Name" : "W^{-}(#mu#nu) MATRIX",
        "Style" : "qual12_green",
        "Members" : [
            "wmmunu_matrix"
        ]
    },
    "wpmunu_matrix_default" : {
        "Name" : "W^{+}(#mu#nu) MATRIX (default)",
        "Style" : "qual12_lightgreen_dash",
        "Members" : [
            "wpmunu_matrix__default"
        ]
    },
    "wpmunu_dynnlo" : {
        "Name" : "W^{+}(e#nu) DYNNLO (FO)",
        "Style" : "qual12_brown_dash",
        "Members" : [
            "wpmunu_dynnlo"
        ]
    },
    "wpmunu_fewz" : {
        "Name" : "W^{+}(e#nu) FEWZ (FO)",
        "Style" : "qual12_orange_dotdash",
        "Members" : [
            "wpmunu_fewz"
        ]
    },
    "wpenu_nloew_photos" : {
        "Name" : "W(e#nu) NLO QCD+EW (photos)",
        "Style" : "qual12_green",
        "Members" : [
            "wpenu_nloew__photos"
        ],
        "Scale" : 0.5,
    },
    "wpenu_nloew" : {
        "Name" : "W(e#nu) NLO QCD+EW",
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
