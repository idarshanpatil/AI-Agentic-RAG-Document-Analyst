def calculator(expression):
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception:
        return "Invalid calculation."


if __name__ == "__main__":

    print(calculator("25 * 40"))
    print(calculator("100 / 5"))