import backtrader as bt
import pandas as pd
import numpy as np

class MacdMomentumTrend(bt.Strategy):
    def __init__(self):
       self.emaPeriod = 50

    def next(self):
        self.macd = self.calculateMacd() 
        self.ema = bt.indicators.EMA(self.data.close, period=self.emaPeriod)
        price = self.data.close[0]
        if price > self.ema and self.macd > 0:
            self.buy(size=10)
        else:                           # trailing stop implementation
            self.close()

    def calculateMacd(self):
        if len(self.data) < 26:
            return 0.0
        closes = np.array([self.data.close[-i] for i in range(26)][::-1])
        ema12 = closes[-12:].mean()
        ema26 = closes.mean()
        return ema12 - ema26