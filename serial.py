"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start) -> None:
        """Initializes a SerialGenerator Instance"""
        self.start = start 
        self.current = start
        self.original = start

    def generate(self):
        """Sets the current variable to return and increments start variable"""
        self.current = self.start
        self.start += 1
        return self.current
        
    def reset(self):
        """resets the number to generate back to the original start value"""
        self.start = self.original
        return self.start