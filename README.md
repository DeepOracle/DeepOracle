# How to run the program

- set hyperparameters(learning rate, iterations)
  - for digital data, we suggest learning rate = 1e-6
  - for string data, we suggest learning rate between 1e-5 and 1e-4 
- set the path of the method and corresponding loading method
- run main.py

# Python file

- main.py: the main file of our approach
- cal_RP.py: calculate the recall and precision of these methods
- cal_ROC.py: calculate ROC and AUC of these methods
- IST.py: the main file of the baseline
- count_label.py: calculate the number of top k in the file
- Coverage.py: sort the test dataset according to line.txt
- draw_pic.py: draw the picture
- loadData.py: load data

# Dataset

1000,000 for training, 100,000 for testing

- before_data.txt: the input dataset of this method(1100000,)
- after_data.txt: the output dataset of this method(1100000,)
- label.txt: the label of the dataset(1100000,)

# Daikon

- daikon_input: the input of the test dataset generated after daikon inspection(100000,)
- daikon_output.txt: the output of the test dataset generated after daikon inspection(100000,)
- daikon_label.txt: the label of the test dataset generated after daikon inspection(100000,)

# Line coverage

- line.txt: the line coverage of each test case(100000,)
- coverage_line.txt: the line coverage of each test case after checking the line coverage(100000,)
- coverage_input.txt: the input of the test dataset generated after checking the line coverage(100000,)
- coverage_output.txt: the output of the test dataset generated after checking the line coverage(100000,)
- coverage_label.txt: the label of the test dataset generated after checking the line coverage(100000,)
- **Some method lack of line.txt because the method has no branch and the line coverage of any test case is the same(M1-M11,M14)**

# Output file of the network

- 1.txt: the output vector of our approach(100000,)
- 2.txt：the output vector of baseline, the size of training dataset is 1000(100000,)
- 3.txt：the output vector of baseline, the size of training dataset is equal to our approach(100000,)
