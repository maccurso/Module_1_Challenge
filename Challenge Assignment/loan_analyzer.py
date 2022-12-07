# coding: utf-8
import csv
from pathlib import Path

loan_costs = [500, 600, 200, 1000, 450]

#calculating total number of loans in the list
number_of_loans = len(loan_costs)
print(f"The number of loans in the list is: {number_of_loans}")

#calculating the total amount of loans in the portfolio
total_amount = sum(loan_costs)
print(f"The total value of the loans is: ${total_amount}")

#calculating the average loan amount
average_loan_amount = total_amount / number_of_loans
print(f"The average loan amount is: ${average_loan_amount}")


loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#extracting future value and remaining months variables
future_value = loan.get("future_value")
print(f"The future value of the loan is: ${future_value}")

remaining_months = loan.get("remaining_months")
print(f"There are {remaining_months} months remaining on this loan.")


#calculating the fair value of the loan using 20% discount rate
discount_rate = 0.20
present_value = (future_value)/(1 + discount_rate/12)**remaining_months
print(f"Present Value is ${present_value:.2f}")

#using a conditional statement to determine if it is worth it to buy the loan
#loan worth being greater than the cost will reflect a buy

if present_value >= loan["loan_price"]:
    print("The loan is worth at least the cost to buy it.")
else:
    print("The loan is too expensive and not worth the price.")

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#defining a function to determine and return the present value of the new loan
def loan_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = (future_value)/(1 + annual_discount_rate/12)**remaining_months
    return(present_value)


#calculating the present value using an annual discount rate of 20%
annual_discount_rate = 0.2
present_value = loan_present_value(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate)
print(f"The present value of the new loan is: ${present_value:.2f}")


loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

#created an empty list to be filled using below functions
inexpensive_loans = []

#filtered out the loans priced at 500 or less, added them to the new list, printed

for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)

print(inexpensive_loans) 

#setting the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

#setting the output file path
output_path = Path("inexpensive_loans.csv")

print("Writing the data to a CSV file...")

#using csv library to export the new list of inexpensive loans
with open(output_path, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())
