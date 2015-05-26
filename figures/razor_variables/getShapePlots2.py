import sys, os
from string import *
import ROOT as rt
from ROOT import TFile, TText

import plotTools, tdrstyle

if __name__ == '__main__':

    outputdir = "./"
    basedir = "./rootfiles/"
    
    inputfile_bg = basedir + "rzrBoostMC_bg.root"
 
    inputfile_T1ttcc_800_125_100 = basedir + "rzrBoostMC_T1ttcc_800_125_100.root"
    inputfile_T1ttcc_1000_425_400 = basedir + "rzrBoostMC_T1ttcc_1000_175_150.root"
    inputfile_T1ttcc_1200_225_200 = basedir + "rzrBoostMC_T1ttcc_1200_225_200.root"

    inputfile_T1t1t_600_225_50 = basedir + "rzrBoostMC_T1t1t_600_225_50.root"
    inputfile_T1t1t_800_275_100 = basedir + "rzrBoostMC_T1t1t_800_275_100.root"
    inputfile_T1t1t_1200_275_100 = basedir + "rzrBoostMC_T1t1t_1200_275_100.root"

    if not os.path.isdir(outputdir):
        os.mkdir(outputdir)

    outfile = TFile.Open(outputdir+"/shapeplots.root","RECREATE")
     
    infile_bg = TFile.Open(inputfile_bg)

    infile_T1ttcc_800_125_100 = TFile.Open(inputfile_T1ttcc_800_125_100)
    infile_T1ttcc_1000_425_400 = TFile.Open(inputfile_T1ttcc_1000_425_400)
    infile_T1ttcc_1200_225_200 = TFile.Open(inputfile_T1ttcc_1200_225_200)
    
    infile_T1t1t_600_225_50 = TFile.Open(inputfile_T1t1t_600_225_50)
    infile_T1t1t_800_275_100 = TFile.Open(inputfile_T1t1t_800_275_100)
    infile_T1t1t_1200_275_100 = TFile.Open(inputfile_T1t1t_1200_275_100)

    # Integrated luminosity in fb-1s
    intlumi = 19.712 # ABCD

    # set root styles
    plotTools.SetBoostStyle()
    tdrstyle.setTDRStyle()

    ########################################################
    # Make comparison of gen level W pt
    hname = "h_MR_jet1ptg200"
    htitle = ""
    xt = "M_{R} (GeV)"
    legd4 = plotTools.ConstructLDict(0.35,0.9,0.6,0.87)
    text1 = TText(0.73,0.55,"T1t1t model")
    text1.SetNDC()
    text1.SetTextSize(0.04)
    hdict_bg = plotTools.ConstructHDict(
        infile_bg.Get(hname),
        name="Total background",
        color=rt.kCyan-8, fillstyle=3003, linewidth=0, 
        title=htitle,
        xtitle=xt)
    hdict_T1t1t_600_225_50 = plotTools.ConstructHDict(
        infile_T1t1t_600_225_50.Get(hname),
        name="m_{#tilde{g}} = 600 GeV, m_{#tilde{t}_{1}} = 225 GeV, m_{#tilde{#chi}_{1}^{0}} = 50 GeV", 
        #name="#splitline{m_{#tilde{g}} = 600 GeV, m_{#tilde{t}_{1}} = 225 GeV,}{m_{#tilde{#chi}_{1}^{0}} = 50 GeV}", 
        color=rt.kCyan+2, 
        title=htitle,
        xtitle=xt)
    hdict_T1t1t_800_275_100 = plotTools.ConstructHDict(
        infile_T1t1t_800_275_100.Get(hname),
        name="m_{#tilde{g}} = 800 GeV, m_{#tilde{t}_{1}} = 275 GeV, m_{#tilde{#chi}_{1}^{0}} = 100 GeV", 
        #name="#splitline{m_{#tilde{g}} = 800 GeV, m_{#tilde{t}_{1}} = 275 GeV,}{m_{#tilde{#chi}_{1}^{0}} = 100 GeV}", 
        color=rt.kCyan+3, 
        title=htitle,
        xtitle=xt)
    hdict_T1t1t_1200_275_100 = plotTools.ConstructHDict(
        infile_T1t1t_1200_275_100.Get(hname),
        name="m_{#tilde{g}} = 1200 GeV, m_{#tilde{t}_{1}} = 275 GeV, m_{#tilde{#chi}_{1}^{0}} = 100 GeV", 
        #name="#splitline{m_{#tilde{g}} = 1200 GeV, m_{#tilde{t}_{1}} = 275 GeV,}{m_{#tilde{#chi}_{1}^{0}} = 100 GeV}", 
        color=rt.kCyan+4, 
        title=htitle,
        xtitle=xt)
    hdictlist=[hdict_bg,
               hdict_T1t1t_600_225_50,
               hdict_T1t1t_800_275_100,
               hdict_T1t1t_1200_275_100]
    canvasname = "T1t1t_MR_comparison"
    plotTools.Plot1DPAS(hdictlist,outputdir,outfile,cname=canvasname,scale="Yes",legdict=legd4,extras=[text1])

    legd5 = plotTools.ConstructLDict(0.35,0.9,0.6,0.87)
    text = TText(0.73,0.55,"T1ttcc model")
    text.SetNDC()
    text.SetTextSize(0.04)
    hdict_bg = plotTools.ConstructHDict(
        infile_bg.Get(hname),
        name="Total background",
        color=rt.kRed-9, fillstyle=3003, linewidth=0, 
        title=htitle,
        xtitle=xt)
    hdict_T1ttcc_800_125_100 = plotTools.ConstructHDict(
        infile_T1ttcc_800_125_100.Get(hname),
        name="m_{#tilde{g}} = 800 GeV, m_{#tilde{t}_{1}} = 125 GeV, m_{#tilde{#chi}_{1}^{0}} = 100 GeV", 
        #name="#splitline{m_{#tilde{g}} = 800 GeV, m_{#tilde{t}_{1}} = 125 GeV,}{m_{#tilde{#chi}_{1}^{0}} = 100 GeV}", 
        color=rt.kRed, 
        title=htitle,
        xtitle=xt)
    hdict_T1ttcc_1000_425_400 = plotTools.ConstructHDict(
        infile_T1ttcc_1000_425_400.Get(hname),
        name="m_{#tilde{g}} = 1000 GeV, m_{#tilde{t}_{1}} = 175 GeV, m_{#tilde{#chi}_{1}^{0}} = 150 GeV", 
        #name="#splitline{m_{#tilde{g}} = 1000 GeV, m_{#tilde{t}_{1}} = 175 GeV,}{m_{#tilde{#chi}_{1}^{0}} = 150 GeV}", 
        color=rt.kRed+2, 
        title=htitle,
        xtitle=xt)
    hdict_T1ttcc_1200_225_200 = plotTools.ConstructHDict(
        infile_T1ttcc_1200_225_200.Get(hname),
        name="m_{#tilde{g}} = 1200 GeV, m_{#tilde{t}_{1}} = 225 GeV, m_{#tilde{#chi}_{1}^{0}} = 200 GeV", 
        #name="#splitline{m_{#tilde{g}} = 1200 GeV, m_{#tilde{t}_{1}} = 225 GeV,}{m_{#tilde{#chi}_{1}^{0}} = 200 GeV}", 
        color=rt.kRed+4, 
        title=htitle,
        xtitle=xt)
    hdictlist=[hdict_bg,
               hdict_T1ttcc_800_125_100,
               hdict_T1ttcc_1000_425_400,
               hdict_T1ttcc_1200_225_200]
    line = rt.TLine(800,0,800,0.2)
    line.SetLineWidth(2)
    line.SetLineColor(rt.kGray+2)
    arrow = rt.TArrow(800,0.16,1200,0.16,0.03,"|>")
    arrow.SetAngle(40)
    arrow.SetLineWidth(2)
    arrow.SetLineColor(rt.kGray+2)
    canvasname = "T1ttcc_MR_comparison"
    plotTools.Plot1DPAS(hdictlist,outputdir,outfile,cname=canvasname,scale="Yes",legdict=legd5,extras=[text,line,arrow])


    ########################################################
    # Make comparison of gen level top pt
    hname = "h_R2_jet1ptg200"
    htitle = ""
    xt = "R^{2}"
    legd4 = plotTools.ConstructLDict(0.38,0.9,0.6,0.87)
    text1 = TText(0.73,0.55,"T1t1t model")
    text1.SetNDC()
    text1.SetTextSize(0.04)
    hdict_bg = plotTools.ConstructHDict(
        infile_bg.Get(hname),
        name="Total background",
        color=rt.kCyan-8, fillstyle=3003, linewidth=0, 
        title=htitle,
        xtitle=xt)
    hdict_T1t1t_600_225_50 = plotTools.ConstructHDict(
        infile_T1t1t_600_225_50.Get(hname),
        name="m_{#tilde{g}} = 600 GeV, m_{#tilde{t}_{1}} = 225 GeV, m_{#tilde{#chi}_{1}^{0}} = 50 GeV", 
        #name="#splitline{m_{#tilde{g}} = 600 GeV, m_{#tilde{t}_{1}} = 225 GeV,}{m_{#tilde{#chi}_{1}^{0}} = 50 GeV}", 
        color=rt.kCyan+2, 
        title=htitle,
        xtitle=xt)
    hdict_T1t1t_800_275_100 = plotTools.ConstructHDict(
        infile_T1t1t_800_275_100.Get(hname),
        name="m_{#tilde{g}} = 800 GeV, m_{#tilde{t}_{1}} = 275 GeV, m_{#tilde{#chi}_{1}^{0}} = 100 GeV", 
        #name="#splitline{m_{#tilde{g}} = 800 GeV, m_{#tilde{t}_{1}} = 275 GeV,}{m_{#tilde{#chi}_{1}^{0}} = 100 GeV}", 
        color=rt.kCyan+3, 
        title=htitle,
        xtitle=xt)
    hdict_T1t1t_1200_275_100 = plotTools.ConstructHDict(
        infile_T1t1t_1200_275_100.Get(hname),
        name="m_{#tilde{g}} = 1200 GeV, m_{#tilde{t}_{1}} = 275 GeV, m_{#tilde{#chi}_{1}^{0}} = 100 GeV", 
        #name="#splitline{m_{#tilde{g}} = 1200 GeV, m_{#tilde{t}_{1}} = 275 GeV,}{m_{#tilde{#chi}_{1}^{0}} = 100 GeV}", 
        color=rt.kCyan+4, 
        title=htitle,
        xtitle=xt)
    hdictlist=[hdict_bg,
               hdict_T1t1t_600_225_50,
               hdict_T1t1t_800_275_100,
               hdict_T1t1t_1200_275_100]
    canvasname = "T1t1t_R2_comparison"
    plotTools.Plot1DPAS(hdictlist,outputdir,outfile,cname=canvasname,scale="Yes",legdict=legd4,extras=[text1],logscale=True,ymax=3)

    legd5 = plotTools.ConstructLDict(0.38,0.9,0.6,0.87)
    text = TText(0.73,0.55,"T1ttcc model")
    text.SetNDC()
    text.SetTextSize(0.04)
    hdict_bg = plotTools.ConstructHDict(
        infile_bg.Get(hname),
        name="Total background",
        color=rt.kRed-9, fillstyle=3003, linewidth=0, 
        title=htitle,
        xtitle=xt)
    hdict_T1ttcc_800_125_100 = plotTools.ConstructHDict(
        infile_T1ttcc_800_125_100.Get(hname),
        name="m_{#tilde{g}} = 800 GeV, m_{#tilde{t}_{1}} = 125 GeV, m_{#tilde{#chi}_{1}^{0}} = 100 GeV", 
        #name="#splitline{m_{#tilde{g}} = 800 GeV, m_{#tilde{t}_{1}} = 125 GeV,}{m_{#tilde{#chi}_{1}^{0}} = 100 GeV}", 
        color=rt.kRed, 
        title=htitle,
        xtitle=xt)
    hdict_T1ttcc_1000_425_400 = plotTools.ConstructHDict(
        infile_T1ttcc_1000_425_400.Get(hname),
        name="m_{#tilde{g}} = 1000 GeV, m_{#tilde{t}_{1}} = 175 GeV, m_{#tilde{#chi}_{1}^{0}} = 150 GeV", 
        #name="#splitline{m_{#tilde{g}} = 1000 GeV, m_{#tilde{t}_{1}} = 175 GeV,}{m_{#tilde{#chi}_{1}^{0}} = 150 GeV}", 
        color=rt.kRed+2, 
        title=htitle,
        xtitle=xt)
    hdict_T1ttcc_1200_225_200 = plotTools.ConstructHDict(
        infile_T1ttcc_1200_225_200.Get(hname),
        name="m_{#tilde{g}} = 1200 GeV, m_{#tilde{t}_{1}} = 225 GeV, m_{#tilde{#chi}_{1}^{0}} = 200 GeV", 
        #name="#splitline{m_{#tilde{g}} = 1200 GeV, m_{#tilde{t}_{1}} = 225 GeV,}{m_{#tilde{#chi}_{1}^{0}} = 200 GeV}", 
        color=rt.kRed+4, 
        title=htitle,
        xtitle=xt)
    hdictlist=[hdict_bg,
               hdict_T1ttcc_800_125_100,
               hdict_T1ttcc_1000_425_400,
               hdict_T1ttcc_1200_225_200]
    line = rt.TLine(0.08,0,0.08,0.5)
    line.SetLineWidth(2)
    line.SetLineColor(rt.kGray+2)
    arrow = rt.TArrow(0.08,0.03,0.18,0.03,0.03,"|>")
    arrow.SetAngle(40)
    arrow.SetLineWidth(2)
    arrow.SetLineColor(rt.kGray+2)
    canvasname = "T1ttcc_R2_comparison"
    plotTools.Plot1DPAS(hdictlist,outputdir,outfile,cname=canvasname,scale="Yes",legdict=legd5,extras=[text,line,arrow],logscale=True,ymax=3)


    outfile.Close()

    infile_bg.Close()

    infile_T1t1t_600_225_50.Close()
    infile_T1t1t_800_275_100.Close()
    infile_T1t1t_1200_275_100.Close()

    infile_T1ttcc_800_125_100.Close()
    infile_T1ttcc_1000_425_400.Close()
    infile_T1ttcc_1200_225_200.Close()
