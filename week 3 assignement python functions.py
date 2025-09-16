def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price-discount_amount
        return final_price
    else:
        return price
    
    def main():
        try:
            original_price = float(input("Enter the originalprice of the item: $"))
            discount_percentage = float(input("Enter the discount percentage: "))

            final_price = calculate_discount(original_price, discount_percentage)
            if discount_percentage >= 20:
                print(f"\nOriginal Price: ${original_price:.2f}")
                print(f"Discount Applied: {discount_percentage}%")
                print(f"Discount Amount: ${(original_price * discount_percentage / 100):.2f}")
                print(f"Final Price after discount: ${final_Price:.2f}")
            else:
                print(f"\nNo discount applied (require 20% or higher)")
                print(f"Final Price: ${final_price:.2f}")
        except ValueError:
            print("Error: Please enter valid Numbers for specific and discount percentage.")
            if __name__ == "__main__":
                    main()
