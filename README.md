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
     - 1 box 1 day all the profiles (3D field) :
       - HSW24 :  error: Exceeded step memory limit at some point.
       - BDW28 : the 6h maximum are not enough to produce the 3D file
       - VISU : the 6h maximum are not enough to produce the 3D file
     - 1 box 1 day mean profile :
       - HSW24 : error: Exceeded step memory limit at some point.
       - BDW28 : error: Exceeded step memory limit at some point.  
       - VISU : the 6h maximum are not enough to produce the 3D file       
     - 1 box 1 day all profiles separate :
       - HSW24 : 1 profile/hour, so max 23 profiles in one job
       - BDW28 : 1 profile/hour, so max 23 profiles in one job
       - VISU : 1 profile/hour, so max 6 profiles in one job
       - in parallel : 129 600 procs, pas réalisable, aussi le nombre de fichiers est prohibitif
     - nouvelles stratégies :
       - changer les chunks + restreindre dès le début à la boîte GS toute entière -> ça n'a pas l'air de changer grand chose ...
       - restreindre les niveaux verticaux ?
       - utiliser dask et chunks pour écrire wprimebprime en 3D pour toute la boite GS ?
     
     
