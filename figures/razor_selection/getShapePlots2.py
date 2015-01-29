import sys, os
from string import *
import ROOT as rt
from ROOT import TFile

import plotTools

if __name__ == '__main__':

    outputdir = "./shapeplots/"
    basedir = "./results_20140917_summary2/"
    inputfile_TTJ = basedir + "rzrBoostMC_TTJets.root"
    inputfile_Top = basedir + "rzrBoostMC_Top.root"
    inputfile_QCD = basedir + "rzrBoostMC_QCD.root"
    inputfile_WJets = basedir + "rzrBoostMC_WJets.root"
    inputfile_DYJets = basedir + "rzrBoostMC_DY.root"
    inputfile_ZJetsToNuNu = basedir + "rzrBoostMC_ZJetsToNuNu.root"
    inputfile_data = basedir + "rzrBoostMC_data.root"
    inputfile_bg = basedir + "rzrBoostMC_bg.root"
    inputfile_1000_325_300 = basedir + "rzrBoostMC_T1ttcc_1000_325_300.root"
    
    if not os.path.isdir(outputdir):
        os.mkdir(outputdir)

    outfile = TFile.Open(outputdir+"/shapeplots.root","RECREATE")
    infile_TTJ = TFile.Open(inputfile_TTJ)
    infile_Top = TFile.Open(inputfile_Top)
    infile_QCD = TFile.Open(inputfile_QCD)
    infile_WJets = TFile.Open(inputfile_WJets)
    infile_DYJets = TFile.Open(inputfile_DYJets)
    infile_Zinv = TFile.Open(inputfile_ZJetsToNuNu)
    infile_data = TFile.Open(inputfile_data)
    infile_bg = TFile.Open(inputfile_bg)
    infile_1000_325_300 = TFile.Open(inputfile_1000_325_300)

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

    leg = plotTools.ConstructLDict(0.6,0.9,0.6,0.87)

    vars = ["MR","R2"]
    vartitles = ["M_{R} (GeV)","R^{2}"]

    for i,var in enumerate(vars):
        hdict_SIG = plotTools.ConstructHDict(infile_TTJ.Get("h_"+var+"_g1Mbg1W0Ll_mdPhig0p5"),
                                             name="Signal region", color=rt.kRed+4,
                                             title="Shape comparison for TTJets in Signal and TTJ Control region",
                                             appear_in_ratio="Ref", xtitle=vartitles[i])
        hdict_TTJmt = plotTools.ConstructHDict(infile_TTJ.Get("h_"+var+"_g1Mbg1W1LlmT100_mdPhig0p5"),
                                             name="T region", color=rt.kRed+1,
                                             title="Shape comparison for TTJets in Signal and TTJ control region",
                                             appear_in_ratio="Yes", xtitle=vartitles[i])
        hdictlist=[hdict_SIG,hdict_TTJmt]
        canvasname = var+"_comparison_TTJ_SIG"
        rtitle = "T/S"
        plotTools.Plot1DWithRatioPAS(hdictlist,outputdir,outfile,cname=canvasname,ratiotitle=rtitle,scale="Yes",
                                     cdim=[800,600],ratiodim=0.3,legdict=leg)

    # build hdictlist for Wjets:
    for i,var in enumerate(vars):
        hdict_SIG = plotTools.ConstructHDict(infile_WJets.Get("h_"+var+"_g1Mbg1W0Ll_mdPhig0p5"),
                                             name="Signal region", color=rt.kGreen+4,
                                             title="Shape comparison for WJets in the S and W region",
                                             appear_in_ratio="Ref", xtitle=vartitles[i])
        hdict_WJets_mt = plotTools.ConstructHDict(infile_WJets.Get("h_"+var+"_0Lbg1Y1LlmT_mdPhig0p5"),
                                             name="W region", color=rt.kGreen+2,
                                             title="Shape comparison for WJets in the S and W region",
                                             appear_in_ratio="Yes", xtitle=vartitles[i])
        hdictlist=[hdict_SIG,hdict_WJets_mt]
        canvasname = var+"_comparison_WJ_SIG"
        rtitle = "W/S"
        plotTools.Plot1DWithRatioPAS(hdictlist,outputdir,outfile,cname=canvasname,ratiotitle=rtitle,scale="Yes",
                                     cdim=[800,600],ratiodim=0.3,legdict=leg)


    # build hdictlist for QCD:
    for i,var in enumerate(vars):
        hdict_SIG = plotTools.ConstructHDict(infile_QCD.Get("h_"+var+"_g1Mbg1W0Ll_mdPhig0p5"),
                                             name="Signal region", color=rt.kMagenta+4,
                                             title="Shape comparison for QCD in the Signal and various QCD Control regions",
                                             appear_in_ratio="Ref", xtitle=vartitles[i])
        hdict_QCD_mdphi = plotTools.ConstructHDict(infile_QCD.Get("h_"+var+"_0Lbg1uW0Ll_mdPhi0p3"),
                                             name="Q region", color=rt.kMagenta+2,
                                             title="Shape comparison for QCD in the Signal and various QCD Control regions",
                                             appear_in_ratio="Yes", xtitle=vartitles[i])
        hdictlist=[hdict_SIG,hdict_QCD_mdphi]
        canvasname = var+"_comparison_QCD_SIG"
        rtitle = "Q/S"
        plotTools.Plot1DWithRatioPAS(hdictlist,outputdir,outfile,cname=canvasname,ratiotitle=rtitle,scale="Yes",
                                     cdim=[800,600],ratiodim=0.3,ratioyscale=[0.,3.4],legdict=leg)

    # build hdictlist for QCD:
    leg = plotTools.ConstructLDict(0.4,0.9,0.6,0.87)
    for i,var in enumerate(vars):
        hdict_SIG = plotTools.ConstructHDict(infile_QCD.Get("h_"+var+"_g1Mbg1W0Ll"),
                                             name="Signal region, no selection on #Delta#phi_{min}", color=rt.kMagenta+4,
                                             title="Shape comparison for QCD in the Signal and various QCD Control regions",
                                             appear_in_ratio="Ref", xtitle=vartitles[i])
        hdict_QCD_mdphi = plotTools.ConstructHDict(infile_QCD.Get("h_"+var+"_0Lbg1uW0Ll_mdPhi0p3"),
                                             name="Q region, no selection on #Delta#phi_{min}", color=rt.kMagenta+2,
                                             title="Shape comparison for QCD in the Signal and various QCD Control regions",
                                             appear_in_ratio="Yes", xtitle=vartitles[i])
        hdictlist=[hdict_SIG,hdict_QCD_mdphi]
        canvasname = var+"_comparison_QCD_SIG_no_deltaphimin"
        rtitle = "Q/S"
        plotTools.Plot1DWithRatioPAS(hdictlist,outputdir,outfile,cname=canvasname,ratiotitle=rtitle,scale="Yes",
                                     cdim=[800,600],ratiodim=0.3,ratioyscale=[0.3,1.7],legdict=leg)

    sys.exit()


    ########################################################
    # Make comparison of gen level W pt
    hname = "h_gen_Wpt"
    htitle = ""
    xt = "generator W pT"
    legd4 = plotTools.ConstructLDict(0.5,0.87,0.7,0.85)
    hdict_TTJ = plotTools.ConstructHDict(infile_TTJ.Get(hname),
                                         name="TTJets", color=rt.kRed, 
                                         title=htitle,
                                         xtitle=xt)
    hdict_1000_325_300 = plotTools.ConstructHDict(infile_1000_325_300.Get(hname),
                                         name="T1ttcc_1000_325_300", color=rt.kCyan+2, 
                                         title=htitle,
                                         xtitle=xt)
    #hdict_1200_125_100 = plotTools.ConstructHDict(infile_1000_125_100.Get(hname),
    #                                     name="T1ttcc_1000_125_100", color=rt.kTeal, 
    #                                     title=htitle,
    #                                     xtitle=xt)
    hdictlist=[hdict_TTJ,hdict_1000_325_300]
    canvasname = "comparison_genWpt"
    plotTools.Plot1D(hdictlist,outputdir,outfile,cname=canvasname,scale="Yes",legdict=legd4)

    ########################################################
    # Make comparison of W pt in signal region
    hname = "h_Wpt_g1Mbg1W0Ll_mdPhig0p5"
    htitle = ""
    xt = "W pT"
    legd4 = plotTools.ConstructLDict(0.5,0.87,0.7,0.85)
    hdict_bg = plotTools.ConstructHDict(infile_bg.Get(hname),
                                         name="Total background (MC)", color=rt.kRed, 
                                         title=htitle,
                                         xtitle=xt,drawoption="histE2")
    hdict_1000_325_300 = plotTools.ConstructHDict(infile_1000_325_300.Get(hname),
                                         name="T1ttcc_1000_325_300", color=rt.kCyan+2, 
                                         title=htitle,
                                         xtitle=xt,drawoption="histE2")
    hdictlist=[hdict_bg,hdict_1000_325_300]
    canvasname = "comparison_Wpt"
    plotTools.Plot1D(hdictlist,outputdir,outfile,cname=canvasname,scale="Yes",legdict=legd4)


    outfile.Close()
    infile_TTJ.Close()
    infile_QCD.Close()
    infile_WJets.Close()
    infile_DYJets.Close()
    infile_Zinv.Close()
    infile_data.Close()
    infile_bg.Close()
    infile_1000_325_300.Close()
