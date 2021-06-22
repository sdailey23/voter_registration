# voter_registration
Creates a short registration application &amp; verifies eligible voters

Official Directions by University of Maryland Global Campus CMSC 350
Using your Python programming environment, write a Python application that supports voter registration. The application will launch and run from the command line prompt. The application will prompt the user for their first name, last name, age, country of citizenship, state of residence and zipcode. To be a valid registration all fields must be entered. If they are at least 18 years old and a U.S citizen, they can move forward and be prompted for the remaining questions and register to vote. If not, they should not be presented with the additional questions. There should be some error checking logic on the input statements to make sure the age numbers entered seem reasonable (e.g. a person is probably not > 120 years) and states should be 2 letters representing only valid U.S. States. The application should prompt the user for the needed questions to complete the registration and re- prompt when data is invalid giving the user the opportunity to retry. The output should summarize the input data and congratulate the user if they are eligible to vote and entered all of the data. The user should be given options to exit the program at any time to cancel the registration process.

Voter Eligibility Requirements:
1. At least 18 years old
2. US Citizen

State & Zip Verification: Program does not check against an official state verification library. System only verifies that state entry is longer than two characters in ength for validation.
