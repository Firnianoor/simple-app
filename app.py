from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    persentase = None
    if request.method == "POST":
        try:
            hadir = int(request.form["hadir"])
            total = int(request.form["total"])

            if total == 0:
                return "total pertemuan tidak boleh 0"
            
            persentase = (hadir / total) * 100

        except ValueError:
            return "input tidak valid! masukkan angka yang benar."
        
    return render_template("kehadiran.html", persentase=round(persentase, 2) if persentase is not None else None)

if __name__ == "__main__":
    app.run(debug=True)