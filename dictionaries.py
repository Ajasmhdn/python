# phone_no={
#     "Ajas": 1234567890,
#     "Arun": 9876543210,
#     "Akhil": 1234567890,
#     "Ajas":8921747219
# }
# phone_no=dict({
# "Ajas":56789,
# "Bheem":456789
# })

phone_no=dict([("Ajas",456789),("Bheem",456789)])
print(phone_no["Ajas"])
phone_no["Ajas"]=1234567890
print(phone_no["Ajas"])