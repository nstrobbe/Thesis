from ROOT import *
import os
import plotTools
import CMS_lumi, tdrstyle

def getGluinoCrossSection(mgluino,f):
    h = f.Get("gluino8TeV_NLONLL")
    binnr = h.GetXaxis().FindBin(mgluino)
    xsec = h.GetBinContent(binnr)
    return xsec

def getStopCrossSection(mstop,f):
    h = f.Get("stop8TeV_NLONLL")
    binnr = h.GetXaxis().FindBin(mstop)
    xsec = h.GetBinContent(binnr)
    return xsec

if __name__ == "__main__":

    # CMS style plots
    tdrstyle.setTDRStyle()

    CMS_lumi.lumi_8TeV = "19.7 fb^{-1}"
    CMS_lumi.writeExtraText = 0
    CMS_lumi.extraText = "Preliminary"
    CMS_lumi.cmsTextSize = 0.29
    #CMS_lumi.lumiTextSize = 0.5

    iPos = 0#11
    if( iPos==0 ): CMS_lumi.relPosX = 0.12+0.08
    iPeriod = 2

    plotTools.SetColorPaletteSMS()

    dirbase = "./rootfiles/"
    indir = dirbase
    outdir = "./"
            
    lumi = 19712.
    
    infile1 = TFile.Open(indir+"/rzrBoost_forThesis_T1ttcc_1000_26_1.root")
    infile2 = TFile.Open(indir+"/rzrBoost_forThesis_T1ttcc_1000_75_50.root")

    outfile = TFile.Open(indir+"/plots_EffDrop.root","RECREATE")
        
    hnames = ["h_met","h_rsq"]
    xtitles = ["#slash{E}_{T}^{miss} (GeV)","R^{2}"]
        
    for i,hname in enumerate(hnames):
        h1 = infile1.Get(hname)
        h2 = infile2.Get(hname)


        c = TCanvas(hname.replace("h_","c_"))
        c.cd()

        h1.GetXaxis().SetTitle(xtitles[i])
        h1.GetXaxis().SetTitleSize(0.05)
        h1.GetXaxis().SetLabelSize(0.04)
        h1.GetXaxis().SetTitleOffset(1.1)

        h1.GetYaxis().SetTitle("A.U.")
        h1.GetYaxis().SetTitleSize(0.05)
        h1.GetYaxis().SetLabelSize(0.04)
        h1.GetYaxis().SetTitleOffset(1.6)

        c.SetRightMargin(0.05)
        c.SetLeftMargin(0.16)
        c.SetBottomMargin(0.14)
        c.SetTopMargin(0.08)

        h1.SetLineColor(kCyan+2)
        h1.SetLineWidth(2)
        h2.SetLineColor(kRed+2)
        h2.SetLineWidth(2)

        #h = TH1D("bla","bla",h1.GetNbinsX(), h1.GetXaxis().GetBinLowEdge(1), h1.GetXaxis().GetBinUpEdge(h1.GetNbinsX()))
        #h.SetMaximum(0.025)
        #h.Draw()
        if i == 1:
            c.SetLogy()
        h1.DrawNormalized("histsame")
        h2.DrawNormalized("histsame")

        leg = TLegend(0.47,0.68,0.9,0.9,"T1ttcc, m_{#tilde{g}} = 1000 GeV")
        leg.AddEntry(h1,"m_{#tilde{t}_{1}} = 26 GeV, m_{#tilde{#chi}^{0}_{1}} = 1 GeV","l")
        leg.AddEntry(h2,"m_{#tilde{t}_{1}} = 75 GeV, m_{#tilde{#chi}^{0}_{1}} = 50 GeV","l")
        leg.SetBorderSize(0)
        leg.Draw()
        c.Update()

        if i == 1:
            max_line = TMath.Power(10,c.GetUymax())
            line = TLine(0.08,0,0.08,max_line)
            line.SetLineWidth(2)
            line.SetLineColor(kBlack)
            line.Draw("same")

            arrow = TArrow(0.08,0.00005,0.18,0.00005,0.03,"|>")
            arrow.SetAngle(40)
            arrow.SetLineWidth(2)
            arrow.Draw()

        CMS_lumi.CMS_lumi(c, iPeriod, iPos)
        c.SaveAs(outdir+"/Eff_drop_"+hname.replace("h_","")+".pdf")
        outfile.cd()
        c.Write()
        c.Close()
            
            
    infile1.Close()
    infile2.Close()
    outfile.Close()
    

