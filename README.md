# Internet_Archive_Downloader

Python utility for downloading files from an archive on the Internet Archive. Uses the `internetarchive` package for downloading files. Utilizes multiprocessing to download multiple files simultaneously and speed up the download of archives with a large number of files.

## Usage ##

Can be used by either running `multi_download.py` with required arguments or
by importing the ArchiveDownloader function into your own program.

#### `multi_download.py` Command Line Arguments

```
-i, --identifier
    type=str
    Identifier of archive item to download from.
```
```
-o, --output_loc
    type=str
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
