def predict_price(current_price, years):
    """
    Predict future property price using appreciation model:
    - Assumes 6% annual appreciation
    - Uses compound growth formula
    """

    annual_growth_rate = 0.06  # 6% appreciation

    future_price = current_price * ((1 + annual_growth_rate) ** years)

    return round(future_price, 2)
