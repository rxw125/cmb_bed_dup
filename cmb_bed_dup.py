#!/usr/bin/env python3
"""
combine dup regions in bed file(3 columns)
"""
import argparse
import os
import sys
import re
bin = os.path.abspath(os.path.dirname(__file__))
__author__='Ren Xue'
__mail__= 'xueren@genome.cn'
__date__= '2019年12月16日 星期一 13时16分32秒'



def main():
	parser=argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter,epilog='author:\t{0}\nmail:\t{1}\ndate:\t{2}\n'.format(__author__,__mail__,__date__))
	parser.add_argument('-o','--outfile',help='outfile name',dest='outfile',type=str,required=True)
	parser.add_argument('-i','--input',help='outfile name',dest='input',type=str,required=True)
	args=parser.parse_args()
	info={}
	dup={}
	print ("##### Anyalysis begin\n")
	with open(args.input,"r") as file:
		for line in file:
			line=line.rstrip("\n")
			chr=line.split("\t")[0]
			start=line.split("\t")[1]
			end=line.split("\t")[2]
			if not chr in info:
				info[chr]={}
			if not start in info[chr]:
				info[chr][start]=end
			else:
				if int(end) >=int(info[chr][start]):
					info[chr][start]=end
	for c in info:
		if not c in dup:
			dup[c]={}
		start_list=[int(x) for x in list(info[c].keys())]
		start_list.sort()
		start=str(start_list[0])
		dup[c][start]=0
		for i in start_list:
			i=str(i)
			end=info[c][i]
			if i in dup[c]:
				if int(end) >= int(dup[c][i]):
					dup[c][i]=end
			else:
				if int(i) >=int(start) and int(i) <=(int(dup[c][start])):
					if int(end)>=int(dup[c][start]):
						dup[c][start]=end
					else:continue
				elif int(i)>int(dup[c][start]):
					dup[c][i]=end
					start=i
	out=open(args.outfile,"w")
	for c in sorted(dup):
		sort_list=[int(x) for x in list(dup[c].keys())]
		sort_list.sort()
		for s in sort_list:
			s=str(s)
			out.write("{0}\t{1}\t{2}\n".format(c,s,dup[c][s]))
	out.close()
	print ("##### Anyalysis End\n")


if __name__=="__main__":
	main()
