info = {
    "CutFlow": {  
        "Initialize": {  
            "type": "TH1F",
            "nbins": 10,
            "xmin": 0,
            "xmax": 10
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Cut flow",  
            "GetYaxis().SetTitle": "Events / selection", 
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMinimum" : 0.1,
            "SetMaximum" : 70000000
        }
    },
    "ZMass": {  
        "Initialize": {  
            "type": "TH1F",
            "nbins": 31,
            "xmin": 75,
            "xmax": 106
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "m_{\\ell^{+}\\ell^{-}} [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 15000000
        }
    },
    "ptl1": {  
        "Initialize": {  
            "type": "TH1F",
            "nbins": 100,
            "xmin": 20,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "p_{\\mathrm{T}}(\\ell_{1}}\\,\\mathrm{[GeV]}",  
            "GetYaxis().SetTitle": "Events / 2 GeV", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 15000000
        }
    },
    "ptl2": {  
        "Initialize": {  
            "type": "TH1F",
            "nbins": 60,
            "xmin": 20,
            "xmax": 80
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "p_{\\mathrm{T}}(\\ell_{1}}\\,\\mathrm{[GeV]}",  
            "GetYaxis().SetTitle": "Events / 2 GeV", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 15000000
        }
    },
    "YieldByChannel": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 3,
            "xmin": 0,
            "xmax": 10
        },
        "Attributes": {  
            "GetYaxis().SetTitle": "Events Passing Selection"
        }
    }
}
