import numpy as np 
from scipy.signal import lti


class RLC_BP3_Filter():

    def __init__(self, R1, R2, C, L):
        """
        Constructor
        """
        self.R1 = R1 
        self.R2 = R2 
        self.C = C 
        self.L = L

    def lti(self):
        """
        Create the transfer function for the filter.

        Returns
        -------
        system : an instance of the LTI class 
        """
        num = [self.L/self.R2,0]
        den = [self.L*self.C, self.L*(self.R1+self.R2)/(self.R1*self.R2), 1]
        return lti(num, den)    

    def get_params(self):
        """
        Compute the maximum gain, the angular frequency and the damping factor of the filter.
        
        Returns
        -------
        Tm : float 
        w0 : float 
        m : float
        """
        Tm = self.R1 / (self.R1+self.R2)
        w0 = 1/ np.sqrt(self.L*self.C)
        m = 0.5*((self.R1+self.R2)/(self.R1*self.R2))*np.sqrt(self.L/self.C)
        return "BP", Tm, w0, m
    
    def set_components(self, Tm, w0, m):
        """
        Set the circuit components C, R1 et R2 from the filter parameters and the attribute L

        Parameters
        ----------
        Tm : float 
        w0 : float 
        m : float
        """

        C = 1 / (self.L*(w0**2)) 
        R2 = (1/(2*m*Tm))*np.sqrt(self.L/C)
        R1 = (R2*Tm) / (1-Tm)
        self.R2 = R2 
        self.R1 = R1
        self.C = C