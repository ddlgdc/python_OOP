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

    def __init__(self, start):
        #  intialize the generator with a start val
        self.start = start
        self.current = start
    
    def generate(self):
        # return the next serial number and increment the curr val
        serial = self.current
        self.current += 1
        return serial
    
    def reset(self):
        #  reset the generator to the intial value
        self.current = self.start
    

# generate() test cases 
serial = SerialGenerator(start=100)
print(serial.generate()) # prints 100
print(serial.generate()) # prints 101
print(serial.generate()) # prints 102

# reset() test cases
serial.reset() 
print(serial.generate()) # prints 100

# additional assertions
assert serial.generate() == 101
assert serial.generate() == 102
assert serial.generate() == 103
assert serial.generate() == 104

print(('All tests cases pass'))