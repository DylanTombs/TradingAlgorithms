import backtrader as bt
import pandas as pd
import os
import random
import numpy as np

class MeanReversion(bt.Strategy):

    def __init__(self):
        self.smiO
        self.oversoldRSI
        self.buffer = 5

    def next(self):
        self.smi = self.calculateSMI(20)
        self.oversoldRSI = self.calculateOversoldRSI()
        price = self.data.close[0]
        if price < self.smi + self.oversoldRSI + self.buffer:
            self.buy(size=10)
        elif price > self.smi + self.oversoldRSI + self.buffer and self.getposition().size > 0:
            self.close()

    def calculateSMI(self, num):
        pass

    def calculateOversoldRSI(self):
        pass