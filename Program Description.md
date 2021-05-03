# Word-Sense-Disambuguation-Using-Decision-List-Classifier

## Program

The program implements a decision list classifier to perform word sense disambiguation. The program uses features from Yarowsky’s method which resulted
in an accurate classifier for our program. 

#### python decision-list.py line-train.xml line-test.xml my-decision-list.txt > my-line-answers.txt

The above command learns a decision list from line-train.xml and applies that decision list to every sentence found in line-test.xml in order to assign a sense to the word line. . As output,thw program shows the decision list it learns as my-decision-list.txt and the file my-decision-list.txt is intended to be used as a log file in debugging this program. The program also outputs the answer tags it creates for every sentence as STDOUT. The answer tags are in the same format as found in line-answers.txt.

## Data Description

line-train.xml contains examples of the word line used in the sense of a phone line and a product line where the correct sense is marked in the text (to serve as an example from which to learn). linetest.xml contains sentences that use the word line without any sense being indicated, where the correct answer is found in the file line-answers.txt. The line-train.xml and linetest.xml are available in the directory directory called line-data. 
