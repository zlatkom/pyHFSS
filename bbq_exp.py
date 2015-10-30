from hfss import get_active_project
import bbq
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import *
plt.close('all')

project = get_active_project()
design = project.get_design("Dump")

bbq_exp = bbq.Bbq(project, design, append_analysis=False, calculate_H=True)

bbq_exp.do_bbq('$LJ_Dump', variations=['1'], modes=[1], surface=False, dielectrics=['Sapphire_Dump','Sapphire_Readout'])
#surface not working yet

#ba=bbq_exp.bbq_analysis
#bbq_exp.bbq_analysis.plot_Hparams(variable_name='_$Circuit_offset_Dump', modes=[1,2,3])
#bbq_exp.bbq_analysis.print_Hparams(variation='4',modes=[0,1,2])

#data_filename = r'Y:\Data\PumpingCats\HFSS\Analyzed\2015-10-02_closerPads\Dump1\Dump1_20151014_204956.hdf5'
#bbq_analysis_exp = bbq.BbqAnalysis(data_filename)
#fig, ax = bbq_analysis_exp.plot_Hparams(variable_name='_$r_pad')
#bbq_analysis_exp.plot_Hparams(variable_name='_$LJ_Dump')