from Rotor import Rotor
from Plugboard import Plugboard
import copy

ENIGMA_SETTINGS = {}
################################# CREATE ROTORS ##########################################
ENIGMA_SETTINGS["ENIGMA1 ROTOR 1"] = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', turnover='Q')

ENIGMA_SETTINGS["ENIGMA1 ROTOR 2"] = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', turnover='E')

ENIGMA_SETTINGS["ENIGMA1 ROTOR 3"] = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', turnover='V')

ENIGMA_SETTINGS["ENIGMA1 ROTOR 4"] = Rotor('ESOVPZJAYQUIRHXLNFTGKDCMWB', turnover='J')

ENIGMA_SETTINGS["ENIGMA1 ROTOR 5"] = Rotor('VZBRGITYUPSDNHLXAWMJQOFECK', turnover='Z')

ENIGMA_SETTINGS["NORWAY ENIGMA ROTOR 5"] = Rotor('HEJXQOTZBVFDASCILWPGYNMURK', turnover='Z')

ENIGMA_SETTINGS["NORWAY ENIGMA ROTOR 4"] = Rotor('FGZJMVXEPBWSHQTLIUDYKCNRAO', turnover='J')

ENIGMA_SETTINGS["NORWAY ENIGMA ROTOR 3"] = Rotor('JWFMHNBPUSDYTIXVZGRQLAOEKC', turnover='V')

ENIGMA_SETTINGS["NORWAY ENIGMA ROTOR 2"] = Rotor('GJLPUBSWEMCTQVHXAOFZDRKYNI', turnover='E')

ENIGMA_SETTINGS["NORWAY ENIGMA ROTOR 1"] = Rotor('WTOKASUYVRBXJHQCPZEFMDINLG', turnover='Q')

################################ CREATE REFLECTORS ###########################################

ENIGMA_SETTINGS["ENIGMA1 REFLECTOR A"] = {chr(i): 'EJMZALYXVBWFCRQUONTSPIKHGD'[i - ord('A')]
                                            for i in range(ord('A'), ord('Z') + 1)}

ENIGMA_SETTINGS["ENIGMA1 REFLECTOR B"] = {chr(i): 'YRUHQSLDPXNGOKMIEBFZCWVJAT'[i - ord('A')]
                                            for i in range(ord('A'), ord('Z') + 1)}

ENIGMA_SETTINGS["ENIGMA1 REFLECTOR C"] = {chr(i): 'FVPJIAOYEDRZXWGCTKUQSBNMHL'[i - ord('A')]
                                            for i in range(ord('A'), ord('Z') + 1)}

ENIGMA_SETTINGS["NORWAY REFLECTOR A"] = {chr(i): 'MOWJYPUXNDSRAIBFVLKZGQCHET'[i - ord('A')]
                                            for i in range(ord('A'), ord('Z') + 1)}

############################### CREATE ENIGMA ##############################################

class Enigma:
    def __init__(self,rotors,reflector,plugboard=Plugboard()):
        self.rotors = copy.deepcopy(rotors)
        self.plugboard = plugboard
        self.reflector = reflector
    # Simulates rotating the rotors
    # forward: a bool that determines the directions (defaults to forward)
    def rotate_rotors(self, forward=True):
        if (forward):
            # Rotates the first rotor
            prev_top = self.rotors[0].get_top()
            self.rotors[0].rotate()
            i = 1
            while (i < len(self.rotors)):
                # Tests for double step
                if (prev_top == self.rotors[i - 1].get_turnover()
                        or (self.rotors[i].get_turnover() == self.rotors[i].get_top()
                            and prev_top == self.rotors[i-1].get_top())):
                    prev_top = self.rotors[i].get_top()
                    self.rotors[i].rotate()
                i += 1
        else:
            prev_top = self.rotors[0].get_top()
            self.rotors[0].rotate(backwards=True)
            i = 1
            while (i < len(self.rotors)):
                if (self.rotors[i-1].get_top() == self.rotors[i-1].get_turnover()):
                    prev_top = self.rotors[i].get_top()
                    self.rotors[i].rotate(backwards=True)
                else:
                    break
                i += 1
    def encrypt_letter(self, letter):
        if not letter.isalpha():
            return letter
        lower = letter.islower()
        letter = self.plugboard.switch(letter)
        self.rotate_rotors()
        slot = ord(letter.upper()) - ord('A')
        # Finds the slot in which the letter enters
        for i in range(len(self.rotors)):
            # sends the letter through all the rotor, from rotor 1 to 3
            slot = self.rotors[i].encrypt(slot)
        # sends letter thru reflector
        slot = ord(self.reflector[chr(slot + ord('A'))]) - ord('A')
        for i in range(-1, -1 * len(self.rotors) - 1, -1):
            # sends the letter through all the rotors, from rotor 3 to 1
            slot = self.rotors[i].encrypt(slot, rev=True)
        encrypted = chr(slot + ord('A'))
        # converts slot to a letter
        encrypted = self.plugboard.switch(encrypted)
        return encrypted.lower() if lower else encrypted

    def encrypt_message(self, message):
        encrypted = ''
        for char in message:
            encrypted += self.encrypt_letter(char)
        return encrypted

    def change_rotor(self, new_rotor, pos):
        self.rotors[pos] = copy.deepcopy(new_rotor)

    def set_ring_offset(self, top, pos):
        self.rotors[pos].set_ring_offset(top)
    def set_rotor_top(self, top, pos):
        self.rotors[pos].set_top(top)

    def set_ring_top(self, top, pos):
        self.rotors[pos].set_ring_top(top)

    def set_rotors(self, positions):
        for i in range(1, len(positions) + 1):
            self.rotors[i - 1].set_top(positions[len(positions) - i])

    # Resets the tops to all be 'A'
    def reset(self):
        for i in range(len(self.rotors)):
            self.rotors[i].set_ring_top(0)
            self.set_rotor_top('A', i)