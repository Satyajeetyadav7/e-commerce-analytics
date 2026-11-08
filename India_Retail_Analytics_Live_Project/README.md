# India Retail & E-Commerce Business Analytics

**End-to-end Data Analyst / BI portfolio project:** Excel + SQL + Power BI + Python.

### Why this project
2026 hiring analyses continue to show strong demand for SQL, Excel, Power BI and Python, and current portfolio guidance favours projects that answer a business question, show the analysis workflow and finish with recommendations. This project is designed around that workflow.

### Business questions
- Which categories, regions and channels drive revenue and profit?
- Does late delivery relate to ratings and returns?
- Which discount levels create margin leakage?
- Which areas need operational attention?

### Dataset
50,000 **synthetic** order records covering Jan 2025–Oct 2026, with Indian states/cities, categories, channels, sales, cost, profit, discounts, delivery SLA, ratings and returns. It is explicitly synthetic and should not be presented as confidential company data.

### Included
- `excel/India_Retail_Analytics.xlsx` — executive Excel dashboard + data + findings
- `powerbi/` — model, DAX measures and theme
- `sql/analysis_queries.sql` — business SQL analysis
- `app/app.py` — rerunnable Streamlit dashboard
- `src/generate_data.py` — regenerates data
- `docs/dashboard_preview.png` — preview
- `docs/resume_bullets.txt` — resume-ready wording

### Run the live dashboard again
```bash
pip install -r app/requirements.txt
streamlit run app/app.py
```
To regenerate the data:
```bash
python src/generate_data.py
streamlit run app/app.py
```

### Power BI
Open Power BI Desktop → Get Data → Text/CSV → `data/orders.csv`, then load customers/products, create the Date table and relationships in `powerbi/POWER_BI_MODEL.md`, and add measures from `powerbi/DAX_Measures.txt`. Save your finished report as `.pbix` and publish if your Power BI account supports publishing.

### Resume project title
**India Retail & E-Commerce Business Analytics Dashboard | Excel, SQL, Power BI, Python**

### Resume bullets
- Analysed **50,000+ order records** across Indian regions, categories and sales channels to identify revenue, profitability and customer-experience drivers.
- Built an **Excel executive dashboard** with KPI reporting, monthly trends, category profitability, AOV, return rate and delivery performance.
- Developed a **Power BI-ready star schema and DAX KPI layer** for sales, profit margin, MoM growth, returns and delivery performance.
- Used SQL **CTEs, CASE expressions, aggregations and window functions** for regional ranking, discount-band analysis and month-over-month performance.
- Built a **rerunnable Streamlit dashboard** so updated CSV data can refresh the analysis rather than leaving it as a static project.

### Interview story
Situation → fragmented sales/operations reporting. Task → create a repeatable decision dashboard. Action → cleaned/modelled 50K records, analysed KPIs in Excel/SQL, built DAX measures and a rerunnable dashboard. Result → one reporting layer covering sales, profit, AOV, delivery SLA, returns and ratings.
