import time
A = 0
B = 0
C = 0
D = 0
E = 0
time.sleep(1)
print("Welcome to Love Language Test")
time.sleep(2)
print("What is your love language?")
time.sleep(2)
print("Take this quiz to discover your primary love language")
time.sleep(2)
print("for each question, you can choose between 1 or 2 and type the number that describe you well.")
time.sleep(2)
print("Let's start!")
time.sleep(2)
print("""
question1""")
question1 = input("""I like to receive note of appreciation. = 1
I like to be hugged = 2""")
if question1 == "1":
    A += 1
else:
    E += 1
print("""
question2""")
question2 = input("""I like to spend one-on-one time with people who are special to me. = 1
I feel appreciated when someone gives me practical help. = 2""")
if question2 == "1":
    B += 1
else:
    D += 1
print("""
question3""")
question3 = input("""I like it when I unexpectedly receive gifts from people = 1
I like leisurely meet up with friends and loved ones. = 2""")
if question3 == "1":
    C += 1
else:
    B += 1
print("""
question4""")
question4 = input("""I feel appreciated when people do things to help me. = 1
I enjoy receiving a pat on the back. = 2""")
if question4 == "1":
    D += 1
else:
    E += 1
print("""
question5""")
question5 = input("""I feel appreciated when someone I care about puts his or her arm around me. = 1
I feel appreciated when I receive a gift from someone. = 2""")
if question5 == '1':
    E +=1
else:
    C +=1
print("""
question6""")
question6 = input("""I like to go various places with friends and loved ones. = 1
I like to high-five or hold hands with people who are special to me. = 2 """)
if question6 == '1':
    B += 1
else:
    E += 1
print("""
question7""")
question7 = input(""" Visible symbols of appreciation (gifts) are important to me. = 1
I feel appreciated when people affirm me. = 2""")
if question7 == '1':
    C += 1
else:
    A += 1
print("""
question8""")
question8 = input("""I like to sit close to people I enjoy being around. = 1
I like for people to tell me I look good. = 2""")
if question8 == '1':
    E += 1
else:
    A += 1
print("""
question9""")
question9 = input("""I like to spend time with my friends and loved ones. = 1
I like to receive little gifts from my friends and loved ones. = 2""")
if question9 == '1':
    B += 1
else:
    C += 1
print("""
question10""")
question10 = input(""" Words of acceptance are important to me. = 1
I know someone appreciates me when they help me with task. = 2""")
if question10 == '1':
    A += 1
else:
    D += 1
print("""
question11""")
question11 = input("""I like working on tasks with my friends and loved ones. = 1
I like it when kind words are spoken to me. = 2""")
if question11 == '1':
    B += 1
else:
    A += 1
print("""
question12""")
question12 = input("""What someone DOES affects me more than what she/he SAYS. = 1
Hugs make me feel connected and valued = 2""")
if question12 == '1':
    D += 1
else:
    E += 1
print("""
question13""")
question13 = input(""" I value praise and try to avoid criticism. = 1
Several small gifts mean more to me than one large gifts. = 2""")
if question13 == '1':
    A += 1
else:
    C += 1
print("""
question14""")
question14 = input("""I feel close to someone when we are talking or doing something together. = 1
I feel closer to my friends or loved ones when they stand closer to me when they address me. = 2""")
if question14 == '1':
    B += 1
else:
    E += 1
print("""
question15""")
question15 = input("""I like for people to compliment my achievements. = 1
I know people love me when they do things for me that they don't enjoy. = 2""")
if question15 == '1':
    A += 1
else:
    D += 1
print("""
question16""")
question16 = input("""I like for my loved one to touch my shoulder as she/he passes by me. = 1
I like it when people listen to me and show genuine interest in what I say. = 2""")
if question16 == '1':
    E += 1
else:
    B += 1
print("""
question17""")
question17 = input("""I feel loved when my loved ones or my friends help me with jobs or projects. = 1
I really enjoy receiving gifts from friends or loved ones.  = 2""")
if question17 == '1':
    D += 1
else:
    C += 1
print("""
question18""")
question18 = input("""I like for people to compliment my appearance. = 1
I feel loved when people take time to understand my feelings. = 2""")
if question18 == '1':
    A += 1
else:
    B += 1
print("""
question19""")
question19 = input("""I feel appreciated when my friends give me a high-five when I do well. = 1
Act of service make me feel loved. = 2""")
if question19 == '1':
    E += 1
else:
    D += 1
print("""
question20""")
question20 = input("""I appreciate the many things that special people do for me. = 1
I like receiving gifts that people give especially for me. = 2""")
if question20 == '1':
    D += 1
else:
    C += 1
print("""
question21""")
question21 = input("""I really enjoy the feeling I get when someone gives me undivided attention. = 1
I really enjoy the feeling I get when someone helps me with a task. = 2""")
if question21 == '1':
    B += 1
else:
    D += 1
print("""
question22""")
question22 = input("""I feel loved when a person celebrates my birthday with a special gift. = 1
I feel loved when a person celebrates my birthday with meaningful words. = 2""")
if question22 == '1':
    C += 1
else:
    A += 1
print("""
question23""")
question23 = input("""I know a person is thinking of me when he or she gives me a gift. = 1
I feel loved when a person helps me with my chores = 2""")
if question23 == '1':
    C += 1
else:
    D += 1
print("""
question24""")
question24 = input("""I appreciate it when someone listens patiently and doesn't interrupt me. = 1
I appreciate it when someone remembers special days with a gift. = 2""")
if question24 == '1':
    B += 1
else:
    C += 1
print("""
question25""")
question25 = input("""I like knowing loved ones are concerened enough to help with my daily tasks. = 1
I enjoy extended trips with someone who is special to me. = 2 """)
if question25 == '1':
    D += 1
else:
    B += 1
print("""
question26""")
question26 = input("""I enjoy when my friend pat on the back = 1
Receiving a gift for no special reason excites me. = 2""")
if question26 == '1':
    E += 1
else:
    C += 1
print("""
question27""")
question27 = input("""I like to be told that I am appreciated. = 1
I like for a person to look at me when we are talking. = 2""")
if question27 == '1':
    A += 1
else:
    B += 1
print("""
question28""")
question28 = input("""Mini candy bars given by my friend or loved one are always special to me. = 1
I feel good when my friend or loved one stands near me when greeting me. = 2""")
if question28 == '1':
    C += 1
else:
    E += 1
print("""
question29""")
question29 = input("""I feel appreciated when a person does a task I have requested. = 1
I feel loved when I am told how much I am appreciated. = 2""")
if question29 == '1':
    D += 1
else:
    A += 1
print("""
question30""")
question30 = input("""I like to receive hugs from my friends daily. = 1
I need words of affirmation daily. = 2""")
if question30 == '1':
    E += 1
else:
    A += 1
print("\nTest Completed. Please wait a moment")
time.sleep(5)
print(f"""
Word of Affirmation:{A}
Quality Time:{B}
Receiving Gifts:{C}
Act of Service:{D}
Physical Touch:{E}""")
time.sleep(3)
a = [A,B,C,D,E]
if max(a) == A:
    print("\nYour primary love language is 'Word of Affirmation'")
    time.sleep(2)
    print("""
-Word of Affirmation-
When worlds of affirmation is your love language,
words build you up. You thrive on spoken affection, praise, encouragement, and compliments.
Harsh words can criticism can bother you for a long time.""")
elif max(a) == B:
    print("\nYour primary love language is 'Quality Time'")
    time.sleep(2)
    print("""
-Quality Time-
To you, nothing says you're loved like undivided attention.
When your partner is truly present and not looking at their phone, it makes you feel important.
Failure to actively listen or long periods without one-on-one time can make you feel unloved.""")
elif max(a) == C:
    print("\nYour primary love language is 'Receiving Gifts'")
    time.sleep(1)
    print("""
-Receiving Gifts-
When you speak this love language, a thoughtful gift shows to you that you are special.
In contrast, generic gifts and forgotten special events have the opposite effect.
This love language isn't necessarily materialistic. It could be as simple as receiving your favorite snack after a bad day.""")
elif max(a) == D:
    print("\nYour primary love language is 'Act of Service'")
    time.sleep(2)
    print("""
-Act of Service-
Anything that your partner does willingly to easy your workload is a sign of love to you.
You feel cared for when your partner vacuums before you get to it or makes you breakfast as a surprise.
On the other hand, broken promises or laziness can make you feel unimportant.""")
elif max(a) == E:
    print("\nYour primary love language is 'Physical Touch'")
    time.sleep(2)
    print("""
-Physical Touch-
Holding hands, kisses, hugs, and other touches are your preferred way to show and receive love.
Appropriate touches convey warmth and safety, while physical neglect can drive a wedge between you and your partner.""")
