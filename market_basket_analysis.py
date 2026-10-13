import pandas as pd
import time
from mlxtend.frequent_patterns import apriori, association_rules

# ==========================================================
# Load Dataset
# ==========================================================

df = pd.read_excel("Online Retail.xlsx")

print("Original shape:")
print(df.shape)

# ==========================================================
# Data Cleaning
# ==========================================================

# Remove missing product descriptions
df = df.dropna(subset=['Description'])

print("\nAfter removing missing descriptions:")
print(df.shape)

# Remove cancelled invoices
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

print("\nAfter removing cancelled invoices:")
print(df.shape)

# Remove invalid quantities
df = df[df['Quantity'] > 0]

print("\nAfter removing invalid quantities:")
print(df.shape)

# Select only United Kingdom transactions
df = df[df['Country'] == 'United Kingdom']

print("\nAfter selecting United Kingdom:")
print(df.shape)

# ==========================================================
# Create Basket Matrix
# ==========================================================

basket = (
    df.groupby(['InvoiceNo', 'Description'])['Quantity']
      .sum()
      .unstack()
      .fillna(0)
)

print("\nBasket shape:")
print(basket.shape)

# Convert quantities to Boolean values
basket = basket > 0

print("\nBinary basket preview:")
print(basket.head())

# ==========================================================
# Store experiment results
# ==========================================================

results = []

# ==========================================================
# Function to Run Apriori
# ==========================================================

def run_apriori(basket, support, confidence):

    print("\n" + "=" * 60)
    print(f"Support = {support}")
    print(f"Confidence = {confidence}")
    print("=" * 60)

    start_time = time.time()

    # Frequent Itemsets
    frequent_items = apriori(
        basket,
        min_support=support,
        use_colnames=True
    )

    # Association Rules
    rules = association_rules(
        frequent_items,
        metric="confidence",
        min_threshold=confidence
    )

    end_time = time.time()

    execution_time = end_time - start_time

    # Sort rules by lift
    if not rules.empty:
        rules = rules.sort_values(
            by="lift",
            ascending=False
        )

    print(f"\nExecution Time: {execution_time:.2f} seconds")
    print(f"Frequent Itemsets: {len(frequent_items)}")
    print(f"Association Rules: {len(rules)}")

    if not rules.empty:
        print("\nTop 20 Rules:")
        print(
            rules[
                [
                    "antecedents",
                    "consequents",
                    "support",
                    "confidence",
                    "lift"
                ]
            ].head(20)
        )
    else:
        print("\nNo association rules generated.")

    # Save rules to Excel
    filename = f"rules_support_{support}.xlsx"

    if not rules.empty:
        rules[
            [
                "antecedents",
                "consequents",
                "support",
                "confidence",
                "lift"
            ]
        ].to_excel(filename, index=False)
    else:
        pd.DataFrame().to_excel(filename, index=False)

    print(f"\nRules saved to {filename}")

    # Store summary for final comparison
    results.append({
        "Support": support,
        "Confidence": confidence,
        "Execution Time (s)": round(execution_time, 2),
        "Frequent Itemsets": len(frequent_items),
        "Rules": len(rules)
    })

# ==========================================================
# Run Experiments
# ==========================================================

run_apriori(basket, 0.05, 0.50)
run_apriori(basket, 0.03, 0.50)
run_apriori(basket, 0.02, 0.50)

# ==========================================================
# Final Summary
# ==========================================================

summary = pd.DataFrame(results)

print("\n")
print("=" * 70)
print("EXPERIMENT SUMMARY")
print("=" * 70)

print(summary)

summary.to_excel("experiment_summary.xlsx", index=False)

print("\nExperiment summary saved to experiment_summary.xlsx")