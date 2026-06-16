# CALL_PRICE = 0.10
# MESSAGE_PRICE = 0.05
# MB_PRICE = 0.07

# used_calls = 450
# used_messages = 130
# used_mb = 600

# total_call_cost = used_calls * CALL_PRICE
# total_message_cost = used_messages * MESSAGE_PRICE
# total_mb_cost = used_mb * MB_PRICE

# # Toplam Aylık Maliyet
# monthly_cost = total_call_cost + total_message_cost + total_mb_cost

# print("***** TMCELL *****")
# print(f"1 call - {CALL_PRICE:.2f} manat")
# print(f"1 message - {MESSAGE_PRICE:.2f} manat")
# print(f"1 Mb - {MB_PRICE:.2f} manat")
# print("- " * 15)

# print(f"Used call by month: {used_calls}")
# print(f"Used message by month: {used_messages}")
# print(f"Used Mb by month: {used_mb}")
# print("- " * 15)

# print(f"{used_calls} call is {int(total_call_cost)} manats")
# print(f"{used_messages} message is {int(total_message_cost)} manats")
# print(f"{used_mb} Mb is {int(total_mb_cost)} manats")
# print("- " * 15)

# print(f"Monthly cost: {int(monthly_cost)} manats")


CALL_PRICE = 0.10
MESSAGE_PRICE = 0.05
MB_PRICE = 0.07

used_calls = int(input("Aylyk gurlesyk wagtyny girizin (call): "))
used_messages = int(input("Aylyk sms sanyny girizin (message): "))
used_mb = int(input("Aylyk internet mocberini girizin (Mb): "))

total_call_cost = used_calls * CALL_PRICE
total_message_cost = used_messages * MESSAGE_PRICE
total_mb_cost = used_mb * MB_PRICE

monthly_cost = total_call_cost + total_message_cost + total_mb_cost

print("\n" + "="*30)
print("***** TMCELL *****")
print(f"1 call - {CALL_PRICE:.2f} manat")
print(f"1 message - {MESSAGE_PRICE:.2f} manat")
print(f"1 Mb - {MB_PRICE:.2f} manat")
print("- " * 15)

print(f"Used call by month: {used_calls}")
print(f"Used message by month: {used_messages}")
print(f"Used Mb by month: {used_mb}")
print("- " * 15)

print(f"Total call is {int(total_call_cost)} manats")
print(f"Total message is {int(total_message_cost)} manats")
print(f"Total Mb is {int(total_mb_cost)} manats")
print("- " * 15)

print(f"Monthly cost: {int(monthly_cost)} manats")
print("="*30)