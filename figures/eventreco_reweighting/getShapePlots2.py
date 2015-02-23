import sys, os
from string import *
import ROOT as rt
from ROOT import TFile

import plotTools

if __name__ == '__main__':

    outputdir = "./"
    basedir = "./pileup/"
    inputfile_data = basedir + "data_pileup.root"
    inputfile_bg = basedir + "mc_pileup.root"
    inputfile_sig = basedir + "sig53X_pileup.root"
    
    inputfile_weight = basedir + "pileup_weights.root"

    if not os.path.isdir(outputdir):
        os.mkdir(outputdir)

    outfile = TFile.Open(outputdir+"/pileup_plots.root","RECREATE")
    infile_data = TFile.Open(inputfile_data)
    infile_bg = TFile.Open(inputfile_bg)
    infile_sig = TFile.Open(inputfile_sig)

    infile_weight = TFile.Open(inputfile_weight)

    # Integrated luminosity in fb-1s
    intlumi = 19.712 # ABCD

    # set root styles
    plotTools.SetBoostStyle()
    

    ##################################################################
    leg = plotTools.ConstructLDict(0.6,0.9,0.6,0.87)

    varis = ["pileup"]
    vartitles = ["Number of pileup interactions"]

    outfile.cd()
    for i,var in enumerate(varis):
        hdict_data = plotTools.ConstructHDict(infile_data.Get(var).Rebin(10),
                                              name="Data", color=rt.kBlack,
                                              title="", drawoption="histP",
                                              markerstyle=20, markersize=1.2,
                                              xtitle=vartitles[i])
        hdict_bg = plotTools.ConstructHDict(infile_bg.Get("h_"+var).Rebin(10),
                                            name="Simulation", color=rt.kRed+1,
                                            title="", drawoption="histP",
                                            markerstyle=22,markersize=1.2,
                                            xtitle=vartitles[i])
        hdictlist=[hdict_data,hdict_bg]
        canvasname = var+"_comparison"
        #plotTools.Plot1DPAS(hdictlist,outputdir,outfile,legdict=leg,cname=canvasname,scale="Yes")

    
    ##################################################################
    hdict_weight = plotTools.ConstructHDict(infile_weight.Get("pileup_weight"),
                                            name="weight", color=rt.kRed+1,
                                            title="", drawoption="hist",
                                            fillstyle=3001,
                                            xtitle="Number of pileup interactions", 
                                            ytitle="Pileup weight")
    hdictlist = [hdict_weight]
    plotTools.Plot1DPAS(hdictlist,outputdir,outfile,legdict=-1,cname="pileup_weight_comparison",ymax=3)


    outfile.Close()
    infile_data.Close()
    infile_bg.Close()
    infile_sig.Close()

    infile_weight.Close()
