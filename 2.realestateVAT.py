ap_value=int(input("Please add the value of the apartment:\n"))
if ap_value < 140000:
    value_5_percent= ap_value *1.05
    print(f"The VAT is 5% and the total value with VAT is {int(value_5_percent)}")
else:
    value_20_percent= ap_value * 1.20
    print(f"The VAT is 20% and the total value with VAT is {int(value_20_percent)}")
    