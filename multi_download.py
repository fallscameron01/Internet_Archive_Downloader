from multiprocessing import Pool
import internetarchive
import numpy as np

class ArchiveDownloader:
    '''
    Archive download utility utilizing multiprocessing.
    '''
    def __init__(self, archive_identifier : str, output_loc : str, glob_str : str, process_num : int) -> None:
        '''
        Initializes utility for downloading archive with given parameters.

        Parameters
        ----------
        archive_identifier : str
            identifier of archive item to download from 
        output_loc : str
            output directory for downloads on local disk
        glob_str : str
            glob pattern to filter items to download within archive
        process_num : int
            number of simultaneous download processes to run
        '''
        self.archive_identifier = archive_identifier
        self.output_loc = output_loc
        self.glob_str = glob_str
        self.process_num = process_num
        
    def download_files(self, files : list) -> None:
        '''
        Downloads the given files.

        Parameters
        ----------
        files : list
            list of the files to download from the archive
        
        Returns
        -------
        None
        '''
        internetarchive.download(self.identifier, destdir=output_loc, verbose=True, ignore_existing=True, files=files)

    def run_parallel(self) -> None:
        '''
        Runs a parallel download task. Splits downloading of an archive over given number of processes.

        Returns
        -------
        None
        '''
        # names of files to download
        names = np.array([f.name for f in internetarchive.get_files(self.identifier, glob_pattern=self.glob_str)])
        
        pool = Pool(processes=self.process_num) # pool object with number of processes to run

        task_lists = np.array_split(names, self.process_num) # split files among processes
        task_lists = [(list(l)) for l in task_lists] # convert back to python list
    
        # map the function to the list and pass function and task_lists as arguments
        # starts downloads
        pool.map(self.download_files, task_lists)

# Driver code
if __name__ == '__main__':
    '''
    Driver for running download task from command line.
    '''
    ## TODO: add command line arguments
    archive_identifier = "" # identifier of item to download from
    output_loc = "" # output directory on local disk
    glob_str = r"" # glob pattern to filter items to download within archive
    process_num = 4 # number of simultaneous download processes to run

    downloader = ArchiveDownloader(archive_identifier, output_loc, glob_str, process_num)
    downloader.run_parallel()
