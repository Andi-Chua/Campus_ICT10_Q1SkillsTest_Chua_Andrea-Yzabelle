
@when("click", "#calculate")
def calculate_receipt(event):

    items = document.querySelectorAll(".item")

    subtotal = 0

    for item in items:
        if item.checked:
            subtotal += float(item.value)

    vat = subtotal * 0.12
    total = subtotal + vat

    document.querySelector("#subtotal").innerText = f"₱{subtotal:.2f}"
    document.querySelector("#vat").innerText = f"₱{vat:.2f}"
    document.querySelector("#total").innerText = f"₱{total:.2f}" 
