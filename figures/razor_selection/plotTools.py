##################################################################
### This file will contain usefull plotting routines that can  ###
### be easily included in other scripts.                       ###
##################################################################
import sys, os
import ROOT as rt
from array import array
import CMS_lumi, tdrstyle

# ---------------------------------------------- #
# -- ROOT style                               -- #
# ---------------------------------------------- # 
def SetBoostStyle():
    rt.gStyle.SetOptStat(0)
    rt.gStyle.SetTextFont(42)
    rt.gStyle.SetPaintTextFormat(".3g")
    rt.TH1.SetDefaultSumw2()

# ---------------------------------------------- #
# -- Constructor for histogram dictionary     -- #
# ---------------------------------------------- # 
def ConstructHDict(h, name="name", color=rt.kBlue, title="title", appear_in_ratio="Yes"
                   , linestyle=1, linewidth=2, markerstyle=20, markersize=1, fillstyle=0
                   , xtitle="", ytitle="", ztitle=None, drawoption = "hist", palette="Default"
                   , appear_in_legend=True):
    hdict = {}
    hdict["name"] = name                         # what will appear in the legend
    hdict["histogram"] = h                       # the actual histogram
    hdict["color"] = color                       # the color for the histogram
    hdict["title"] = title                       # title of the histogram
    hdict["appear in ratio"] = appear_in_ratio   # can be "Yes", "No", "Ref"
    hdict["appear in legend"] = appear_in_legend # can be True or False
    hdict["linestyle"] = linestyle               # line style
    hdict["linewidth"] = linewidth               # line width
    hdict["markerstyle"] = markerstyle           # marker style
    hdict["markersize"] = markersize             # marker size
    hdict["fillstyle"] = fillstyle               # fill style
    hdict["xtitle"] = xtitle                     # x axis title
    hdict["ytitle"] = ytitle                     # y axis title
    hdict["ztitle"] = ztitle                     # z axis title
    hdict["drawoption"] = drawoption             # draw option
    hdict["palette"] = palette                   # color palette: "Default" or "SMS"
    return hdict

# ---------------------------------------------- #
# -- Constructor for legend dictionary        -- #
# ---------------------------------------------- # 
def ConstructLDict(xmin,xmax,ymin,ymax,title="",ncolumns=1,fillstyle=1001):
    legdict = {}
    legdict["xmin"] = xmin
    legdict["ymin"] = ymin
    legdict["xmax"] = xmax
    legdict["ymax"] = ymax
    legdict["title"] = title
    legdict["ncolumns"] = ncolumns
    legdict["fillstyle"] = fillstyle
    return legdict

# -----------------------------------------------#
# -- Color style for 2D plots                 -- #
# ---------------------------------------------- #

def SetColorPaletteSMS():
    # define the palette for z axis
    NRGBs = 5
    NCont = 255
    stops = array("d",[0.00, 0.34, 0.61, 0.84, 1.00])
    red= array("d",[0.50, 0.50, 1.00, 1.00, 1.00])
    green = array("d",[ 0.50, 1.00, 1.00, 0.60, 0.50])
    blue = array("d",[1.00, 1.00, 0.50, 0.40, 0.50])
    rt.TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont)
    rt.gStyle.SetNumberContours(NCont)

# -----------------------------------------------# 
# -- Color style for 2D ratio plots           -- # 
# ---------------------------------------------- # 

def SetColorPalette2DRatio():
    # define the palette for z axis
    NRGBs = 5 
    NCont = 255 
    stops = array("d",[0.00, 0.16, 0.2, 0.24, 1.00]) 
    red   = array("d",[0.10, 0.10, 0.10, 1.00, 1.00])
    green = array("d",[0.20, 0.90, 1.00, 0.80, 0.20])
    blue  = array("d",[1.00, 0.90, 0.00, 0.00, 0.20])
    rt.TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont)
    rt.gStyle.SetNumberContours(NCont)
    
# ---------------------------------------------- #
# -- Plot routine for 2D plots                -- #
# ---------------------------------------------- # 
def Plot2D(hdict,outputdir="plots",outfile=0,cname="canvas"
           ,logscale=False,scale="No"):
    # First do some checks on the input
    if outfile == 0:
        print "You did not pass me a root file to store the plots. I will only produce pdf files."
    if not os.path.isdir(outputdir):
        print "Output directory doesn't exist yet"
        print "Will create directory %s" % (outputdir)
        os.makedirs(outputdir)

    # placeholder for draw objects
    rootEvil = []

    # Make the canvas
    canvas = rt.TCanvas(cname,"")
    canvas.SetLeftMargin(0.13)
    canvas.SetRightMargin(0.17)
    canvas.SetBottomMargin(0.13)
    if logscale:
        canvas.SetLogz(1)
    canvas.cd()
    
    # Get histogram from dictionary, and plot it 
    print "Getting histogram"

    h = hdict["histogram"] # Get the histogram
    if scale == "Yes":
        sf = h.Integral(0,h.GetNbinsX()+1,0,h.GetNbinsY()+1)
        h.Scale(1./sf)
    if scale == "Width":
        h.Scale(1,"width")
            
    if scale == "Yes":
        h.GetZaxis().SetTitle("A.U.")
    elif hdict["ztitle"] != None:
        h.GetZaxis().SetTitle(hdict["ztitle"])
    else:
        h.GetZaxis().SetTitle("Events")
    
    maxi = h.GetMaximum()
    if logscale:
        h.SetMaximum(maxi*2)
    else:
        h.SetMaximum(maxi*1.2)
    if scale == "Yes":
        h.SetMaximum(1)
    h.GetXaxis().SetTitle(hdict["xtitle"])
    h.GetXaxis().SetTitleSize(0.05)
    h.GetXaxis().SetTitleOffset(1.1)
    h.GetXaxis().SetLabelSize(0.04)
    h.GetYaxis().SetTitle(hdict["ytitle"])
    h.GetYaxis().SetTitleSize(0.05)
    h.GetYaxis().SetTitleOffset(1.1)
    h.GetYaxis().SetLabelSize(0.04)
    h.GetZaxis().SetTitleSize(0.05)
    h.GetZaxis().SetTitleOffset(1.1)
    h.GetZaxis().SetLabelSize(0.04)
    h.SetTitle(hdict["title"])

    
    drawoption = hdict["drawoption"]
    palette = hdict["palette"]
    if "colz" in drawoption and palette == "SMS":
        print "change color palette"
        SetColorPaletteSMS()
    if "colz" in drawoption and palette == "2DRatio":
        SetColorPalette2DRatio()
    rootEvil.append(h.DrawClone(drawoption))
            
    print "Drew histogram"
    
    canvas.cd()
    canvas.SaveAs(outputdir+"/"+cname+".pdf")
    if outfile != 0:
        outfile.cd()
        canvas.Write()
    canvas.Close()


# ---------------------------------------------- #
# -- Plot routine for 2D plots with CMS style -- #
# ---------------------------------------------- # 
def Plot2DPAS(hdict,outputdir="plots",outfile=0,cname="canvas"
           ,logscale=False,scale="No",lumitext="Preliminary", zmax=0):

    # CMS style plots
    tdrstyle.setTDRStyle()

    # First do some checks on the input
    if outfile == 0:
        print "You did not pass me a root file to store the plots. I will only produce pdf files."
    if not os.path.isdir(outputdir):
        print "Output directory doesn't exist yet"
        print "Will create directory %s" % (outputdir)
        os.makedirs(outputdir)

    # placeholder for draw objects
    rootEvil = []

    # Make the canvas
    canvas = rt.TCanvas(cname,"",50,50,800,600)
    CMS_lumi.lumi_8TeV = "19.7 fb^{-1}"
    CMS_lumi.writeExtraText = 0
    CMS_lumi.extraText = lumitext

    iPos = 0#11
    if( iPos==0 ): CMS_lumi.relPosX = 0.12
    iPeriod = 2
    H_ref = 600 
    W_ref = 800 
    W = W_ref
    H  = H_ref
    
    # references for T, B, L, R
    T = 0.08*H_ref
    B = 0.12*H_ref 
    L = 0.11*W_ref
    R = 0.16*W_ref

    canvas.SetLeftMargin( L/W )
    canvas.SetRightMargin( R/W )
    canvas.SetTopMargin( T/H )
    canvas.SetBottomMargin( B/H )

    if logscale:
        canvas.SetLogz(1)
    canvas.cd()
    
    # Get histogram from dictionary, and plot it 
    print "Getting histogram"

    h = hdict["histogram"] # Get the histogram
    if scale == "Yes":
        sf = h.Integral(0,h.GetNbinsX()+1,0,h.GetNbinsY()+1)
        h.Scale(1./sf)
    if scale == "Width":
        h.Scale(1,"width")
            
    if scale == "Yes":
        h.GetZaxis().SetTitle("A.U.")
    elif hdict["ztitle"] != None:
        h.GetZaxis().SetTitle(hdict["ztitle"])
    else:
        h.GetZaxis().SetTitle("Events / bin")
    
    maxi = h.GetMaximum()
    if zmax != 0:
        h.SetMaximum(zmax)
    elif logscale:
        h.SetMaximum(maxi*2)
    else:
        h.SetMaximum(maxi*1.2)
    if scale == "Yes":
        h.SetMaximum(1)
    h.GetXaxis().SetTitle(hdict["xtitle"])
    h.GetXaxis().SetTitleSize(0.05)
    h.GetXaxis().SetTitleOffset(1.05)
    h.GetXaxis().SetLabelSize(0.04)
    h.GetYaxis().SetTitle(hdict["ytitle"])
    h.GetYaxis().SetTitleSize(0.06)
    h.GetYaxis().SetTitleOffset(0.8)
    h.GetYaxis().SetLabelSize(0.04)
    h.GetZaxis().SetTitleSize(0.05)
    #h.GetZaxis().SetTitleOffset(1.1)
    h.GetZaxis().SetLabelSize(0.04)
    h.SetTitle(hdict["title"])

    
    drawoption = hdict["drawoption"]
    palette = hdict["palette"]
    if "colz" in drawoption and palette == "SMS":
        print "change color palette"
        SetColorPaletteSMS()
    if "colz" in drawoption and palette == "2DRatio":
        SetColorPalette2DRatio()
    rootEvil.append(h.DrawClone(drawoption))
            
    print "Drew histogram"
    print hdict["name"]
    if hdict["name"] != "":
        t = '#scale[1.1]{%s}' % (hdict["name"])
        if len(hdict["name"]) > 20:
            tex = rt.TLatex(0.45,0.82,t)
        else:
            tex = rt.TLatex(0.58,0.82,t)
        tex.SetNDC();
        #tex.SetFillColor(kWhite)
        tex.Draw("same");

    
    canvas.cd()
    CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)
    canvas.SaveAs(outputdir+"/"+cname+".pdf")
    canvas.SaveAs(outputdir+"/"+cname+".C")
    if outfile != 0:
        outfile.cd()
        canvas.Write()
    canvas.Close()

# ---------------------------------------------- #
# -- Plot routine for 2D ratio plots          -- #
# ---------------------------------------------- # 
def Plot2DRatio(hdict1,hdict2,outputdir="plots",outfile=0,
                cname="canvas",logscale=False,scale="No",
                ztitle="Data/MC",ctitle="Title", 
                zmin = 0, zmax = 5, lumitext="Preliminary"):
    # CMS style plots
    tdrstyle.setTDRStyle()
    rt.gStyle.SetPaintTextFormat(".2f")

    # First do some checks on the input
    if outfile == 0:
        print "You did not pass me a root file to store the plots. I will only produce pdf files."
    if not os.path.isdir(outputdir):
        print "Output directory doesn't exist yet"
        print "Will create directory %s" % (outputdir)
        os.makedirs(outputdir)

    # placeholder for draw objects
    rootEvil = []

    # Make the canvas
    canvas = rt.TCanvas(cname,"", 800,600)

    CMS_lumi.lumi_8TeV = "19.7 fb^{-1}"
    CMS_lumi.writeExtraText = 0
    CMS_lumi.extraText = lumitext

    iPos = 0#11
    if( iPos==0 ): CMS_lumi.relPosX = 0.12
    iPeriod = 2
    H_ref = 600 
    W_ref = 800 
    W = W_ref
    H  = H_ref
    
    # references for T, B, L, R
    T = 0.08*H_ref
    B = 0.12*H_ref 
    L = 0.11*W_ref
    R = 0.16*W_ref

    canvas.SetLeftMargin( L/W )
    canvas.SetRightMargin( R/W )
    canvas.SetTopMargin( T/H )
    canvas.SetBottomMargin( B/H )

    #canvas.SetLeftMargin(0.13)
    #canvas.SetRightMargin(0.17)
    #canvas.SetBottomMargin(0.13)
    
    if logscale:
        canvas.SetLogz(1)
    canvas.cd()
    
    # Get histograms from dictionary, and plot it 
    print "Getting histograms"

    h1 = hdict1["histogram"] # Get the histogram
    h1.Sumw2()
    h2 = hdict2["histogram"] # Get the histogram
    h2.Sumw2()
    if scale == "Yes":
        sf1 = h1.Integral(0,h1.GetNbinsX()+1,0,h1.GetNbinsY()+1)
        h1.Scale(1./sf1)
        sf2 = h2.Integral(0,h2.GetNbinsX()+1,0,h2.GetNbinsY()+1)
        h2.Scale(1./sf2)
    if scale == "Width":
        h1.Scale(1,"width")
        h2.Scale(1,"width")

    ratio = h1.Clone("ratio")
    ratio.Divide(h2)
    ratio.SetMaximum(zmax)
    ratio.SetMinimum(zmin)
    ratio.GetZaxis().SetTitle(ztitle)
    
    ratio.GetXaxis().SetTitle(hdict1["xtitle"])
    ratio.GetXaxis().SetTitleSize(0.05)
    ratio.GetXaxis().SetTitleOffset(1.1)
    ratio.GetXaxis().SetLabelSize(0.04)
    ratio.GetYaxis().SetTitle(hdict1["ytitle"])
    ratio.GetYaxis().SetTitleSize(0.05)
    ratio.GetYaxis().SetTitleOffset(1.1)
    ratio.GetYaxis().SetLabelSize(0.04)
    ratio.GetZaxis().SetTitleSize(0.05)
    ratio.GetZaxis().SetTitleOffset(1.1)
    ratio.GetZaxis().SetLabelSize(0.04)
    ratio.SetTitle(ctitle)

    
    drawoption = hdict1["drawoption"]
    palette = hdict1["palette"]
    if "colz" in drawoption:
        #SetColorPalette2DRatio()
        SetColorPaletteSMS()
    rootEvil.append(ratio.DrawClone(drawoption))
            
    print "Drew histogram"
    
    canvas.cd()
    CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)
    canvas.SaveAs(outputdir+"/"+cname+".pdf")
    canvas.SaveAs(outputdir+"/"+cname+".C")
    if outfile != 0:
        outfile.cd()
        canvas.Write()
    canvas.Close()


# ---------------------------------------------- #
# -- Plot routine for 1D comparison plots     -- #
# ---------------------------------------------- # 
def Plot1DWithRatio(hdictlist,outputdir="plots",outfile=0,legdict=0,cname="canvas"
                    ,ratiotitle="ratio",logscale=False,scale="No",scalefactor=1,cdim=[696,472],ratiodim=0.25,ymax=0):
    # First do some checks on the input
    if outfile == 0:
        print "You did not pass me a root file to store the plots. I will only produce pdf files."
    if not os.path.isdir(outputdir):
        print "Output directory doesn't exist yet"
        print "Will create directory %s" % (outputdir)
        os.makedirs(outputdir)

    # placeholder for draw objects
    rootEvil = []

    # Place to store histogram that will be used as reference in ratio plot
    h_ref = None

    # Make the canvas, which will have two pads
    canvas = rt.TCanvas(cname,"",cdim[0],cdim[1])
    pad1 = rt.TPad("pad1","",0,0.25,1,1)
    if ratiodim != 0:
        pad1 = rt.TPad("pad1","",0,ratiodim,1,1)        
    pad1.SetBottomMargin(0)
    if logscale:
        pad1.SetLogy(1)
    pad1.Draw()
    pad1.cd()

    # Make the legend
    legend = rt.TLegend(0.5,0.5,0.87,0.87,"")
    if legdict != 0:
        legend = rt.TLegend(legdict["xmin"],legdict["ymin"],legdict["xmax"],legdict["ymax"],legdict["title"])
        legend.SetNColumns(legdict["ncolumns"])
    legend.SetFillColor(0)
    legend.SetBorderSize(0)
    # Get histograms from a list of dictionaries, and plot them 
    print "Getting all histograms"

    first = 0 # to keep track whether this is the first histogram we're plotting
    maxi = 0
    for hdict in hdictlist:
        h = hdict["histogram"] # Get the histogram
        h.Sumw2() # need to put this otherwise errors in ratio plot are wrong
        if scale == "Yes":
            sf = h.Integral(0,h.GetNbinsX()+1)
            h.Scale(scalefactor/sf)
        if scale == "Width":
            h.Scale(scalefactor,"width")
            
        if hdict["appear in ratio"] == "Ref":
            print "Found ref histo"
            h_ref=h.Clone("h_ref")

        if scale == "Yes":
            h.GetYaxis().SetTitle("A.U.")
        else:
            h.GetYaxis().SetTitle("Events")
        if h.GetMaximum() > maxi:
            maxi = h.GetMaximum()

    for hdict in hdictlist:
        h = hdict["histogram"] # Get the histogram again
        if ymax == 0:
            if logscale:
                h.SetMaximum(maxi*5)
            else:
                h.SetMaximum(maxi*1.2)
        else: 
            h.SetMaximum(ymax)
        h.GetYaxis().SetTitleSize(0.055)
        h.GetYaxis().SetTitleOffset(0.8)
        h.GetYaxis().SetLabelSize(0.05)

        h.SetLineColor(hdict["color"])
        h.SetLineWidth(hdict["linewidth"])
        if hdict["fillstyle"] != 0:
            h.SetFillStyle(hdict["fillstyle"])
            h.SetFillColor(hdict["color"])
        if "P" in hdict["drawoption"]:
            h.SetMarkerColor(hdict["color"])
            h.SetMarkerSize(hdict["markersize"])
            h.SetMarkerStyle(hdict["markerstyle"])
        h.SetTitle(hdict["title"])
        if hdict["ytitle"] != "":
            h.GetYaxis().SetTitle(hdict["ytitle"])
            
        if hdict["appear in legend"]:
            legoption = "l"
            if "E" in hdict["drawoption"]:
                legoption = "epl"
            legend.AddEntry(h,hdict["name"],legoption)
            
        if logscale:
            h.SetMinimum(0.01)
            #h.SetMinimum(0.00005)

        drawoption = hdict["drawoption"]
        if first > 0:
            drawoption = drawoption + " same"
        rootEvil.append(h.DrawClone(drawoption))
        if "E2" in drawoption:
            if first > 0:
                rootEvil.append(h.DrawClone(drawoption.replace("E2","E0")))
            else:
                rootEvil.append(h.DrawClone(drawoption.replace("E2","E0")+" same"))
        first = first+1
        
    print "Drew all histograms"
    legend.Draw("same")
    
    # Make the second canvas, with the ratios
    canvas.cd()
    pad2 = rt.TPad("pad2","",0,0,1,0.25)
    if ratiodim != 0:
        pad2 = rt.TPad("pad2","",0,0,1,ratiodim)        
    pad2.SetBottomMargin(0.35*0.25/ratiodim)#0.25
    pad2.SetTopMargin(0)#0.05
    pad2.SetGridy(1)
    pad2.Draw()
    pad2.cd()

    # Get all the ratio plots
    print "Getting all ratios"
    firstB = 0
    for hdict in hdictlist:
        if hdict["appear in ratio"]!= "Yes": continue

        h = hdict["histogram"]
        h.Sumw2()
        ratio = h.Clone()
        ratio.Sumw2()
        h_ref_ratio = h_ref.Clone()
        h_ref_ratio.Sumw2()
        ratio.Divide(h_ref_ratio)

        ratio.SetMarkerColor(hdict["color"])
        ratio.SetMarkerStyle(hdict["markerstyle"])
        ratio.SetMarkerSize(hdict["markersize"])
        ratio.SetTitle("")
        ratio.SetName("ratio"+str(firstB))
        ratio.GetYaxis().SetRangeUser(0,2.2)
        ratio.GetYaxis().SetNdivisions(4,8,0)
        ratio.GetYaxis().SetLabelSize(0.14*0.25/ratiodim)
        ratio.GetYaxis().SetTitleSize(0.1*0.25/ratiodim)
        ratio.GetYaxis().SetTitle(ratiotitle)
        ratio.GetYaxis().SetTitleOffset(0.22*ratiodim/0.25)
        ratio.GetXaxis().SetLabelSize(0.13*0.25/ratiodim)
        ratio.GetXaxis().SetTitleSize(0.15*0.25/ratiodim)
        ratio.GetXaxis().SetTickLength(0.1*0.25/ratiodim)
        ratio.GetXaxis().SetTitle(hdict["xtitle"])
        ratio.SetStats(0)
        if outfile != 0:
            outfile.cd()
            ratio.Write("ratio_"+hdict["xtitle"]+"_"+str(firstB))
        drawoption="E P"
        if firstB > 0:
            drawoption=drawoption + " SAME"
        rootEvil.append(ratio.DrawClone(drawoption))
        firstB = firstB+1
        
    print "Drew the ratio plot"

    rt.SetOwnership(pad1, False) # to avoid seg fault
    rt.SetOwnership(pad2, False) # to avoid seg fault
    
    canvas.cd()
    canvas.SaveAs(outputdir+"/"+cname+".pdf")
    if outfile != 0:
        outfile.cd()
        canvas.Write()
    canvas.Close()

# ---------------------------------------------- #
# -- Plot routine for 1D comparison plots     -- #
# ---------------------------------------------- # 
def Plot1DWithRatioPAS(hdictlist,outputdir="plots",outfile=0,legdict=0,cname="canvas"
                    ,ratiotitle="ratio",logscale=False,scale="No",scalefactor=1,cdim=[696,472],ratiodim=0.25,ymax=0,ratioyscale=[0.3,1.7]):
    tdrstyle.setTDRStyle()
    
    # First do some checks on the input
    if outfile == 0:
        print "You did not pass me a root file to store the plots. I will only produce pdf files."
    if not os.path.isdir(outputdir):
        print "Output directory doesn't exist yet"
        print "Will create directory %s" % (outputdir)
        os.makedirs(outputdir)

    # placeholder for draw objects
    rootEvil = []

    # Place to store histogram that will be used as reference in ratio plot
    h_ref = None

    # Make the canvas, which will have two pads
    canvas = rt.TCanvas(cname,"",cdim[0],cdim[1])
    pad1 = rt.TPad("pad1","",0,0.25,1,1)
    if ratiodim != 0:
        pad1 = rt.TPad("pad1","",0,ratiodim,1,1)        
    pad1.SetBottomMargin(0)
    pad1.SetTopMargin(0.1)
    pad1.SetLeftMargin(0.12)
    pad1.SetRightMargin(0.05)
    if logscale:
        pad1.SetLogy(1)
    pad1.Draw()
    pad1.cd()

    # Make the legend
    legend = rt.TLegend(0.5,0.5,0.87,0.87,"")
    if legdict != 0:
        legend = rt.TLegend(legdict["xmin"],legdict["ymin"],legdict["xmax"],legdict["ymax"],legdict["title"])
        legend.SetNColumns(legdict["ncolumns"])
    legend.SetFillColor(0)
    legend.SetBorderSize(0)
    # Get histograms from a list of dictionaries, and plot them 
    print "Getting all histograms"

    first = 0 # to keep track whether this is the first histogram we're plotting
    maxi = 0
    for hdict in hdictlist:
        h = hdict["histogram"] # Get the histogram
        h.Sumw2() # need to put this otherwise errors in ratio plot are wrong
        if scale == "Yes":
            sf = h.Integral(0,h.GetNbinsX()+1)
            h.Scale(scalefactor/sf)
        if scale == "Width":
            h.Scale(scalefactor,"width")
            
        if hdict["appear in ratio"] == "Ref":
            print "Found ref histo"
            h_ref=h.Clone("h_ref")

        if scale == "Yes":
            h.GetYaxis().SetTitle("A.U.")
        else:
            h.GetYaxis().SetTitle("Events / bin")
        if h.GetMaximum() > maxi:
            maxi = h.GetMaximum()

    for hdict in hdictlist:
        h = hdict["histogram"] # Get the histogram again
        if ymax == 0:
            if logscale:
                h.SetMaximum(maxi*5)
            else:
                h.SetMaximum(maxi*1.2)
        else: 
            h.SetMaximum(ymax)
        h.GetYaxis().SetTitleSize(0.08)
        h.GetYaxis().SetTitleOffset(0.65)
        h.GetYaxis().SetLabelSize(0.06)

        h.SetLineColor(hdict["color"])
        h.SetLineWidth(hdict["linewidth"])
        if hdict["fillstyle"] != 0:
            h.SetFillStyle(hdict["fillstyle"])
            h.SetFillColor(hdict["color"])
        if "P" in hdict["drawoption"]:
            h.SetMarkerColor(hdict["color"])
            h.SetMarkerSize(hdict["markersize"])
            h.SetMarkerStyle(hdict["markerstyle"])
        h.SetTitle(hdict["title"])
        if hdict["ytitle"] != "":
            h.GetYaxis().SetTitle(hdict["ytitle"])
            
        if hdict["appear in legend"]:
            legoption = "l"
            if "E" in hdict["drawoption"]:
                legoption = "eplf"
            if "E1X0" in hdict["drawoption"]:
                legoption = "ep"
            legend.AddEntry(h,hdict["name"],legoption)
            
        if logscale:
            h.SetMinimum(0.05)
            #h.SetMinimum(0.00005)

        drawoption = hdict["drawoption"]
        if first > 0:
            drawoption = drawoption + " same"
        rootEvil.append(h.DrawClone(drawoption))
        if "E2" in drawoption:
            if first > 0:
                rootEvil.append(h.DrawClone(drawoption.replace("E2","E0")))
            else:
                rootEvil.append(h.DrawClone(drawoption.replace("E2","E0")+" same"))
        first = first+1
        
    print "Drew all histograms"
    legend.Draw("same")
    
    # Make the second canvas, with the ratios
    canvas.cd()
    pad2 = rt.TPad("pad2","",0,0,1,0.25)
    if ratiodim != 0:
        pad2 = rt.TPad("pad2","",0,0,1,ratiodim)        
    pad2.SetBottomMargin(0.18*(1-ratiodim)/ratiodim)
    pad2.SetTopMargin(0)#0.05
    pad2.SetLeftMargin(0.12)
    pad2.SetRightMargin(0.05)
    pad2.SetGridy(1)
    pad2.Draw()
    pad2.cd()

    # Get all the ratio plots
    print "Getting all ratios"
    firstB = 0
    for hdict in hdictlist:
        if hdict["appear in ratio"]!= "Yes": continue

        h = hdict["histogram"]
        h.Sumw2()
        ratio = h.Clone()
        ratio.Sumw2()
        h_ref_ratio = h_ref.Clone()
        h_ref_ratio.Sumw2()
        ratio.Divide(h_ref_ratio)

        ratio.SetMarkerColor(hdict["color"])
        ratio.SetMarkerStyle(hdict["markerstyle"])
        ratio.SetMarkerSize(hdict["markersize"])
        ratio.SetTitle("")
        ratio.SetName("ratio"+str(firstB))
        ratio.GetYaxis().SetRangeUser(ratioyscale[0],ratioyscale[1])
        ratio.GetYaxis().SetNdivisions(4,8,0)
        ratio.GetYaxis().SetLabelSize(0.06*(1-ratiodim)/ratiodim)
        ratio.GetYaxis().SetTitleSize(0.08*(1-ratiodim)/ratiodim)
        ratio.GetYaxis().SetTitle(ratiotitle)
        ratio.GetYaxis().SetTitleOffset(0.65*ratiodim/(1-ratiodim))
        ratio.GetXaxis().SetLabelSize(0.06*(1-ratiodim)/ratiodim)
        ratio.GetXaxis().SetTitleSize(0.08*(1-ratiodim)/ratiodim)
        ratio.GetXaxis().SetTickLength(0.05*(1-ratiodim)/ratiodim)
        ratio.GetXaxis().SetTitle(hdict["xtitle"])
        ratio.SetStats(0)
        if outfile != 0:
            outfile.cd()
            ratio.Write("ratio_"+hdict["xtitle"]+"_"+str(firstB))
        drawoption="E P"
        if firstB > 0:
            drawoption=drawoption + " SAME"
        rootEvil.append(ratio.DrawClone(drawoption))
        firstB = firstB+1
        
    print "Drew the ratio plot"

    rt.SetOwnership(pad1, False) # to avoid seg fault
    rt.SetOwnership(pad2, False) # to avoid seg fault
    
    canvas.cd()
    CMS_lumi.lumi_8TeV = "19.7 fb^{-1}"
    CMS_lumi.writeExtraText = 0
    CMS_lumi.extraText = "Preliminary"

    iPos = 0#11
    if( iPos==0 ): CMS_lumi.relPosX = 0.12
    iPeriod = 2
    CMS_lumi.CMS_lumi(pad1, iPeriod, iPos)


    canvas.SaveAs(outputdir+"/"+cname+".pdf")
    canvas.SaveAs(outputdir+"/"+cname+".C")
    if outfile != 0:
        outfile.cd()
        canvas.Write()
    canvas.Close()

# --------------------------------------------------------------- #
# -- Plot routine for 1D comparison plots without a ratio plot -- #
# --------------------------------------------------------------- # 
def Plot1D(hdictlist,outputdir="plots",outfile=0,legdict=0,cname="canvas"
           ,logscale=False,scale="No",scalefactor=1,ymax=0):
    # First do some checks on the input
    if outfile == 0:
        print "You did not pass me a root file to store the plots. I will only produce pdf files."
    if not os.path.isdir(outputdir):
        print "Output directory doesn't exist yet"
        print "Will create directory %s" % (outputdir)
        os.makedirs(outputdir)

    # placeholder for draw objects
    rootEvil = []

    # Make the canvas
    canvas = rt.TCanvas(cname,"")
    canvas.SetLeftMargin(0.15)
    canvas.SetBottomMargin(0.15)
    #canvas.SetTopMargin(0.17)
    if logscale:
        canvas.SetLogy(1)
    canvas.cd()
    
    # Make the legend
    legend = rt.TLegend(0.67,0.5,0.87,0.87,"")
    if legdict != 0:
        legend = rt.TLegend(legdict["xmin"],legdict["ymin"],legdict["xmax"],legdict["ymax"],legdict["title"])
        legend.SetNColumns(legdict["ncolumns"])
        legend.SetFillStyle(legdict["fillstyle"])
    legend.SetFillColor(0)
    legend.SetBorderSize(0)
    
    # Get histograms from a list of dictionaries, and plot them 
    print "Getting all histograms"

    first = 0 # to keep track whether this is the first histogram we're plotting
    maxi = 0
    for hdict in hdictlist:
        h = hdict["histogram"] # Get the histogram
        h.Sumw2() # need to put this otherwise errors in ratio plot are wrong
        if scale == "Yes":
            sf = h.Integral(0,h.GetNbinsX()+1)
            h.Scale(scalefactor/sf)
        if scale == "Width":
            h.Scale(scalefactor,"width")
        if scale == "YesWidth" or scale == "WidthYes": 
            sf = h.Integral(0,h.GetNbinsX()+1)
            h.Scale(scalefactor/sf,"width")
            
        if scale == "Yes":
            h.GetYaxis().SetTitle("A.U.")
        else:
            h.GetYaxis().SetTitle("Events")
        if h.GetMaximum() > maxi:
            maxi = h.GetMaximum()

    for hdict in hdictlist:
        h = hdict["histogram"] # Get the histogram again
        if ymax==0:
            if logscale:
                h.SetMaximum(maxi*5)
            else:
                h.SetMaximum(maxi*1.2)
        else:
            h.SetMaximum(ymax)
        h.GetXaxis().SetTitle(hdict["xtitle"])
        h.GetXaxis().SetTitleSize(0.05)
        h.GetXaxis().SetTitleOffset(1.1)
        h.GetXaxis().SetLabelSize(0.04)
        h.GetYaxis().SetTitleSize(0.055)
        h.GetYaxis().SetTitleOffset(1.1)
        h.GetYaxis().SetLabelSize(0.04)

        h.SetLineColor(hdict["color"])
        h.SetLineWidth(hdict["linewidth"])
        h.SetLineStyle(hdict["linestyle"])
        if hdict["fillstyle"] != 0:
            h.SetFillStyle(hdict["fillstyle"])
            h.SetFillColor(hdict["color"])
        if "P" in hdict["drawoption"]:
            h.SetMarkerColor(hdict["color"])
            h.SetMarkerSize(hdict["markersize"])
            h.SetMarkerStyle(hdict["markerstyle"])
        h.SetTitle(hdict["title"])
        if hdict["ytitle"] != "":
            h.GetYaxis().SetTitle(hdict["ytitle"])

        if hdict["appear in legend"]:
            legoption = "l"
            if "E" in hdict["drawoption"]:
                legoption = "epl"
            legend.AddEntry(h,hdict["name"],legoption)
        if logscale:
            #h.SetMinimum(0.1)
            h.SetMinimum(0.00005)
            if scale == "Yes":
                h.SetMaximum(1)
        else:
            h.SetMinimum(0.)

        drawoption = hdict["drawoption"]
        if first > 0:
            drawoption = drawoption + " same"
        rootEvil.append(h.DrawClone(drawoption))
        if "E2" in drawoption:
            if first > 0:
                rootEvil.append(h.DrawClone(drawoption.replace("E2","E0")))
            else:
                rootEvil.append(h.DrawClone(drawoption.replace("E2","E0")+" same"))
        first = first+1
        
    print "Drew all histograms"

    legend.Draw("same") 
    
    canvas.cd()
    canvas.SaveAs(outputdir+"/"+cname+".pdf")
    if outfile != 0:
        outfile.cd()
        canvas.Write()
    canvas.Close()

# ----------------------------------------------- #
# -- Plot routine for Data/MC comparison plots -- #
# ----------------------------------------------- # 
def PlotDataMC(hdictlist_bg, hdict_data, hdictlist_sig=0, legdict=0
               , outputdir="plots", outfile=0, cname="canvas", plotinfo="Selection X"
               , ratiotitle="ratio", logscale=False, scale="No", scalefactor=1, intlumi=19.712, style="Boost"):

    # First do some checks on the input
    if outfile == 0:
        print "You did not pass me a root file to store the plots. I will only produce pdf files."
    if not os.path.isdir(outputdir):
        print "Output directory doesn't exist yet. \nWill create directory %s" % (outputdir)
        os.makedirs(outputdir)

    # Get clones of all the mc histograms and put them in a list
    hQCD_index = -1 # will need this if we want to scale QCD only
    histos = []
    for i,hdict in enumerate(hdictlist_bg):
        # first check that the histogram exists
        if not hdict["histogram"]:
            print "Histogram for sample", hdict["name"], "and canvas", cname, "doesn't exist, will stop making this plot now"
            return
        h = hdict["histogram"].Clone() 
        h.Sumw2()
        h.SetFillColor(hdict["color"])
        h.SetLineColor(hdict["color"])
        h.GetYaxis().SetTitle(hdict["ytitle"])
        h.GetXaxis().SetTitle(hdict["xtitle"])
        h.SetTitle(hdict["title"])
        histos.append(h)
        if "QCD" in hdict["name"]:
            hQCD_index = i

    # Get data histogram
    hdata = 0
    if hdict_data == 0:
        print "Will make plots without data"
    else:
        if not hdict_data["histogram"]:
            print hdict["name"], "doesn't exist, will stop making this plot now"
            return
        hdata = hdict_data["histogram"].Clone()
        hdata.Sumw2()
        hdata.SetMarkerStyle(hdict_data["markerstyle"])
        hdata.SetLineColor(hdict_data["color"])
        hdata.GetYaxis().SetTitle(hdict_data["ytitle"])
        hdata.SetTitle(hdict_data["title"])

    # Get signal histograms
    hsignal = []
    if hdictlist_sig != 0:
        for hdict in hdictlist_sig:
            if not hdict["histogram"]:
                print hdict["name"], "doesn't exist, will stop making this plot now"
                return
            h = hdict["histogram"].Clone()
            h.Sumw2()
            h.SetFillColor(hdict["color"])
            h.SetLineColor(hdict["color"])
            hsignal.append(h)

    # make a stack of all the mc, will use the reverse order of the list
    mc = rt.THStack()
    for h in reversed(histos):
        mc.Add(h,"hist")
    for h in hsignal:
        mc.Add(h,"hist")
        
    # make the total mc histogram, used for the ratio plot
    htotal = histos[0].Clone()
    for h in histos[1:]:
        htotal.Add(h)

    # scale MC to data if required
    if scale == "Yes" and hdata != 0:
        sf = scalefactor
        if sf == 1: # we should rescale to match data
            mc_int = htotal.Integral(0,htotal.GetNbinsX()+1)
            if mc_int == 0:
                mc_int = 1.
            data_int = hdata.Integral()
            sf = data_int/mc_int
        for h in histos:
            h.Scale(sf)
        print "Scaled all histograms by factor", sf

    # Scale everything according to the bin width
    if scale == "Width":
        for h in histos:
            h.Scale(scalefactor,"width")
        if hdata != 0:
            hdata.Scale(scalefactor,"width")
        for h in hsignal:
            h.Scale(scalefactor,"width")
        print "Will plot per bin width"
        
    # scale only QCD to match data in the first non-empty bin
    if scale == "QCD" and hdata != 0:
        sf = scalefactor
        if sf == 1:
            # find first non-empty bin
            first_bin = 0
            for b in range(hdata.GetNbinsX()):
                if hdata.GetBinContent(b+1)>0:
                    first_bin = b+1
                    break
            # compute the scale factor
            if histos[hQCD_index].GetBinContent(first_bin) != 0:
                sf = (hdata.GetBinContent(first_bin) - htotal.GetBinContent(first_bin) + histos[hQCD_index].GetBinContent(first_bin)) / histos[hQCD_index].GetBinContent(first_bin)
        histos[hQCD_index].Scale(sf)
        print "Scaled QCD histogram by factor", sf

    if scale != "No":
        # we scaled some histograms, will need to remake htotal
        htotal = histos[0].Clone()
        for h in histos[1:]:
            htotal.Add(h)
        
        
    # make the legend
    legend = rt.TLegend(0.63,0.4,0.87,0.8,"")
    if legdict != 0:
        legend = rt.TLegend(legdict["xmin"],legdict["ymin"],legdict["xmax"],legdict["ymax"],legdict["title"])
        legend.SetNColumns(legdict["ncolumns"])
    legend.SetFillColor(0)
    legend.SetBorderSize(0)
    if hdata != 0:
        legend.AddEntry(hdata," data ("+ str(intlumi) + "/fb)","epl")
    for i,h in enumerate(histos):
        if hdictlist_bg[i]["appear in legend"]:
            legend.AddEntry(h,hdictlist_bg[i]["name"],"f")
    for i,h in enumerate(hsignal):
        if hdictlist_sig[i]["appear in legend"]:
            legend.AddEntry(h,hdictlist_sig[i]["name"],"f")
        
    # Get the maximum of the histograms, so that we can set the Y-axis range
    maxi = 0
    if hdata != 0:
        hdata.GetMaximum()
    if htotal.GetMaximum() > maxi:
        maxi = htotal.GetMaximum()

    # Make the canvas, which will have two pads if we have data, and only one if there is no data
    canvas = rt.TCanvas(cname,"")
    pad1 = 0
    if hdata != 0:
        pad1 = rt.TPad("pad1","",0,0.25,1,1)
        pad1.SetBottomMargin(0)
        if logscale:
            pad1.SetLogy(1)
        pad1.Draw()
        pad1.cd()
    else:
        if logscale:
            canvas.SetLogy(1)
        canvas.SetBottomMargin(0.12)
        canvas.SetLeftMargin(0.12)
        canvas.cd()

    if hdata != 0:
        hdata.GetYaxis().SetTitleSize(0.055)
        hdata.GetYaxis().SetTitleOffset(0.8)
        hdata.GetYaxis().SetLabelSize(0.05)
        hdata.SetMaximum(2.*maxi)
        if logscale:
            hdata.SetMaximum(5.*maxi)
            hdata.SetMinimum(0.007)
        hdata.Draw("EP")
    else:
        mc.Draw()
        mc.SetTitle(hdictlist_bg[0]["title"])
        mc.GetYaxis().SetTitleSize(0.05)
        mc.GetYaxis().SetTitleOffset(1)
        mc.GetYaxis().SetLabelSize(0.045)
        mc.GetXaxis().SetTitleSize(0.05)
        mc.GetXaxis().SetTitleOffset(1)
        mc.GetXaxis().SetLabelSize(0.045)
        mc.GetYaxis().SetTitle(hdictlist_bg[0]["ytitle"])
        mc.GetXaxis().SetTitle(hdictlist_bg[0]["xtitle"])
        mc.SetMaximum(1.5*maxi)
        if logscale:
            mc.SetMaximum(5.*maxi)
            mc.SetMinimum(0.007)
        
    mc.Draw("same")
    mc.Draw("axis same")
    if hdata != 0:
        hdata.Draw("EPsame")
    legend.Draw("same")
    t = '#scale[1.1]{%s}' % (plotinfo)
    if len(plotinfo) > 20:
        tex = rt.TLatex(0.32,0.82,t)
    else:
        tex = rt.TLatex(0.52,0.82,t)
    tex.SetNDC();
    tex.Draw("same");

    if style == "CMS":
        CMS_lumi.lumi_8TeV = "19.7 fb^{-1}"
        CMS_lumi.writeExtraText = 0
        CMS_lumi.extraText = "Preliminary"
        CMS_lumi.CMS_lumi(canvas, 2, 0)

    # Make the second pad, with the ratios; only if hdata!=0
    if hdata != 0:
        canvas.cd()
        pad2 = rt.TPad("pad2","",0,0,1,0.25)
        pad2.SetBottomMargin(0.35)#0.25
        pad2.SetTopMargin(0)#0.05
        pad2.SetGridy(1)
        pad2.Draw()
        pad2.cd()

        ratio = rt.TH1D()
        ratio = hdata.Clone()
        ratio.Divide(htotal)
        ratio.SetTitle("")
        ratio.SetName("histoRatio")
        ratio.GetYaxis().SetRangeUser(0,2.2)
        ratio.GetYaxis().SetNdivisions(4,8,0)
        ratio.GetYaxis().SetLabelSize(0.14)
        ratio.GetYaxis().SetTitleSize(0.15)
        ratio.GetYaxis().SetTitle(ratiotitle)
        ratio.GetYaxis().SetTitleOffset(0.22)
        ratio.GetXaxis().SetLabelSize(0.13)
        ratio.GetXaxis().SetTitleSize(0.15)
        ratio.GetXaxis().SetTickLength(0.1)
        ratio.GetXaxis().SetTitle(hdict_data["xtitle"])

        ratio.SetStats(0)
        ratio.Draw("pe")

        rt.SetOwnership(pad1, False) # to avoid seg fault
        rt.SetOwnership(pad2, False) # to avoid seg fault
    
    canvas.cd()
    canvas.SaveAs(outputdir+"/"+cname+".pdf")
    if outfile != 0:
        outfile.cd()
        canvas.Write()
    canvas.Close()


# -------------------------------------------------------------- #
# -- Plot routine for Data/MC comparison plots with PAS style -- #
# -------------------------------------------------------------- # 
def PlotDataMCPAS(hdictlist_bg, hdict_data, hdictlist_sig=0, legdict=0
               , outputdir="plots", outfile=0, cname="canvas", plotinfo="Selection X"
               , ratiotitle="ratio", logscale=False, scale="No", scalefactor=1, intlumi=19.7, style="CMS"):

    # CMS style plots
    if style == "CMS":
        tdrstyle.setTDRStyle()

    # First do some checks on the input
    if outfile == 0:
        print "You did not pass me a root file to store the plots. I will only produce pdf files."
    if not os.path.isdir(outputdir):
        print "Output directory doesn't exist yet. \nWill create directory %s" % (outputdir)
        os.makedirs(outputdir)

    # Get clones of all the mc histograms and put them in a list
    hQCD_index = -1 # will need this if we want to scale QCD only
    histos = []
    for i,hdict in enumerate(hdictlist_bg):
        # first check that the histogram exists
        if not hdict["histogram"]:
            print "Histogram for sample", hdict["name"], "and canvas", cname, "doesn't exist, will stop making this plot now"
            return
        h = hdict["histogram"].Clone() 
        h.Sumw2()
        h.SetFillColor(hdict["color"])
        h.SetLineColor(hdict["color"])
        h.GetYaxis().SetTitle(hdict["ytitle"])
        h.GetXaxis().SetTitle(hdict["xtitle"])
        h.SetTitle(hdict["title"])
        histos.append(h)
        if "QCD" in hdict["name"]:
            hQCD_index = i

    # Get data histogram
    hdata = 0
    if hdict_data == 0:
        print "Will make plots without data"
    else:
        if not hdict_data["histogram"]:
            print hdict["name"], "doesn't exist, will stop making this plot now"
            return
        hdata = hdict_data["histogram"].Clone()
        hdata.Sumw2()
        hdata.SetMarkerStyle(hdict_data["markerstyle"])
        hdata.SetLineColor(hdict_data["color"])
        hdata.GetYaxis().SetTitle(hdict_data["ytitle"])
        hdata.SetTitle(hdict_data["title"])

    # Get signal histograms
    hsignal = []
    if hdictlist_sig != 0:
        for hdict in hdictlist_sig:
            if not hdict["histogram"]:
                print hdict["name"], "doesn't exist, will stop making this plot now"
                return
            h = hdict["histogram"].Clone()
            h.Sumw2()
            h.SetFillColor(hdict["color"])
            h.SetLineColor(hdict["color"])
            hsignal.append(h)

    # make a stack of all the mc, will use the reverse order of the list
    mc = rt.THStack()
    for h in reversed(histos):
        mc.Add(h,"hist")
    for h in hsignal:
        mc.Add(h,"hist")
        
    # make the total mc histogram, used for the ratio plot
    htotal = histos[0].Clone()
    for h in histos[1:]:
        htotal.Add(h)

    # scale MC to data if required
    if scale == "Yes" and hdata != 0:
        sf = scalefactor
        if sf == 1: # we should rescale to match data
            mc_int = htotal.Integral(0,htotal.GetNbinsX()+1)
            if mc_int == 0:
                mc_int = 1.
            data_int = hdata.Integral()
            sf = data_int/mc_int
        for h in histos:
            h.Scale(sf)
        print "Scaled all histograms by factor", sf

    # Scale everything according to the bin width
    if scale == "Width":
        for h in histos:
            h.Scale(scalefactor,"width")
        if hdata != 0:
            hdata.Scale(scalefactor,"width")
        for h in hsignal:
            h.Scale(scalefactor,"width")
        print "Will plot per bin width"
        
    # scale only QCD to match data in the first non-empty bin
    if scale == "QCD" and hdata != 0:
        sf = scalefactor
        if sf == 1:
            # find first non-empty bin
            first_bin = 0
            for b in range(hdata.GetNbinsX()):
                if hdata.GetBinContent(b+1)>0:
                    first_bin = b+1
                    break
            # compute the scale factor
            if histos[hQCD_index].GetBinContent(first_bin) != 0:
                sf = (hdata.GetBinContent(first_bin) - htotal.GetBinContent(first_bin) + histos[hQCD_index].GetBinContent(first_bin)) / histos[hQCD_index].GetBinContent(first_bin)
        histos[hQCD_index].Scale(sf)
        print "Scaled QCD histogram by factor", sf

    if scale != "No":
        # we scaled some histograms, will need to remake htotal
        htotal = histos[0].Clone()
        for h in histos[1:]:
            htotal.Add(h)
        
        
    # make the legend
    legend = rt.TLegend(0.63,0.4,0.87,0.8,"")
    if legdict != 0:
        legend = rt.TLegend(legdict["xmin"],legdict["ymin"],legdict["xmax"],legdict["ymax"],legdict["title"])
        legend.SetNColumns(legdict["ncolumns"])
    legend.SetFillColor(0)
    legend.SetBorderSize(0)
    if hdata != 0:
        legend.AddEntry(hdata," data ("+ str(intlumi) + "/fb) ","epl")
    for i,h in enumerate(histos):
        if hdictlist_bg[i]["appear in legend"]:
            legend.AddEntry(h,hdictlist_bg[i]["name"],"f")
    for i,h in enumerate(hsignal):
        if hdictlist_sig[i]["appear in legend"]:
            legend.AddEntry(h,hdictlist_sig[i]["name"],"f")
        
    # Get the maximum of the histograms, so that we can set the Y-axis range
    maxi = 0
    if hdata != 0:
        hdata.GetMaximum()
    if htotal.GetMaximum() > maxi:
        maxi = htotal.GetMaximum()

    # Make the canvas, which will have two pads if we have data, and only one if there is no data
    canvas = rt.TCanvas(cname,"",50,50,800,600)
    canvas.cd()

    pad1 = 0
    if hdata != 0:
        pad1 = rt.TPad("pad1","",0,0.25,1,1)
        pad1.SetBottomMargin(0)
        pad1.SetRightMargin(0.03)
        pad1.SetLeftMargin(0.1)
        pad1.SetTopMargin(0.1)
        if logscale:
            pad1.SetLogy(1)
        pad1.Draw()
        pad1.cd()
    else:
        pad1 = rt.TPad("pad1","",0,0,1,1)
        if logscale:
            pad1.SetLogy(1)
        pad1.SetTopMargin(0.08)
        pad1.SetBottomMargin(0.12)
        pad1.SetLeftMargin(0.12)
        pad1.SetRightMargin(0.05)
        pad1.Draw()
        pad1.cd()

    if hdata != 0:
        hdata.GetYaxis().SetTitleSize(0.06)
        hdata.GetYaxis().SetTitleOffset(0.8)
        hdata.GetYaxis().SetLabelSize(0.055)
        hdata.SetMaximum(2.*maxi)
        if logscale:
            hdata.SetMaximum(5.*maxi)
            hdata.SetMinimum(0.05)
        hdata.Draw("EP")
    else:
        mc.Draw()
        mc.SetTitle(hdictlist_bg[0]["title"])
        mc.GetYaxis().SetTitleSize(0.05)
        mc.GetYaxis().SetTitleOffset(1)
        mc.GetYaxis().SetLabelSize(0.045)
        mc.GetXaxis().SetTitleSize(0.05)
        mc.GetXaxis().SetTitleOffset(1)
        mc.GetXaxis().SetLabelSize(0.045)
        mc.GetYaxis().SetTitle(hdictlist_bg[0]["ytitle"])
        mc.GetXaxis().SetTitle(hdictlist_bg[0]["xtitle"])
        mc.SetMaximum(1.5*maxi)
        if logscale:
            mc.SetMaximum(5.*maxi)
            mc.SetMinimum(0.01)
        
    mc.Draw("same")
    mc.Draw("axis same")
    if hdata != 0:
        hdata.Draw("EPsame")
    legend.Draw("same")
    t = '#scale[1.2]{%s}' % (plotinfo)
    tex = rt.TLatex()
    tex.SetNDC()
    tex.SetTextAlign(31)
    tex.DrawLatex(0.9,0.82,t)
    #if len(plotinfo) > 20:
    #    tex.DrawLatex(0.42,0.82,t)
    #else:
    #    tex.DrawLatex(0.6,0.82,t)
    #tex.SetNDC();
    #tex.DrawLatex("same");


    # Make the second pad, with the ratios; only if hdata!=0
    if hdata != 0:
        canvas.cd()
        pad2 = rt.TPad("pad2","",0,0,1,0.25)
        pad2.SetBottomMargin(0.35)#0.25
        pad2.SetTopMargin(0)#0.05
        pad2.SetLeftMargin(0.1)
        pad2.SetRightMargin(0.03)
        pad2.SetGridy(1)
        pad2.Draw()
        pad2.cd()

        ratio = rt.TH1D()
        ratio = hdata.Clone()
        ratio.Divide(htotal)
        ratio.SetTitle("")
        ratio.SetName("histoRatio")
        ratio.GetYaxis().SetRangeUser(0,2.2)
        ratio.GetYaxis().SetNdivisions(4,8,0)
        ratio.GetYaxis().SetLabelSize(0.15)
        ratio.GetYaxis().SetTitleSize(0.18)
        ratio.GetYaxis().SetTitle(ratiotitle)
        ratio.GetYaxis().SetTitleOffset(0.22)
        ratio.GetXaxis().SetLabelSize(0.15)
        ratio.GetXaxis().SetTitleSize(0.18)
        ratio.GetXaxis().SetTitleOffset(0.8)
        ratio.GetXaxis().SetTickLength(0.1)
        ratio.GetXaxis().SetTitle(hdict_data["xtitle"])

        ratio.SetStats(0)
        ratio.Draw("pe")

        rt.SetOwnership(pad1, False) # to avoid seg fault
        rt.SetOwnership(pad2, False) # to avoid seg fault

    canvas.cd()
    if style == "CMS":
        CMS_lumi.lumi_8TeV = "19.7 fb^{-1}"
        CMS_lumi.writeExtraText = 0
        CMS_lumi.extraText = "Preliminary"

        iPos = 0#11
        if( iPos==0 ): CMS_lumi.relPosX = 0.12
        iPeriod = 2
        CMS_lumi.CMS_lumi(pad1, iPeriod, iPos)


    canvas.cd()
    canvas.SaveAs(outputdir+"/"+cname+".pdf")
    if outfile != 0:
        outfile.cd()
        canvas.Write()
    canvas.Close()

if __name__ == "__main__":
    print "This is the tools script, which isn't supposed to be run on it's own"
