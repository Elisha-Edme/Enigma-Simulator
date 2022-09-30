class Plugboard:
    # Creates a dictionary for all the letters and their swapping letters
    # plugboard: an optional variable that allows this to act as a copy constructor
    # rep: an optional variable that makes a copy of another plugboard based on the other plugboard's representation
    def __init__(self, rep=None, plugboard=None, alphabet=None):
        if plugboard:
            self.alphabet = {key:plugboard.alphabet[key] for key in plugboard.alphabet}
            return
        if alphabet:
            self.alphabet = alphabet
            return
        self.alphabet = {chr(i):chr(i) for i in range(ord('A'), ord('Z') + 1)}
        if rep:
            lst = rep.split()
            for i in range(0, len(lst), 3):
                self.setPlug(lst[i], lst[i + 2])

    # Validates that char is a letter. Raises Exception if not
    def __validateLetter(self, char):
        char = chr(char)
        if not char.isalpha():
            raise ValueError(char + " is not a valid english letter")

    # Performs main function of Plugboard: swaps a letter with the one it is plugged into
    # if the letter is not plugged in, it reflects back the same letter
    def switch(self, char):
        char = char.upper()
        return self.alphabet[char]

    # Creates string with mapping for each letter (no duplicate mapping)
    def __str__(self):
        # Creates a set of letters that we have already seen
        seen = set()
        s = ""
        for key in self.alphabet:
            if key not in seen:
                # Adds relationship between key and value to string
                s += (key + ' <----> ' + str(self.alphabet[key]))
                s += '\n'
                # If the key maps to a letter, then the letter is added to the set so that the letter
                # is not repeated in the string
                seen.add(self.alphabet[key])
        return s

    # Returns whether two plugboards are the same (settings are the same)
    def __eq__(self, other):
        return self.alphabet == other.alphabet

    def empty(self, char):
        return self.alphabet[char] == char

########################### MANUAL METHODS TO CHANGE THE SETTINGS OF THE PLUGBOARD #################################
    # Plugs a wire between char1 and char2
    def plug(self, char1, char2):
        # Validates the letters
        char1 = char1.upper()
        char2 = char2.upper()
        # Makes sure the letters aren't the same
        if char1 == char2:
            raise Exception("Letters cannot be plugged into themselves")
        # If one of them is plugged into another letter, raises an error
        if not self.empty(char1) :
            raise Exception(char1 + " is already plugged into " + self.alphabet[char1])
        elif not self.empty(char2):
            raise Exception(char2 + " is already plugged into " + self.alphabet[char2])
        self.alphabet[char2] = char1
        self.alphabet[char1] = char2

    # Simulates removing a wire from char1 (and does the same to the letter it was plugged into)
    # Returns whether a wire was removed from char1
    def unplug(self, char1):
        char1 = char1.upper()
        removed = bool(self.alphabet[char1])
        if self.alphabet[char1]:
            self.alphabet[self.alphabet[char1]] = None
        self.alphabet[char1] = None
        return removed

    # Returns what char is mapped to (ie swapped with)
    def plugVal(self, char):
        return self.alphabet[char.upper()]
