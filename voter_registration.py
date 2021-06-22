"""Lab 1 Voter Registation
Creates a short registration application and verifies voter eligibility
"""

import sys

errors = {
    'name' : '\n** Input error: first & last name required for registation **',
    'age' : '\n** Input error: age must be greater than 0  & less than 120 year(s) old **',
    'yes' : "\n** Input Error: response must be [y] or [n] **",
    'residence' : '\n** Input Error: state symbol must be two letters long and reflect voter state of residence **',
    'zipcode' : '\n** Input Error: zipcode must be 5 integers long **'
}

def verify(key, data):
    """User inputs verification"""

    if data in ("q","Q"):
        print("\nSYSTEM TERMINATED: Voter has not been registered\n")
        sys.exit()
    else:
        try:
            verified = False
            if key == 'name':
                verified = bool(len(data) > 0)
            elif key == 'age':
                data = int(data)
                verified = bool(data > 0 and data < 120)
            elif key in ('restart', 'citizen', 'done'):
                verified = bool(str(data).lower() in ('y', 'n'))
            elif key == 'residence':
                verified = bool(len(data) == 2)
            elif key == 'zipcode':
                verified = bool(len(data) == 5 and str(data).isnumeric())

            # Verified?
            if verified is False:
                raise ValueError # incorrect input format
            return verified
        except ValueError:
            # Error Message
            print(f'{errors[key]}' if key in errors.keys()\
                else '\n** System error: undefined key **')
            return False

def get_user_details():
    """Gets voter registration elements from user"""

    complete = False
    while complete is False:
        voter = list() # Actual list of voters would be kept in dictionary
        print('\n__Please enter user details as prompted or type [Q] to exit the system at any time__')

        while True:
            firstName = input('\nEnter first name: ')
            if verify('name', firstName) is True:
                voter.append(firstName)
                break

        while True:
            lastName = input('\nEnter last name: ')
            if verify('name', lastName) is True:
                voter.append(lastName)
                break

        while True:
            age = input('\nEnter age: ')
            if verify('age', age) is True:
                voter.append(int(age))
                print(age)
                break

        while True:
            citizen = input('\nAre you a US citizen? type [Y] for yes or [N] for no: ')
            if verify('citizen', citizen) is True:
                voter.append(True if str(citizen).lower() == 'y' else False )
                print(citizen)
                break

        while True:
            residence = input('\nEnter two letter symbol for state of residency: ')
            if verify('residence', residence) is True:
                voter.append(residence)
                break

        while True:
            zipcode = input('\nEnter 5 digit zipcode: ')
            if verify('zipcode', zipcode) is True:
                voter.append(int(zipcode))
                break

        while True:
            print('\n\t____Verify Voter Details____'\
                f'\nName: {lastName}, {firstName}'\
                f'\nAge: {age}'\
                f'\nUS Citizen: {citizen}'\
                f'\nState of Residence: {residence}'\
                f'\nZipcode: {zipcode}')

            verify_details = input('\nEnter [Y] to verify voter information, or [N] to restart voter registration: ')
            if verify('done', verify_details) is True:
                if str(verify_details).lower() == 'y':
                    complete = True
                    break
    return voter

def verify_registration(voter): #verifies voter eligibility
    """Verifies voter eligbility"""

    return bool(voter[2] >= 18 and voter[3] is True)

def main():
    """Main Program"""

    complete = False
    while complete is False: 
        print('\n\tWelcome to Shawn\'s Voter Registration System') 
        voter = get_user_details()
        
        if verify_registration(voter) is True:
            print(f'\nCongratulations! {voter[0]} you\'re registered to vote!')
        else:
            print('\nVoter not eligible to vote. Voters must be above 18 years of age and a citizen of the United States of America')

        while True:
            restart = input('\n\nWould you like to register another voter? Enter [y] for yes, or [n] to restart')
            if verify('done', restart) is True:
                if str(restart).lower() == 'n':
                    complete = True
                    print('\nThank you for using Shawm\'s voter registration system. Please come again soon!\n')
                    break

main()
