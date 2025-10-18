#!/usr/bin/env python3
"""
Google Trends Data Analysis - Standalone Python Script
This script runs the complete analysis from the Jupyter notebook
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import warnings
warnings.filterwarnings('ignore')

print("🚀 Starting Google Trends Data Analysis...")
print("=" * 50)

# Read the Data
print("📊 Loading datasets...")
df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')
df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')
df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-20.csv')

print(f"✅ Tesla data: {df_tesla.shape}")
print(f"✅ Bitcoin search data: {df_btc_search.shape}")
print(f"✅ Bitcoin price data: {df_btc_price.shape}")
print(f"✅ Unemployment data: {df_unemployment.shape}")

# Data Exploration
print("\n📈 Data Overview:")
print("-" * 30)
print(f"Tesla Web Search Range: {df_tesla.TSLA_WEB_SEARCH.min()} - {df_tesla.TSLA_WEB_SEARCH.max()}")
print(f"Tesla Stock Price Range: ${df_tesla.TSLA_USD_CLOSE.min():.2f} - ${df_tesla.TSLA_USD_CLOSE.max():.2f}")
print(f"Bitcoin Search Range: {df_btc_search.BTC_NEWS_SEARCH.min()} - {df_btc_search.BTC_NEWS_SEARCH.max()}")
print(f"Unemployment Benefits Search Range: {df_unemployment.UE_BENEFITS_WEB_SEARCH.min()} - {df_unemployment.UE_BENEFITS_WEB_SEARCH.max()}")

# Convert to datetime
print("\n🔄 Converting date columns...")
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)

# Create visualizations
print("\n📊 Creating visualizations...")

# Tesla Analysis
plt.figure(figsize=(14, 8))

# Tesla subplot 1 - Search trends
plt.subplot(2, 2, 1)
plt.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, 'b-', linewidth=2)
plt.title('Tesla Web Search Trends', fontsize=12, fontweight='bold')
plt.ylabel('Search Interest')
plt.grid(True, alpha=0.3)

# Tesla subplot 2 - Stock price
plt.subplot(2, 2, 2)
plt.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, 'r-', linewidth=2)
plt.title('Tesla Stock Price', fontsize=12, fontweight='bold')
plt.ylabel('Price (USD)')
plt.grid(True, alpha=0.3)

# Unemployment Analysis
plt.subplot(2, 2, 3)
plt.plot(df_unemployment.MONTH, df_unemployment.UE_BENEFITS_WEB_SEARCH, 'g-', linewidth=2)
plt.title('Unemployment Benefits Search Trends', fontsize=12, fontweight='bold')
plt.ylabel('Search Interest')
plt.grid(True, alpha=0.3)

plt.subplot(2, 2, 4)
plt.plot(df_unemployment.MONTH, df_unemployment.UNRATE, 'orange', linewidth=2)
plt.title('Actual Unemployment Rate', fontsize=12, fontweight='bold')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('google_trends_analysis.png', dpi=300, bbox_inches='tight')
print("✅ Saved: google_trends_analysis.png")

# Bitcoin Analysis (resample daily to monthly)
print("\n🔄 Resampling Bitcoin data from daily to monthly...")
df_btc_price_monthly = df_btc_price.set_index('DATE').resample('M').mean()
df_btc_price_monthly.reset_index(inplace=True)
df_btc_price_monthly['MONTH'] = df_btc_price_monthly['DATE'].dt.to_period('M').dt.start_time

# Bitcoin visualization
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(df_btc_search.MONTH, df_btc_search.BTC_NEWS_SEARCH, 'purple', linewidth=2)
plt.title('Bitcoin Search Trends', fontsize=12, fontweight='bold')
plt.ylabel('Search Interest')
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(df_btc_price_monthly.MONTH, df_btc_price_monthly.CLOSE, 'gold', linewidth=2)
plt.title('Bitcoin Price (Monthly Average)', fontsize=12, fontweight='bold')
plt.ylabel('Price (USD)')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('bitcoin_analysis.png', dpi=300, bbox_inches='tight')
print("✅ Saved: bitcoin_analysis.png")

# Summary Statistics
print("\n📊 Summary Statistics:")
print("=" * 50)
print("\nTesla Data:")
print(df_tesla[['TSLA_WEB_SEARCH', 'TSLA_USD_CLOSE']].describe())

print("\nUnemployment Data:")
print(df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].describe())

print("\nBitcoin Search Data:")
print(df_btc_search[['BTC_NEWS_SEARCH']].describe())

# Correlation Analysis
print("\n🔗 Correlation Analysis:")
print("-" * 30)
tesla_corr = df_tesla['TSLA_WEB_SEARCH'].corr(df_tesla['TSLA_USD_CLOSE'])
unemployment_corr = df_unemployment['UE_BENEFITS_WEB_SEARCH'].corr(df_unemployment['UNRATE'])

print(f"Tesla Search vs Stock Price Correlation: {tesla_corr:.3f}")
print(f"Unemployment Search vs Rate Correlation: {unemployment_corr:.3f}")

print("\n🎉 Analysis Complete!")
print("📁 Check the generated PNG files for visualizations")
print("💡 Key Insights:")
print(f"   • Tesla search interest correlates {tesla_corr:.1%} with stock price")
print(f"   • Unemployment search correlates {unemployment_corr:.1%} with actual unemployment rate")

if tesla_corr > 0.5:
    print("   • Strong positive correlation between Tesla search and stock price!")
if unemployment_corr > 0.5:
    print("   • Strong positive correlation between unemployment search and actual rates!")

plt.show()