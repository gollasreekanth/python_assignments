score = 0
count = 0

def lvl_hrd():
    return 30

def lvl_mdm():
    return 20

def lvl_easy():
    return 10

print("Welcome to the Quiz")

Q1 = "The World Largest desert is?"
choice = "A. Thar B. Kalahari C. Sahara D. Sonoran"
print(Q1)
print(choice)
print("Enter your choice")
user_choice = input().lower()
if user_choice == 'c':
    print("Your Correct..")
    count += 1
    score += lvl_easy()
else:
    print("Your Wrong")

Q2 = "Which one of the following river flows between Vindhyan and Satpura ranges?"
choice = "A. Narmada B. Mahanadi C. Son D. Netravati"
print(Q2)
print(choice)
print("Enter your choice")
user_choice = input().lower()
if user_choice == 'a':
    print("Your Correct..")
    count += 1
    score += lvl_easy()
else:
    print("Your Wrong")

Q3 = "The Central Rice Research Station is situated in?"
choice = "A. Chennai B. Cuttack C. Mumbai D. Delhi"
print(Q3)
print(choice)
print("Enter your choice")
user_choice = input().lower()
if user_choice == 'b':
    print("Your Correct..")
    count += 1
    score += lvl_easy()
else:
    print("Your Wrong")

Q4 = "Who among the following wrote Sanskrit grammar?"
choice = "A. Kalidasa B. Charak C. Panini D. Aryabhatt"
print(Q4)
print(choice)
print("Enter your choice")
user_choice = input().lower()
if user_choice == 'c':
    print("Your Correct..")
    count += 1
    score += lvl_mdm()
else:
    print("Your Wrong")

Q5 = "Which among the following headstreams meets the Ganges in last?"
choice = "A. Alaknanda B. Pindar C. Mandakini D. Bhagirathi"
print(Q5)
print(choice)
print("Enter your choice")
user_choice = input().lower()
if user_choice == 'd':
    print("Your Correct..")
    count += 1
    score += lvl_mdm()
else:
    print("Your Wrong")

Q6 = "Patanjali is well known for the compilation of _"
choice = "A. Yoga Sutra B. Panchatantra C. Brahma Sutra D. Ayurveda"
print(Q6)
print(choice)
print("Enter your choice")
user_choice = input().lower()
if user_choice == 'a':
    print("Your Correct..")
    count += 1
    score += lvl_mdm()
else:
    print("Your Wrong")

Q7 = "River Luni originates near Pushkar and drains into which one of the following?"
choice = "A. Rann of Kachchh B. Arabian Sea C. Gulf of Cambay D. Lake Sambhar"
print(Q7)
print(choice)
print("Enter your choice")
user_choice = input().lower()
if user_choice == 'a':
    print("Your Correct..")
    count += 1
    score += lvl_hrd()
else:
    print("Your Wrong")

Q8 = "Which one of the following rivers originates in Brahmagiri range of Western Ghats?"
choice = "A. Pennar B. Cauvery C. Krishna D. Tapti"
print(Q8)
print(choice)
print("Enter your choice")
user_choice = input().lower()
if user_choice == 'b':
    print("Your Correct..")
    count += 1
    score += lvl_hrd()
else:
    print("Your Wrong")

Q9 = "The country that has the highest in Barley Production?"
choice = "A. China B. India C. Russia D. France"
print(Q9)
print(choice)
print("Enter your choice")
user_choice = input().lower()
if user_choice == 'c':
    print("Your Correct..")
    count += 1
    score += lvl_hrd()
else:
    print("Your Wrong")

def marks():
    return score

total_score = marks()

print(f"You Answered {count} Questions")
print(f"You got {total_score} out of 180.")
