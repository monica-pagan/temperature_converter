# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 14:54:08 2024

@author: PaganM
"""



class tempfunction:
    def __init__(self, degree, metric):
        self.degree = degree
        self.metric = metric
        self.temp_result = None
        
        
    def temp_calculator(self):

        self.metric = self.metric.capitalize()

        celsius_to_farenheit_formula = (self.degree * (9/5)) + 32
        farenheit_to_celsius_formula = (self.degree - 32) * (5/9) 

        if self.metric.startswith('F'):
            return ('Farenheit to Celisus is ' +  str(farenheit_to_celsius_formula) + "C.")
        elif self.metric.startswith('C'):
            return ('Celsius to Farenheit is ' + str(celsius_to_farenheit_formula) + "F.")
        else:
            return ('Not working.')


           
    def runtemp(self):
        '''
        self.bmi_calculator()
        '''
        
        self.temp_result = self.temp_calculator()