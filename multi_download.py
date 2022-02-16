from multiprocessing import Pool
import internetarchive
import numpy as np

class ArchiveDownloader:
    '''
    Internet Archive download utility utilizing multiprocessing.
    '''
    def __init__(self, archive_identifier : str, output_loc : str, glob_str : str = None, process_num : int = 4) -> None:
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
    
    def set_params(self, archive_identifier : str, output_loc : str, glob_str : str = None, process_num : int = 4) -> None:
        '''
        Sets parameters for an archive download.

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
        
        Returns
        -------
        None
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

    def download_archive(self) -> None:
        '''
        Runs a download task. Splits downloading of an archive over given number of processes.

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
    Driver for running archive download task from command line.

    Command Line Arguments
    ----------------------
    -i, --identifier
        type=str
        Required
        Identifier of archive item to download from.
    -o, --output_loc
        type=str
        Required
        Output location to download items to.
    -g, --glob_str
        type=str
        Default: None
        Glob string to filter items within archive for download.
    -p, --process_num
        type=int
        Default: 4
        Number of simultaneous download processes to run.
    '''
    import argparse

    ## Define command line argument parser and arguments ##

    archive_identifier = "" # identifier of item to download from
    output_loc = "" # output directory on local disk
    glob_str = None # glob pattern to filter items to download within archive
    process_num = 4 # number of simultaneous download processes to run

    parser = argparse.ArgumentParser(description="Downloads items from an archive on the InternetArchive. Must specify archive identifier and output location.")

    parser.add_argument("-i", "--identifier", type=str, help="Identifier of archive item to download from.")
    parser.add_argument("-o", "--output_loc", type=str, help="Output location to download items to.")
    parser.add_argument("-g", "--glob_str", type=str, help="Glob string to filter items within archive for download. Default: None.")
    parser.add_argument("-p", "--process_num", type=int, help="Number of simultaneous download processes to run. Default: 4.")

    args = parser.parse_args()

    ## Validate arguments ##
    if not args.identifier:
        raise RuntimeError("Must specify archive identifier with -i <identifier>.")
    if not args.output_loc:
        raise RuntimeError("Must specify output location with -o <output_loc>.")
    if not args.glob_str:
        glob_str = None
    if not args.process_num:
        process_num = 4

    ## Run download task ##
    downloader = ArchiveDownloader(archive_identifier, output_loc, glob_str, process_num)
    downloader.download_archive()
