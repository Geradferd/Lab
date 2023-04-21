class Account:
    
    """
    This class allows you to keep track of the amount
    of money in your account.
    
    :param __account_name: the users name
    :param __account_name: the users account balance
    """
    
    def __init__(self, name):
        """
        Parameters
        ----------
        name : name of user

        Returns
        -------
        None.

        """
        self.__account_name = name
        self.__account_balance = 0
    
    def deposit(self, amount) -> bool:
        """
        add given ammount of money to your balance

        Parameters
        ----------
        amount : amount of money to be added

        Returns : boolean
        -------

        """
        if amount > 0:
            self.__account_balance += amount # 8
            return True
        return False
    
    def withdraw(self, amount) -> bool:
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
            self.__account_balance -= amount # 4
            return True
        return False
    
    def get_balance(self) -> int:
        """
        

        Returns
        -------
        user's current balance

        """
        return self.__account_balance
    
    def get_name(self) -> int:
        """
        

        Returns
        -------
        users current name

        """
        return self.__account_name

