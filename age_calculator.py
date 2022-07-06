
from datetime import date





def get_dob():
	year = input("Enter year of birth:")
	month = input("Enter month of birth:")
	day = input("Enter day of birth:")
	dob = date({int(year)}/{int(month)}/{int(day)})

	return dob



def get_age(dob):
	current_date = date.today()
	age = current_date - dob
	return age

def main():
	dob = get_dob
	current_date = date.today()
	age = int((current_date - dob).days/365)
	if dob <= current_date:
		print(f"You are {age} years old")
	else:
		print("You can't be born in the future")
  


if __name__ == '__main__':
    main()

