# Word-Sense-Disambuguation-Using-Decision-List-Classifier

The program implements a decision list classifier to perform word sense disambiguation. The program uses features from Yarowsky’s method which resulted
in an accurate classifier for our program. 

#### python decision-list.py line-train.xml line-test.xml my-decision-list.txt >
#### my-line-answers.txt

This command should learn a decision list from line-train.xml and apply that decision list to each
of the sentences found in line-test.xml in order to assign a sense to the word line.
