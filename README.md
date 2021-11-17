# S3-dowloader
Easily download files from any S3 Bucket!

## Usage
Firstly you need to setup the conf.json configuration file.
- files_list_path: the relative path to a csv file containing the files in the bucket
- bucket_name: the name of the S3 bucket
- folder_path: the path **inside the bucket** to the folder you want to download from
- destination_path: the local path where the files will be saved to

Then to call the downloader script just write in the command line:
```
python3 download_files.py -n NUMBER_OF_FILES [-sl FILE_SIZE_LIMIT_IN_BYTES]
```

## How to generate the required csv file
The S3 CLI offers a nice command line option to retrieve all the filenames in a bucket folder. The output will be something like: last-modified-date, last-modified-time, size, file-key.
The command is the following:
```
aws s3 ls s3://BUCKET_PATH > file_list.txt
```
The *read_files.py* script will take the *file_list.txt* file and generate a nice csv file which can be used for this downloader
```
python3 read_files.py
```