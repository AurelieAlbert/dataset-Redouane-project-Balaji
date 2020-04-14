# dataset-Redouane-project-Balaji

Here I gather all the scripts needed for the preparation of Redouane's dataset in Balaji MOGPA project.
The initial material set up with Anna Sommer is available here : https://github.com/auraoupa/preparation_eNATL60_profiles_ANNA

## The boxes 

  - files defining the 1°x1° boxes indexes in eNATL60:
    - https://github.com/AurelieAlbert/dataset-Redouane-project-Balaji/blob/master/boxes/boxes_GS_1x1_eNATL60.csv
    - 
    -
  - plots to see the boxes :
    - https://github.com/AurelieAlbert/dataset-Redouane-project-Balaji/blob/master/boxes/test_map_boxes_1x1_GS.png
    -
    -
  
## The predictors

  - script for one 1°x1° box and one day mean profiles : https://github.com/AurelieAlbert/dataset-Redouane-project-Balaji/blob/master/predictors/extractions-gradients-all-variables-boxes.py
  - scalability tests :
    - 1 box 1 day on :
       - HSW24 : 1h30
       - BDW28 :  1h50
       - VISU : 1h30
    - 1 box 1 month ?
    - 1 box 3 month ?
    - 10 box 1 day ?
    
## The result w'b'

  - script
  - scalability tests :
     - 1 box 1 day all the profiles or mean profile :
       - HSW24 :  error: Exceeded step memory limit at some point.
       - BDW28 :   error: Exceeded step memory limit at some point.
       - VISU : the 6h maximum are not enough to produce the 3D file
     - 1 box 1 day 1 profile (out of 8740) :
       - HSW24 : error: Exceeded step memory limit at some point.
       - BDW28 : error: Exceeded step memory limit at some point. 
       - VISU : 1h33
     - the result is : I can squeeze 3 profiles (maybe 4 ?) in a row per script, 112 times in parallel on visu ? hence 27 jobs of 6h (162h, 7 days) each to complete all the profiles in 1 box for 1 day
    
    
