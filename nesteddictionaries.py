phone_no={
    "Ajas":2345678,
    "Bheem":3456789
}
print(phone_no)
print()
phone_no["Madhav"]={12345678,9876543}
print(phone_no)
print()
phone_no["Ajas"]={"Home":1234567890,"Office":9876543210}
print(phone_no.get("Ajas"))
del phone_no["Bheem"]
print(phone_no)
phone_no.pop("Madhav")
print(phone_no)
phone_no["Airen"]=23456789
print(phone_no)
print(phone_no.popitem())
print(phone_no)
# phone_no.clear()
print(phone_no.keys())
print(phone_no.values())
print(phone_no.items())
phone_no2=phone_no.copy()
print(phone_no2)
print(len(phone_no2))