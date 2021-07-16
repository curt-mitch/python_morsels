def fancy_input(question, validator):
    complete = False
    while not complete:
        value = input(f"{question} ")
        try:
            validated_value = validator(value)
            complete = True
        except Exception:
            print("\nPlease enter a valid response.\n")
    return validated_value