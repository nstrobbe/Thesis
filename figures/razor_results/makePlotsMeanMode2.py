from ROOT import *
import os
import plotTools
import tdrstyle, CMS_lumi


if __name__ == "__main__":

    # CMS style plots
    tdrstyle.setTDRStyle()

    CMS_lumi.lumi_8TeV = "19.7 fb^{-1}"
    CMS_lumi.writeExtraText = 0

    iPos = 0#11
    if( iPos==0 ): CMS_lumi.relPosX = 0.12+0.08
    iPeriod = 2

    plotTools.SetColorPaletteSMS()

    dirbase = "./"
    indir = dirbase
    outdir = "./"
            
    lumi = 19712.
    
    infile1 = TFile.Open(indir+"/mean_vs_mode2.root")

    outfile = TFile.Open(indir+"/plots_mean_vs_mode.root","RECREATE")
        
    hnames = ["b_S_TTJ_001","b_S_TTJ_005"]
    xtitles = ["Count"]*2
    modes = [14.4,13.57]
    means = [15.33,14.98]
    bins = ["#splitline{800 < M_{R} < 1000 GeV}{0.08 < R^{2} < 0.12}",
            "#splitline{1000 < M_{R} < 1200 GeV}{0.08 < R^{2} < 0.12}"
            ]
        
    for i,hname in enumerate(hnames):
        h1 = infile1.Get(hname)

        c = TCanvas(hname.replace("h_","c_"))
        c.cd()

        h1.GetXaxis().SetTitle(xtitles[i])
        h1.GetXaxis().SetTitleSize(0.05)
        h1.GetXaxis().SetLabelSize(0.04)
        h1.GetXaxis().SetTitleOffset(0.8)

        h1.GetYaxis().SetTitle("Samples")
        h1.GetYaxis().SetTitleSize(0.05)
        h1.GetYaxis().SetLabelSize(0.04)
        h1.GetYaxis().SetTitleOffset(1)

        c.SetRightMargin(0.05)
        c.SetLeftMargin(0.12)
        c.SetBottomMargin(0.1)
        c.SetTopMargin(0.08)

        h1.SetFillColor(kRed-7)
        h1.SetFillStyle(1001)

        h1.Draw()

        c.Update()

        max_line = c.GetUymax()
        line = TLine(means[i],0,means[i],max_line)
        line.SetLineWidth(3)
        line.SetLineColor(kGray+3)
        line.SetLineStyle(3)
        line.Draw("same")

        line2 = TLine(modes[i],0,modes[i],max_line)
        line2.SetLineWidth(3)
        line2.SetLineColor(kGray+3)
        line2.SetLineStyle(7)
        line2.Draw("same")

        tex = TLatex()
        tex.SetNDC()
        tex.SetTextSize(0.04)
        tex.DrawLatex(0.5,0.8,bins[i])

        CMS_lumi.CMS_lumi(c, iPeriod, iPos)
        c.SaveAs(outdir+"/mean_mode_"+hname.replace("h_","")+".pdf")
        outfile.cd()
        c.Write()
        c.Close()
            
            
    infile1.Close()
    outfile.Close()
    

