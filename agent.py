# Class Agent 

import numpy as np 

class Agent (object): 

    def __init__ (self, ID): 
        self.ID = ID 
        self.bank = 0
        self.strat = 0
        self.passort = 0 
        self.switchprob = 0

    def get_id (self):
        return self.ID

    def set_strat (self, strat):
        self.strat = strat 

    def get_strat (self):
        return self.strat 

    def set_assort (self, assort):
        self.passort = assort

    def get_assort (self):
        return self.passort
    
    def set_bank (self, bank):
        self.bank = bank

    def get_bank (self):
        return self.bank 

    def set_sp (self, switchprob):
        self.switchprob = switchprob

    def get_sp (self):
        return self.switchprob



