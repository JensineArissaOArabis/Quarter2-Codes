total_fee = 0

def compute_fee(distance, rate):
    fee = distance * rate
    return fee 
    
distance = float(input("Enter distance in kilometers: "))
rate = float(input("Enter rate per kilometer (₱): "))

def main():
    global total_fee  
    total_fee = compute_fee(distance, rate)
    print(f"\nTotal Delivery Fee: ₱{total_fee:.2f}")

main()