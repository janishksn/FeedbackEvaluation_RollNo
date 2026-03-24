import ezsheets

# Connect to sheet
ss = ezsheets.Spreadsheet('1mhjfHeewheJFl-nJwsJjDLib404XPxEENNeXXBaK-OE')
sheet = ss[0]

rows = sheet.getRows()

total_score = 0
count = 0

# weights
w_event = 0.30
w_org = 0.25
w_food = 0.20
w_overall = 0.25

for row in rows[1:]:  # skip header
    
    if row[1] == '':   # skip empty rows
        continue
    
    # convert values to float
    event = float(row[1])
    org = float(row[2])
    food = float(row[3])
    overall = float(row[4])
    
    # weighted score
    score = (event * w_event +
             org * w_org +
             food * w_food +
             overall * w_overall)
    
    total_score += score
    count += 1

# final result
if count > 0:
    final_score = total_score / count
    final_score = round(final_score, 2)
    
    print("\nFinal Performance Score:", final_score)
    
    if final_score >= 4:
        print("Performance: EXCELLENT 🌟")
    elif final_score >= 3:
        print("Performance: GOOD ✅")
    elif final_score >= 2:
        print("Performance: AVERAGE ⚠️")
    else:
        print("Performance: POOR ❌")
else:
    print("No valid data")

# Save result to file
with open("result.txt", "w") as f:
    f.write(f"Final Score: {final_score}\n")
    
    if final_score >= 4:
        f.write("Performance: EXCELLENT")
    elif final_score >= 3:
        f.write("Performance: GOOD")
    elif final_score >= 2:
        f.write("Performance: AVERAGE")
    else:
        f.write("Performance: POOR")