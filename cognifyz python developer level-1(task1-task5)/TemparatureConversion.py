def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Conversion")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        celsius = float(input("Enter the temperature in Celsius: "))
        converted_temperature = celsius_to_fahrenheit(celsius)
        print(f"The temperature {celsius} Celsius is {converted_temperature:.2f} Fahrenheit.")
    elif choice == 2:
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        converted_temperature = fahrenheit_to_celsius(fahrenheit)
        print(f"The temperature {fahrenheit} Fahrenheit is {converted_temperature:.2f} Celsius.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
