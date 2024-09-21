from flask import Flask, render_template, request
from queries import get_disease_information, get_top_five_drugs, get_symptom_percentages, get_substitute_drugs
from queries import get_drug_information, get_drug_reviews

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    desc = None
    if request.method == "POST":
        disease = request.form["disease"]
        print("Requested Disease =", disease)

        # IANS QUERIES
        # desc = get_disease_information(disease)
        # desc = get_top_five_drugs(disease)
        # desc = get_symptom_percentages(disease)
        # desc = get_substitute_drugs(disease)

        # SHAURYAS QUERIES
        # desc = get_drug_information(disease)
        desc = get_drug_reviews(disease)
    return render_template("home.html.j2", desc=desc)

app.run(host="0.0.0.0", port=3000, debug=True)