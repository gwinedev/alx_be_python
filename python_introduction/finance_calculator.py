income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your monthly expenses: "))

m_savings = income - expenses
y_savings = m_savings * 12 + (m_savings * 12 * 0.05)

print(f'Your monthly savings are ${m_savings}')
print(f'Projected savings after one year, with interest, is: ${y_savings}')
