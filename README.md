# Cross-Border Arbitrage Simulator

## Overview

The **Cross-Border Arbitrage Simulator** is a tool designed to analyze and simulate arbitrage opportunities between domestic and foreign stock markets. This project focuses on utilizing Shopify's ticker for demonstration purposes, allowing users to explore the potential for profit through cross-border trading strategies.

## Project Structure

The project consists of the following files:

- **notebooks/cross_border_arbitrage_simulator.ipynb**: This Jupyter notebook contains the main logic for the Cross-Border Arbitrage Simulator. It includes sections for importing libraries, fetching data, processing it, and visualizing results.

- **src/cross_border_arbitrage_simulator.py**: This Python script contains the core functionality of the simulator. It includes functions for fetching stock prices, calculating exchange rates, and executing the arbitrage strategy based on the provided parameters.

- **requirements.txt**: This file lists the dependencies required for the project, including libraries such as pandas, numpy, yfinance, and matplotlib.

## Setup Instructions

1. Clone the repository

2. Navigate to the project directory:
   ```
   cd cross-border-arbitrage-simulator
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To use the Cross-Border Arbitrage Simulator:

1. Open the Jupyter notebook located in the `notebooks` directory:
   ```
   jupyter notebook notebooks/cross_border_arbitrage_simulator.ipynb
   ```

2. Follow the instructions in the notebook to run the simulation and analyze the results.

## Methodology

The simulator operates by fetching historical stock prices for Shopify (SHOP) from both the domestic (TSX) and foreign (NYSE) exchanges. It calculates the exchange rates and identifies potential arbitrage opportunities based on the price discrepancies between the two markets. The results are visualized to provide insights into the profitability of the strategy over time.