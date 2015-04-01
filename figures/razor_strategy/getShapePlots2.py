import sys, os
from string import *
import ROOT as rt
from ROOT import TFile, TText, TLine

import plotTools, tdrstyle

if __name__ == '__main__':

    outputdir = "./"
    basedir = "./rootfiles/"
    inputfile_TTJ = basedir + "rzrBoostMC_TTJets.root"

    inputfile_T1ttcc_800_125_100 = basedir + "rzrBoostMC_T1ttcc_800_125_100.root"
    inputfile_T1ttcc_1000_425_400 = basedir + "rzrBoostMC_T1ttcc_1000_175_150.root"
    inputfile_T1ttcc_1200_225_200 = basedir + "rzrBoostMC_T1ttcc_1200_225_200.root"

    inputfile_T1t1t_600_225_50 = basedir + "rzrBoostMC_T1t1t_600_225_50.root"
    inputfile_T1t1t_800_275_100 = basedir + "rzrBoostMC_T1t1t_800_275_100.root"
    inputfile_T1t1t_1200_275_100 = basedir + "rzrBoostMC_T1t1t_1200_275_100.root"

    if not os.path.isdir(outputdir):
        os.mkdir(outputdir)

    outfile = TFile.Open(outputdir+"/shapeplots.root","RECREATE")
    infile_TTJ = TFile.Open(inputfile_TTJ)
    
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
    hname = "h_gen_Wpt"
    htitle = ""
    xt = "generator W p_{T} (GeV)"
    legd4 = plotTools.ConstructLDict(0.25,0.9,0.5,0.87)
    text1 = TText(0.73,0.45,"T1t1t model")
    text1.SetNDC()
    text1.SetTextSize(0.04)
    line1 = TLine(320,0,320,0.07)
    line1.SetLineWidth(2)
    line1.SetLineColor(rt.kGray+2)
    line1.SetLineStyle(2)
    arrow1 = rt.TArrow(320,0.06,450,0.06,0.03,"|>")
    arrow1.SetAngle(40)
    arrow1.SetLineWidth(2)
    arrow1.SetLineColor(rt.kGray+2)
    arrow1.SetFillColor(rt.kGray+2)
    hdict_TTJets1 = plotTools.ConstructHDict(
        infile_TTJ.Get(hname),
        name="t#bar{t}+jets", 
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
    hdictlist=[hdict_TTJets1,
               hdict_T1t1t_600_225_50,
               hdict_T1t1t_800_275_100,
               hdict_T1t1t_1200_275_100]
    canvasname = "T1t1t_genWpt"
    plotTools.Plot1DPAS(hdictlist,outputdir,outfile,cname=canvasname,scale="Yes",legdict=legd4,extras=[text1,line1,arrow1])


    legd5 = plotTools.ConstructLDict(0.25,0.9,0.5,0.87)
    text = TText(0.73,0.45,"T1ttcc model")
    text.SetNDC()
    text.SetTextSize(0.04)
    hdict_TTJets = plotTools.ConstructHDict(
        infile_TTJ.Get(hname),
        name="t#bar{t}+jets", 
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
    hdictlist=[hdict_TTJets,
               hdict_T1ttcc_800_125_100,
               hdict_T1ttcc_1000_425_400,
               hdict_T1ttcc_1200_225_200]
    canvasname = "T1ttcc_genWpt"
    plotTools.Plot1DPAS(hdictlist,outputdir,outfile,cname=canvasname,scale="Yes",legdict=legd5,extras=[text,line1,arrow1])


    ########################################################
    # Make comparison of gen level top pt
    hname = "h_gen_toppt"
    htitle = ""
    xt = "generator top p_{T} (GeV)"
    legd4 = plotTools.ConstructLDict(0.28,0.9,0.5,0.87)
    text1 = TText(0.73,0.45,"T1t1t model")
    text1.SetNDC()
    text1.SetTextSize(0.04)
    line2 = TLine(700,0,700,0.05)
    line2.SetLineWidth(2)
    line2.SetLineColor(rt.kGray+2)
    line2.SetLineStyle(2)
    arrow2 = rt.TArrow(700,0.04,850,0.04,0.03,"|>")
    arrow2.SetAngle(40)
    arrow2.SetLineWidth(2)
    arrow2.SetLineColor(rt.kGray+2)
    arrow2.SetFillColor(rt.kGray+2)
    hdict_TTJets1 = plotTools.ConstructHDict(
        infile_TTJ.Get(hname),
        name="t#bar{t}+jets", 
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
    hdictlist=[hdict_TTJets1,
               hdict_T1t1t_600_225_50,
               hdict_T1t1t_800_275_100,
               hdict_T1t1t_1200_275_100]
    canvasname = "T1t1t_gentoppt"
    plotTools.Plot1DPAS(hdictlist,outputdir,outfile,cname=canvasname,scale="Yes",legdict=legd4,extras=[text1,line2,arrow2])

    legd5 = plotTools.ConstructLDict(0.28,0.9,0.5,0.87)
    text = TText(0.73,0.45,"T1ttcc model")
    text.SetNDC()
    text.SetTextSize(0.04)
    hdict_TTJets = plotTools.ConstructHDict(
        infile_TTJ.Get(hname),
        name="t#bar{t}+jets", 
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
    hdictlist=[hdict_TTJets,
               hdict_T1ttcc_800_125_100,
               hdict_T1ttcc_1000_425_400,
               hdict_T1ttcc_1200_225_200]
    canvasname = "T1ttcc_gentoppt"
    plotTools.Plot1DPAS(hdictlist,outputdir,outfile,cname=canvasname,scale="Yes",legdict=legd5,extras=[text,line2,arrow2])


    outfile.Close()
    infile_TTJ.Close()
    infile_T1t1t_600_225_50.Close()
    infile_T1t1t_800_275_100.Close()
    infile_T1t1t_1200_275_100.Close()

    infile_T1ttcc_800_125_100.Close()
    infile_T1ttcc_1000_425_400.Close()
    infile_T1ttcc_1200_225_200.Close()
