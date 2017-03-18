# Class Agent 

import numpy as np 

class Agent (object): 

    def __init__ (self, ID): 
        self.ID = ID 
        self.bank = 0
        self.strat = 0
        self.passort = 0 
        self.switchprob = 0
        
        self.coop = np.random.normal(.5, .15)
        while self.coop <= 0 or self.coop >= 1:
            self.coop = np.random.normal(.6, .12)

        self.bayes = np.random.normal(.5, .15)
        while self.bayes <= 0 or self.bayes >= 1:
            self.bayes = np.random.normal(.5, .15)

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

    def get_coop (self):
        return self.coop

    def set_coop (self, coop):
        self.coop = coop

    def get_bayes (self):
        return self.bayes

    def set_bayes (self, bayes):
        self.bayes = bayes


