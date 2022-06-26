import os

folders = os.listdir('new_sqm_averages')
for folder in folders:
    os.rename('new_sqm_averages/'+folder, 'new_sqm_averages/'+folder+'.jpg')
