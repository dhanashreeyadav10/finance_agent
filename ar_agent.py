
# from forecasting import forecast_series
# from llm_client import call_llm

# def ar_agent(ar_df):
#     ar_df["DSO"] = ar_df["days_overdue"] + 30
#     forecast = forecast_series(ar_df["DSO"])

#     return call_llm(
#         "You are an AR expert.",
#         f"Avg DSO: {ar_df['DSO'].mean()}, Forecast: {forecast[:5]}"
#     )

from forecasting import forecast_series
from llm_client import call_llm

def ar_agent(ar_df):
    ar_df = ar_df.copy()
    ar_df["DSO"] = ar_df["days_overdue"] + 30

    forecast = forecast_series(ar_df["DSO"])

    return call_llm(
        "You are an Accounts Receivable expert.",
        f"Average DSO: {ar_df['DSO'].mean():.2f}, Forecast (next days): {forecast[:5]}"
    )
