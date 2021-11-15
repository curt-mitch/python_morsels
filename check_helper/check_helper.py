import sys

def dollar_format():
    value = float(sys.argv[1])
    formatted_value = f"${value:,.2f}"

    return formatted_value

print(dollar_format())