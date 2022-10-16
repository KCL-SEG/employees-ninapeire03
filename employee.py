"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type, commission_type):
        self.name = name
        self.contract_type = contract_type
        self.commission_type = commission_type

    def get_commission_type(self):
        return commission_type

    def get_pay(self):
        if isinstance(self.contract_type, HourlyContract):
            pay = self.contract_type.hourly_wage * self.contract_type.hours_worked
        elif isinstance(self.contract_type, SalaryContract):
            pay = self.contract_type.salary
        else:
            raise TypeError("This contract type does not exist.")

        if isinstance(self.commission_type, ContractCommission):
            pay += (self.commission_type.number_of_contracts * self.commission_type.commission_per_contract)
        elif isinstance(self.commission_type, BonusCommission):
            pay += self.commission_type.bonus

        return pay

    def __str__(self):
        if isinstance(self.contract_type, HourlyContract):
            str = f"{self.name} works on a contract of {self.contract_type.hours_worked} at {self.contract_type.hourly_wage}/hour"
        elif isinstance(self.contract_type, SalaryContract):
            str = f"{self.name} works on a monthly salary of {self.contract_type.salary}"
        else:
            raise TypeError("This contract type does not exist.")

        if isinstance(self.commission_type, ContractCommission):
            str += f" and receives a commission for {self.commission_type.number_of_contracts} contract(s) at {self.commission_type.commission_per_contract}/contract."
        elif isinstance(self.commission_type, BonusCommission):
            str += f" and receives a bonus commission of {self.commission_type.bonus}."
        else:
            str += "."

        str += f" Their total pay is {self.get_pay()}."

        return str

class Contract:
    def __init__(self):
        pass

class HourlyContract(Contract):
    def __init__(self, hourly_wage, hours_worked):
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

class SalaryContract(Contract):
    def __init__(self, salary):
        self.salary = salary


class Commission:
    def __init__(self):
        pass

class ContractCommission(Commission):
    def __init__(self, number_of_contracts, commission_per_contract):
        self.number_of_contracts = number_of_contracts
        self.commission_per_contract = commission_per_contract

class BonusCommission(Commission):
    def __init__(self, bonus):
        self.bonus = bonus

class NoCommission(Commission):
    def __init(self):
        pass


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', SalaryContract(4000), NoCommission())

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyContract(25, 100), NoCommission())

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', SalaryContract(3000), ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContract(25, 150), ContractCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', SalaryContract(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContract(30, 120), BonusCommission(600))


# Tests for command line execution.
print(billie)
print(charlie)
print(renee)
print(jan)
print(robbie)
print(ariel)
