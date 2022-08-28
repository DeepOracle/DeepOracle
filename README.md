
# Table of Contents
- [Introduction](#introduction) 
- [Structure](#structure)
- [SourceCode Description](#sourcecode-description-code)
- [Operating Instruction](#operating-instruction)
    - [Test case generation](#test-case-generation)
    - [Environmental requirements](#environmental-requirements)
    - [DeepOracle](#deeporacle)
    - [Random-based selection](#random-based-selection)
    - [Coverage-based selection](#coverage-based-selection)
    - [Daikon-based selection](#daikon-based-selection)
# Introduction
This is the replication package of the paper "Generating and Exploiting Approximate Unit Test Oracles". It is composed of tools (including the proposed approach and baseline approaches) and  data employed in the evaluation
# Structure
- Code: source code of the experiment
- Data: Top-100 result of experiment
- Data/DeepOracle: The experimental results of DeepOracle
- Data/Random: The experimental results of random-based selection
- Data/Coverage: The experimental results of coverage-based selection
- Data/Daikon: The experimental results of daikon-based selection
- TM: real world defects method employed by the evaluation
- MM: mutated method employed by ghe evaluation
- DeepOracle.zip: plugin project of DeepOracle

# SourceCode Description (/Code)

- main.py: main file for DeepOracle
- load.py: Loading and processing data
- Coverage.py: main file for coverage-based selection
- daikon.py: main file for daikon-based selection
- DataGenerator.jar: Jar package for random generation of test cases
- TestOracle: IDEA plug-in project that randomly generates test cases
# Operating Instruction
## Test case generation
- Download DataGenerator.jar,TestOracle project
- Run TestOracle as IDEA plug-in project
- Import the DataGenerator.jar into the project under test
- Click the ***Generate a Test Method*** button
- Select the method under test  
- Invoke the ***generateData*** method

![image](https://github.com/DeepOracle/DeepOracle/blob/main/DeepOracle.gif)

## Environmental requirements
- jdk1.8/jdk11
- python3.6
- daikon

- Daikon (only for daikon-based selection)
    - Download daikon from [Daikon](http://plse.cs.washington.edu/daikon/download/)
    - Install Daikon environment according to the [Daikon Documentation](http://plse.cs.washington.edu/daikon/download/doc/daikon.html#Installing-Daikon)
    - Compile the target java files: run ```javac -g RootPath/*.java```
    - Run DynComp: ```java -cp .:$DAIKONDIR/daikon.jar daikon.Chicory --daikon --comparability-file=ClassName.decls-DynComp PackageName.ClassName```
    - Run Chicory: ```java -cp .:$DAIKONDIR/daikon.jar daikon.Chicory --comparability-file=ClassName.decls-DynComp PackageName.ClassName```
    - Run Daikon: ```java -cp $DAIKONDIR/daikon.jar daikon.Daikon ClassName.dtrace.gz > daikon.txt```

## DeepOracle
- Generate Test cases
    - before_file.txt: the input of test cases
    - after_data.txt: the output of test cases
- Select the corresponding data processing function
    ``` loadData.load_isInner_before(before_file)```
- Run ``` python main.py```

## Random-based selection
- Load the corresponding data as dataset.(input,output,label)
- Run ```random.shuffle(dataset)```

## Coverage-based selection
- Get the line coverage information corresponding to the test case (line_coverage.txt)
- Select the corresponding test case and line coverage file path (```load_file(compare_path)```)
- Run ``` python Coverage.py```
## Daikon-based selection
- Run Daikon on MUT and get Daikon output information
- Select the sorting algorithm and path of corresponding MUT
    ```mm1(in_line, out_line, label_line)```
    ```method_path = mutation_path + mm1_name```
- Run ```python daikon.py```




