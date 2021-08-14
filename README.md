# How to run the program

- set hyperparameters(learning rate, iterations)
  - for digital data, we suggest learning rate = 1e-6
  - for string data, we suggest learning rate between 1e-5 and 1e-4 
- set the path of the method and corresponding loading method
- run main.py

# How to generate dataset

- step 1: Generate the legal input of MUT randomly

- step 2: Perform the method call procedure

- step 3: Capture the output

- step 4: Repeat step 1

- Example:

  ````java
  int train_iter = 1000000;
  int test_iter = 100000;
  for (int i=0;i<train_iter+test_iter;i++){
      String token = "";
      int num = random.nextInt(10)+1;
      for(int j=0;j<num;j++){
          char ch;
          if(random.nextInt(2)==0){
              ch = (char)('a'+random.nextInt(26));
          }else{
              ch = (char)('A'+random.nextInt(26));
          }
          token+=ch;
      }
      final Lexer lexer = getLexer(token, formatWithEscaping);
      Token result = lexer.nextToken(new Token());
      String input = token;
      String output = result.toString();
  	# save the input and output    
  }
  ````

# Python

- main.py: the main file of our approach
- count_label.py: calculate the number of top k in the file
- Coverage.py: sort the test dataset according to line.txt
- daikon.py: sort the test dataset according to the output of **Daikon**
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
- **Some method lack of daikon.txt because they failed to execute Daikon(M14,M22)**

# Line coverage

- line.txt: the line coverage of each test case(100000,)
- coverage_line.txt: the line coverage of each test case after checking the line coverage(100000,)
- coverage_input.txt: the input of the test dataset generated after checking the line coverage(100000,)
- coverage_output.txt: the output of the test dataset generated after checking the line coverage(100000,)
- coverage_label.txt: the label of the test dataset generated after checking the line coverage(100000,)
- **Some method lack of line.txt because the method has no branch and the line coverage of any test case is the same(M1-10,M12,M14-15,M17)**

- 

