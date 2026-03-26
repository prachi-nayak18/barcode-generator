from utils import generate_code128, generate_ean13

def main():
    print("Barcode Generator Tool ")
    print("1. Generate EAN-13 Barcode (12 digits only)")
    print("2. Generate Code128 Barcode (Any text)")
    
    choice = input("Enter choice (1/2): ")

    if choice == "1":
        data = input("Enter 12-digit number: ")
        filename = input("Enter file name: ")
        
        try:
            path = generate_ean13(data, filename)
            print(f" Barcode saved at: {path}.png")
        except Exception as e:
            print(f" Error: {e}")

    elif choice == "2":
        data = input("Enter text/data: ")
        filename = input("Enter file name: ")

        try:
            path = generate_code128(data, filename)
            print(f"Barcode saved at: {path}.png")
        except Exception as e:
            print(f" Error: {e}")

    else:
        print(" Invalid choice")

if __name__ == "__main__":
    main()