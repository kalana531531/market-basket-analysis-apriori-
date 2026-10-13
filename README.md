# Market Basket Analysis Using Association Rule Mining

Discovering product purchasing patterns with Python and the Apriori algorithm.

## Overview

Market Basket Analysis is a data mining technique used to identify products that customers frequently purchase together. This project analyzes transactional retail data to uncover product associations and translate them into actionable business insights.

Using the Online Retail dataset, the project applies the Apriori algorithm to discover frequent itemsets and generate association rules. The results demonstrate how data mining can support product recommendations, cross-selling, product bundling, and inventory planning.

## Objectives

- Identify frequently co-purchased products.
- Discover meaningful associations between retail products.
- Evaluate association rules using support, confidence, and lift.
- Explore the impact of different minimum support thresholds.
- Derive business recommendations from the discovered patterns.

## Tech Stack

- **Language:** Python
- **Data Processing:** Pandas
- **Association Rule Mining:** MLxtend
- **Algorithm:** Apriori
- **Dataset:** Online Retail

## Dataset

The project uses the Online Retail dataset, containing transactions from a UK-based online retailer between December 2010 and December 2011.

The original dataset contains 541,909 records and includes invoice numbers, product descriptions, quantities, prices, customer IDs, and country information.

For this analysis, transactions from the United Kingdom were selected to focus on a single retail market.

## Data Preprocessing

The raw transactional data was prepared for association rule mining through the following steps:

- Removed records with missing product descriptions.
- Excluded cancelled invoices.
- Removed records with zero or negative quantities.
- Filtered transactions to include UK purchases only.
- Selected relevant transaction and product attributes.
- Transformed the cleaned data into a binary transaction matrix.

Each invoice represents a transaction, and each product is represented as an item. A value of `1` indicates that the product was included in the transaction, while `0` indicates that it was absent.

**Final dataset:** 18,194 transactions and 4,058 unique products.

## Methodology

### 1. Frequent Itemset Mining

The Apriori algorithm was used to identify product combinations that occur frequently within transactions.

### 2. Association Rule Generation

Association rules were generated from the frequent itemsets using a minimum confidence threshold.

### 3. Rule Evaluation

The generated rules were evaluated using three key metrics:

- **Support:** How frequently a product combination occurs across all transactions.
- **Confidence:** How often the consequent product appears when the antecedent product is purchased.
- **Lift:** How strongly two products are associated compared with their expected co-occurrence under independence.

A lift greater than `1` indicates a positive association.

### 4. Parameter Experimentation

Different minimum support thresholds were tested while keeping minimum confidence fixed at `0.50`.

| Minimum Support | Frequent Itemsets | Association Rules | Execution Time |
|---:|---:|---:|---:|
| 0.05 | 33 | 0 | 0.16 s |
| 0.03 | 140 | 13 | 1.77 s |
| 0.02 | 392* | 72 | 8.92 s |

The lower support threshold revealed more product associations, but required additional computation time.

*The final itemset count should be verified against the actual Python output before publication.*

## Key Findings

The analysis identified associations between products belonging to related collections and complementary product ranges.

| Product Association | Support | Confidence | Lift |
|---|---:|---:|---:|
| Wooden Star Christmas Scandinavian → Wooden Heart Christmas Scandinavian | 2.02% | 76.83% | 27.46 |
| Green Regency Teacup and Saucer → Pink Regency Teacup and Saucer | 3.17% | 61.78% | 15.99 |
| Dolly Girl Lunch Box → Spaceboy Lunch Box | 2.34% | 60.94% | 15.82 |
| Strawberry Charlotte Bag → Woodland Charlotte Bag | 2.06% | 55.57% | 14.80 |
| Gardeners Kneeling Pad Keep Calm → Gardeners Kneeling Pad Cup of Tea | 2.97% | 60.24% | 14.61 |
| Jumbo Bag Pink Polkadot → Jumbo Bag Red Retrospot | 4.31% | 67.73% | 6.36 |

### What Do These Results Tell Us?

- **Related product collections:** Customers may purchase multiple designs from the same product range.
- **Complementary purchases:** Some products show strong co-purchasing relationships that could support cross-selling.
- **Seasonal buying patterns:** Christmas-themed products exhibit strong associations that could be useful for seasonal campaigns.
- **Recommendation opportunities:** Association rules can help identify relevant products to suggest during online shopping.

These associations describe patterns in the analyzed transactions; they do not by themselves establish why customers purchase the products together.

## Business Applications

The discovered patterns could support several retail strategies:

- **Product recommendations:** Suggest related products when a customer views or adds an item to their cart.
- **Product bundling:** Create bundles from products with strong purchasing associations.
- **Cross-selling:** Promote complementary items to increase the number of products purchased per order.
- **Inventory planning:** Consider relationships between product demand when planning stock availability.
- **Seasonal marketing:** Design targeted promotions around associated seasonal products.

## Project Structure

```text
Market-Basket-Analysis/
├── README.md
├── Market_Basket_Analysis_Report.pdf
├── market_basket_analysis.py
└── requirements.txt
```

Replace the example Python filename with your actual script or notebook filename.

## Installation and Usage

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Market-Basket-Analysis
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Prepare the dataset

Download the Online Retail dataset and place it in the location expected by the source code. Update the dataset path if necessary.

### 4. Run the analysis

For a Python script:

```bash
python market_basket_analysis.py
```

For a Jupyter Notebook, open the notebook and execute the cells in order.

## What I Learned

Through this project, I gained practical experience in:

- Cleaning and preprocessing transactional data.
- Transforming retail records into a transaction matrix.
- Implementing frequent itemset mining with the Apriori algorithm.
- Evaluating association rules using support, confidence, and lift.
- Experimenting with algorithm parameters and comparing results.
- Interpreting data mining results to develop business recommendations.

## Future Improvements

- Visualize association rules and product relationships.
- Compare Apriori with alternative frequent itemset mining algorithms.
- Explore transaction patterns across different countries.
- Investigate changes in purchasing associations over time.
- Develop a simple product recommendation interface based on the discovered rules.

---

**Project Focus:** Data Mining · Python · Association Rule Mining · Retail Analytics · Business Intelligence