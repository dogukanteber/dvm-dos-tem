#!/bin/bash

# Paths here assume that you are running inside 
# docker container with the input catalog and a 
# workflows directory mounted in /data


# Copy paste as needed to run workflow...
# Or maybe this will actually run as a script??
# Haven't tried doing it all at once


# 1) setup working directories:
for i in basecase modopt1 modopt2 modopt3;
do
  ./scripts/setup_working_directory.py \
  --input-data-path /data/input-catalog/cru-ts40_ar5_rcp85_ncar-ccsm4_CALM_Betty_Pingo_MNT_10x10/ \
  /data/workflows/workshop-lab2/$i
done

# 2) run mod script
for i in 1 2 3;
do
  ./scripts/Input_exp.py --opt $i \
  --inpath /data/input-catalog/cru-ts40_ar5_rcp85_ncar-ccsm4_CALM_Betty_Pingo_MNT_10x10/ \
  --outpath /data/workflows/workshop-lab2/modopt$i
done

# Now you might want to run the Input_exp.py --plot-inputs option to 
# to see what you've got! **Beaware** that if you have
# been working inside a docker container up to this point, and you want
# to run the plotting script inside the docker container, you will want
# to change the plt.show() call in the plot function to 
# plt.save_fig('your file.png') with an appropriate file name.
# Also you will likely want to adjust the plot so it is only showing
# the data of interest.  When you run with plt.show() and get the
# interactive viewer you can zoom as needed, but it is hard to get the
# interactive viewer to show up from w/in a docker container. So save a
# figure instead. 
# Alternatively, if you have a functioning python environment outside of
# the docker container, you can work there.

