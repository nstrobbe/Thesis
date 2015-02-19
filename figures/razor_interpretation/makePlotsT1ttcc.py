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
    CMS_lumi.lumiTextSize = 0.35

    iPos = 0#11
    if( iPos==0 ): CMS_lumi.relPosX = 0.12+0.08
    iPeriod = 2

    #gStyle.SetOptStat(0)
    #gStyle.SetLabelSize(0.045,"xyz")
    #gStyle.SetTitleSize(0.06,"xyz")
    #gROOT.ForceStyle()
    plotTools.SetColorPaletteSMS()

    dirbase = "./rootfiles/"
    indir = dirbase
    bfile = TFile.Open(dirbase+"rzrBoostMC_bg.root")
    counts = bfile.Get("counts")

    outdir = "./"
            
    crosssectionfilename = "referenceXSecs.root"
    cf = TFile.Open(crosssectionfilename)

    lumi = 19712.
    
    DMs = ["T1t1t"]
    #DMs = ["T1ttcc_DM-25"]
    #DMs = ["T1ttcc_DM-10","T1ttcc_DM-25","T1ttcc_DM-80"]
    
    for DM in DMs:
        #dm = DM[-2:]
        #CMS_lumi.cmsText = "#splitline{pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow #tilde{t}_{1} t, #tilde{t}_{1} #rightarrow c #tilde{#chi}^{0}_{1}}{m_{#tilde{t}_{1}} - m_{#tilde{#chi}^{0}_{1}} = %s GeV}" % (dm)

        dm = "175"
        CMS_lumi.cmsText = "#splitline{pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow #tilde{t}_{1} t, #tilde{t}_{1} #rightarrow t #tilde{#chi}^{0}_{1}}{m_{#tilde{t}_{1}} - m_{#tilde{#chi}^{0}_{1}} = %s GeV}" % (dm)

        infile = TFile.Open(indir+"/rzrBoostMC_SMS_SMS-"+DM+".root")
        
        outfile = TFile.Open(indir+"/"+DM+".root","RECREATE")
        
        #h_nevents = infile.Get("h_mstop_mLSP_Pileup")
        h_nevents = infile.Get("h_mstop_mLSP_ISR")
        
        basename = "h_mstop_mLSP"
        selections2 = ["HCAL_noise","vertexg0","njetge3","HLT","jet1ptg200",
                      "SIG","neleeq0","nmueq0","trackIso",
                      "g1Mb0Ll","g1Mbg1W0Ll","1Mbg1W0Ll","g2Mbg1W0Ll",
                      "g1Mbg1W0Ll_mdPhiHat4","g1Mbg1W0Ll_mdPhiHatg4",
                      "g1Mbg1W0Ll_mdPhi0p3","g1Mbg1W0Ll_mdPhig0p3",
                      "g1Mbg1W0Ll_mdPhi0p5","g1Mbg1W0Ll_mdPhig0p5",
                      "g1Mb0Wg1uW0Ll",
                      "0Lb0Ll","0Lbg1uW0Ll","0Lbg1uW0Ll_mdPhi0p3","0Lbg1uW0Ll_mdPhiHat4","0Lbg1uW0Ll_mdPhiHat5","0Lbg1W0Ll",
                      "1Ll","g1Mb1Ll","g1Mbg1W1Ll","g1Mbg1W1LlmT100_mdPhig0p5","1Mbg1W1LlmT100","g2Mbg1W1LlmT100",
                      "g1Mbg1W1LlmT",
                      "0Lb1Ll","0Lbg1Y1Ll","0Lbg1Y1LlmT100","0Lbg1Y1LlmT_mdPhig0p5",
                      "2munoZmass","2mu","2mu0el","0Lb2mu0el","0Lbg1Y2mu0el","g1Mb2mu0el","g1Mbg1Y2mu0el",
                      "2elnoZmass","2el","2el0mu","0Lb2el0mu","0Lbg1Y2el0mu","g1Mb2el0mu","g1Mbg1Y2el0mu",
                      "2lnoZmass","2l","2l0ol","0Lb2l0ol","0Lbg1Y2l0ol","g1Mb2l0ol","g1Mbg1Y2l0ol",
                      ]
        selections = ["g1Mbg1W0Ll_mdPhig0p5"]

        for selection in selections:
            # make plots
            hname = basename + "_" + selection
            print hname
            h = infile.Get(hname)
            print h
            # efficiency
            h_eff = h.Clone("eff")
            h_eff.Divide(h_nevents)
            # if "T1ttcc" in DM or "T1t1t" in DM:
            #     h_eff.GetXaxis().SetTitle("m_{gluino} (GeV)")
            # if "T1ttcc_old" in DM:
            #     h_eff.GetXaxis().SetTitle("m_{stop} (GeV)")
            # if "T2tt" in DM:
            #     h_eff.GetXaxis().SetTitle("m_{stop} (GeV)")
            # h_eff.GetYaxis().SetTitle("m_{LSP} (GeV)")
            # h_eff.GetZaxis().SetTitle("Efficiency")
            # h_eff.GetXaxis().SetTitleSize(0.05)
            # h_eff.GetXaxis().SetLabelSize(0.04)
            # h_eff.GetXaxis().SetTitleOffset(1.1)
            # h_eff.GetYaxis().SetTitleSize(0.05)
            # h_eff.GetYaxis().SetLabelSize(0.04)
            # h_eff.GetYaxis().SetTitleOffset(1.2)
            # h_eff.GetZaxis().SetTitleSize(0.05)
            # h_eff.GetZaxis().SetLabelSize(0.04)
            # h_eff.GetZaxis().SetTitleOffset(1.5)
            # h_eff.SetTitle("Efficiency for "+DM)
            # c_eff = TCanvas("efficiency_"+DM+"_"+selection)
            # c_eff.cd()
            # c_eff.SetRightMargin(0.2)
            # c_eff.SetLeftMargin(0.13)
            # c_eff.SetBottomMargin(0.12)
            # c_eff.SetTopMargin(0.08)
            # h_eff.DrawCopy("colz")
            # CMS_lumi.CMS_lumi(c_eff, iPeriod, iPos)
            # c_eff.SaveAs(outdir+"/efficiency_"+DM+"_"+selection+".pdf")
            # outfile.cd()
            # c_eff.Write()
            # c_eff.Close()
            
            # #events
            h_events = h_eff.Clone("h_events")
            for x in range(1,h_eff.GetNbinsX()+1):
                for y in range(1,h_eff.GetNbinsY()+1):
                    eff = h_eff.GetBinContent(x,y)
                    if "T1ttcc_old" in DM:
                        sf = 0.0243547
                    elif "T1ttcc" in DM or "T1t1t" in DM:
                        sf = getGluinoCrossSection(h_eff.GetXaxis().GetBinLowEdge(x),cf)
                    elif "T2tt" in DM:
                        sf = getStopCrossSection(h_eff.GetXaxis().GetBinLowEdge(x),cf)
                    #print h_eff.GetXaxis().GetBinLowEdge(x), sf
                    h_events.SetBinContent(x,y,eff*sf)
                    
            h_events.Scale(lumi)
            if "T1ttcc" in DM or "T1t1t" in DM:
                h_events.GetXaxis().SetTitle("m_{gluino} (GeV)")
            if "T1ttcc_old" in DM:
                h_eff.GetXaxis().SetTitle("m_{stop} (GeV)")
            if "T2tt" in DM:
                h_events.GetXaxis().SetTitle("m_{stop} (GeV)")
            h_events.GetYaxis().SetTitle("m_{LSP} (GeV)")
            h_events.GetZaxis().SetTitle("Events / bin")
            h_events.SetTitle("Number of events for "+DM+" (19.712 fb-1)")
            c_events = TCanvas("events_"+DM+"_"+selection)
            c_events.cd()
            h_events.GetXaxis().SetTitleSize(0.05)
            h_events.GetXaxis().SetLabelSize(0.04)
            h_events.GetXaxis().SetTitleOffset(1.1)
            h_events.GetYaxis().SetTitleSize(0.05)
            h_events.GetYaxis().SetLabelSize(0.04)
            h_events.GetYaxis().SetTitleOffset(1.2)
            h_events.GetZaxis().SetTitleSize(0.05)
            h_events.GetZaxis().SetLabelSize(0.04)
            h_events.GetZaxis().SetTitleOffset(1.2)
            c_events.SetRightMargin(0.18)
            c_events.SetLeftMargin(0.13)
            c_events.SetBottomMargin(0.12)
            c_events.SetTopMargin(0.12)
            #c_events.SetTopMargin(0.08)
            c_events.SetLogz()
            h_events.DrawCopy("colz")
            CMS_lumi.CMS_lumi(c_events, iPeriod, iPos)
            c_events.SaveAs(outdir+"/events_"+DM+"_"+selection+".pdf")
            outfile.cd()
            c_events.Write()
            c_events.Close()
            
            # significance
            
            # binnumber = counts.GetXaxis().FindBin(selection)
            # B = counts.GetBinContent(binnumber)
            # print B
            # h_signif = h_events.Clone("signif")
            # h_signif.Scale(1./TMath.Sqrt(B))
            # if "T1ttcc" in DM or "T1t1t" in DM:
            #     h_signif.GetXaxis().SetTitle("m_{gluino} (GeV)")
            # if "T1ttcc_old" in DM:
            #     h_eff.GetXaxis().SetTitle("m_{stop} (GeV)")
            # if "T2tt" in DM:
            #     h_signif.GetXaxis().SetTitle("m_{stop} (GeV)")
            # h_signif.GetYaxis().SetTitle("m_{LSP} (GeV)")
            # h_signif.GetZaxis().SetTitle("S/#sqrt{B}")
            # h_signif.SetTitle("significance S/sqrt(B) for "+DM)
            # h_signif.GetXaxis().SetTitleSize(0.05)
            # h_signif.GetXaxis().SetLabelSize(0.04)
            # h_signif.GetXaxis().SetTitleOffset(1.1)
            # h_signif.GetYaxis().SetTitleSize(0.05)
            # h_signif.GetYaxis().SetLabelSize(0.04)
            # h_signif.GetYaxis().SetTitleOffset(1.2)
            # h_signif.GetZaxis().SetTitleSize(0.05)
            # h_signif.GetZaxis().SetLabelSize(0.04)
            # h_signif.GetZaxis().SetTitleOffset(1.2)
            # c_signif = TCanvas("significance_"+DM+"_"+selection)
            # c_signif.cd()
            # c_signif.SetRightMargin(0.18)
            # c_signif.SetLeftMargin(0.13)
            # c_signif.SetBottomMargin(0.12)
            # c_signif.SetTopMargin(0.08)
            # h_signif.SetMaximum(10)
            # h_signif.DrawCopy("colz")
            # CMS_lumi.CMS_lumi(c_signif, iPeriod, iPos)
            # c_signif.SaveAs(outdir+"/significance_"+DM+"_"+selection+".pdf")
            # outfile.cd()
            # c_signif.Write()
            # c_signif.Close()
            
        infile.Close()
        outfile.Close()
    
        # print region, selection, h_eff.GetBinContent(1), h_events.GetBinContent(1), B, h_signif.GetBinContent(1)
    
    bfile.Close()
    cf.Close()
