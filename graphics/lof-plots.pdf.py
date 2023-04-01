#!/usr/bin/env python3
from matplotlib.backends.backend_pdf import PdfPages
from utils import filename, save2pdf, setup
from utils.plots_helper import lof

make, fname = filename("lof-plots.pdf")
dfile = "../datasets/real/intel/sensors-1000-dirty.txt"

pdf = PdfPages(fname)
for k in [2, 10]:
    title = "Local Outlier Factor\n$k=" + str(k) + "$"
    ofile = "../results/k" + str(k) + "data01.out"
    setup()
    lof(title, dfile, ofile)
    save2pdf(pdf)
pdf.close()
