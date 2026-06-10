#example 1
ticket=list(map(str,input().split()))
text=''
if 'urgent' in ticket:
    print("Priority: P1 — Immediate Escalation")
elif 'slow' in ticket:
    print("Priority: P2 — Standard Queue")
else:
    print("Priority: P3 — General Request")

#example 2
name = input().lower().split()
print(name[0] + "." + name[-1] + "@company.com")

#example 3
line = input()
ts = line.split(']')[0][1:]
level = line.split(']')[1].split(':')[0].strip()
print("Timestamp:", ts, "| Level:", level, "| Route: On-Call Alert")

#example 4
sku = input()
if len(sku) != 12:
    print(f"Invalid - Length is {len(sku)}, expected 12")
elif not sku.startswith("SKU-"):
    print("Invalid - Must start with 'SKU-'")
elif not sku[-1].isdigit():
    print("Invalid - Must end with digit")
else:
    print("Valid SKU")

#example 5
name = input()
clean_name = " ".join(name.strip().split()).title()
print(repr(clean_name))

#example 6
msg=input()
print(next(word for word in msg.split() if word.isdigit() and len(word)==6))

#example 7
import re; s=input().lower().strip().replace(' ','-')
print(re.sub(r'[^a-z0-9-]', '', s).strip('-'))

#example 10
text = input().lower()
keywords = eval(input())
for k in keywords:
    c = text.count(k.lower())
    print(k, ":", c, "|", "Missing" if c == 0 else "Present")

#example 11
msg = input()
banned = eval(input())
words = msg.split()
for i in range(len(words)):
    for b in banned:
        if words[i].lower() == b.lower():
            words[i] = '*' * len(words[i])
print(' '.join(words))

#example 12
first = input()
last = input()
phone = input()
pnr = first[:2].upper() + last[:2].upper() + phone[-2:]
print("PNR:", pnr)

#example 13
text = input()
start = text.upper().find("SKILLS:")
sub = text[start+7:]
end = len(sub)
for i in range(len(sub)):
    if sub[i:].startswith(tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")) and ":" in sub[i:]:
        end = i
        break
print(sub[:end].strip())

#example 14
num=list(map(str,input().split()))
for i in num:
    if i.isalnum():
        print(i)
        print("valid IFSC code")
    else:
        print("Invalid IFSC code")

#exaample 15
d={'name':'Ravi','product':'Laptop','discount':15}
print(f"Template: 'Hi {d['name']}, your {d['product']} order has a {d['discount']}% discount!'")