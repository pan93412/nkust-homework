from flask import Flask, request, render_template

app = Flask(__name__)


class PrimeFinder:
    max: int = 0
    table: list[bool] = []

    def __init__(self, max=2 ** 24):
        # create a table from 1 to n
        table = [True] * (max + 1)

        # 0 and 1 are not prime
        table[0] = table[1] = False

        # iterate through the table
        for i in range(2, max + 1):
            # if i is prime, mark all multiples of i as not prime
            if table[i]:
                for j in range(i * i, max + 1, i):
                    table[j] = False

        self.table = table

    def is_prime(self, n: int) -> bool:
        # if n is greater than max, generate a new table
        if n >= self.max:
            self.__init__(n + 1)

        return self.table[n]


prime_finder = PrimeFinder()


@app.route("/prime/<int:n>")
def is_prime(n: int):
    return {"result": prime_finder.is_prime(n)}


def calculate_bmi(weight: int, height: int) -> tuple[str, float]:
    table = {
        "underweight": (0, 18.5),
        "normal": (18.5, 25),
        "overweight": (25, 30),
        "obese": (30, float("inf")),
    }

    # weight in kg, height in cm
    height /= 100

    for category, (lower, upper) in table.items():
        if lower <= weight / (height ** 2) < upper:
            v = weight / (height ** 2)
            return category, round(v)

    return "error", 0


@app.route("/bmi/<int:height>/<int:weight>")
def bmi_route(weight: int, height: int):
    category, bmi = calculate_bmi(weight, height)
    return {"category": category, "bmi": bmi}


@app.route("/bmi")
def bmi_page():
    return render_template("form.html")


@app.route("/bmi", methods=["POST"])
def bmi_post():
    weight = int(request.form.get("weight"))
    height = int(request.form.get("height"))

    category, bmi = calculate_bmi(weight, height)
    return "Your BMI is {} and you are {}".format(bmi, category)


if __name__ == "__main__":
    app.run(debug=True)
