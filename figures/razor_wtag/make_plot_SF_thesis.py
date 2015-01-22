from ROOT import *
import CMS_lumi, tdrstyle

# xmin, xmax, value, stat, syst
#Wmass_info = [[200,220,1.046,0.069,0.012],
#              [220,240,1.014,0.040,0.004],
#              [240,260,1.152,0.032,0.002],
#              [260,280,1.154,0.025,0.010],
#              [280,300,1.137,0.026,0.005],
#              [300,320,1.022,0.017,0.005],
#              [320,340,1.131,0.017,0.007],
#              [340,360,1.158,0.018,0.002],
#              [360,380,1.175,0.021,0.005],
#              [380,400,1.175,0.029,0.001],
#              [400,500,1.154,0.016,0.002],
#              [500,1000,1.175,0.017,0.004]
#              ]

Wmass_info = [
    [200.0,220.0,1.144,0.050,0.012],
    [220.0,240.0,1.118,0.028,0.024], 
    [240.0,260.0,1.193,0.024,0.008], 
    [260.0,280.0,1.250,0.018,0.015], 
    [280.0,300.0,1.273,0.017,0.021], 
    [300.0,320.0,1.126,0.013,0.010], 
    [320.0,340.0,1.199,0.012,0.017], 
    [340.0,360.0,1.298,0.013,0.007], 
    [360.0,380.0,1.327,0.016,0.008], 
    [380.0,400.0,1.339,0.025,0.007], 
    [400.0,500.0,1.339,0.012,0.005], 
    [500.0,1000.0,1.370,0.011,0.000]
    ]
antitagged_info = [
    [200.0,220.0,1.217,0.072,0.032],
    [220.0,240.0,1.186,0.037,0.046],
    [240.0,260.0,1.216,0.033,0.011],
    [260.0,280.0,1.319,0.024,0.019],
    [280.0,300.0,1.379,0.022,0.037],
    [300.0,320.0,1.203,0.017,0.015],
    [320.0,340.0,1.244,0.016,0.026],
    [340.0,360.0,1.409,0.019,0.015],
    [360.0,380.0,1.448,0.022,0.020],
    [380.0,400.0,1.472,0.033,0.014],
    [400.0,500.0,1.487,0.017,0.012],
    [500.0,1000.0,1.505,0.014,0.004]
    ]
tagged_info = [
    [200.0,220.0,1.043,0.068,0.012], 
    [220.0,240.0,1.013,0.040,0.004], 
    [240.0,260.0,1.156,0.032,0.002], 
    [260.0,280.0,1.158,0.024,0.010], 
    [280.0,300.0,1.147,0.025,0.004], 
    [300.0,320.0,1.033,0.016,0.005], 
    [320.0,340.0,1.143,0.016,0.007], 
    [340.0,360.0,1.167,0.018,0.001], 
    [360.0,380.0,1.180,0.020,0.005], 
    [380.0,400.0,1.175,0.028,0.000], 
    [400.0,500.0,1.153,0.015,0.002], 
    [500.0,1000.0,1.175,0.016,0.004]
    ]
FullFast_info = [
    [200.0,250.0,0.952,0.010], 
    [250.0,350.0,0.912,0.012], 
    [350.0,1000.0,0.891,0.026]
    ]


def makeSFplot(info,name,title,ymin=0.6,ymax=1.4):
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
    L = 0.12*W_ref
    R = 0.06*W_ref

    c.SetLeftMargin( L/W )
    c.SetRightMargin( R/W )
    c.SetTopMargin( T/H )
    c.SetBottomMargin( B/H )

    g_stat = TGraphErrors()
    g_tot = TGraphErrors()

    for i,p in enumerate(info):
        x = p[0]+0.5*(p[1]-p[0])
        g_stat.SetPoint(i,x,p[2])    
        g_stat.SetPointError(i,0.5*(p[1]-p[0]),p[3])    
        tot_error = sqrt(p[3]*p[3]+p[4]*p[4])
        g_tot.SetPoint(i,x,p[2])
        g_tot.SetPointError(i,0.5*(p[1]-p[0]),tot_error)    
        print p[0], "-", p[1], ": ", p[2], "+- %.3f"%(tot_error) 

    g_tot.SetFillColor(kCyan-8)
    g_tot.SetFillStyle(1001)
    g_tot.SetLineColor(kCyan-8)
    g_tot.Draw("a2")
    g_tot.GetXaxis().SetTitle("p_{T} (CA8 jet) (GeV)")
    g_tot.GetXaxis().SetTitleOffset(1.1)
    g_tot.GetXaxis().SetRangeUser(100,1000)
    g_tot.GetYaxis().SetTitle(title)
    g_tot.GetYaxis().SetTitleOffset(0.9)
    g_tot.GetYaxis().SetRangeUser(ymin,ymax)

    g_stat.SetLineColor(kBlack)
    g_stat.Draw("Zpsame")
        
    leg = TLegend(0.55,0.25,0.8,0.4,"")
    leg.SetFillStyle(0)
    leg.SetBorderSize(0)
    leg.AddEntry(g_stat,"stat only","lep")
    leg.AddEntry(g_tot,"stat + syst","f")
    leg.Draw()

    c.cd()
    CMS_lumi.CMS_lumi(c, iPeriod, iPos)

    c.SaveAs("SF_%s_Thesis.pdf"%(name))

def makeSFplot_nosyst(info,name,title,ymin=0.6,ymax=1.4):
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
    L = 0.14*W_ref
    R = 0.06*W_ref

    c.SetLeftMargin( L/W )
    c.SetRightMargin( R/W )
    c.SetTopMargin( T/H )
    c.SetBottomMargin( B/H )

    g_stat = TGraphErrors()

    for i,p in enumerate(info):
        x = p[0]+0.5*(p[1]-p[0])
        g_stat.SetPoint(i,x,p[2])    
        g_stat.SetPointError(i,0.5*(p[1]-p[0]),p[3])    

    g_stat.GetXaxis().SetTitle("p_{T} (CA8 jet) (GeV)")
    g_stat.GetXaxis().SetTitleOffset(1.1)
    g_stat.GetXaxis().SetRangeUser(100,1000)
    g_stat.GetYaxis().SetTitle(title)
    g_stat.GetYaxis().SetTitleOffset(1.05)
    g_stat.GetYaxis().SetRangeUser(ymin,ymax)
    g_stat.SetLineColor(kBlack)
    g_stat.Draw("aZpsame")
        
    leg = TLegend(0.55,0.25,0.8,0.4,"")
    leg.SetFillStyle(0)
    leg.SetBorderSize(0)
    leg.AddEntry(g_stat,"stat only","lep")
    leg.Draw()

    c.cd()
    CMS_lumi.CMS_lumi(c, iPeriod, iPos)

    c.SaveAs("SF_%s_Thesis.pdf"%(name))

if __name__ == "__main__":

    tdrstyle.setTDRStyle()

    #makeSFplot(Wmass_info,"Wmass","W mass tagging efficiency",0.8,1.6)
    #makeSFplot(antitagged_info,"Wantitagged","W antitagging efficiency",0.8,1.6)
    #makeSFplot(tagged_info,"Wfake","W fake rate")

    makeSFplot(Wmass_info,"Wmass","W mass-tag fake rate SF ",0.8,1.6)
    makeSFplot(antitagged_info,"Wantitagged","W anti-tag fake rate SF",0.8,1.6)
    makeSFplot(tagged_info,"Wfake","W tag fake rate SF")
    makeSFplot_nosyst(FullFast_info,"FullFast","W tag efficiency Full/Fast SF",0.7,1.04)
