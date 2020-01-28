info = {  
   "Z1lep1_Pt": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 20,
            "xmin": 0,
            "xmax": 200
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Leading lepton p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / 10 GeV",
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
   "Z1lep1_Eta": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 15,
            "xmin": -2.5,
            "xmax": 2.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Leading lepton #eta",  
            "GetYaxis().SetTitle": "Events"
        }
    },
    "backgroundControlYield": {
        "Initialize": {  
            "type": "TH1D",
            "nbins": 1,
            "xmin": 0,
            "xmax": 10
        },
        "Attributes": {  
            "GetYaxis().SetTitle": "Events Passing Selection"
        }
    },
    "yield": {
        "Initialize": {  
            "type": "TH1D",
            "nbins": 1,
             "xmin": 0,
             "xmax": 10
        },
        "Attributes": {  
            "GetYaxis().SetTitle": "Events Passing Selection"
              }
    },
    "nTruePU": {
        "Initialize": {  
            "type": "TH1D",
            "nbins": 100,
             "xmin": 0,
             "xmax": 100
        },
        "Attributes": {
            "GetXaxis().SetTitle": "No. of true PU interactions",  
            "GetYaxis().SetTitle": "Events Passing Selection"
              }
    },
   "LepPt": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 20,
            "xmin": 0,
            "xmax": 200
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Lepton p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / 10 GeV",
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
   "LepEta": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 15,
            "xmin": -2.5,
            "xmax": 2.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Lepton #eta",  
            "GetYaxis().SetTitle": "Events",
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
   "Lep12Pt": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 20,
            "xmin": 0,
            "xmax": 200
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Lepton_{12} p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / 10 GeV",
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
   "Lep12Eta": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 15,
            "xmin": -2.5,
            "xmax": 2.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Lepton_{12} #eta",  
            "GetYaxis().SetTitle": "Events",
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
   "Lep34Pt": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 20,
            "xmin": 0,
            "xmax": 200
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Lepton_{34} p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / 10 GeV",
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
   "Lep34Eta": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 15,
            "xmin": -2.5,
            "xmax": 2.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Lepton_{34} #eta",  
            "GetYaxis().SetTitle": "Events",
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
   "Z1lep1_Phi": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 25,
            "xmin": -3.5,
            "xmax": 3.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Leading lepton #phi",  
            "GetYaxis().SetTitle": "Events"
        }
    },
   "Z1lep2_Pt": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 20,
            "xmin": 0,
            "xmax": 200
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Lepton 2 p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / 10 GeV",
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
   "Z1lep2_Eta": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 15,
            "xmin": -2.5,
            "xmax": 2.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Lepton 2 #eta",  
            "GetYaxis().SetTitle": "Events",
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
   "Z1lep2_Phi": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 25,
            "xmin": -3.5,
            "xmax": 3.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Leading lepton #phi",  
            "GetYaxis().SetTitle": "Events"
        }
    },
   "Z2lep1_Pt": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 20,
            "xmin": 0,
            "xmax": 200
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Lepton 3 p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events",
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
   "Z2lep1_Eta": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 15,
            "xmin": -2.5,
            "xmax": 2.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Lepton 3 #eta",  
            "GetYaxis().SetTitle": "Events",
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
   "Z2lep1_Phi": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 25,
            "xmin": -3.5,
            "xmax": 3.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Leading lepton #phi",  
            "GetYaxis().SetTitle": "Events"
        }
    },
   "Z2lep2_Pt": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 20,
            "xmin": 0,
            "xmax": 200
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Lepton 4 p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events",
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
   "Z2lep2_Eta": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 15,
            "xmin": -2.5,
            "xmax": 2.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Lepton 4 #eta",  
            "GetYaxis().SetTitle": "Events",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMaximum": 35  
        }
    },
   "Z2lep2_Phi": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 25,
            "xmin": -3.5,
            "xmax": 3.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Leading lepton #phi",  
            "GetYaxis().SetTitle": "Events"
        }
    },
   "Z1Pt": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 30,
            "xmin": 0,
            "xmax": 300
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Z_{1} p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / 10 GeV",
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
   "Z1Phi": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 30,
            "xmin": -3.0,
            "xmax": 3.0
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Z_{1} #phi",  
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
   "Z2Phi": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 30,
            "xmin": -3.0,
            "xmax": 3.0
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Z_{2} #phi",  
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
   "dPhiZ1Z2": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 35,
            "xmin": 0,
            "xmax": 3.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "#delta #phi_{Z1,Z2}",  
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
   "ZPt": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 60,
            "xmin": 0,
            "xmax": 600
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Z p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / 10 GeV",
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
  "ZMass": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 60,
            "xmin": 60,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "m_{Z} [GeV]",  
            "GetYaxis().SetTitle": "Z bosons / 1 GeV", 
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
  "Z1Mass": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 60,
            "xmin": 60,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "m_{Z_{1}} [GeV]",  
            "GetYaxis().SetTitle": "Events / 1 GeV", 
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
  "Z1Mass_PPPF": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 60,
            "xmin": 0,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "m_{Z_{1}} [GeV]",  
            "GetYaxis().SetTitle": "Events / 2 GeV", 
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
  "Z1Mass_PPFF": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 60,
            "xmin": 0,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "m_{Z_{1}} [GeV]",  
            "GetYaxis().SetTitle": "Events / 2 GeV", 
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
   "Z2Pt": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 30,
            "xmin": 0,
            "xmax": 300
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Z_{2} p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / 10 GeV",
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
  "Z2Mass": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 60,
            "xmin": 60,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "m_{Z_{2}} [GeV]",  
            "GetYaxis().SetTitle": "Events / 1 GeV", 
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
  "Z2Mass_PPPF": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 60,
            "xmin": 0,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "m_{Z_{2}} [GeV]",  
            "GetYaxis().SetTitle": "Events / 2 GeV", 
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
  "Z2Mass_PPFF": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 60,
            "xmin": 0,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "m_{Z_{2}} [GeV]",  
            "GetYaxis().SetTitle": "Events / 2 GeV", 
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
   "Mass_PPPF": { 
        "Initialize": {  
            "type": "TH1D",
            "nbins": 40,
            "xmin": 70,
            "xmax": 870
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "m_{4l} [GeV]",  
            "GetYaxis().SetTitle": "Events / 20 GeV",
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
   "Mass_PPFF": { 
        "Initialize": {  
            "type": "TH1D",
            "nbins": 40,
            "xmin": 70,
            "xmax": 870
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "m_{4l} [GeV]",  
            "GetYaxis().SetTitle": "Events / 20 GeV",
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
   "Mass": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 22,
            "xmin": 100,
            "xmax": 1200
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "m_{ZZ} [GeV]",  
            "GetYaxis().SetTitle": "Events / 50 GeV",
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
   "ZZPt": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 24,
            "xmin": 0,
            "xmax": 1200
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "ZZ p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / 50 GeV",
            "GetYaxis().SetTitleOffset": 1.2
        }
    },
   "Z1Mass_Z2Mass": {  
        "Initialize": {  
            "type": "TH2D",
            "nbinsx": 60,
            "xmin": 60,
            "xmax": 120,
            "nbinsy": 60,
            "ymin": 60,
            "ymax": 120

        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Z_{1,l1} p_{T} [GeV]",  
            "GetXaxis().SetTitleOffset": 1.2,
            "GetXaxis().SetTitle": "Z_{1,l2} p_{T} [GeV]",  
            "GetXaxis().SetTitleOffset": 1.2  
        }
  },
   "Z1lep1_Z1lep2_Pt": {  
        "Initialize": {  
            "type": "TH2D",
            "nbinsx": 20,
            "xmin": 0,
            "xmax": 200,
            "nbinsy": 20,
            "ymin": 0,
            "ymax": 200
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Z_{1,l1} p_{T} [GeV]",  
            "GetXaxis().SetTitleOffset": 1.2,
            "GetXaxis().SetTitle": "Z_{1,l2} p_{T} [GeV]",  
            "GetXaxis().SetTitleOffset": 1.2  
        }
   },
   "Z1lep1_Z1lep2_Eta": {  
        "Initialize": {  
            "type": "TH2D",
            "nbinsx": 15,
            "xmin": -2.5,
            "xmax": 2.5,
            "nbinsy": 15,
            "ymin": -2.5,
            "ymax": 2.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Z_{1,l1} #eta",  
            "GetXaxis().SetTitleOffset": 1.2,
            "GetXaxis().SetTitle": "Z_{1,l2} #eta",  
            "GetXaxis().SetTitleOffset": 1.2 
        }
    },
   "Z1lep1_Z1lep2_Phi": {  
        "Initialize": {  
            "type": "TH2D",
            "nbinsx": 25,
            "xmin": -3.5,
            "xmax": 3.5,
            "nbinsy": 25,
            "ymin": -3.5,
            "ymax": 3.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Z_{1,l1} #phi",  
            "GetXaxis().SetTitleOffset": 1.2,
            "GetXaxis().SetTitle": "Z_{1,l2} #phi",  
            "GetXaxis().SetTitleOffset": 1.2  
        }
    },
   "Z2lep1_Z2lep2_Pt": {  
        "Initialize": {  
            "type": "TH2D",
            "nbinsx": 15,
            "xmin": 0,
            "xmax": 75,
            "nbinsy": 10,
            "ymin": 0,
            "ymax": 50
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Z_{2,l1} p_{T} [GeV]",  
            "GetXaxis().SetTitleOffset": 1.2,
            "GetXaxis().SetTitle": "Z_{2,l2} p_{T} [GeV]",  
            "GetXaxis().SetTitleOffset": 1.2 
        }
    },
   "Z2lep1_Z2lep2_Eta": {  
        "Initialize": {  
            "type": "TH2D",
            "nbinsx": 15,
            "xmin": -2.5,
            "xmax": 2.5,
            "nbinsy": 15,
            "ymin": -2.5,
            "ymax": 2.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Z_{2,l1} #eta",  
            "GetXaxis().SetTitleOffset": 1.2,
            "GetXaxis().SetTitle": "Z_{2,l2} #eta",  
            "GetXaxis().SetTitleOffset": 1.2 
        }
    },
   "Z2lep1_Z2lep2_Phi": {  
        "Initialize": {  
            "type": "TH2D",
            "nbinsx": 25,
            "xmin": -3.5,
            "xmax": 3.5,
            "nbinsy": 25,
            "ymin": -3.5,
            "ymax": 3.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Z_{2,l1} #phi",  
            "GetXaxis().SetTitleOffset": 1.2,
            "GetXaxis().SetTitle": "Z_{2,l2} #phi",  
            "GetXaxis().SetTitleOffset": 1.2  
        }
    },
   "Z1lep1_PdgId": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 50,
            "xmin": 0,
            "xmax": 50
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Z_{1,l1} PdgID",  
            "GetYaxis().SetTitle": "Events"
        }
    },
   "Z1lep2_PdgId": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 50,
            "xmin": 0,
            "xmax": 50
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Z_{1,l2} PdgID",  
            "GetYaxis().SetTitle": "Events"
        }
    },
   "Z2lep1_PdgId": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 50,
            "xmin": 0,
            "xmax": 50
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Z_{2,l1} PdgID",  
            "GetYaxis().SetTitle": "Events"
        }
    },
   "Z2lep2_PdgId": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 50,
            "xmin": 0,
            "xmax": 50
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Z_{2,l2} PdgID",  
            "GetYaxis().SetTitle": "Events"
        }
    },
    "YieldByChannel": {
      "Initialize": {  
        "type": "TH1D",
        "nbins": 4,
        "xmin": 0,
        "xmax": 4
        },
      "Attributes": {  
       "GetYaxis().SetTitle": "Events",
       "GetXaxis().SetBinLabel": [[1, "Total"],
            [2, "eeee"],
            [3, "ee#mu#mu"],
            [4, "#mu#mu#mu#mu"]
            ],
           "GetXaxis().SetLabelSize" : 0.05,
           "GetXaxis().SetLabelOffset" : 1.2,
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMaximum" : 1200,
            "SetMinimum" : 0.001
        }
    }
}
