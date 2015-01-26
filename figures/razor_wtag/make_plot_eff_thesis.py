from ROOT import *
import CMS_lumi, tdrstyle


def makeEffplot(info,name,title,ymin=0.6,ymax=1.4):
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
    g_tot = TGraphErrors()

    h = info.Get(name)
    h_up = info.Get(name+"up")
    h_down = info.Get(name+"down")

    for i in xrange(h.GetNbinsX()):
        xmin = h.GetXaxis().GetBinLowEdge(i+1)
        xmax = h.GetXaxis().GetBinUpEdge(i+1)
        x = xmin+0.5*(xmax-xmin)
        y = h.GetBinContent(i+1)
        e = h.GetBinError(i+1)
        e_sys = 0.5*abs(h_up.GetBinContent(i+1) - h_down.GetBinContent(i+1))
        g_stat.SetPoint(i,x,y)    
        g_stat.SetPointError(i,0.5*(xmax-xmin),e)    
        tot_error = sqrt(e*e+e_sys*e_sys)
        g_tot.SetPoint(i,x,y)
        g_tot.SetPointError(i,0.5*(xmax-xmin),tot_error)    
        print i+1, ": ", x , "+- %.3f"%(tot_error) 

    g_tot.SetFillColor(kMagenta-8)
    g_tot.SetFillStyle(1001)
    g_tot.SetLineColor(kMagenta-8)
    g_tot.Draw("a2")
    g_tot.GetXaxis().SetTitle("p_{T} (CA8 jet) (GeV)")
    g_tot.GetXaxis().SetTitleOffset(1.1)
    g_tot.GetXaxis().SetRangeUser(100,1000)
    g_tot.GetYaxis().SetTitle(title)
    g_tot.GetYaxis().SetTitleOffset(1.1)
    g_tot.GetYaxis().SetRangeUser(ymin,ymax)

    g_stat.SetLineColor(kBlack)
    g_stat.Draw("Zpsame")
        
    leg = TLegend(0.55,0.25,0.8,0.4,"")
    leg.SetFillStyle(0)
    leg.SetBorderSize(0)
    leg.AddEntry(g_stat,"stat only","lep")
    leg.AddEntry(g_tot,"stat + syst","f")
    leg.Draw()

    text = TText(0.85,0.8,"Simulation")
    text.SetNDC()
    text.SetTextAlign(31)
    text.SetTextSize(0.07)
    text.Draw("same")

    c.cd()
    CMS_lumi.CMS_lumi(c, iPeriod, iPos)

    c.SaveAs("Eff_MC_%s_Thesis.pdf"%(name))

def makeEffplot_data(info,name,title,ymin=0.6,ymax=1.4):
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
        g_stat.SetPoint(i,x,y)    
        g_stat.SetPointError(i,0.5*(xmax-xmin),e)    

    g_stat.GetXaxis().SetTitle("p_{T} (CA8 jet) (GeV)")
    g_stat.GetXaxis().SetTitleOffset(1.1)
    g_stat.GetXaxis().SetRangeUser(100,1000)
    g_stat.GetYaxis().SetTitle(title)
    g_stat.GetYaxis().SetTitleOffset(1.1)
    g_stat.GetYaxis().SetRangeUser(ymin,ymax)

    g_stat.SetLineColor(kBlack)
    g_stat.Draw("Zpasame")
        
    leg = TLegend(0.55,0.25,0.8,0.4,"")
    leg.SetFillStyle(0)
    leg.SetBorderSize(0)
    leg.AddEntry(g_stat,"stat only","lep")
    leg.Draw()

    text = TText(0.85,0.8,"Data")
    text.SetNDC()
    text.SetTextAlign(31)
    text.SetTextSize(0.07)
    text.Draw()

    c.cd()
    CMS_lumi.CMS_lumi(c, iPeriod, iPos)

    c.SaveAs("Eff_Data_%s_Thesis.pdf"%(name))


if __name__ == "__main__":

    tdrstyle.setTDRStyle()

    inputfilename = "Wtag_plots_pt.root"
    inputfile = TFile.Open(inputfilename)

    makeEffplot(inputfile, "ratio_pt_Wmass_all_MC", "W mass-tagging fake rate",0,0.15)
    makeEffplot(inputfile, "ratio_pt_antitagged_all_MC", "W anti-tagging fake rate",0,0.09)
    makeEffplot(inputfile, "ratio_pt_tagged_all_MC", "W tagging fake rate",0,0.06)

    makeEffplot_data(inputfile, "ratio_pt_Wmass_all_Data", "W mass-tagging fake rate",0,0.15)
    makeEffplot_data(inputfile, "ratio_pt_antitagged_all_Data", "W anti-tagging fake rate",0,0.09)
    makeEffplot_data(inputfile, "ratio_pt_tagged_all_Data", "W tagging fake rate",0,0.06)
