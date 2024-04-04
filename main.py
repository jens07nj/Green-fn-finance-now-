def moneybuckets():
    print('welcome to money buckets where we will plan how you can live on 60% of your income and grow your wealth ')
    income =int( input('What is your income?') )
    print('your money buckets')
    blow = income * 60 / 100
    print(f'blow money: {income *60/100}')
    print(f'{blow*60/100} of your blow money is for daily expences')
    print(f'{blow * 10 / 100} of your blow money is for splurging(e.g. movie tickets, takeaway coffees)')
    print(f'{blow * 10 / 100} of your blow money is for smile( long term goals you need to save for e.g. STEM tour)')
    print(f'{blow * 20 / 100} of your blow money is for unexpected expences  (e.g. unexpected vet bill)
    print(f'Grow money(to build long-term wealth and security):  {income *20/100}')
    print(f'Mojo money(safety money):  {income * 20 / 100}')

    return
def compoundinterest():
    return

print('welcome to green fn')

game = input ('to select money buckets enter (1), to select compound interest enter (2)')
if game ==1:
    moneybuckets()
if game ==2:
    moneybuckets()

else:
    print ('invalid selection')
    game = input ('to select money buckets enter (1), to select compound interest enter (2)')






