import os

def main():
	files_read = 0
	with open('file_list.csv', 'w') as outf:
		with open('file_list.txt', 'r') as inf:
			line = inf.readline()
			while line:
				line = inf.readline()
				if line is not None and len(line) > 10:
					files_read += 1
					listed = line.split()
					csvved = ','.join(listed)
					outf.write(csvved + '\n')

print(f"Copied a total of {files_read} files")

if __name__ == '__main__':
	main()