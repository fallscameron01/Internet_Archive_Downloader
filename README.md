# Internet_Archive_Downloader

Python utility for downloading files from an archive on the Internet Archive. Uses the `internetarchive` package for downloading files. Utilizes multiprocessing to download multiple files simultaneously and speed up the download of archives with a large number of files.

## Usage ##

Can be used by either running `multi_download.py` with required arguments or
by importing the ArchiveDownloader function into your own program.

#### Details

An archive download requires specifying the identifier of the archive. The identifier tag can be found on the archive's details page. Additionally, a glob string may be specified to filter which items to download from an archive. The user must specify a location for the download to be output on disk.

The `ArchiveDownloader` class speeds up the downloading of an archive with a large number of files by splitting the files to download among simultaneous processes. This allows multiple files to be downloaded at the same time, increasing the total bandwidth available. By default, the `ArchiveDownloader` class will use 4 processes, but this number can be increased or decreased by specifying the `process_num` parameter.

#### `multi_download.py` Command Line Arguments

```
-i, --identifier
    type=str
    Required
    Identifier of archive item to download from.
```
```
-o, --output_loc
    type=str
    Required
    Output location to download items to.
```
```
-g, --glob_str
    type=str
    Default: None
    Glob string to filter items within archive for download.
```
```
-p, --process_num
    type=int
    Default: 4
    Number of simultaneous download processes to run.
```
#### Example Command Line Usage

The command `python multi_download.py -i example_archive_item -o C:\My_Output_Folder -g "*.jpg" -p 16` will download jpg files from "example_archive_item" to the folder "C:\My_Output_Folder" using 16 processes.

