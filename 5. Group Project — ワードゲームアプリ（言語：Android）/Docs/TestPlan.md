# Test Plan
**Author**: <Team 29>   
**Version**:\<3.0-0303-bfD4\>    
**Description:**\<Third version. Done Mar 3rd. Proofread on Mar 5th. Before deliverable 4 submission ddl>   

## 1 Testing Strategy

### 1.1 Overall strategy
For this project, we will design a set of test cases to confirm our software could satisfy all the required functionality, responds correctly to different inputs, and performs efficiently within an acceptable runtime. 

The unit test is used to test whether every unit in our software can achieve the desired functions individually. The unit test in this project will be test manually. Each member of our team will run the unit test for his/her responsible units. There will be some overlap between the unit test and regression test. After the unit test, integration testing would be conducted, in which individual units are combined and tested as a group to expose defects in the interfaces and interaction between integrated components. This test would be done manually. For simplification, one interface would be tested at a time.Top0-Down integration testing would be adapted, where top-level units are tested first and lower level units are tested step by step after that. This test would be done by each of our teammates for their responsible interfaces. The system testing will be conducted on a complete and integrated software. It would include both functional tests and no functional tests. A set of specific test cases would be designed, supplying inputs, and examining expected outputs and runtime. This testing would be done manually by each of our teammates. The regression testing will be conducted each time a correction is made to ensure such change would not affect existing features. Part of the important and complex test suite would be picked as the regression test set and will be checked each time a modification was made. This test will be done by whoever makes the corrections. 

### 1.2 Test Selection
In the early stage, static testings will be conducted by reviewing, inspecting, and walking through the source code to identify obvious defects as early as possible. After that, dynamic testing will be adapted to test software performances. The black box technique will be mainly used in the testing, which focuses on the specification of software. We will primarily utilise the Category-Partition Method to select the test case for unit test, integration test, and regression test, which will eliminate the meaningless combinations and reduce the number of test cases. For the calculation of scoring, and the checking of word validation, we would use control-flow based White box technique to do the testing. We will use test case that ensure Modified condition/decision coverage. For system testing, we plan to use Finite State Machines to select the test cases. 

### 1.3 Adequacy Criterion
The unit, integration, and regression tests will be designed based on the specifications of the software. The test case that covers the boundary case, where the error is more likely to occur, is high quality. Therefore, we will also try to ensure our test case cover all the key boundary cases. Moreover, we also would like to include one middle (i.e., common cases) for each method and each integration. For the testing of word validation and scoring, since it is a relatively complex process and involve lots of if statement, we will use test case that ensure Modified condition/decision coverage. For system testing, we will use Finite State Machines. We will try to use paths that can go through all the states in the machine. We will also generate test cases to cover all possible transitions between different states.

### 1.4 Bug Tracking
Since it is a small software, bugs and enhancement requests will be tracked in an excel sheet within the repository. In the excel sheet, we will list the bugs, write info about them, and work through them once available. For future complex software, we may use a formal bug-tracking tool such as Jira.

### 1.5 Technology
We mainly use manual method to do the unit test, integration test and regression test. 

## 2 Test Cases
| Test ID        | Purpose           | Action  | Prereqs |Expected result | Actual result| Pass/ Fail?|Regression Test?|
| :-------------: |:-------------:| :-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|IT1| User can adjust game setting| Click "Adjust the game settings"|At main menu|Three settings appear: a. Length of game; b.Size of Board ; c. Weight of word. | As expected | Pass  | YES |
|UT1|Test Default "Num Minutes" and "Board Size"| Do Not Select "Num Minutes" and "Board Size"|At game setting (e.g. after IT1)|"Num Minutes" equal to 3, <br>"Board Size"equal to 4| As expected | Pass | NO |
|UT2|Adjust "Num Minutes"| Select "Num Minutes" <br> equal to 5|At game setting (e.g. after IT1)| "Num Minutes" <br> equal to 5| As expected | Pass| NO |
|UT3|Adjust "Board Size"| Select "Board Size" <br> equal to 8|At game setting (e.g. after IT1)| "Board Size" <br> equal to 8|As expected | Pass| NO |
|UT4|Adjust Letter Weight and check default Letter Weight|Select Letter Weight of Q equal to 5|At game setting (e.g. after IT1)| Letter Weight of Q equal to 5, other equal to 1|  As expected | Pass | NO |
|IT2| User can Play Game and should generate board and timer| Click "Play game"|At main menu| Board generated with random letter with set "Board Size", timer generated with set "Num Minutes"|  As expected | Pass | YES |
|UT5| Q on board be displayed as ‘Qu’, ⅕ (rounded up) of the letters will be vowels, distribution of letters reflecting the weights, letters may appear more than once|Click "Play game"|There is Q on the board (e.g. after UT4), |Q on board be displayed as ‘Qu’, ⅕ (rounded up) of the letters will be vowels, distribution of letters reflecting the weights,letters may appear more than once|As expected | Pass | NO |
|IT3| Timer should count down and Game should exit when timer counts to zero| Wait until time counts to zero|At game play (e.g. after TI2)|Game would end|  As expected | Pass   | YES |
|UT6|The word should only contain letter on the board| Try to click letter that not exist on the board|At game play (e.g. after TI2)| One can only click word on the board| As expected  | Pass   | YES |
|UT7|The word must contain two or more letters | Enter word with less or equal to one letter|At game play (e.g. after TI2)|Error message appear and word is not recorded| As expected | Pass | YES |
|UT8|The word must contain only letters from the board that are each adjacent| Enter word with all letter in board but not adjacent|At game play (e.g. after TI2)|Error message appear and word is not recorded| As expected | Pass | YES |
|UT9|Single letter on the board may not be used twice| Try to use used letter |At game play (e.g. after TI2)| The used letter would be gray out and can not be clicked again |   As expected | Pass  | YES |
|UT10|Valid word will be record and update with score, Qu letter would score 2 points| Enter a valid word with Qu|At game play (e.g. after TI2), Qu on the board| The score for that word and word statistics is recorded. The score is 2 point for Qu and 1 points for others|  As expected | Pass  | YES |
|UT11|Re-roll the board cost 5 points| Click on "Re-roll the board"|At game play (e.g. after TI2)|Reduce the score by 5 points|  As expected | Pass   | YES |
|UT12|Score can be negative| Click on "Re-roll the board" without other action|At game play (e.g. after TI2)|Final score would be -5|   As expected | Pass   | NO |
|IT4| Re-roll the board generate new board without change in timer|clicks on “Re-roll the board”|At game play (e.g. after TI2)| New board would be generated without affecting timer|    As expected | Pass   | YES |
|IT5|User can exit game early and stop the timer, the final score would display|Clicks on "Exit the game"|At game play (e.g. after TI2)| The countdown would stop and ends the game| As expected | Pass | YES |
|IT6|The final score would display at game end, then continue back to the main menu| Game end|Game end by IT2 or IT5| The final score would be displayed, continue back to the main menu| As expected | Pass  | YES |
|IT7|User can view statistics|Click on "View statistics"|At main menu|The system displays two choice "game score statistics" and "word statistics"| As expected | Pass  | YES |
|IT8|User can view game statistics|Click on "game score statistics"| At statistics with previous successful game play history|The system displays the list of final game scores in descending order followed by the number of times the board was reset, and the number of words entered in the game|  As expected | Pass  | YES |
|IT9|User can view setting and statistics of a specific game|Select any of the game scores from game score list|At game statistics with previous successful game play history (e.g. after IT8)|The system displays the settings of the games and the highest scored word|   As expected | Pass   | YES |
|IT10|Game statistics can be empty|Click on "game score statistics"|At statistics without previous successful game play history|The system displays nothing|   As expected | Pass  | YES |
|IT11|User can view word statistics|Clicks on "word statistics"|At statistics with previous successful game play history|The system displays the list of word entered in game followed by frequency. The order of word is sorted by frequency| As expected | Pass | YES |
|IT12|Word statistics can be empty|Click on "word score statistics"|At statistics without previous successful game play history|The system displays nothing|   As expected | Pass   | YES |
