def display_invoince(username, amount, due_date):
    print(f"hello {username},")
    print(f"your bill of ${amount:.2f} is due by {due_date}.")


display_invoince("joe", 54.6, "03/15/2026")