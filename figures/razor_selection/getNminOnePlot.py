import sys, os
from string import *
import ROOT as rt
from ROOT import TFile

import plotTools

if __name__ == '__main__':

    outputdir = "./"
    basedir = "./results_finebin/"
    inputfile_bg = basedir + "rzrBoostMC_bg.root"
    inputfile_1000_325_300 = basedir + "rzrBoostMC_T1ttcc_1000_325_300.root"
    inputfile_800_425_400 = basedir + "rzrBoostMC_T1ttcc_800_425_400.root"
    inputfile_T1t1t_1200_275_100 = basedir + "rzrBoostMC_T1t1t_1200_275_100.root"
    
    if not os.path.isdir(outputdir):
        os.mkdir(outputdir)

    outfile = TFile.Open(outputdir+"/NminOnePlots.root","RECREATE")
    infile_bg = TFile.Open(inputfile_bg)
    infile_1000_325_300 = TFile.Open(inputfile_1000_325_300)
    infile_800_425_400 = TFile.Open(inputfile_800_425_400)
    infile_T1t1t_1200_275_100 = TFile.Open(inputfile_T1t1t_1200_275_100)

    # Integrated luminosity in fb-1s
    intlumi = 19.712 # ABCD

    # set root styles
    plotTools.SetBoostStyle()
    
    # comparison plots to be made:
    # 1. comparison between process in signal region and relevant control region
    #    * QCD
    #    * TTJets
    #    * WJets
    #    * ZJets
    # 2. comparison between different control regions
    #    * different QCD regions
    #    * different TTjets regions

    leg = plotTools.ConstructLDict(0.15,0.9,0.6,0.87)

    hnames = ["h_Nmin1_njets_g1Mbg1W0Ll_mdPhig0p5"]
    vartitles = ["Jet multiplicity"]

    for i,hname in enumerate(hnames):
        hdict_bg = plotTools.ConstructHDict(infile_bg.Get(hname),
                                             name="Total background", color=rt.kBlack,
                                             title="",
                                             xtitle=vartitles[i])
        hdict_sig1 = plotTools.ConstructHDict(
            infile_1000_325_300.Get(hname),
            name="T1ttcc, m_{#tilde{g}} = 1000 GeV, m_{#tilde{t}_{1}} = 325 GeV, m_{#tilde{#chi}_{1}^{0}} = 300 GeV", 
            color=rt.kRed+1,
            title="",
            xtitle=vartitles[i])
        hdict_sig2 = plotTools.ConstructHDict(
            infile_800_425_400.Get(hname),
            name="T1ttcc, m_{#tilde{g}} = 800 GeV, m_{#tilde{t}_{1}} = 425 GeV, m_{#tilde{#chi}_{1}^{0}} = 400 GeV",
            color=rt.kRed+3,
            title="",
            xtitle=vartitles[i])
        hdict_sig3 = plotTools.ConstructHDict(
            infile_T1t1t_1200_275_100.Get(hname),
            name="T1t1t, m_{#tilde{g}} = 1200 GeV, m_{#tilde{t}_{1}} = 275 GeV, m_{#tilde{#chi}_{1}^{0}} = 100 GeV",
            color=rt.kCyan+2,
            title="",
            xtitle=vartitles[i])

        hdictlist=[hdict_bg, hdict_sig1, hdict_sig2, hdict_sig3]
        canvasname = "njets_signal_region"
        plotTools.Plot1DPAS(hdictlist,outputdir,outfile,cname=canvasname,scale="Yes",
                            cdim=[800,600],legdict=leg,ymax=0.57)



    outfile.Close()
    infile_bg.Close()
    infile_1000_325_300.Close()
