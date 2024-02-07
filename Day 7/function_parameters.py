
def display_invoice(username, amount, due_date):
    print(f"Hellow {username}!")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Matthew", 42.50, "01/09/2025")

