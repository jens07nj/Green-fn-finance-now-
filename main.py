def moneybuckets():
    #welcome to money buckets, explain game
    print('welcome to money buckets where we will plan how you can live on 60% of your income and grow your wealth ')
    #user input income
    income =float( input('What is your income?') )
    print('your money buckets')
    #divie income and print in diveded categorys
    blow = income * 60 / 100
    print(f'blow money: ${income *60/100}')
    print(f'   ${blow*60/100} of your blow money is for daily expences')
    print(f'   ${blow * 10 / 100} of your blow money is for splurging(e.g. movie tickets, takeaway coffees)')
    print(f'   ${blow * 10 / 100} of your blow money is for smile( long term goals you need to save for e.g. STEM tour)')
    print(f'   ${blow * 20 / 100} of your blow money is for unexpected expences  (e.g. unexpected vet bill)')
    print(f'Grow money(to build long-term wealth and security):  ${income *20/100}')
    print(f"$Mojo money(safety money): {income * 20 / 100}")

    return
def compoundinterest():
    #user input age, interest rate and how much money they add each year.
    age = int(input ("What age are you beginning to invest?"))
    interest= float(input ('average annual interest return (e.g. 10%):'))
    add = float(input ('How much will you invest every year:'))
    # print headings of table
    print ('age   invested   savings')
    #print contents of table looped till age is 60
    bal = 0
    while age < 61:
        bal = bal + add + (bal + add)* interest/100
        print (f'{age}    {add}       ${round(bal)}')
        age = age +1


    return
#welcome to app
print('welcome to green fn')
game =(input ('to select money buckets enter (1), to select compound interest enter (2), to end game enter (3):'))
#user chooses a game or to end app, run chosen game
while game != '':
    if game =='1':
        moneybuckets()
        game =(input ('to select money buckets enter (1), to select compound interest enter (2), to end game enter (3):'))
    if game =='2':
        compoundinterest()
        game =game = (input ('to select money buckets enter (1), to select compound interest enter (2), to end game enter (3):'))
    if game =='3':
        game = ''
    else:
        print ('invalid selection')
        game = (input ('to select money buckets enter (1), to select compound interest enter (2), to end game enter (3):'))

print ('Thank you for playing green FN')





