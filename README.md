# ⚽ La Liga 2025/26 Betting Market & Performance Analytics

A data-driven football analytics project exploring **match outcomes, bookmaker odds efficiency, team performance vs expectations, and betting market risk** in the 2025/2026 season of La Liga.

---

## 📊 Project Overview

This project analyzes all 380 matches from the 2025/26 season of **La Liga** using match results and bookmaker odds from BetMGM.

The goal is to evaluate:

- How accurate betting markets are
- Which teams over/underperform expectations
- Where upsets are most likely to occur
- Which teams create the most betting risk

---

## 🧠 Business Questions Answered

This project answers 5 key football analytics questions:

### 1. Which teams outperform bookmaker expectations?
Identifies teams that consistently beat market predictions.

### 2. Which odds ranges produce the most upsets?
Finds where betting markets are least reliable.

### 3. Which teams are most reliable at home?
Measures home conversion rates vs bookmaker expectations.

### 4. Are bookmakers more accurate for home wins, draws, or away wins?
Evaluates prediction accuracy across outcome types.

### 5. Which teams create the most betting risk?
Builds a volatility index based on upset frequency.

---

## 📁 Dataset

- **Matches:** 378  
- **Season:** 2025/26 La Liga  
- **Columns:** 10  

### Features:
- `Div` → League division  
- `Date` → Match date  
- `HomeTeam` → Home team  
- `AwayTeam` → Away team  
- `FTHG` → Full-time home goals  
- `FTAG` → Full-time away goals  
- `FTR` → Full-time result (H/D/A)  
- `BMGMH` → Home win odds  
- `BMGMD` → Draw odds  
- `BMGMA` → Away win odds  

---

## 🧪 Methodology

### 1. Data Cleaning
- Removed missing values in odds columns
- Standardized team names and match results

### 2. Feature Engineering
- Implied probability from odds
- Favorite team identification
- Upset detection
- Odds range segmentation

### 3. Performance Analysis
- Expected vs actual outcomes
- Team-level over/underperformance
- Home advantage analysis

### 4. Risk Modeling
- Upset frequency by team
- Volatility score per club
- Odds range risk analysis

---

## 📊 Key Insights

### 🟢 Market Efficiency
- Bookmakers are highly accurate for **home wins (86%)**
- Away wins are moderately accurate (46%)

### 🔴 Market Weakness
- Draws are the least predictable outcome (0% accuracy in model)
- Mid-range odds (1.5–3.0) produce most upsets

---

## ⚽ Team Performance Insights

### 📈 Overperformers
- Barcelona
- Villarreal
- Getafe
- Real Madrid

### 📉 Underperformers
- Real Sociedad
- Athletic Club
- Girona
- Sevilla

### ⚠️ Most Volatile Teams
- Girona
- Celta
- Sevilla
- Rayo Vallecano

---

## 📊 Key Metrics

- Upset Rate by Odds Range
- Home Favorite Conversion Rate
- Team Overperformance Score
- Prediction Accuracy by Outcome Type
- Risk Index per Team

---

## 🛠️ Tools & Technologies

- Python 🐍
- Pandas
- NumPy
- Matplotlib / Seaborn
- Streamlit (dashboard development)
- Jupyter Notebook

---

## 📈 Visualizations

- Upset rate vs odds range
- Team performance ranking
- Home conversion rate leaderboard
- Prediction accuracy breakdown
- Risk heatmap of teams
<img width="1592" height="770" alt="image" src="https://github.com/user-attachments/assets/3112834a-f4a3-4ec2-a453-5ab423b19c3e" />


---

## 🚀 Key Takeaway

> Betting markets are highly efficient for strong favorites but struggle significantly in balanced matches — especially draws and mid-tier teams.

Football unpredictability is not random; it is structured around odds uncertainty.

---

## 📌 Recommendations

Based on the analysis, several strategic recommendations emerge for betting analysts, sportsbooks, and football analytics teams.

### 1. Improve Draw Prediction Models
Draw outcomes showed the weakest prediction accuracy in the dataset.

Recommendation:
- Build draw-specific predictive models
- Incorporate tactical and defensive metrics
- Use additional features such as:
  - xG difference
  - possession balance
  - recent defensive form

---

### 2. Increase Risk Weighting for Mid-Range Odds
Matches within odds ranges:
- 1.5–2.0
- 2.0–2.5
- 2.5–3.0

produced the highest upset rates.

Recommendation:
- Apply dynamic pricing adjustments
- Increase uncertainty margins for balanced fixtures
- Improve volatility estimation models

---

### 3. Treat High-Volatility Teams Differently
Teams such as:
- Girona
- Celta
- Sevilla
- Rayo Vallecano

generated frequent unexpected outcomes.

Recommendation:
- Assign higher volatility scores to inconsistent teams
- Reduce confidence in standard probability models for these clubs
- Use team-level risk profiling in betting simulations

---

### 4. Leverage Home Advantage More Aggressively
Elite home teams showed extremely high conversion rates.

Examples:
- Barcelona → 100%
- Real Madrid → 84%
- Villarreal → 88%

Recommendation:
- Prioritize home-performance features in predictive systems
- Incorporate stadium-specific advantage metrics

---

### 5. Develop Match Risk Classification Models
The analysis shows that football matches can be grouped into:
- low-risk predictable games
- medium-risk balanced games
- high-risk volatile fixtures

Recommendation:
- Build a match risk scoring engine
- Add confidence intervals to predictions
- Improve betting exposure management

---

## 🏁 Conclusion

This project analyzed bookmaker odds and match outcomes across the 2025/26 La Liga season to evaluate betting market efficiency and football unpredictability.

The findings reveal that:

- Bookmakers are highly accurate when pricing strong home favorites
- Mid-range fixtures produce the highest level of unpredictability
- Draws remain the most difficult outcome to model
- Team inconsistency is one of the biggest drivers of betting risk

The analysis also demonstrates that football betting markets are not completely random.

Instead, uncertainty follows identifiable patterns linked to:
- odds balance
- team consistency
- home advantage
- market confidence

By combining football performance analysis with probability modeling, this project provides a strong foundation for:
- sports analytics
- betting intelligence systems
- predictive modeling
- football business analytics

This project highlights how data can transform football from simple match analysis into a deeper study of risk, market behavior, and competitive performance.

## 💼 Project Value

This project demonstrates skills in:

- Sports analytics
- Probability modeling
- Data storytelling
- Betting market analysis
- Feature engineering
- Risk modeling

---

## 📌 Future Improvements

- Add machine learning model for match prediction
- Build interactive Streamlit dashboard
- Include xG (expected goals) data
- Add live betting simulation engine
- Extend analysis to multiple seasons

---

## 📬 Author

Built by a football analytics enthusiast using Python and real-world La Liga data.

---

## ⭐ If you like this project

Give it a star ⭐ and follow for more sports analytics projects.
