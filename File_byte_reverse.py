import os
import argparse
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', type=str, required=True,  help='Please input filename. eg. -f exp.jpg or C:\\exp.jpg')
	parser.add_argument('-s', '--size', type=int, required=True,  help='Please enter the unit of bytes to be split. eg. -s 8')
	parser.add_argument('-o', '--output', type=str, required=True, help='Please input output filename. eg. -o flag.zip')
	args = parser.parse_args()
	if os.path.isfile(args.output):
		print('{} is already exist'.format(args.output))
		exit()
	if not os.path.isfile(args.file):
		print('{} can\'t open , please check if the file exists'.format(args.file))
		exit()
	f=open(args.file,'rb').read()
	Size=int(len(f))
	if  args.size >= Size:
		print('Please input  split size < file size({})'.format(Size))
		exit()
	while Size % args.size != 0:
		Size+=1
	g=open(args.output,'ab')
	g.write(f[args.size-1::-1])
	for i in range(2,int(Size/args.size)+1):
		a=i*args.size-1
		g.write(f[a:a-args.size:-1])
	print('success!\noutput is {}'.format(args.output))	
