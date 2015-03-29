import sys, os
from string import *
import ROOT as rt
from ROOT import TFile, TText, TLatex

import plotTools

if __name__ == '__main__':


    outputdir = "."
    outfile = TFile.Open(outputdir+"/trigplots.root","RECREATE")

    # Integrated luminosity in fb-1s
    intlumi = 19.7 # ABCD

    # set root styles
    plotTools.SetBoostStyle()
            

    ##########################################
    # Plot with trigger efficiency
    ##########################################

    trigdir = "."
    inputfile_trig = trigdir + "/hlteff_0_pre_singlel.root"
    infile_trig = TFile.Open(inputfile_trig)

    hdict_trig = plotTools.ConstructHDict(infile_trig.Get("h_HT_j1pt_pre_effph_l"),
                                          name="",
                                          #name="#splitline{Preselection}{SingleL}", 
                                          title="",
                                          xtitle="H_{T} (GeV)", ytitle="p_{T}(j_{1}) (GeV)", ztitle="Efficiency",
                                          drawoption="colz", palette="SMS") 
    canvasname = "h_HT_j1pt_pre_eff_ph_l"
    #plotTools.Plot2DPAS(hdict_trig,outputdir,outfile,cname=canvasname,scale="No",logscale=False,lumitext=" Preliminary", zmax=1.)

    text1 = TLatex(0.15,0.2,"#splitline{SingleL, preselection,}{unc = max(err+, diff)}")
    text1.SetNDC()
    text1.SetTextSize(0.05)
    text1.SetTextFont(42)

    hdict_trig2 = plotTools.ConstructHDict(infile_trig.Get("h_HT_j1pt_0_pre_errdiff_up_ph_l"),
                                          name="",
                                          #name="#splitline{Preselection}{SingleL}", 
                                          title="",
                                          xtitle="H_{T} (GeV)", ytitle="p_{T}(j_{1}) (GeV)", ztitle="Efficiency uncertainty",
                                          drawoption="colz", palette="SMS") 
    canvasname = "h_HT_j1pt_0_pre_errdiff_up_ph_l_forThesis"
    plotTools.Plot2DPAS(hdict_trig2,outputdir,outfile,cname=canvasname,scale="No",logscale=True,lumitext="", zmax=1., extras=[text1])
    

    text2 = TLatex(0.15,0.2,"#splitline{SingleL, preselection,}{unc = max(err-, diff)}")
    text2.SetNDC()
    text2.SetTextSize(0.05)
    text2.SetTextFont(42)

    hdict_trig3 = plotTools.ConstructHDict(infile_trig.Get("h_HT_j1pt_0_pre_errdiff_low_ph_l"),
                                          name="",
                                          #name="#splitline{Preselection}{SingleL}", 
                                          title="",
                                          xtitle="H_{T} (GeV)", ytitle="p_{T}(j_{1}) (GeV)", ztitle="Efficiency uncertainty",
                                          drawoption="colz", palette="SMS") 
    canvasname = "h_HT_j1pt_0_pre_errdiff_low_ph_l_forThesis"
    plotTools.Plot2DPAS(hdict_trig3,outputdir,outfile,cname=canvasname,scale="No",logscale=True,lumitext="", zmax=1., extras=[text2])
    

    
    outfile.Close()
    infile_trig.Close()
