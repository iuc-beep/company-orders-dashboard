# Company Orders Dashboard — GitHub Pages

This dashboard is designed for daily order reporting.

## What updates automatically

- The table always uses the two latest dates available in `data.csv`.
- The date headers change automatically (for example: `31 Aug 2026` and `30 Aug 2026`).
- Current-month and previous-month totals are recalculated from the latest date in the dataset.
- Company-wise order counts are recalculated whenever `data.csv` changes.

## How to update the dashboard

1. Prepare your latest order dump with at least these columns:
   - `date`
   - `COMPANY_NAME`
   - `orders`
2. Update `data.csv` in this GitHub repository.
3. Commit the change.
4. Wait a short time for GitHub Pages to redeploy.
5. Open the same GitHub Pages URL. The dashboard will show the updated data.

### Important

For a public GitHub repository, do not upload buyer names, phone numbers, addresses, order IDs, payment information, or other sensitive/raw order-level data. Keep `data.csv` aggregated to company + date + order count.

## GitHub Pages

Keep `index.html` and `data.csv` in the root of the repository and publish the `main` branch from `/root`.
