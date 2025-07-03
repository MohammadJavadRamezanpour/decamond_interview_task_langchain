def input_node(data):
    return data

def processing_node(data):
    today = data['today']
    yesterday = data['yesterday']

    revenue_today = today['revenue']
    cost_today = today['cost']
    customers_today = today['customers']

    revenue_yesterday = yesterday['revenue']
    cost_yesterday = yesterday['cost']
    customers_yesterday = yesterday['customers']

    profit = revenue_today - cost_today
    cac_today = cost_today / customers_today if customers_today else 0
    cac_yesterday = cost_yesterday / customers_yesterday if customers_yesterday else 0

    revenue_change_pct = ((revenue_today - revenue_yesterday) / revenue_yesterday) * 100 if revenue_yesterday else 0
    cost_change_pct = ((cost_today - cost_yesterday) / cost_yesterday) * 100 if cost_yesterday else 0
    cac_change_pct = ((cac_today - cac_yesterday) / cac_yesterday) * 100 if cac_yesterday else 0

    return {
        "profit": profit,
        "cac_today": cac_today,
        "cac_change_pct": cac_change_pct,
        "revenue_change_pct": revenue_change_pct,
        "cost_change_pct": cost_change_pct
    }

def recommendation_node(metrics):
    recommendations = []
    alerts = []

    if metrics['profit'] < 0:
        recommendations.append("Reduce costs or improve sales to avoid losses.")

    if metrics['cac_change_pct'] > 20:
        alerts.append("CAC increased significantly.")
        recommendations.append("Review marketing campaigns to optimize CAC.")

    if metrics['revenue_change_pct'] > 10:
        recommendations.append("Consider increasing ad spend; sales are growing.")

    return {
        "status": "Profit" if metrics['profit'] >= 0 else "Loss",
        "alerts": alerts,
        "recommendations": recommendations
    }