import backtrader as bt
import pandas as pd
import numpy as np
from datetime import datetime

# Your existing strategies

class StrategyEvaluator(bt.Analyzer):
    def __init__(self):
        self.start_val = None
        self.end_val = None
        self.trades = []
        self.values = []
        self.trade_returns = []

    def start(self):
        self.start_val = self.strategy.broker.getvalue()

    def next(self):
        self.values.append(self.strategy.broker.getvalue())

    def stop(self):
        self.end_val = self.strategy.broker.getvalue()

    def notify_trade(self, trade):
        if trade.isclosed:

            start_val = self.values[trade.baropen] if trade.baropen < len(self.values) else self.values[-1]
            end_val = self.values[trade.barclose - 1] if trade.barclose - 1 < len(self.values) else self.values[-1]
            pct_return = (end_val - start_val) / start_val if start_val != 0 else 0.0

            self.trade_returns.append(pct_return)

            self.trades.append({
                'pnl': trade.pnl,
                'pnlcomm': trade.pnlcomm,
                'duration': trade.barclose - trade.baropen,
                'price': trade.price,
                'size': trade.history[0].size if trade.history else 1,  # Fallback
                'return': pct_return
            })