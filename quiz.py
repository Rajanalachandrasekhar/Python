A=[{"question":"what is smallest prime number?",
    "options":["A.2","B.3","C.1","D.7"],
    "answer":"A"},
   {"question":"who is the CSK captain?",
    "options":["A.MSD","B.RUTHU RAJ","C.JADDU","D.RAINA"],
    "answer":"B"},
   {"question":"highest centuries in ODI?",
    "options":["A.VIRAT","B.DHONI","C.SACHIN","D.ROHIT"],
    "answer":"A"},
   {"question":"highest centuries in CRICKET?",
    "options":["A.VIRAT","B.DHONI","C.SACHIN","D.ROHIT"],
    "answer":"C"},
   {"question":"HTML H stands for?",
    "options":["A.HYPER","B.HYDRA","C.HERO","D.HIGH"],
    "answer":"A"},
   {"question":"CSS 1st.S stands for?",
    "options":["A.STYLE","B.STNAD","C.SHEET","D.SOFT"],
    "answer":"A"},
   {"question":"which country won highest world cups?",
    "options":["A.AUS","B.IND","C.SA","D.SL"],
    "answer":"A"},
   {"question":"what is smallest whole number?",
    "options":["A.2","B.0","C.1","D.7"],
    "answer":"B"},
   {"question":"what is smallest natural number?",
    "options":["A.2","B.3","C.1","D.7"],
    "answer":"C"}]
name=input("enter your good name please:")
score=0
for i in A:
    print(i["question"])
    for j in i["options"]:
        print(j)
    s=input("enter the option:").upper()
    if(s==i["answer"]):
        print("correct answer",name)
        score+=1
    else:
        print("wrong answer",name)
        print("correct answer is",i["answer"])
print("your score is:",score,"out of 9")
