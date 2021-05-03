'''Scorrer for the decision list'''

#Date: 22nd April 2021.
#Amit Raj

import re
import pandas as pd
import sys
import os
import bs4

def extract_line(file):
    with open(file, "r", encoding ='utf-8') as tags:
        dd = tags.read()
        dcode = str(dd).strip()
        dcode = dcode.replace('\n','')
    return dcode

def extract_data(data):
    instances, senses =[],[] 
    for vv in bs4.BeautifulSoup(data,'html.parser'):
        instances.append(vv.attrs['instance'])
    for ss in bs4.BeautifulSoup(data, 'html.parser'):
        senses.append(ss.attrs['senseid'])
    return instances, senses

def accuracy(pred_file, gd_file):
	pod,ww = {}, {}

	for vv in bs4.BeautifulSoup(pred_file, "html.parser"):
	    vv.find_all("answer")
	    pod.update({vv.get("instance"):vv.get("senseid")})

	for sppd in bs4.BeautifulSoup(gd_file, "html.parser"):
	    ww.update({sppd.get("instance"):sppd.get("senseid")})

	mnv =0
	for keys1,keys2 in zip(pod.items(), ww.items()):
	    if (keys1 == keys2):
	        mnv+=1

	# print(mnv)
	# print(len(ww))

	accuracy = ((mnv/len(ww)) * 100)
	print("The accuracy of the decision list is :{0}".format(accuracy))
	return pod, ww

#     print 'Not', x_values, y_values
    #     if(list(pod.keys)[i] == list(ww.keys)[i]):
#         if(list(pod.value)[i] == list(ww.value)[i])
#             print("vv")


def confusion_matrix(pod, ww):
	prd_senses = (list(pod.items()))
	gld_senses = (list(ww.items()))

	prd_sens_list,gld_sense_list = [],[]

	for i in range(0, len(pod.keys())):
	    prd_sens_list.append((prd_senses[i][1]))
	    
	for j in range(0, len(pod.keys())):
	    gld_sense_list.append((gld_senses[j][1]))

	# print(pd.Series(prd_sens_list))

	# print(pd.Series(gld_sense_list))

	mMatrix = pd.crosstab(pd.Series(prd_sens_list), pd.Series(gld_sense_list))
	print(mMatrix)


def main():
	predicted = sys.argv[1]
	gold_std_file = sys.argv[2]

	pred_file = extract_line(predicted)

	gd_file = extract_line(gold_std_file)
	
	dict1, dict2 = accuracy(pred_file,gd_file)

	confusion_matrix(dict1, dict2)


if __name__ == '__main__':
	main()
