# Google Trends Data Analysis
**Day 75 Python Project: Resampling and Visualizing Time Series**

A comprehensive data analysis project exploring the relationship between Google search trends and real-world economic indicators using Python, pandas, and matplotlib.

## 🎯 Project Overview

This project investigates whether Google search popularity correlates with actual market prices and economic conditions by analyzing:

- **Tesla stock trends** vs web search interest
- **Bitcoin price movements** vs search volume  
- **Unemployment benefits searches** vs actual unemployment rates

## 📊 Key Findings

- **Tesla**: 73.5% correlation between search interest and stock price
- **Unemployment**: 85.3% correlation between "unemployment benefits" searches and actual unemployment rates
- **Bitcoin**: Strong search volume spikes during major price movements (2014-2020)

## 🗂️ Dataset Sources

- [Google Trends](https://trends.google.com/trends/explore) - Search volume data
- [Yahoo Finance](https://finance.yahoo.com/) - Tesla and Bitcoin price data
- [FRED Economic Data](https://fred.stlouisfed.org/series/UNRATE/) - US Unemployment rates

## 📁 Project Structure

```
Py-Day75/
├── Google_Trends_and_Data_Visualisation.ipynb  # Main Jupyter notebook
├── run_analysis.py                             # Standalone Python script
├── Bitcoin Search Trend.csv                    # Bitcoin search data (73 records)
├── Daily Bitcoin Price.csv                     # Bitcoin daily prices (2,203 records)
├── TESLA Search Trend vs Price.csv             # Tesla data (124 records)
├── UE Benefits Search vs UE Rate 2004-20.csv   # Unemployment data (200 records)
├── README.md                                   # This file
└── .gitignore                                  # Git ignore rules
```

## 🚀 How to Run

### Prerequisites
```bash
pip install pandas matplotlib jupyter
```

### Method 1: Python Script (Recommended)
```bash
python run_analysis.py
```

### Method 2: Jupyter Notebook
```bash
jupyter notebook Google_Trends_and_Data_Visualisation.ipynb
```

### Method 3: Jupyter Lab
```bash
python -m jupyterlab
```

## 📈 Generated Outputs

The analysis creates:
- `google_trends_analysis.png` - Tesla and unemployment visualizations
- `bitcoin_analysis.png` - Bitcoin search vs price trends
- Correlation statistics and summary insights

## 🔍 Technical Features

- **Data Cleaning**: Handles missing values and data type conversions
- **Time Series Resampling**: Converts daily Bitcoin data to monthly aggregates
- **Correlation Analysis**: Quantifies relationships between search trends and real metrics
- **Data Visualization**: Creates publication-ready charts with matplotlib
- **Statistical Summary**: Comprehensive descriptive statistics

## 💡 Business Applications

This analysis demonstrates how Google search data can be used for:
- **Market Sentiment Analysis** - Predicting stock price movements
- **Economic Forecasting** - Early indicators of unemployment trends  
- **Investment Strategy** - Using search volume as a trading signal
- **Policy Making** - Understanding public concern about economic issues

## 🛠️ Technologies Used

- **Python 3.14+**
- **pandas** - Data manipulation and analysis
- **matplotlib** - Data visualization
- **Jupyter** - Interactive development environment

## 📋 Data Quality

All datasets have been cleaned and validated:
- ✅ No missing values
- ✅ Proper datetime formatting
- ✅ Consistent data ranges
- ✅ Outlier detection completed

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements such as:
- Additional data sources
- Enhanced visualizations
- Statistical modeling
- Predictive analytics features

## 📄 License

This project is open source and available under the MIT License.
