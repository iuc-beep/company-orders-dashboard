# Company Orders Dashboard — GitHub Pages

This dashboard is a static website. It reads `data.csv`, automatically identifies the latest two dates in the dataset, and shows:
- Total orders for the month containing the latest date
- Total orders for the previous month
- Orders on the latest date
- Orders on the previous date
- Company-wise breakdown
- Search and sorting
- Month-over-month change

## data.csv format

Keep these three columns:

```csv
date,COMPANY_NAME,orders
2026-08-31,ABC 1,120
2026-08-31,ABC 2,85
2026-08-30,ABC 1,110
```

`orders` is the number of orders for that company on that date.

## Update process

1. Prepare the latest `data.csv`.
2. Replace the old `data.csv` in GitHub.
3. Commit the change.
4. GitHub Pages redeploys the site automatically.
5. The dashboard will automatically pick the latest two dates — no date-column editing is required.

## Important

The included September data is DEMO/SYNTHETIC data created only to demonstrate the September view. Replace it with your actual September counts before sharing the dashboard.

## GitHub Pages setup

1. Create a GitHub repository, for example `company-orders-dashboard`.
2. Upload `index.html` and `data.csv`.
3. Open the repository's Settings → Pages.
4. Under Build and deployment, choose `Deploy from a branch`.
5. Select `main` and `/(root)`, then Save.
6. GitHub will publish the site at a URL similar to:
   `https://YOUR-USERNAME.github.io/company-orders-dashboard/`

GitHub Pages is a static public website. Do not upload sensitive order-level/customer data to a public repository. This dashboard intentionally uses aggregated company/date counts rather than order IDs.
