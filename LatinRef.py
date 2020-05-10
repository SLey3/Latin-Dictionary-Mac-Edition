"""
Latin Initial reference for the .csv file
"""
# INITILIZATION 
class Initial:
    """
    Initial __init__ and __str__ to read and organize information from the .csv file
    """
    def __init__(self, definition, others = None, nominative = None, dative = None , accusative = None, present = None, imperfect = None, perfect = None , otherInfo = None):
        self.definition = definition
        self.other_meanings = others
        self.nominative = nominative
        self.dative = dative
        self.accusative = accusative
        self.present = present
        self.imperfect = imperfect
        self.perfect = perfect
        self.additionalInfo = otherInfo

    def __str__(self):
        return  str(self.__class__) + '\n' + '\n'.join((str(item) + ' = ' + "\n " + str(self.__dict__[item]) for item in self.__dict__ if str(self.__class__) != ""))