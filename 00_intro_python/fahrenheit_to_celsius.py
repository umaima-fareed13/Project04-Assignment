def main():
    Temperature : float = float(input("Enter temperature in Fahrenheit:"))
    degrees_celsius = (Temperature - 32) * 5.0/9.0
    print(f"{Temperature}°F = {degrees_celsius:.2f}°C")


if __name__ == '__main__':
    main()