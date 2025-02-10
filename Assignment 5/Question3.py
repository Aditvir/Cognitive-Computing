import numpy as np

name_initials = 'AR'  # Given initials
ascii_sum = sum(ord(char) for char in name_initials)
revenue = np.array([ascii_sum, ascii_sum + 50, ascii_sum + 100, ascii_sum + 150, ascii_sum + 200])

vat_rate = ((ascii_sum % 5) + 5) / 100
revenue_with_vat = revenue * (1 + vat_rate)

adjusted_revenue = np.where(revenue < ascii_sum + 100, revenue_with_vat * 0.95, revenue_with_vat * 0.90)

monthly_revenue = np.tile(adjusted_revenue, (3, 1))  
monthly_revenue *= (1 + 0.02 * np.arange(3)[:, None])

print("Monthly Revenue Data:\n", monthly_revenue)