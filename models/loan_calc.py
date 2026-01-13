def calculate_loan(property_price, years=20):
    """
    Calculates Loan Handling Insights:
    - Assumes 20% down payment
    - 7% annual interest rate
    - Monthly EMI calculation
    """

    down_payment = property_price * 0.20
    loan_amount = property_price - down_payment

    annual_interest_rate = 0.07  # 7% interest
    monthly_interest_rate = annual_interest_rate / 12
    months = years * 12

    # EMI Formula
    emi = (
        loan_amount
        * monthly_interest_rate
        * ((1 + monthly_interest_rate) ** months)
    ) / (((1 + monthly_interest_rate) ** months) - 1)

    total_repayment = emi * months

    return {
        "property_price": f"₹{property_price:,.2f}",
        "down_payment": f"₹{down_payment:,.2f}",
        "monthly_emi": f"₹{emi:,.2f}",
        "total_repayment": f"₹{total_repayment:,.2f}",
        "loan_tenure_years": years
    }
