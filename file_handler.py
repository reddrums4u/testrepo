import os
import shutil
from racing_post_sort import *
import csv
# Set the source and destination folder paths
src_folder = 'to_process'
arc_folder = 'archive'
res_folder = 'results'
cwd=os.getcwd()


# Get a list of all files in the source folder

file_list = os.listdir(src_folder)


# Loop over each file in the list

def handle_file(file_list):
    for file_name in file_list:
    
        per_pos=file_name.find(".")

        print("What to call the output file",file_name[0:per_pos]+"_processed"+file_name[per_pos:])
        exit_name=file_name[0:per_pos]+"_processed"+file_name[per_pos:]
        
        file_w_path=os.path.join(src_folder,file_name)
        print("Opening file:",file_w_path)
        # open the CSV file in read mode
        with open(file_w_path, mode='r') as csv_file:
            # read each row of the CSV file
            # create a reader object
            csv_reader = csv.reader(csv_file, delimiter =',')
        
        
            output=data_crunch(csv_reader)
            
                          
        #Results full file path name creation
        full_res_path = os.path.join(res_folder, 'data_'+file_name)
        topline_res_path=os.path.join(res_folder,'top_line_'+file_name)
    
        with open(full_res_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(output[0])
        print("Full result file written at:", full_res_path)
        
        
        with open(topline_res_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(output[1])
        print("Full topline file written at:", topline_res_path)
    
    
    
    
    
    
    
    
        # Full file path for archived file
        arc_w_path=os.path.join(arc_folder,exit_name)
        # Copy the source data file to the destination folder
        shutil.copy(file_w_path, arc_w_path)
        print("Moved source file to archive folder")
        # Delete the original file
        os.remove(file_w_path)
        print("Deleted source file in To process folder")


handle_file(file_list)

