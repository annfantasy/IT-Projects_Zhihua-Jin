# Test Plan

**Author**: Cyberlife

## 1 Testing Strategy

### 1.1 Overall strategy

Types of testing that will be done for unit, integration, system and regression strategies, and it will include what will be tested, and the specific use cases that determine how the testing is done. 

No. | Activity | Member 
--- | --- | ---
1 |Organize Project involves creating a Test Plan, Schedule & Test Approach, and assigning responsibilities.
2 |Design/Build Test involves identifying Test Cycles, Test Cases, Entrance & Exit Criteria, Expected Results, etc. In general, test conditions/expected results will be identified by the Test Team in conjunction with the Development Team. The Test Team will then identify Test Cases and the Data required. The Test conditions are derived from the Program Specifications Document.
3 |Design/Build Test Procedures includes setting up procedures such as Error Management systems and Status reporting.
4 |Build Test Environment includes requesting/building software and data set-ups.
5 |Execute Tests include The tests identified in the Design/Build Test Procedures will be executed.  All results will be documented and Bug Report Forms filled out and given to the Development Team as necessary.
6 |Signoff happens when all pre-defined exit criteria have been achieved.

### 1.2 Test Selection

Unit Testing
White Box testing will be accomplished by the developing team mostly by the programmer him/herself during coding/performing.
Unit Testing (testing Interface, sample output, data printouts, defect integration)

Integration Testing
After two or more Unit testing is performed the integration test will be on action,
The gray box test will be performed by the tester and programmer. Firstly the programmer will test it and he/she will provide all the documentation (test case, list sample output, data printouts and defect information).

System Testing
This Black Box testing will be done by professional tester and will keep all the records, the whole process will be supervised directly by the Project Manager and this whole process of test will be documented.

Regression Testing
Gain the knowledge on new functions and the bug fixes and how it affect the system, which inncludes the area of frequent defects,the area which has undergone many/recent code changes and the area which is highly visible to the users, reset the test case for regression testing and concluding the results.

 

### 1.3 Adequacy Criterion

Firstly,every test should describe the criteria that should be met to pass that specific test;
The tester will understand each requirement and prepare corresponding test case to ensure all requirements are covered;
Each Test case will be mapped to use cases;
Each of the test cases will undergo review by the TA and the review defects are captured and shared to the Test team. The testers will rework on the review defects and finally obtain approval and sign-off;
During the preparation phase, tester will use the prototype, use case and functional specification to write step by step test cases;
Testers will maintain a clarification Tracker sheet and same will be shared periodically with the Requirements team and accordingly the test case will be updated. The clarifications may sometimes lead to Change Requests or not in scope or detailing implicit requirements;
Sign-off for the test cases would be communicates by TA;

### 1.4 Bug Tracking

During testing, the testing team members normally encounter behavior that goes against a specified or implied design requirement in the product.  When this happens, we will document and reproduce the bugs for the developers.  

### 1.5 Technology

SpringBootTest; Selenium

## 2 Test Cases

Test Case | Description | Process | Test Data | Expect
--- | --- | --- | --- | ---
1 | User Sign Up | Fill in required information; Send request | user information |User has been successfully created
2 | User Log in | Fill in required information; Send request | user id & user password | Log in successfully
2 | User Log out | Fill in required information; Send request | { diagnosis: none } | Log out successfully
