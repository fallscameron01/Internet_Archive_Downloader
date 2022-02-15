## TODO: update documentation

import internetarchive

identifier = "" # identifier of item to download from
output_loc = "C:\\" # output directory on local disk
glob_str = r"" # glob pattern to filter items to download

internetarchive.download(identifier, destdir=output_loc, verbose=True, ignore_existing=True, glob_pattern=glob_str)
