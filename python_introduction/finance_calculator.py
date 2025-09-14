# Prompt user for financial details
income = 5000
expenses = 4000

# Calculate monthly savings
monthly_savings = income - expenses

# Annual projection with 5% simple interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# Display results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
