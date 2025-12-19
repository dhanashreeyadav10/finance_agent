
# import pandas as pd
# from llm_client import call_llm

# def ap_agent(ap_df):
#     ap_df["due_date"] = pd.to_datetime(ap_df["due_date"], errors="coerce")

#     late = ap_df[
#         (ap_df["payment_status"] == "Unpaid") &
#         (ap_df["due_date"] < pd.Timestamp.today())
#     ]

#     context = f"""
# Late unpaid invoices by vendor:
# {late.groupby("vendor")["amount"].sum()}
# """
    
    

#     return call_llm(
#         "You are an AP optimization expert.",
#         context
#     )

import pandas as pd
from llm_client import call_llm

def ap_agent(ap_df: pd.DataFrame) -> str:
    ap_df = ap_df.copy()
    ap_df["due_date"] = pd.to_datetime(ap_df["due_date"], errors="coerce")

    late = ap_df[
        (ap_df["payment_status"] == "Unpaid") &
        (ap_df["due_date"] < pd.Timestamp.today())
    ]

    if late.empty:
        return "No overdue unpaid invoices found."

    summary = (
        late.groupby("vendor", as_index=False)["amount"]
        .sum()
        .to_string(index=False)
    )

    context = f"""
Late unpaid invoices by vendor:
{summary}
"""

    return call_llm("You are an AP optimization expert.", context)
