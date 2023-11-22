def age_output(age):
    if age < 0:
        raise ValueError("Сan't be")
    if age % 2 == 0:
        return "Even"
    if age % 2 == 1:
        return "Odd"

def main():
    try:
        age = int(input("How old are you?\n-> "))
        output = age_output(age)
        print(f"Your age : {output}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
