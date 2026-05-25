import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="La Liga Betting Analytics Dashboard",
    layout="wide"
)

st.title("⚽ La Liga 2025/26 Betting Market Analytics")

st.markdown("""
A full football analytics dashboard exploring:
- Bookmaker efficiency
- Team performance vs expectations
- Upsets by odds range
- Home advantage reliability
- Betting market risk analysis
""")

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("SP1.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# ---------------------------------------------------
# FEATURE ENGINEERING
# ---------------------------------------------------
df["GoalDiff"] = df["FTHG"] - df["FTAG"]
df["TotalGoals"] = df["FTHG"] + df["FTAG"]

df["Favorite"] = np.where(
    df["BMGMH"] < df["BMGMA"],
    df["HomeTeam"],
    df["AwayTeam"]
)

df["Favorite_Won"] = (
    ((df["Favorite"] == df["HomeTeam"]) & (df["FTR"] == "H")) |
    ((df["Favorite"] == df["AwayTeam"]) & (df["FTR"] == "A"))
)

df["Upset"] = ~df["Favorite_Won"]

# ---------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------
st.sidebar.header("🔎 Filters")

teams = sorted(df["HomeTeam"].unique())
selected_team = st.sidebar.selectbox("Select Team", ["All"] + teams)

if selected_team != "All":
    df = df[(df["HomeTeam"] == selected_team) | (df["AwayTeam"] == selected_team)]

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Matches", len(df))
col2.metric("Total Goals", df["TotalGoals"].sum())
col3.metric("Upsets", df["Upset"].sum())
col4.metric("Upset Rate", f"{df['Upset'].mean():.2%}")

st.divider()

# ---------------------------------------------------
# 1. TEAM PERFORMANCE (OVER/UNDER EXPECTATION)
# ---------------------------------------------------
st.subheader("📊 Team Performance vs Market")

team_perf = df.groupby("HomeTeam").agg(
    Matches=("FTR", "count"),
    Wins=("FTR", lambda x: (x == "H").sum())
).reset_index()

team_perf["WinRate"] = team_perf["Wins"] / team_perf["Matches"]

fig1 = px.bar(
    team_perf.sort_values("WinRate", ascending=False),
    x="WinRate",
    y="HomeTeam",
    orientation="h",
    title="Home Win Rate by Team"
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------------------------------------------
# 2. ODDS RANGE ANALYSIS
# ---------------------------------------------------
st.subheader("⚖️ Upsets by Odds Range")

def odds_bucket(row):
    odds = min(row["BMGMH"], row["BMGMA"])
    if odds <= 1.5:
        return "1.0–1.5"
    elif odds <= 2.0:
        return "1.5–2.0"
    elif odds <= 2.5:
        return "2.0–2.5"
    elif odds <= 3.0:
        return "2.5–3.0"
    else:
        return "3.0+"

df["Odds_Range"] = df.apply(odds_bucket, axis=1)

odds_analysis = df.groupby("Odds_Range").agg(
    Matches=("Upset", "count"),
    Upsets=("Upset", "sum")
)

odds_analysis["Upset_Rate"] = odds_analysis["Upsets"] / odds_analysis["Matches"]

fig2 = px.bar(
    odds_analysis.reset_index(),
    x="Odds_Range",
    y="Upset_Rate",
    title="Upset Rate by Odds Range"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------------------
# 3. HOME ADVANTAGE ANALYSIS
# ---------------------------------------------------
st.subheader("🏠 Home Advantage Analysis")

home_fav = df[df["BMGMH"] < df["BMGMA"]]

home_analysis = home_fav.groupby("HomeTeam").agg(
    Home_Fav_Matches=("FTR", "count"),
    Home_Wins=("FTR", lambda x: (x == "H").sum())
)

home_analysis["Conversion_Rate"] = (
    home_analysis["Home_Wins"] / home_analysis["Home_Fav_Matches"]
)

fig3 = px.bar(
    home_analysis.reset_index().sort_values("Conversion_Rate", ascending=False),
    x="Conversion_Rate",
    y="HomeTeam",
    orientation="h",
    title="Home Conversion Rate by Team"
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------------------------------------------
# 4. RISK ANALYSIS (VOLATILITY)
# ---------------------------------------------------
st.subheader("🚨 Team Risk (Volatility Index)")

home_upsets = df[df["Upset"]].groupby("HomeTeam").size()
away_upsets = df[df["Upset"]].groupby("AwayTeam").size()

team_upsets = home_upsets.add(away_upsets, fill_value=0)

team_matches = df["HomeTeam"].value_counts().add(
    df["AwayTeam"].value_counts(),
    fill_value=0
)

risk = (team_upsets / team_matches).reset_index()
risk.columns = ["Team", "Risk_Score"]

fig4 = px.bar(
    risk.sort_values("Risk_Score", ascending=False),
    x="Risk_Score",
    y="Team",
    orientation="h",
    title="Team Risk Index (Upset Frequency)"
)

st.plotly_chart(fig4, use_container_width=True)

# ---------------------------------------------------
# 5. RAW DATA VIEW
# ---------------------------------------------------
st.subheader("📁 Raw Data Preview")

st.dataframe(df.head(20))

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")
st.markdown("Author")
st.markdown("Stephen Yaw Ayamah, Football Data Analyst")
st.markdown("---")
st.markdown("Built using Python, Pandas, Plotly, and Streamlit")
