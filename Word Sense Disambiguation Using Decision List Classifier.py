'''WORD SENSE DISAMBIGUATION USING DECISION LIST CLASSIFIER'''

#Date: 22nd April 2021.
#Author: Amit Raj

# The accuracy of the decision list is :76.98412698412699

# col_0    phone  product
# row_0                  
# phone       50        7
# product     22       47



import bs4 as bs
import nltk
import math
import re
import sys
from nltk.tokenize import RegexpTokenizer
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.probability import ConditionalFreqDist
from nltk.probability import ConditionalProbDist, ELEProbDist

def main():
 ##### check open the input files and check whether the input 
	### is less than required #####  

	inpt = sys.argv[1:]
	if(len(inpt) < 5):
		file1 = sys.argv[1]
		file2 = sys.argv[2]
		decision_list = sys.argv[3]
		my_line_answer = sys.argv[4]

		with open(file1, "r") as textdata:
			parsed_textdata = bs.BeautifulSoup(textdata,'html.parser')

			print(parsed_textdata.prettify())

		with open(file2, "r") as test_data:
			parsed_testdata = bs.BeautifulSoup(test_data,'html.parser')

			print(parsed_testdata.prettify())

		####  Read the sense and instance id from the train_xml file ####

		sense = []
		inst_id = []
		for l in parsed_textdata.find_all('answer'):
		    sense.append(l.get('senseid'))
		    inst_id.append(l.get('instance'))
		print(sense[:10])
		print(inst_id[:10])


		#### Read the text file and then collect all the instances and contents
		### related

		text = []
		for m in parsed_textdata.find_all('instance'):
		    x = ""
		    for t in m.find_all('s'):
		        x = x+ " "+ t.get_text()
		    x = x.lower()
		    x = x.replace("lines", "line")
		    tokenizer = RegexpTokenizer(r'\w+')
		    tokens = tokenizer.tokenize(x)
		    text.append(tokens)
		print(text[:10])


		#### Create a dictionary for the sense, instance id and text in train ####

		datadict = []
		for i in range(len(sense)-1):
		    dict1 = dict()
		    dict1['id'] = inst_id[i]
		    dict1['sense'] = sense[i]
		    dict1['text'] = text[i]
		    datadict.append(dict1)
		print(datadict)

		cfdist = ConditionalFreqDist()
		
		### The word index position from the ambiguous word ###

		pos = [-2, -1, +1]


		#### calculate conditional frequency distribution ###

		cfdist = ConditionalFreqDist()
		print(len(datadict))
		count = 0
		overall = 0
		for i in pos:
		    for values in datadict:
		        word = "line"
		        sense, text = values['sense'], values['text']
		        word_ind = text.index(word)
		        count += 1
		        print(count)
		        if len(text) > word_ind+1: 
		            if i > 0:
		                strings = "+" + str(i) + "_" + text[word_ind+i]
		                print(strings)
		                cfdist[strings][sense] += 1 
		            else:
		                strings = str(i) + "_" + text[word_ind+i]
		                print(strings)
		                cfdist[strings][sense] += 1  
		                   

		print(cfdist)    

		#### calculate the conditional probability distribution using 
		#### ELEProbDist method and calculate the log likeihood values.

		declist = []
		cpdist = ConditionalProbDist(cfdist, ELEProbDist, 10)
		for strings in cpdist.conditions():
		    cpphone = cpdist[strings].prob("phone")
		    cpprod = cpdist[strings].prob("product")
		    result = cpphone / cpprod
		    if result == 0:
		        result_lkelhd = 0
		    else:
		        result_lkelhd = math.log(result, 2) 
		    declist.append([strings, result_lkelhd, "phone" if result_lkelhd > 0 else "product"])
		    declist.sort(key=lambda strings: math.fabs(strings[1]), reverse=True)
		#print(declist)
		for stg in cpdist.conditions():
		    print(stg)
		    print(stg[1])
		    
		print(declist)
		print(len(cpdist.conditions())) 


		#### Calculate the frequency of the sense values ####

		freq_1=0
		freq_2=0
		for data_sense in datadict:
		    if data_sense['sense'] == "phone":
		        freq_1 += 1
		    else:
		        freq_2 += 1
		if freq_1 > freq_2:
		    highest_freq = "phone"
		else:
		    highest_freq = "product"
		    
		print(highest_freq)
		print(freq_1)
		print(freq_2)


		#### creating the id and text for textxml data ####

		#sense_test = []
		id_test = []
		for l1 in parsed_testdata.find_all('instance'):
		    #sense_test.append(l1.get('senseid'))
		    id_test.append(l1.get('id'))
		#print(sense_test[:10])
		#print(id_test[:10])
		text_test = []
		for m1 in parsed_testdata.find_all('instance'):
		    x1 = ""
		    for t1 in m1.find_all('s'):
		        x1 = x1+ " "+ t1.get_text()
		    x1 = x1.lower()
		    x1 = x1.replace("lines", "line")
		    tokenizer = RegexpTokenizer(r'\w+')
		    tokens1 = tokenizer.tokenize(x1)
		    text_test.append(tokens1)
		#print(text_test[:2])
		print(len(id_test))
		print(len(text_test))
		print(id_test[125])


		#### creating the test id dictionary using id and text from the test xml ####
		testdict = []
		print(len(id_test))
		for i in range(len(id_test)):
		    print(i)
		    dict2 = dict()
		    dict2['id'] = id_test[i]
		    dict2['text'] = text_test[i]
		    testdict.append(dict2)


		####  Predicting the sense for the test xml data #### 
		####  prediction takes place by using the decision list from the train data ####

		pred_sen = []
		count_phone = 0
		count_product = 0
		for values1 in testdict:
		    word = "line"
		    id_extract = values1['id']
		    text_test = values1['text']
		    for strings in declist:
		        word_index = text_test.index(word)
		        x, y = strings[0].split("_")
		        x = int(x)
		        test_word_ind = word_index + x
		        if len(text_test) > word_index+1: 
		            test_word =  text_test[test_word_ind]            
		        else:
		            test_word = ""
		        
		        if test_word == y:
		            if strings[1] > 0:
		                predicted_sense = "phone"
		                break
		            elif strings[1] < 0:
		                predicted_sense = "product"
		                break
		                
		        if test_word == "":
		            predicted_sense = highest_freq
		            break
		    if predicted_sense == "phone":
		        count_phone += 1
		        
		    if predicted_sense == "product":
		        count_product += 1
		        
		    
		    pred_sen.append(f'<answer instance="{id_extract}" senseid="{predicted_sense}"/>')
		    print(f'<answer instance="{id_extract}" senseid="{predicted_sense}"/>')
		    
		print(count_phone, count_product)

		##### writing the data of the program that is decision list and 
		#### the line answers of the program to the file my_line_answer.txt

		with open(decision_list, 'w') as output:
		    for string in declist:
		        output.write("<answer instance="'%s\n' % string)

		with open (my_line_answer, 'w') as output:
			for string in pred_sen:
				output.write('%s\n' % string)


	else:
		print("Please input the necessary input arguments")

if __name__ == '__main__':
	main()


