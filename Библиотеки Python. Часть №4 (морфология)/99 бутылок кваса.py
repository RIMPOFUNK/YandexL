import pymorphy2

morph = pymorphy2.MorphAnalyzer()
i = 99
while i != 0:
    temp = morph.parse('бутылка')[0]
    g = "Осталось"
    g_2 = "Осталась"
    print(f"В холодильнике {i} {temp.make_agree_with_number(i).methods_stack[0][1]} кваса.")
    print('Возьмём одну и выпьем.')
    i -= 1
    if str(i)[-1] == "1" and i != 11:
        print(f'{g_2} {i}'
              f' {temp.make_agree_with_number(i).methods_stack[0][1]} ква'
              f'са.')
    else:
        print(f'{g} {i}'
              f' {temp.make_agree_with_number(i).methods_stack[0][1]} ква'
              f'са.')
