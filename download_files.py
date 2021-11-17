import boto3
from tqdm import tqdm
import os
import random
import argparse
import json

def main(num_files, size_limit):
	s3 = boto3.resource('s3')

	files_list_path, bucket_name, key_pre, samples_dir= read_conf()

	files_list = []

	# Read all the filenames of the available files in the bucket_name
	with open(files_list_path, 'r') as f:
		line = f.readline()
		
		# Read all lines until eof
		while line:
			try:
				listed = line.split(',')
				file_key = listed[3]
				file_key = file_key[:-1] # Every entry in the csv file is /n terminated
				file_size = int(listed[2])
				if file_size <= size_limit or size_limit == -1:
					files_list.append(file_key)
			except Exception as e:
				print(f"Damaged entry for key {file_key}")
			line = f.readline()
		
		if size_limit == -1:
			print(f"Total files found in the files list: {len(files_list)}")
		else:
			print(f"Total files found in the files list smaller than {size_limit} bytes: {len(files_list)}")

	# Check I didn't request too many files
	if num_files > len(files_list):
		print('Requested too many files! Cutting to the maximum number available...')
		num_files = len(files_list)

	# Get the filenames already downloaded
	if os.path.exists(samples_dir):
		existing_files = os.listdir(samples_dir)
		num_existing_files = len(existing_files)
		print(f"Files already downloaded are: {num_existing_files}")
	else:
		existing_files = []
		os.mkdir(samples_dir)
		print("Destination folder doesn't exist, I'll create it")
		num_existing_files = 0
	
	# Compute how many I have to download
	num_downloads = num_files - num_existing_files

	final_file_list = list(set(files_list) - set(existing_files))
	random.shuffle(final_file_list)

	print(f"Downloading {num_downloads} files")

	for i in tqdm(range(num_downloads), position=0, leave=True):
		key_post = final_file_list[i]
		full_key = key_pre + '/' + key_post
		try:
			s3.meta.client.download_file(bucket_name, full_key, os.path.join(samples_dir, key_post))
		except Exception as e:
			print(e)
			print(full_key)

def read_conf():
	with open('conf.json',) as f:
		data = json.load(f)
		return data['files_list_path'], data['bucket_name'], data['folder_path'], data['destination_path']


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-n', required=True, help='Number of desired files to be downloaded')
	parser.add_argument('-sl', default=-1, help='Maximum byte size of a single file')
	args = parser.parse_args()
	num_files = int(args.n)
	size_limit = int(args.sl)

	main(num_files, size_limit)
