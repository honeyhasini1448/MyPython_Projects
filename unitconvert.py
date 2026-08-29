# unitconverter.py
# A simple unit converter program

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def kilometers_to_miles(km):
    return km * 0.621371

def kilograms_to_pounds(kg):
    return kg * 2.20462

def megabytes_to_gigabytes(mb):
    return mb / 1024

def main():
    print("==== Unit Conversion Tool ====")
    print("Select a conversion category:")
    print("1. Temperature (Celsius to Fahrenheit)")
    print("2. Length (Kilometers to Miles)")
    print("3. Weight (Kilograms to Pounds)")
    print("4. Data Storage (Megabytes to Gigabytes)")

    choice = input("\nEnter your choice (1-4): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C = {result:.2f}°F")

    elif choice == '2':
        km = float(input("Enter distance in Kilometers: "))
        result = kilometers_to_miles(km)
        print(f"{km} km = {result:.2f} miles")

    elif choice == '3':
        kg = float(input("Enter weight in Kilograms: "))
        result = kilograms_to_pounds(kg)
        print(f"{kg} kg = {result:.2f} pounds")

    elif choice == '4':
        mb = float(input("Enter data size in Megabytes: "))
        result = megabytes_to_gigabytes(mb)
        print(f"{mb} MB = {result:.4f} GB")

    else:
        print("Invalid choice! Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
