#!/usr/bin/env python
#
"""
This script extracts profiles of temperature, salinity and vertical velocity in 1degx1deg boxes and one date in eNATL60-BLBT02. It computes buoyancy and spatially filters it and the vertical velocity. The resulting product of the two quantities (w' and b') are saved in a single file
"""

##imports

import xarray as xr 
import dask 
import numpy as np 
import os 
import time 
import glob
import datetime
import pandas as pd
import sys

today=datetime.date.today()

import sys
sys.path.insert(0,'/scratch/cnt0024/hmg2840/albert7a/DEV/git/xscale')
import xscale

## data location and gridfile

data_dir = '/store/CT1/hmg2840/lbrodeau/eNATL60/eNATL60-BLBT02-S/'
gridfile='/store/CT1/hmg2840/lbrodeau/eNATL60/eNATL60-I/mesh_mask_eNATL60_3.6_lev1.nc4'
dsgrid=xr.open_dataset(gridfile,chunks={'x':1000,'y':1000})

## box indices 
def read_csv(box):
    boxes=pd.read_csv('/scratch/cnt0024/hmg2840/albert7a/DEV/git/dataset-Redouane-project-Balaji/boxes/boxes_'+str(box)+'_1x1_eNATL60.csv',sep = '\t',index_col=0)
    imin=boxes['imin']
    imax=boxes['imax']
    jmin=boxes['jmin']
    jmax=boxes['jmax']
    box_name=boxes.index
    return imin,imax,jmin,jmax,box_name

## functions useful for computations

def compute_buoy(t,s):
    rau0  = 1000
    grav  = 9.81
    buoy= -1*(grav/rau0)*sigma0(t,s)
    return buoy

def sigma0(t,s):
    zrau0=1000
    zsr=np.sqrt(np.abs(s))
    zs=s
    zt=t
    zr1 = ( ( ( ( 6.536332e-9*zt-1.120083e-6 )*zt+1.001685e-4)*zt - 9.095290e-3 )*zt+6.793952e-2 )*zt+999.842594
    zr2= ( ( ( 5.3875e-9*zt-8.2467e-7 )*zt+7.6438e-5 ) *zt - 4.0899e-3 ) *zt+0.824493
    zr3= ( -1.6546e-6*zt+1.0227e-4 ) *zt-5.72466e-3
    zr4= 4.8314e-4
    sigma0=( zr4*zs + zr3*zsr + zr2 ) *zs + zr1 - zrau0
    return sigma0

def filt(w):
    win_box2D = w.window
    win_box2D.set(window='hanning', cutoff=90, dim=['x', 'y'], n=[90, 90])
    bw = win_box2D.boundary_weights(drop_dims=[])
    w_LS = win_box2D.convolve(weights=bw)
    w_SS=w-w_LS
    return w_SS

## main computation function
def compute_mean_wprime_bprime(date,ibox,profile_name,imin,imax,jmin,jmax,box_name):
    print('read the data')
    tfilename = sorted(glob.glob(data_dir+'*/eNATL60-BLBT02_1h_*_gridT_'+date+'-'+date+'.nc'))
    tfile=tfilename[0]
    dst=xr.open_dataset(tfile,chunks={'x':1000,'y':1000,'time_counter':1,'deptht':1})
    tdata=dst['votemper'][:,:,np.min(jmin)-60:np.max(jmax)+60,np.min(imin)-60:np.max(imax)+60]
    deptht=dst['deptht']
    sfilename = sorted(glob.glob(data_dir+'*/eNATL60-BLBT02_1h_*_gridS_'+date+'-'+date+'.nc'))
    sfile=sfilename[0]
    dss=xr.open_dataset(sfile,chunks={'x':1000,'y':1000,'time_counter':1,'deptht':1})
    sdata=dss['vosaline'][:,:,np.min(jmin)-60:np.max(jmax)+60,np.min(imin)-60:np.max(imax)+60]
    wfilename = sorted(glob.glob(data_dir+'*/eNATL60-BLBT02_1h_*_gridW_'+date+'-'+date+'.nc'))
    wfile=wfilename[0]
    dsw=xr.open_dataset(wfile,chunks={'x':1000,'y':1000,'time_counter':1,'depthw':1})
    wdata=dsw['vovecrtz'][:,:,np.min(jmin)-60:np.max(jmax)+60,np.min(imin)-60:np.max(imax)+60]
    print('compute buoyancy')
    buoy=compute_buoy(tdata,sdata)
    print('filter w')
    wprime=filt(wdata)
    print('filter buoyancy')
    bprime=filt(buoy)
    wprime_rechunk=wprime.chunk(chunks={'x':1000,'y':1000,'time_counter':1,'depthw':300}) 
    wprime_ont=wprime_rechunk.interp(depthw=deptht.values)
    wprime_goodw=wprime_ont.rename({'depthw':'deptht'})
    wprimebprime=wprime_goodw*bprime
    profile=wprimebprime[:,:,jmin[ibox]-(np.min(jmin)-60):jmax[ibox]-(np.min(jmin)-60),imin[ibox]-(np.min(imin)-60):imax[ibox]-(np.min(imin)-60)].mean(dim={'x','y','time_counter'})
    print('to dataset')
    dataset=profile.to_dataset(name='wprimebprime')
    dataset['wprimebprime'].attrs=tdata.attrs
    dataset['wprimebprime'].attrs['standard_name']='vertical flux of small scales buoyancy'
    dataset['wprimebprime'].attrs['long_name']='wprimebprime'
    dataset['wprimebprime'].attrs['units']='m2/s3'
    dataset.attrs['global_attribute']= 'vertical flux of small scales buoyancy times w profile averaged over 24h and in '+box_name[ibox]+' computed on occigen '+str(today)
    print('to netcdf')
    dataset.to_netcdf(path=profile_name,mode='w')
    return profile


## parser and main
def script_parser():
    """Customized parser.
    """
    from optparse import OptionParser
    usage = "usage: %prog box k[which box] date"
    parser = OptionParser(usage=usage)
    return parser

def main():
    parser = script_parser()
    (options, args) = parser.parse_args()
    if len(args) < 3: # print the help message if number of args is not 3.
        parser.print_help()
        sys.exit()
    optdic = vars(options)

    box = str(args[0])
    k = int(args[1])
    date = str(args[2])

    before=datetime.datetime.now()
    print("Start at ", before.strftime("%Y-%m-%d %H:%M:%S"))
    imin,imax,jmin,jmax,box_name=read_csv(box)
    profile_name='/scratch/cnt0024/hmg2840/albert7a/eNATL60/eNATL60-BLBT02-S/RL/'+str(box)+'/eNATL60'+str(box)+box_name[k]+'-BLBT02_y'+date[0:4]+'m'+date[4:6]+'d'+date[6:9]+'_wprimebprime-profile.nc'

    if not os.path.exists(profile_name):
        print("Computing wprimebprime profile")
        compute_mean_wprime_bprime(date,k,profile_name,imin,imax,jmin,jmax,box_name)
    else:
        print("Not computing, profiles already exist")


    after=datetime.datetime.now()
    print("End at ", after.strftime("%Y-%m-%d %H:%M:%S"))
    print("Execution time", after-before)


if __name__ == '__main__':
    sys.exit(main() or 0)

