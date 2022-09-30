'''
Rotors are composed of two parts: The ring and the rotor itself
The ring is just a family of internal wiring, and this ring can turn
independent of the rotor. Thus, the ring can be offset from the rotors,
allowing the letters the rotors map, can change.
'''
class Rotor:
    class Ring:
        # Initializes a ring with a family of wiring with the same relationship from mapping
        # Top of the ring sets the offset
        def __init__(self, mapping, top=0):
            # Creates a list of functions that simulate the internal wiring
            # The invmap is just the reversed map, so that the wiring works both ways
            # (for when the letter passes through on either side of the rotor)
            self.mapping, self.invmap = [], [0] * 26
            for i in range(len(mapping)):
                # letter is set to the ith letter of the Alphabet
                letter = ord('A') + i
                # jump holds the difference between the letter and the letter it encrypts to
                # this jump simulates the wire between the letter and its encrypted counterpart
                jump = (letter - ord(mapping[i].upper())) * -1
                self.mapping.append(jump)
                # creates the opposite jump for the encrypted letter
                # to simulate the bidirectional relationship of the wire
                self.invmap[i + jump] = jump * - 1
            self.top = top

        def __str__(self):
            s = "Top: " + chr(self.top + ord('A')) + '\n'
            for i in range(ord('A'), ord('Z') + 1):
                s += chr(i) + ' : ' + chr(i + self.mapping[i - ord('A')]) + '\n'
            return s

        # Private method to make sure char is an actual english letter
        def __validate_letter(self, char):
            if not char.isalpha():
                raise ValueError(char + " is not a valid english letter")

        # simulates rotating the ring
        # backwards: a parameter that determines the direction of the rotation (default to forward)
        def rotate(self, backwards=False):
            if backwards:
                self.top = (self.top - 1) % 26
            else:
                self.top = (self.top + 1) % 26

        def get_top(self):
            return self.top

        def set_top(self, top):
            self.top = top

        # returns the jump (how many slots away the new letter should be)
        def encrypt(self, slot, inverted=False):
            index = (self.top + slot) % 26
            return self.invmap[index] if inverted else self.mapping[index]

        # simulates making a wire between key and val
        def create_mapping(self, key, val):
            # jump holds the difference between the letter and the letter it encrypts to
            # this jump simulates the wire between the letter and its encrypted counterpart
            jump = (ord(key) - ord(val)) * -1
            self.mapping[ord(key) - ord('A')] = jump
            self.invmap[ord(val) - ord('A')] = jump * -1

    # Creates a rotor with a ring using mapping and ring_top
    # turnover: letter at which the next rotor will rotate
    # top: The letter at the top
    def __init__(self, mapping, turnover = 'Z', top = 'A', ring_top=0):
        self.ring = Rotor.Ring(mapping, ring_top)
        self.set_turnover(turnover)
        self.top = top

    def __validateLetter(self, char):
        if not char.isalpha():
            raise ValueError(char + " is not a valid english letter")

    def get_turnover(self):
        return self.turnover

    def set_turnover(self, letter):
        self.turnover = letter

    # Simulates rotates the rotor
    # backwards: determines the direction in which the rotor rotates
    def rotate(self, backwards=False):
        self.ring.rotate(backwards)
        # calculates the distance of the new letter
        new_letter_dist = (ord(self.top)-ord('A') + 1) % 26
        if backwards:
            new_letter_dist = (ord(self.top)-ord('A') - 1) % 26
        self.top = chr(new_letter_dist + ord('A'))

    def create_mapping(self, key, val):
        self.ring.create_mapping(key, val)

    def get_top(self):
        return self.top

    # simulates rotating the rotor to a new top
    def set_top(self, letter):
        prevtop = self.top
        self.top = letter
        # calculates the shift from previous top to the new letter top
        shift = ord(letter) - ord(prevtop)
        # uses the shift to set new ring top (since the ring top is independent of the rotor top)
        new_ring_top = (self.get_ring_top() + shift) % 26
        self.set_ring_top(new_ring_top)

    def get_ring_top(self):
        return self.ring.get_top()

    def set_ring_offset(self, offset):
        offset = 26 - offset + 1
        offset %= 26
        self.ring.set_top(offset)
    def set_ring_top(self, top):
        self.ring.set_top(top)

    # Simulates encrypting a single letter
    # slot: the slot number that the letter pass through
    # rev: determines the whether the letter is passing from the left or right (default is from the right)
    def encrypt(self, slot, rev=False):
        dist_new_slot = self.ring.encrypt(slot, rev)
        new_slot = (slot + dist_new_slot) % 26
        return new_slot

    def __repr__(self):
        s = '''##################################################\nRing Settings:\n'''
        ls = str(self.ring).split('\n')
        ls.pop()
        for line in ls:
            s += ('\t' + line + '\n')
        s += '#################################################\nRotor Settings:\n'
        s += "Top: " + self.top + "\nTurnover: " + self.turnover
        return s

    def __str__(self):
        return "".join([chr(ord('A') +  self.encrypt(a)) for a in range(26)])
