from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 122)
    email = models.CharField(max_length = 122)
    phone = models.CharField(max_length = 12)
    desc = models.CharField(max_length = 500 )

    # __str__ is one of the  dunder or magic method, we can call this method without using its complete name unlike other methods
    # it is defined inside the class and with the help of this we can return the object or its attribute in human readable form
    # unlike objects return as <class int>(something like this) -> *** for more reference go through its actual code file. ***
    # we can implement abstraction using this methods(dunder) by hiding functionality or performing similar operations.
    
    def __str__(self):
        return str(self.name)
    
    # just for testing, we can put any number of data members or instance variables inside the 'str'
        # return str(self.name + " " + self.email)