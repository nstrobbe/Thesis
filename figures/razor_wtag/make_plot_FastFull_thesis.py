from ROOT import *
import CMS_lumi, tdrstyle

def makeEffplot(inputfilename,name,title,tag,ymin=0.6,ymax=1.4):
    info = TFile.Open(inputfilename)

    c = TCanvas("c_"+name,"", 800,600)
    c.cd()

    CMS_lumi.lumi_8TeV = "19.7 fb^{-1}"
    CMS_lumi.writeExtraText = 0
    CMS_lumi.extraText = " Preliminary"
    CMS_lumi.cmsText = ""
    iPos = 0#11                                                                                                                                       
    if( iPos==0 ): CMS_lumi.relPosX = 0.12
    iPeriod = 2
    H_ref = 600
    W_ref = 800
    W = W_ref
    H  = H_ref

    # references for T, B, L, R 
    T = 0.08*H_ref
    B = 0.15*H_ref
    L = 0.13*W_ref
    R = 0.06*W_ref

    c.SetLeftMargin( L/W )
    c.SetRightMargin( R/W )
    c.SetTopMargin( T/H )
    c.SetBottomMargin( B/H )

    g_stat = TGraphErrors()

    h = info.Get(name)

    for i in xrange(h.GetNbinsX()):
        xmin = h.GetXaxis().GetBinLowEdge(i+1)
        xmax = h.GetXaxis().GetBinUpEdge(i+1)
        x = xmin+0.5*(xmax-xmin)
        y = h.GetBinContent(i+1)
        e = h.GetBinError(i+1)
        if y != 0:
            g_stat.SetPoint(i,x,y)    
            g_stat.SetPointError(i,0.5*(xmax-xmin),e)    

    g_stat.GetXaxis().SetTitle("p_{T} (CA8 jet) (GeV)")
    g_stat.GetXaxis().SetTitleOffset(1.1)
    g_stat.GetXaxis().SetRangeUser(100,1000)
    g_stat.GetYaxis().SetTitle(title)
    g_stat.GetYaxis().SetTitleOffset(1.1)
    g_stat.GetYaxis().SetRangeUser(ymin,ymax)

    g_stat.SetLineColor(kBlue+2)
    g_stat.Draw("Zpasame")
        
    text = TText(0.2,0.8,tag)
    text.SetNDC()
    #text.SetTextAlign(31)
    text.SetTextSize(0.07)
    text.Draw()

    c.cd()
    CMS_lumi.CMS_lumi(c, iPeriod, iPos)

    c.SaveAs("Eff_%s_%s_Thesis.pdf"%(name,tag))

    info.Close()

if __name__ == "__main__":

    tdrstyle.setTDRStyle()

    makeEffplot("Wtag_plots_Full.root", "ratio_tagged_all", "W boson tag efficiency","FullSim",0,1)
    makeEffplot("Wtag_plots_Fast.root", "ratio_tagged_all", "W boson tag efficiency","FastSim",0,1)
    makeEffplot("Wtag_plots_Full_varbin.root", "ratio_tagged_all_varbin", "W boson tag efficiency","FullSim",0.42,0.68)
    makeEffplot("Wtag_plots_Fast_varbin.root", "ratio_tagged_all_varbin", "W boson tag efficiency","FastSim",0.42,0.68)

