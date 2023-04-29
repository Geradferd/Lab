class Account:
    

    def __init__(self, name: str):
        """
        Constructor to create initialstate of a account
        :param account_name: Person's first name
        :param account_balance: amount of money in the account
        """
        self.__account_name = name
        self.__account_balance = 0
    
    def deposit(self, amount: int) -> bool:
        """
        add given ammount of money to your balance

        Parameters
        ----------
        amount : amount of money to be added

        Returns : boolean
        -------

        """

        if amount > 0:
            self.__account_balance += amount
            return True
        return False
    

    def withdraw(self, amount: int) -> bool:
        """
        removes a given amount of money from the
        user's balance

        Parameters
        ----------
        amount : amount of money to be removed

        Returns: boolean
        -------
        bool
            chacks if the amount removed is greater than 0
            and you are removing less than the current balance

        """

        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False
    

    def get_balance(self) -> int:
        """
        Method to get the person's current balance
        :return: current balance
        """
        return self.__account_balance
    
    def get_name(self) -> int:
        """
        Method to get the user's name
        :return: Person's name
        """

        return self.__account_name
    
      
