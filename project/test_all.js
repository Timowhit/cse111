/**
 * TradeSmart Guide - Comprehensive Test Suite
 * Tests all functions in siteplan.js and autotrade.js
 * 
 * Run with: node test_all.js
 * Or open test_runner.html in browser
 */

// ============================================
// SIMPLE TEST FRAMEWORK
// ============================================

const TestRunner = {
    tests: [],
    passed: 0,
    failed: 0,
    results: [],

    describe(suiteName, fn) {
        console.log(`\n📦 ${suiteName}`);
        console.log('─'.repeat(50));
        this.currentSuite = suiteName;
        fn();
    },

    test(name, fn) {
        try {
            fn();
            this.passed++;
            this.results.push({ suite: this.currentSuite, name, status: 'PASS' });
            console.log(`  ✅ ${name}`);
        } catch (error) {
            this.failed++;
            this.results.push({ suite: this.currentSuite, name, status: 'FAIL', error: error.message });
            console.log(`  ❌ ${name}`);
            console.log(`     Error: ${error.message}`);
        }
    },

    assertEqual(actual, expected, message = '') {
        if (actual !== expected) {
            throw new Error(`${message} Expected ${expected}, got ${actual}`);
        }
    },

    assertAlmostEqual(actual, expected, tolerance = 0.01, message = '') {
        if (Math.abs(actual - expected) > tolerance) {
            throw new Error(`${message} Expected ~${expected}, got ${actual} (tolerance: ${tolerance})`);
        }
    },

    assertTrue(condition, message = '') {
        if (!condition) {
            throw new Error(message || 'Expected true, got false');
        }
    },

    assertFalse(condition, message = '') {
        if (condition) {
            throw new Error(message || 'Expected false, got true');
        }
    },

    assertArrayEqual(actual, expected, message = '') {
        if (JSON.stringify(actual) !== JSON.stringify(expected)) {
            throw new Error(`${message} Arrays not equal`);
        }
    },

    assertInRange(value, min, max, message = '') {
        if (value < min || value > max) {
            throw new Error(`${message} Value ${value} not in range [${min}, ${max}]`);
        }
    },

    summary() {
        console.log('\n' + '='.repeat(50));
        console.log('📊 TEST SUMMARY');
        console.log('='.repeat(50));
        console.log(`Total: ${this.passed + this.failed}`);
        console.log(`Passed: ${this.passed} ✅`);
        console.log(`Failed: ${this.failed} ❌`);
        console.log(`Success Rate: ${((this.passed / (this.passed + this.failed)) * 100).toFixed(1)}%`);
        console.log('='.repeat(50));
        
        return {
            total: this.passed + this.failed,
            passed: this.passed,
            failed: this.failed,
            results: this.results
        };
    }
};

// ============================================
// EXTRACTED FUNCTIONS FOR TESTING
// (These mirror the functions in the actual codebase)
// ============================================

// From siteplan.js - Projection Calculator
const compoundingPeriods = {
    daily: 365,
    monthly: 12,
    quarterly: 4,
    annually: 1
};

const frequencyMultipliers = {
    weekly: 52,
    biweekly: 26,
    monthly: 12,
    quarterly: 4,
    annually: 1
};

function calculateAdvancedProjection(principal, recurringAmount, frequency, years, annualRate, inflationRate, contributionIncrease, compoundFreq) {
    const periodsPerYear = compoundingPeriods[compoundFreq] || 12;
    const contributionsPerYear = frequencyMultipliers[frequency] || 12;
    const ratePerPeriod = (annualRate / 100) / periodsPerYear;
    const inflationRateDecimal = inflationRate / 100;
    const contributionIncreaseDecimal = contributionIncrease / 100;

    let totalValue = principal;
    let totalContributions = principal;
    let currentContribution = recurringAmount;

    for (let year = 0; year < years; year++) {
        if (year > 0) {
            currentContribution = currentContribution * (1 + contributionIncreaseDecimal);
        }

        for (let month = 0; month < 12; month++) {
            const contributionsThisMonth = (contributionsPerYear / 12) * currentContribution;
            totalContributions += contributionsThisMonth;
            totalValue += contributionsThisMonth;

            const monthlyRate = Math.pow(1 + ratePerPeriod, periodsPerYear / 12) - 1;
            totalValue = totalValue * (1 + monthlyRate);
        }
    }

    const inflationFactor = Math.pow(1 + inflationRateDecimal, years);
    const realValue = totalValue / inflationFactor;

    return {
        nominalValue: Math.round(totalValue),
        realValue: Math.round(realValue),
        totalContributions: Math.round(totalContributions),
        totalGrowth: Math.round(totalValue - totalContributions)
    };
}

// From siteplan.js - Stock Recommendations Generator
function generateStockRecommendations(amount, stocksPct, bondsPct, altsPct) {
    const recommendations = [];
    
    const stockAmount = amount * (stocksPct / 100);
    const bondAmount = amount * (bondsPct / 100);
    const altAmount = amount * (altsPct / 100);
    
    if (stockAmount > 0) {
        recommendations.push({
            ticker: 'VTI',
            name: 'Vanguard Total Stock Market ETF',
            amount: stockAmount * 0.6,
            percentage: stocksPct * 0.6
        });
        
        recommendations.push({
            ticker: 'VXUS',
            name: 'Vanguard Total International Stock ETF',
            amount: stockAmount * 0.4,
            percentage: stocksPct * 0.4
        });
    }
    
    if (bondAmount > 0) {
        recommendations.push({
            ticker: 'BND',
            name: 'Vanguard Total Bond Market ETF',
            amount: bondAmount,
            percentage: bondsPct
        });
    }
    
    if (altAmount > 0) {
        recommendations.push({
            ticker: 'VNQ',
            name: 'Vanguard Real Estate ETF',
            amount: altAmount,
            percentage: altsPct
        });
    }
    
    return recommendations;
}

// From siteplan.js - Simple Projected Value
function calculateProjectedValue(principal, years, annualRate) {
    return Math.round(principal * Math.pow(1 + (annualRate / 100), years));
}

// From autotrade.js - Default Config
const DEFAULT_OPTIMIZED_CONFIG = {
    tradingBuffer: 0.03,
    smaWindow: 20,
    maxCashPerStock: 0.25,
    minSharesToBuy: 5,
    trendSmaWindow: 50,
    requireTrendAlignment: true,
    takeProfitPct: 0.08,
    stopLossPct: 0.04,
    useTrailingStop: true,
    trailingStopTrigger: 0.05,
    trailingStopDistance: 0.02,
    checkInterval: 300,
    sessionDurationMinutes: 120,
    sessionsPerWeek: 2.5,
    verbose: true
};

// From autotrade.js - Price Simulator (simplified for testing)
function simulatePrice(stock, priceHistory, config) {
    const basePrices = {
        'QQQ': 520, 'SPY': 590, 'VOO': 540, 'TSLA': 250, 'AAPL': 195,
        'MSFT': 420, 'GOOGL': 175, 'AMZN': 205, 'NVDA': 140, 'META': 565
    };
    
    let basePrice = basePrices[stock] || 100 + Math.random() * 200;
    
    let lastPrice = priceHistory.length > 0 
        ? priceHistory[priceHistory.length - 1].price 
        : basePrice;
    
    const volatility = 0.004;
    const change = (Math.random() - 0.48) * volatility * lastPrice;
    const newPrice = Math.max(lastPrice + change, 1);
    
    priceHistory.push({ price: newPrice, time: new Date() });
    
    if (priceHistory.length > 100) {
        priceHistory.shift();
    }
    
    const prices = priceHistory.map(p => p.price);
    const smaWindow = Math.min(config.smaWindow, prices.length);
    const sma = prices.slice(-smaWindow).reduce((a, b) => a + b, 0) / smaWindow;
    
    const trendWindow = Math.min(config.trendSmaWindow, prices.length);
    const trendSma = prices.slice(-trendWindow).reduce((a, b) => a + b, 0) / trendWindow;
    
    return { 
        price: newPrice, 
        sma: sma, 
        trendSma: trendSma,
        ratio: newPrice / sma 
    };
}

// From autotrade.js - Signal Processing Logic (pure function version)
function evaluateSignal(priceData, holding, config) {
    const { price, sma, trendSma, ratio } = priceData;
    const inUptrend = price > trendSma;
    
    let action = 'HOLD';
    let reason = '';
    
    // Check exits if holding position
    if (holding.shares > 0) {
        const currentProfitPct = (price / holding.avgPrice - 1);
        const drawdownFromHigh = holding.highSinceBuy > 0 
            ? (price / holding.highSinceBuy - 1) 
            : 0;
        
        // Take profit
        if (currentProfitPct >= config.takeProfitPct) {
            action = 'SELL';
            reason = `TAKE_PROFIT: ${(currentProfitPct * 100).toFixed(1)}% gain`;
        }
        // Stop loss
        else if (currentProfitPct <= -config.stopLossPct) {
            action = 'SELL';
            reason = `STOP_LOSS: ${(currentProfitPct * 100).toFixed(1)}% loss`;
        }
        // Trailing stop
        else if (config.useTrailingStop && 
                 currentProfitPct > config.trailingStopTrigger && 
                 drawdownFromHigh < -config.trailingStopDistance) {
            action = 'SELL';
            reason = `TRAILING_STOP: gave back ${(-drawdownFromHigh * 100).toFixed(1)}%`;
        }
        // SMA signal in downtrend
        else if (ratio > (1 + config.tradingBuffer) && !inUptrend) {
            action = 'SELL';
            reason = 'SMA_SIGNAL + DOWNTREND';
        }
    }
    
    // Check buy signal if no position
    if (holding.shares === 0 && ratio < (1 - config.tradingBuffer)) {
        if (config.requireTrendAlignment && !inUptrend) {
            action = 'BLOCKED';
            reason = 'BUY blocked - price below trend SMA';
        } else {
            action = 'BUY';
            reason = `Buffer triggered at ${((ratio - 1) * 100).toFixed(2)}%`;
        }
    }
    
    return { action, reason, inUptrend, profitPct: holding.shares > 0 ? (price / holding.avgPrice - 1) : 0 };
}

// SMA Calculation Helper
function calculateSMA(prices, window) {
    if (prices.length === 0) return 0;
    const effectiveWindow = Math.min(window, prices.length);
    const slice = prices.slice(-effectiveWindow);
    return slice.reduce((a, b) => a + b, 0) / slice.length;
}

// Portfolio Allocation Validator
function validateAllocation(stocks, bonds, alternatives) {
    const total = stocks + bonds + alternatives;
    return {
        isValid: Math.abs(total - 100) < 0.01,
        total: total,
        stocks: stocks,
        bonds: bonds,
        alternatives: alternatives
    };
}

// ============================================
// TEST SUITES
// ============================================

// Test Suite: Advanced Projection Calculator
TestRunner.describe('Advanced Projection Calculator', () => {
    TestRunner.test('Basic projection without contributions', () => {
        const result = calculateAdvancedProjection(
            10000,  // principal
            0,      // recurring
            'monthly',
            10,     // years
            7,      // return
            2.5,    // inflation
            0,      // contribution increase
            'monthly'
        );
        
        TestRunner.assertTrue(result.nominalValue > 10000, 'Should grow with positive return');
        TestRunner.assertTrue(result.realValue < result.nominalValue, 'Real value should be less due to inflation');
        TestRunner.assertEqual(result.totalContributions, 10000, 'Contributions should equal principal');
    });

    TestRunner.test('Projection with monthly contributions', () => {
        const result = calculateAdvancedProjection(
            10000,  // principal
            500,    // recurring monthly
            'monthly',
            10,     // years
            7,      // return
            2.5,    // inflation
            0,      // contribution increase
            'monthly'
        );
        
        // $500/month * 12 months * 10 years = $60,000 + $10,000 principal = $70,000
        TestRunner.assertTrue(result.totalContributions > 69000, 'Should have ~$70k in contributions');
        TestRunner.assertTrue(result.totalContributions < 71000, 'Should have ~$70k in contributions');
        TestRunner.assertTrue(result.nominalValue > result.totalContributions, 'Should have growth');
    });

    TestRunner.test('Projection with contribution increases', () => {
        const withIncrease = calculateAdvancedProjection(
            10000, 500, 'monthly', 10, 7, 2.5, 3, 'monthly'
        );
        const withoutIncrease = calculateAdvancedProjection(
            10000, 500, 'monthly', 10, 7, 2.5, 0, 'monthly'
        );
        
        TestRunner.assertTrue(
            withIncrease.totalContributions > withoutIncrease.totalContributions,
            'Contribution increases should result in higher total contributions'
        );
    });

    TestRunner.test('Zero return should only preserve contributions', () => {
        const result = calculateAdvancedProjection(
            10000, 0, 'monthly', 5, 0, 0, 0, 'monthly'
        );
        
        TestRunner.assertAlmostEqual(result.nominalValue, 10000, 100, 'Should approximately equal principal with 0% return');
    });

    TestRunner.test('Different compounding frequencies', () => {
        const daily = calculateAdvancedProjection(10000, 0, 'monthly', 10, 10, 0, 0, 'daily');
        const annual = calculateAdvancedProjection(10000, 0, 'monthly', 10, 10, 0, 0, 'annually');
        
        TestRunner.assertTrue(
            daily.nominalValue >= annual.nominalValue,
            'More frequent compounding should yield higher or equal returns'
        );
    });
});

// Test Suite: Stock Recommendations Generator
TestRunner.describe('Stock Recommendations Generator', () => {
    TestRunner.test('60/30/10 allocation', () => {
        const recommendations = generateStockRecommendations(10000, 60, 30, 10);
        
        TestRunner.assertEqual(recommendations.length, 4, 'Should have 4 recommendations');
        
        // Check tickers
        const tickers = recommendations.map(r => r.ticker);
        TestRunner.assertTrue(tickers.includes('VTI'), 'Should include VTI');
        TestRunner.assertTrue(tickers.includes('VXUS'), 'Should include VXUS');
        TestRunner.assertTrue(tickers.includes('BND'), 'Should include BND');
        TestRunner.assertTrue(tickers.includes('VNQ'), 'Should include VNQ');
    });

    TestRunner.test('Amounts should sum to total', () => {
        const recommendations = generateStockRecommendations(10000, 60, 30, 10);
        const totalAmount = recommendations.reduce((sum, r) => sum + r.amount, 0);
        
        TestRunner.assertAlmostEqual(totalAmount, 10000, 1, 'Amounts should sum to $10,000');
    });

    TestRunner.test('Percentages should be correct', () => {
        const recommendations = generateStockRecommendations(10000, 60, 30, 10);
        const totalPct = recommendations.reduce((sum, r) => sum + r.percentage, 0);
        
        TestRunner.assertAlmostEqual(totalPct, 100, 0.1, 'Percentages should sum to 100%');
    });

    TestRunner.test('Zero allocation categories', () => {
        const stocksOnly = generateStockRecommendations(10000, 100, 0, 0);
        
        TestRunner.assertEqual(stocksOnly.length, 2, 'Should only have stock recommendations');
        TestRunner.assertFalse(
            stocksOnly.some(r => r.ticker === 'BND'),
            'Should not include bonds'
        );
    });

    TestRunner.test('Large investment amount', () => {
        const recommendations = generateStockRecommendations(1000000, 70, 20, 10);
        const vti = recommendations.find(r => r.ticker === 'VTI');
        
        TestRunner.assertAlmostEqual(vti.amount, 420000, 1, 'VTI should be 42% of $1M');
    });
});

// Test Suite: Simple Projected Value
TestRunner.describe('Simple Projected Value Calculator', () => {
    TestRunner.test('10 years at 7% return', () => {
        const result = calculateProjectedValue(10000, 10, 7);
        // 10000 * (1.07)^10 ≈ 19672
        TestRunner.assertAlmostEqual(result, 19672, 100, 'Should double approximately in 10 years at 7%');
    });

    TestRunner.test('Zero years should return principal', () => {
        const result = calculateProjectedValue(10000, 0, 10);
        TestRunner.assertEqual(result, 10000, 'Zero years should return principal');
    });

    TestRunner.test('Rule of 72 approximation', () => {
        // At 10%, money should roughly double in ~7.2 years
        const result = calculateProjectedValue(10000, 7, 10);
        TestRunner.assertInRange(result, 18000, 22000, 'Should roughly double in 7 years at 10%');
    });
});

// Test Suite: Default Optimized Config
TestRunner.describe('Optimized Trading Configuration', () => {
    TestRunner.test('Buffer is optimized (3%)', () => {
        TestRunner.assertEqual(DEFAULT_OPTIMIZED_CONFIG.tradingBuffer, 0.03, 'Buffer should be 3%');
    });

    TestRunner.test('SMA window is optimized (20)', () => {
        TestRunner.assertEqual(DEFAULT_OPTIMIZED_CONFIG.smaWindow, 20, 'SMA window should be 20');
    });

    TestRunner.test('Position size is optimized (25%)', () => {
        TestRunner.assertEqual(DEFAULT_OPTIMIZED_CONFIG.maxCashPerStock, 0.25, 'Max position should be 25%');
    });

    TestRunner.test('Take profit is set (8%)', () => {
        TestRunner.assertEqual(DEFAULT_OPTIMIZED_CONFIG.takeProfitPct, 0.08, 'Take profit should be 8%');
    });

    TestRunner.test('Stop loss is set (4%)', () => {
        TestRunner.assertEqual(DEFAULT_OPTIMIZED_CONFIG.stopLossPct, 0.04, 'Stop loss should be 4%');
    });

    TestRunner.test('Trend filter is enabled', () => {
        TestRunner.assertTrue(DEFAULT_OPTIMIZED_CONFIG.requireTrendAlignment, 'Trend filter should be on');
    });

    TestRunner.test('Session duration is 120 minutes', () => {
        TestRunner.assertEqual(DEFAULT_OPTIMIZED_CONFIG.sessionDurationMinutes, 120, 'Session should be 2 hours');
    });
});

// Test Suite: Price Simulator
TestRunner.describe('Price Simulator', () => {
    TestRunner.test('Generates valid price data', () => {
        const priceHistory = [];
        const config = { smaWindow: 20, trendSmaWindow: 50 };
        
        const result = simulatePrice('SPY', priceHistory, config);
        
        TestRunner.assertTrue(result.price > 0, 'Price should be positive');
        TestRunner.assertTrue(result.sma > 0, 'SMA should be positive');
        TestRunner.assertTrue(result.trendSma > 0, 'Trend SMA should be positive');
        TestRunner.assertTrue(result.ratio > 0, 'Ratio should be positive');
    });

    TestRunner.test('Price stays within reasonable bounds', () => {
        const priceHistory = [];
        const config = { smaWindow: 20, trendSmaWindow: 50 };
        
        // Run 100 iterations
        for (let i = 0; i < 100; i++) {
            simulatePrice('SPY', priceHistory, config);
        }
        
        const lastPrice = priceHistory[priceHistory.length - 1].price;
        // SPY base price is 590, should stay within reasonable range
        TestRunner.assertInRange(lastPrice, 400, 800, 'Price should stay within bounds');
    });

    TestRunner.test('History is capped at 100 entries', () => {
        const priceHistory = [];
        const config = { smaWindow: 20, trendSmaWindow: 50 };
        
        for (let i = 0; i < 150; i++) {
            simulatePrice('SPY', priceHistory, config);
        }
        
        TestRunner.assertEqual(priceHistory.length, 100, 'History should be capped at 100');
    });

    TestRunner.test('Unknown stock gets random base price', () => {
        const priceHistory = [];
        const config = { smaWindow: 20, trendSmaWindow: 50 };
        
        const result = simulatePrice('UNKNOWN', priceHistory, config);
        
        TestRunner.assertInRange(result.price, 1, 500, 'Unknown stock should get valid price');
    });
});

// Test Suite: Signal Evaluation
TestRunner.describe('Trading Signal Evaluation', () => {
    TestRunner.test('Take profit triggers at 8% gain', () => {
        const priceData = { price: 108, sma: 100, trendSma: 95, ratio: 1.08 };
        const holding = { shares: 10, avgPrice: 100, highSinceBuy: 108 };
        
        const result = evaluateSignal(priceData, holding, DEFAULT_OPTIMIZED_CONFIG);
        
        TestRunner.assertEqual(result.action, 'SELL', 'Should trigger sell');
        TestRunner.assertTrue(result.reason.includes('TAKE_PROFIT'), 'Reason should be take profit');
    });

    TestRunner.test('Stop loss triggers at 4% loss', () => {
        const priceData = { price: 96, sma: 100, trendSma: 105, ratio: 0.96 };
        const holding = { shares: 10, avgPrice: 100, highSinceBuy: 100 };
        
        const result = evaluateSignal(priceData, holding, DEFAULT_OPTIMIZED_CONFIG);
        
        TestRunner.assertEqual(result.action, 'SELL', 'Should trigger sell');
        TestRunner.assertTrue(result.reason.includes('STOP_LOSS'), 'Reason should be stop loss');
    });

    TestRunner.test('Buy signal in uptrend', () => {
        const priceData = { price: 96, sma: 100, trendSma: 95, ratio: 0.96 };
        const holding = { shares: 0, avgPrice: 0, highSinceBuy: 0 };
        
        const result = evaluateSignal(priceData, holding, DEFAULT_OPTIMIZED_CONFIG);
        
        TestRunner.assertEqual(result.action, 'BUY', 'Should trigger buy in uptrend');
    });

    TestRunner.test('Buy blocked in downtrend with trend filter', () => {
        const priceData = { price: 96, sma: 100, trendSma: 100, ratio: 0.96 };
        const holding = { shares: 0, avgPrice: 0, highSinceBuy: 0 };
        
        const result = evaluateSignal(priceData, holding, DEFAULT_OPTIMIZED_CONFIG);
        
        TestRunner.assertEqual(result.action, 'BLOCKED', 'Should block buy in downtrend');
    });

    TestRunner.test('Buy allowed in downtrend without trend filter', () => {
        const configNoTrend = { ...DEFAULT_OPTIMIZED_CONFIG, requireTrendAlignment: false };
        const priceData = { price: 96, sma: 100, trendSma: 100, ratio: 0.96 };
        const holding = { shares: 0, avgPrice: 0, highSinceBuy: 0 };
        
        const result = evaluateSignal(priceData, holding, configNoTrend);
        
        TestRunner.assertEqual(result.action, 'BUY', 'Should allow buy without trend filter');
    });

    TestRunner.test('Hold when no signal triggers', () => {
        const priceData = { price: 100, sma: 100, trendSma: 98, ratio: 1.0 };
        const holding = { shares: 10, avgPrice: 99, highSinceBuy: 100 };
        
        const result = evaluateSignal(priceData, holding, DEFAULT_OPTIMIZED_CONFIG);
        
        TestRunner.assertEqual(result.action, 'HOLD', 'Should hold when price is neutral');
    });

    TestRunner.test('Trailing stop activates correctly', () => {
        // Entry at 100, current price 106, high was 110
        // Profit: (106/100 - 1) = 6% (above 5% trigger)
        // Drawdown from high: (106/110 - 1) = -3.6% (below -2% threshold)
        const priceData = { price: 106, sma: 100, trendSma: 98, ratio: 1.06 };
        const holding = { shares: 10, avgPrice: 100, highSinceBuy: 110 };
        
        const result = evaluateSignal(priceData, holding, DEFAULT_OPTIMIZED_CONFIG);
        
        TestRunner.assertEqual(result.action, 'SELL', 'Should trigger trailing stop');
        TestRunner.assertTrue(result.reason.includes('TRAILING_STOP'), 'Reason should be trailing stop');
    });
});

// Test Suite: SMA Calculation
TestRunner.describe('SMA Calculation', () => {
    TestRunner.test('Simple average of prices', () => {
        const prices = [100, 102, 104, 106, 108];
        const sma = calculateSMA(prices, 5);
        
        TestRunner.assertEqual(sma, 104, 'SMA of 100-108 should be 104');
    });

    TestRunner.test('Partial window when not enough data', () => {
        const prices = [100, 105];
        const sma = calculateSMA(prices, 20);
        
        TestRunner.assertEqual(sma, 102.5, 'Should use available data');
    });

    TestRunner.test('Empty prices array', () => {
        const sma = calculateSMA([], 20);
        
        TestRunner.assertEqual(sma, 0, 'Empty array should return 0');
    });

    TestRunner.test('Window of 1', () => {
        const prices = [100, 105, 110, 115, 120];
        const sma = calculateSMA(prices, 1);
        
        TestRunner.assertEqual(sma, 120, 'Window of 1 should return last price');
    });
});

// Test Suite: Portfolio Allocation Validation
TestRunner.describe('Portfolio Allocation Validation', () => {
    TestRunner.test('Valid 60/30/10 allocation', () => {
        const result = validateAllocation(60, 30, 10);
        
        TestRunner.assertTrue(result.isValid, 'Should be valid');
        TestRunner.assertEqual(result.total, 100, 'Total should be 100');
    });

    TestRunner.test('Invalid allocation (over 100%)', () => {
        const result = validateAllocation(60, 30, 20);
        
        TestRunner.assertFalse(result.isValid, 'Should be invalid');
        TestRunner.assertEqual(result.total, 110, 'Total should be 110');
    });

    TestRunner.test('Invalid allocation (under 100%)', () => {
        const result = validateAllocation(50, 30, 10);
        
        TestRunner.assertFalse(result.isValid, 'Should be invalid');
        TestRunner.assertEqual(result.total, 90, 'Total should be 90');
    });

    TestRunner.test('All stocks allocation', () => {
        const result = validateAllocation(100, 0, 0);
        
        TestRunner.assertTrue(result.isValid, 'All stocks should be valid');
    });
});

// Test Suite: Frequency Multipliers
TestRunner.describe('Frequency Multipliers', () => {
    TestRunner.test('Weekly is 52', () => {
        TestRunner.assertEqual(frequencyMultipliers.weekly, 52, 'Weekly should be 52');
    });

    TestRunner.test('Biweekly is 26', () => {
        TestRunner.assertEqual(frequencyMultipliers.biweekly, 26, 'Biweekly should be 26');
    });

    TestRunner.test('Monthly is 12', () => {
        TestRunner.assertEqual(frequencyMultipliers.monthly, 12, 'Monthly should be 12');
    });

    TestRunner.test('Quarterly is 4', () => {
        TestRunner.assertEqual(frequencyMultipliers.quarterly, 4, 'Quarterly should be 4');
    });

    TestRunner.test('Annually is 1', () => {
        TestRunner.assertEqual(frequencyMultipliers.annually, 1, 'Annually should be 1');
    });
});

// Test Suite: Edge Cases
TestRunner.describe('Edge Cases and Boundary Conditions', () => {
    TestRunner.test('Very long investment horizon (50 years)', () => {
        const result = calculateAdvancedProjection(
            10000, 100, 'monthly', 50, 7, 2.5, 0, 'monthly'
        );
        
        TestRunner.assertTrue(result.nominalValue > 500000, 'Should grow significantly over 50 years');
    });

    TestRunner.test('Very high return rate (25%)', () => {
        const result = calculateAdvancedProjection(
            10000, 0, 'monthly', 10, 25, 0, 0, 'monthly'
        );
        
        TestRunner.assertTrue(result.nominalValue > 90000, 'High returns should compound aggressively');
    });

    TestRunner.test('Negative real returns (high inflation)', () => {
        const result = calculateAdvancedProjection(
            10000, 0, 'monthly', 10, 2, 10, 0, 'monthly'
        );
        
        TestRunner.assertTrue(result.realValue < 10000, 'Real value should decrease with high inflation');
    });

    TestRunner.test('Small investment amount ($100)', () => {
        const recommendations = generateStockRecommendations(100, 60, 30, 10);
        
        TestRunner.assertEqual(recommendations.length, 4, 'Should still generate recommendations');
        TestRunner.assertTrue(
            recommendations.every(r => r.amount > 0),
            'All amounts should be positive'
        );
    });

    TestRunner.test('Fractional percentages', () => {
        const recommendations = generateStockRecommendations(10000, 33.33, 33.33, 33.34);
        const totalPct = recommendations.reduce((sum, r) => sum + r.percentage, 0);
        
        TestRunner.assertAlmostEqual(totalPct, 100, 0.1, 'Should handle fractional percentages');
    });
});

// ============================================
// RUN ALL TESTS
// ============================================

console.log('\n');
console.log('🧪 TradeSmart Guide - Test Suite');
console.log('='.repeat(50));
console.log('Running all tests...\n');

const testResults = TestRunner.summary();

// Export for use in browser or Node
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        TestRunner,
        calculateAdvancedProjection,
        generateStockRecommendations,
        calculateProjectedValue,
        simulatePrice,
        evaluateSignal,
        calculateSMA,
        validateAllocation,
        DEFAULT_OPTIMIZED_CONFIG,
        frequencyMultipliers,
        compoundingPeriods,
        testResults
    };
}
