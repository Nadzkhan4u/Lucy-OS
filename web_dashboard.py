from flask import Flask, render_template_string
import json
import os

app = Flask(__name__)

DATA_DIR = "data"

def read_json(file, default):
    path = os.path.join(DATA_DIR, file)
    if not os.path.exists(path):
        return default
    with open(path, "r") as f:
        return json.load(f)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Lucy OS — Read-Only Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 30px; background: #f7f7f7; }
        h1, h2 { color: #222; }
        .card { background: #fff; padding: 20px; margin-bottom: 20px;
                border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.08); }
        .done { color: green; font-weight: bold; }
        .planned { color: #444; }
        .stalled { color: red; font-weight: bold; }
        ul { padding-left: 20px; }
    </style>
</head>
<body>

<h1>Lucy OS — Read-Only Dashboard</h1>

<div class="card">
<h2>Today — Plan & Execution</h2>
{% if plan.tasks %}
    <ul>
    {% for t in plan.tasks %}
        <li class="{{ t.status }}">
            [{{ t.status|upper }}] {{ t.time_block }} — {{ t.title }}
        </li>
    {% endfor %}
    </ul>
{% else %}
    <p>No active plan.</p>
{% endif %}
</div>

<div class="card">
<h2>Revenue Focus</h2>
<p><strong>Hot Leads</strong></p>
<ul>
{% for l in leads if l.category == "hot" %}
    <li class="stalled" if "stalled" in l.flags else "">
        {{ l.client_name }} ({{ l.flags }})
    </li>
{% endfor %}
</ul>

<p><strong>Warm Leads</strong></p>
<ul>
{% for l in leads if l.category == "warm" %}
    <li>{{ l.client_name }}</li>
{% endfor %}
</ul>
</div>

<div class="card">
<h2>Escalations</h2>
<ul>
{% set found = false %}
{% for l in leads %}
    {% for f in l.flags %}
        {% set found = true %}
        <li>{{ f|upper }} — {{ l.client_name }}</li>
    {% endfor %}
{% endfor %}
{% if not found %}
    <p>No active escalations.</p>
{% endif %}
</ul>
</div>

<div class="card">
<h2>Weekly Overview</h2>
{% if weekly.week_start %}
<p><strong>Week:</strong> {{ weekly.week_start }} → {{ weekly.week_end }}</p>

<p><strong>Top Goals</strong></p>
<ul>
{% for g in weekly.top_5_goals %}
    <li>{{ g }}</li>
{% endfor %}
</ul>

<p><strong>Rollover Tasks</strong></p>
<ul>
{% for r in weekly.rollover_tasks %}
    <li>{{ r }}</li>
{% endfor %}
</ul>
{% else %}
<p>No weekly plan available.</p>
{% endif %}
</div>

<div class="card">
<h2>Monthly Signals</h2>
<ul>
{% for l in leads if "stalled" in l.flags %}
    <li class="stalled">STALLED — {{ l.client_name }}</li>
{% endfor %}
{% if leads|length == 0 %}
    <li>No signals.</li>
{% endif %}
</ul>
</div>

</body>
</html>
"""

@app.route("/")
def dashboard():
    plan = read_json("plan.json", {})
    leads = read_json("leads.json", [])
    weekly = read_json("weekly_plan.json", {})

    return render_template_string(
        HTML_TEMPLATE,
        plan=plan,
        leads=leads,
        weekly=weekly
    )

if __name__ == "__main__":
    app.run(debug=False)
