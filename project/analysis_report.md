
# TradeSmart Guide - 20-Year Backtest Analysis Report

## Executive Summary

The SMA mean-reversion strategy with default parameters (0.2% buffer, 12-period SMA) 
**significantly underperforms simple buy-and-hold** over 20 years across all tested stocks.

| Metric | Strategy | Buy & Hold | Difference |
|--------|----------|------------|------------|
| Avg Total Return | 17.4% | 2,411% | **-2,394%** |
| Avg CAGR | 0.79% | 13.7% | -12.9% |
| Avg Win Rate | 74.7% | N/A | - |
| Avg Max Drawdown | -9.2% | ~-35% | Better |

## Key Findings

### 1. Strategy Characteristics
- **High win rate (74.7%)** but **tiny profits per trade** (~0.2%)
- Excellent at capital preservation during crashes
- Completely misses major bull market gains
- ~200+ trades per stock over 20 years = significant commission drag

### 2. Parameter Sensitivity
Best configurations identified:

| Goal | Buffer | SMA Window | Result |
|------|--------|------------|--------|
| Best Sharpe | 1.0% | 30 | 0.56 |
| Best Return | 3.0% | 12 | 5.1% |
| Best Win Rate | 5.0% | 5 | 100% |
| Lowest Drawdown | 3.0% | 20 | -0.7% |

### 3. Market Regime Performance
- **Best in**: 2008 Crisis (+1.7% while market crashed)
- **Worst in**: Any trending market (misses gains)

### 4. Limited Sessions Impact
Trading 2-3x/week reduces returns by **5.1%** on average vs daily trading.

## Recommendations for 2hr/2-3x Week Use

### Immediate Configuration Changes

1. **Trading Buffer**: 0.2% → **3-5%**
   - Current setting triggers on noise
   - Larger buffer = fewer but more meaningful trades
   
2. **SMA Window**: 12 → **20-30 periods**
   - Smoother signal for intermittent monitoring
   - Less whipsawing
   
3. **Position Size**: 10% → **25-50%**
   - Fewer trades need more impact
   - Current 10% severely limits upside

4. **Add Trend Filter**
   - Only BUY when price > 50-day SMA (uptrend)
   - Only SELL when price < 50-day SMA (downtrend)
   - Don't mean-revert against the trend

### Alternative Strategy for Semi-Regular Use

Consider replacing mean-reversion with **Dual Momentum**:

```
Weekly Check:
1. Is SPY above its 200-day SMA?
   - YES: Invest in top momentum stocks (highest 6-month returns)
   - NO: Move to bonds/cash

2. Monthly Rebalance:
   - Rotate into top 3-5 momentum stocks
   - Historical CAGR: ~12-15%
   - Max Drawdown: ~15-20%
```

This approach:
- Only requires weekly checks (matches your schedule)
- Captures major trends instead of fighting them
- Has strong historical evidence of outperformance
- Fewer trades = lower costs

## Optimal Use Cases for Current Strategy

The mean-reversion strategy DOES work well for:
- **Intraday scalping** on volatile stocks
- **Market-making** in range-bound conditions
- **Risk-off periods** when you want capital preservation
- **High-frequency trading** with minimal commissions

## NOT Recommended For:
- Long-term wealth building
- Part-time/casual trading
- Accounts with trading commissions
- Trending markets

---

*Analysis based on 20 years of synthetic data modeled on real market characteristics*
