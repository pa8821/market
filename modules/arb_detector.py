import pandas as pd

def detect_arbitrage_opportunities(df, min_profit_percent=1.0):
    """
    Detect arbitrage opportunities from a DataFrame containing back and lay odds.

    Args:
        df (pd.DataFrame): Must contain columns ['match', 'back_odds', 'lay_odds']
        min_profit_percent (float): Minimum profit percentage to flag as an arbitrage opportunity

    Returns:
        pd.DataFrame: Filtered rows where arbitrage is possible
    """
    opportunities = []

    for _, row in df.iterrows():
        back = row['back_odds']
        lay = row['lay_odds']
        match = row['match']

        if back > lay:
            # Calculate the potential profit margin
            profit_percent = ((back - lay) / lay) * 100

            if profit_percent >= min_profit_percent:
                opportunities.append({
                    'match': match,
                    'back_odds': back,
                    'lay_odds': lay,
                    'profit_percent': round(profit_percent, 2)
                })

    return pd.DataFrame(opportunities)
