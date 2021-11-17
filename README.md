# S3-dowloader
Easily download files from any S3 Bucket!

## Usage
Firstly you need to setup the conf.json configuration file.
- files_list_path: the relative path to a csv file containing on every line the result of list_files.py script
- bucket_name: the name of the S3 bucket
- folder_path: the path *inside the bucket* to the folder you want to download from
- destination_path: the local path where the files will be saved to

Then to call the downloader script just write in the command line:
```python3 download_files.py -n NUMBER_OF_FILES [-sl SIZE_LIMIT_IN_BYTES]```
