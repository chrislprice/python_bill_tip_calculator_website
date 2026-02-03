from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Tip Calculator</title></head>
<body>
    <h2>💰 Tip Calculator</h2>
    <form method="POST">
        Enter Bill: $<input type="text" name="bill" required><br><br>
        Enter Tip %: <input type="text" name="percentage" required><br>
        <button type="submit">Calculate</button>
    </form>
    {% if total %}
        <h3>Total Bill (with tip): ${{ total }}</h3>
    {% endif %}
</body>
</html>
"""

def calculate_total(bill, percentage):
    return round(bill + (bill * (percentage / 100)), 2)

@app.route("/", methods=["GET", "POST"])
def home():
    total = None
    if request.method == "POST":
        bill = float(request.form.get("bill", 2))
        percentage = float(request.form.get("percentage", 2))
        total = calculate_total(bill, percentage)
    return render_template_string(HTML_TEMPLATE, total=total)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)