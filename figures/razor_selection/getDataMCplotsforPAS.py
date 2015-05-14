import sys, os
from string import *
import ROOT as rt
from ROOT import TFile

import plotTools

if __name__ == '__main__':

    outputdir = "./plots/"
    inputdir = "./results_20140917_summary2/"
    analyzer = "rzrBoostMC"
    
    if not os.path.isdir(outputdir):
        os.mkdir(outputdir)

    outfile = TFile.Open(outputdir+"/plots.root","RECREATE")

    # Integrated luminosity in fb-1s
    intlumi = 19.7 # ABCD

    plotTools.SetBoostStyle()
    
    print "Will make plots for integrated luminosity of %.3f fb-1" % (intlumi)

    # define all the datasets we want to plot, and their colors
    # backgrounds
    #mc_datasets = ["QCD","TTJets","WJetsToLNu","Wbb","Top","TTX","ZJetsToNuNu","DYJetsToLL","DYToBB","DYToCC","VV","VVV"]
    #mc_colors   = [rt.kMagenta,rt.kRed,rt.kGreen+1,rt.kGreen+3,rt.kCyan,rt.kCyan+2,rt.kOrange,rt.kOrange+2,rt.kOrange+7,rt.kOrange+9,rt.kBlue+1,rt.kBlue-3]
    mc_datasets = ["QCD"      ,"TTJets"  ,"WJets"    ,"Top"       ,"ZJetsToNuNu"            ,"DY"        ,"rare"]
    mc_colors   = [rt.kMagenta+1,rt.kRed-4   ,rt.kGreen+1,rt.kCyan    ,rt.kOrange               ,rt.kOrange+2,rt.kBlue+1]
    mc_titles   = [" multijet" ," t#bar{t}"," W+jets"   ," single top"," Z#rightarrow#nu#nu+jets"," Drell-Yan" ," VV(V) + t#bar{t}V(V)"]
    flist = []
    for d in mc_datasets:
        f = TFile.Open(inputdir+analyzer+"_"+d+".root")
        flist.append(f)
    # signal
    sig_datasets = ["T1ttcc_1000_325_300"]
    sig_colors   = [rt.kGray]
    sig_titles   = [" signal"]
    fsiglist = []
    for d in sig_datasets:
        f = TFile.Open(inputdir+analyzer+"_"+d+".root")
        fsiglist.append(f)
    # data
    fdata = TFile.Open(inputdir+analyzer+"_data.root")
        
    # make the dictionaries to pass to the plot routine
    vars = ["MR","R2"]
    vartitles = ["M_{R} (GeV)","R^{2}"]
    cuts = ["g1Mbg1W0Ll_mdPhig0p5",
            "g1Mbg1W1LlmT100_mdPhig0p5",
            "0Lbg1Y1LlmT_mdPhig0p5",
            "0Lbg1uW0Ll_mdPhi0p3",
            "HLT",
            "g1Mbg1Y2l0ol"
            ]
    plotinfos = ["Signal region","T region", "W region", "Q region","Baseline","Z-enriched region"]
    legd = plotTools.ConstructLDict(0.58,0.92,0.45,0.8,ncolumns=2)

    for cut in cuts:
        for var in vars:
            hname = "h_%s_%s" % (var,cut)
            htitle = ""
            hlist = []
            for i in range(len(mc_datasets)):
                if not flist[i]: continue
                hdict = plotTools.ConstructHDict(flist[i].Get(hname),name=mc_titles[i],color=mc_colors[i],title=htitle,xtitle=vartitles[vars.index(var)])
                hlist.append(hdict)
        
            hsiglist = []
            for i in range(len(sig_datasets)):
                if not fsiglist[i]: continue
                hdict = plotTools.ConstructHDict(fsiglist[i].Get(hname),name=sig_titles[i],
                                                 color=sig_colors[i],#linestyle=sig_styles[i],linewidth=sig_widths[i],
                                                 title=htitle,xtitle=vartitles[vars.index(var)])
                hsiglist.append(hdict)

            hdict_data = plotTools.ConstructHDict(fdata.Get(hname),name="data",color=rt.kBlack,title=htitle,xtitle=vartitles[vars.index(var)],ytitle="Events",markerstyle=20)
            
            # now make the actual plot
            plotTools.PlotDataMCPAS(hlist,hdict_data,hsiglist,legdict=legd,outputdir=outputdir, outfile=outfile,
                                 cname="DataMC_%s_%s"%(var,cut), plotinfo=plotinfos[cuts.index(cut)],
                                 ratiotitle="Data/MC ", logscale=True, scale="No", style="CMS")

            # scale according to bin width; need to adjust y axis title according to variable
            if var == "MR":
                hdict_data2 = plotTools.ConstructHDict(fdata.Get(hname),name="data",color=rt.kBlack,title=htitle,
                                                       xtitle=vartitles[vars.index(var)],ytitle="< Events / 100 GeV >",markerstyle=20)
                #hdict_data2=0
                plotTools.PlotDataMCPAS(hlist,hdict_data2,hsiglist,legdict=legd,outputdir=outputdir, outfile=outfile,
                                     cname="DataMC_%s_%s_width"%(var,cut), plotinfo=plotinfos[cuts.index(cut)],
                                     ratiotitle="Data/MC ", logscale=True, scale="Width", scalefactor=100, style="CMS", stacksignal=True)
            else:
                hdict_data2 = plotTools.ConstructHDict(fdata.Get(hname),name="data",color=rt.kBlack,title=htitle,
                                                       xtitle=vartitles[vars.index(var)],ytitle="< Events / 0.01 units >",markerstyle=20)
                #hdict_data2=0
                plotTools.PlotDataMCPAS(hlist,hdict_data2,hsiglist,legdict=legd,outputdir=outputdir, outfile=outfile,
                                     cname="DataMC_%s_%s_width"%(var,cut), plotinfo=plotinfos[cuts.index(cut)],
                                     ratiotitle="Data/MC ", logscale=True, scale="Width", scalefactor=0.01, style="CMS", stacksignal=True)

    ##############################################################################################################

    # Make plot of signal region without data
    vars = ["MR","R2"]
    vartitles = ["M_{R} (GeV)","R^{2}"]
    ytitles = [" GeV"," units"]
    cuts = ["g1Mbg1W0Ll_mdPhig0p5"]
    plotinfos = ["Signal region"]
    sf = [100,0.01]
    legd2 = plotTools.ConstructLDict(0.6,0.92,0.5,0.8,ncolumns=2)
    for cut in cuts:
        for vi,var in enumerate(vars):
            hname = "h_%s_%s" % (var,cut)
            htitle = ""
            hlist = []
            for i in range(len(mc_datasets)):
                if not flist[i]: continue
                hdict = plotTools.ConstructHDict(flist[i].Get(hname),name=mc_titles[i],color=mc_colors[i],title=htitle,
                                                 xtitle=vartitles[vars.index(var)],ytitle="< Events / %s%s >"%(sf[vi],ytitles[vi]))
                hlist.append(hdict)
        
            hsiglist = []
            for i in range(len(sig_datasets)):
                if not fsiglist[i]: continue
                hdict = plotTools.ConstructHDict(fsiglist[i].Get(hname),name=sig_titles[i],
                                                 color=sig_colors[i],#linestyle=sig_styles[i],linewidth=sig_widths[i],
                                                 title=htitle,
                                                 xtitle=vartitles[vars.index(var)],ytitle="< Events / %s%s >"%(sf[vi],ytitles[vi]))
                hsiglist.append(hdict)

            plotTools.PlotDataMCPAS(hlist,0,hsiglist,legdict=legd2,outputdir=outputdir, outfile=outfile,
                                 cname="DataMC_%s_%s_width_nodata"%(var,cut), plotinfo=plotinfos[cuts.index(cut)],
                                 ratiotitle="Data/MC ", logscale=True, scale="Width", scalefactor=sf[vi], style="CMS", stacksignal=True)


    ##############################################################################################################

    # make mT plots
    vars = ["mT"]
    vartitles = ["m_{T} (GeV)"]
    cuts = ["g1Mbg1W1Ll_rebin",
            "0Lbg1Y1Ll_rebin",
            ]
    plotinfos = ["T region, no selection on m_{T} and #Delta#phi_{min}", "W region, no selection on m_{T} and #Delta#phi_{min}"]
    #legd = plotTools.ConstructLDict(0.65,0.92,0.5,0.8,ncolumns=2)

    for cut in cuts:
        for var in vars:
            hname = "h_%s_%s" % (var,cut)
            htitle = ""
            hlist = []
            for i in range(len(mc_datasets)):
                if not flist[i]: continue
                hdict = plotTools.ConstructHDict(flist[i].Get(hname),name=mc_titles[i],color=mc_colors[i],title=htitle,xtitle=vartitles[vars.index(var)])
                hlist.append(hdict)
        
            hsiglist = []
            for i in range(len(sig_datasets)):
                if not fsiglist[i]: continue
                hdict = plotTools.ConstructHDict(fsiglist[i].Get(hname),name=sig_titles[i],
                                                 color=sig_colors[i],#linestyle=sig_styles[i],linewidth=sig_widths[i],
                                                 title=htitle,xtitle=vartitles[vars.index(var)])
                hsiglist.append(hdict)

            binwidth = fdata.Get(hname).GetXaxis().GetBinWidth(1)
            hdict_data = plotTools.ConstructHDict(fdata.Get(hname),name="data",color=rt.kBlack,title=htitle,xtitle=vartitles[vars.index(var)],ytitle="Events / %d GeV"%(binwidth),markerstyle=20)
            
            # now make the actual plot
            plotTools.PlotDataMCPAS(hlist,hdict_data,hsiglist,legdict=legd,outputdir=outputdir, outfile=outfile,
                                 cname="DataMC_%s_%s"%(var,cut), plotinfo=plotinfos[cuts.index(cut)],
                                 ratiotitle="Data/MC ", logscale=True, scale="No", style="CMS", stacksignal=True)

    ##############################################################################################################

    # make mindeltaphi plots
    vars = ["minDeltaPhi"]
    vartitles = ["#Delta#phi_{min}"]
    cuts = ["0Lbg1uW0Ll_rebin",
            "g1Mbg1W1LlmT100_rebin",
            "0Lbg1Y1LlmT_rebin",
            "g1Mbg1W0Ll_rebin"]
    plotinfos = ["Q region, no selection on #Delta#phi_{min}", 
                 "T region, no selection on #Delta#phi_{min}",
                 "W region, no selection on #Delta#phi_{min}",
                 "Signal region, no selection on #Delta#phi_{min}"]
    #legd = plotTools.ConstructLDict(0.65,0.92,0.5,0.8,ncolumns=2)
    sig_colors2   = [rt.kCyan+3]
    sig_styles2   = [5]
    sig_widths2   = [2]
    stack_signals = [True, True, True, False]

    for cc, cut in enumerate(cuts):
        for var in vars:
            hname = "h_%s_%s" % (var,cut)
            htitle = ""
            hlist = []
            for i in range(len(mc_datasets)):
                if not flist[i]: continue
                hdict = plotTools.ConstructHDict(flist[i].Get(hname),name=mc_titles[i],
                                                 color=mc_colors[i],
                                                 title=htitle,xtitle=vartitles[vars.index(var)])
                hlist.append(hdict)
        
            hsiglist = []
            for i in range(len(sig_datasets)):
                if not fsiglist[i]: continue
                if cut == "g1Mbg1W0Ll_rebin":
                    hdict = plotTools.ConstructHDict(fsiglist[i].Get(hname),name=sig_titles[i],
                                                     color=sig_colors2[i],linestyle=sig_styles2[i],linewidth=sig_widths2[i],
                                                     title=htitle,xtitle=vartitles[vars.index(var)])
                else:
                    hdict = plotTools.ConstructHDict(fsiglist[i].Get(hname),name=sig_titles[i],
                                                     color=sig_colors[i],
                                                     title=htitle,xtitle=vartitles[vars.index(var)])
                hsiglist.append(hdict)

            binwidth = fdata.Get(hname).GetXaxis().GetBinWidth(1)
            hdict_data = plotTools.ConstructHDict(fdata.Get(hname),name="data",color=rt.kBlack,title=htitle,xtitle=vartitles[vars.index(var)],ytitle="Events / %0.2f units"%(binwidth),markerstyle=20)
            
            # now make the actual plot
            plotTools.PlotDataMCPAS(hlist,hdict_data,hsiglist,legdict=legd,outputdir=outputdir, outfile=outfile,
                                 cname="DataMC_%s_%s"%(var,cut), plotinfo=plotinfos[cuts.index(cut)],
                                 ratiotitle="Data/MC ", logscale=True, scale="No", style="CMS", stacksignal=stack_signals[cc])

            plotTools.PlotDataMCPAS(hlist,0,hsiglist,legdict=legd2,outputdir=outputdir, outfile=outfile,
                                 cname="DataMC_%s_%s_nodata"%(var,cut), plotinfo=plotinfos[cuts.index(cut)],
                                 logscale=True, scale="No", style="CMS", stacksignal=stack_signals[cc])

    ##############################################################################################################

    # make met plot
    vars = ["met","Wpt"]
    vartitles = ["E_{T}^{miss} (GeV)","W tagged jet p_{T} (GeV)"]
    cuts = ["g1Mbg1W0Ll_mdPhig0p5"]
    plotinfos = ["Signal region"]
    #legd = plotTools.ConstructLDict(0.65,0.92,0.5,0.8,ncolumns=2)

    for cut in cuts:
        for var in vars:
            hname = "h_%s_%s" % (var,cut)
            htitle = ""
            hlist = []
            for i in range(len(mc_datasets)):
                if not flist[i]: continue
                hdict = plotTools.ConstructHDict(flist[i].Get(hname),name=mc_titles[i],color=mc_colors[i],title=htitle,xtitle=vartitles[vars.index(var)])
                hlist.append(hdict)
        
            hsiglist = []
            for i in range(len(sig_datasets)):
                if not fsiglist[i]: continue
                hdict = plotTools.ConstructHDict(fsiglist[i].Get(hname),name=sig_titles[i],
                                                 color=sig_colors[i],#linestyle=sig_styles[i],linewidth=sig_widths[i],
                                                 title=htitle,xtitle=vartitles[vars.index(var)])
                hsiglist.append(hdict)

            # now make the actual plot
            plotTools.PlotDataMCPAS(hlist,0,hsiglist,legdict=legd2,outputdir=outputdir, outfile=outfile,
                                 cname="DataMC_%s_%s_nodata"%(var,cut), plotinfo=plotinfos[cuts.index(cut)],
                                 logscale=False, scale="No", style="CMS",ymax=35, stacksignal=True)

    ##############################################################################################################


    outfile.Close()

