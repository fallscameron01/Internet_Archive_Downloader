from multiprocessing import Pool
import internetarchive
import numpy as np

def download_files(files):
    identifier = "" # identifier of item to download from
    output_loc = "" # output directory on local disk

    internetarchive.download(identifier, destdir=output_loc, verbose=True, ignore_existing=True, files=files)


def run_parallel():
    ## TODO: update documentation
    ## TODO: turn vars into parameters
    identifier = ""
    output_loc = ""
    glob_str = r"" # glob pattern to filter items to download

    # names of files to download
    names = np.array([f.name for f in internetarchive.get_files(identifier, glob_pattern=glob_str)])
    
    process_num = 16 # number of processes to run
    pool = Pool(processes=process_num) # pool object with number of processes to run

    task_lists = np.array_split(names, process_num) # split files among processes
    task_lists = [list(l) for l in task_lists] # convert back to python list
  
    # map the function to the list and pass function and task_lists as arguments
    # starts downloads
    pool.map(download_files, task_lists)

# Driver code
if __name__ == '__main__':
    ## TODO: add command line arguments
    run_parallel()
