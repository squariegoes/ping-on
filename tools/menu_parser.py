import re


# text = "1. CHEF'S SPECIAL (FOR 2 PERSONS)  (COMBINATION OF BBCLRIBS, WUN TUN, SPRING ROLL AND SESAME PRAWN TOAST) £10.50 "
# TEXT = "1. CHEF'S SPECIAL (FOR 2 PERSONS)  (COMBINATION OF BBCLRIBS, WUN TUN, SPRING ROLL AND SESAME PRAWN TOAST) £10.50 2. HAIL KAU PRAWN DUMPLING (DIM-SUM) (20 MIN)  £3.40 3. PORK AND PRAWN OR BEEF SHUI-MAI (DIM-SUM) (20 MEN)   £3.40 1 4. STEAMED SPARE RIBS IN BLACK BEAN SAUCE (DIM-SUM) (20 MIN)  £3A0 5. CRISPY SPRING ROLLS  £3.60 6. PRAWN COCKTAIL  £4.50 7. BARBECUED SPARE RIBS   £5.60 8. SPARE RIBS PEAKING STYLE  £5.60 1 9. HONEY CHILLI SPARE RIBS  £5.60 _} 10. SPARE RIBS WITH SPICED SALT AND CHILLI   £5.60 1 11. SPICY CHICKEN WINGS   £5.50 _.../ 12. HONEY CHILLI CHICKEN WINGS  £5.50 13. PAPER WRAPPED CHICKEN  £5.50 14. PAPER WRAPPED PRAWNS  £5.50 15. SESAME PRAWN TOAST   £4.80 16. SESAME CHICKEN TOAST  £4.80 17. DEEP FRIED PRAWN BALL  £5.80 1 18. DEEP FRIED WUN TUN  £5.50 1 19. CRISPY CURRY CHICKEN TRIANGLES (SAMOSA)  £5.20 1 20. CRISPY DUCK SPRING ROLLS   £4.20 21. DEEP FRIED SEAWEED WITH CASHEW NUTS   £5.00 ..../ 22. SATAY CHICKEN OR BEEF SKEWERS IN SAUCE (3 SKEWERS)   £5.50 -.1 23. SATAY KING PRAWN SKEWERS IN SAUCE (2 SKEWERS)  £5.50"

html_template = '<div class="menuItemContainer">' \
                '  <div class="menuItemLeft">' \
                '    <div class="menuItemNum{veg_num_class}">{number}</div>' \
                '    {item}' \
                '  </div>' \
                '    <div class="menuItemRight">{price}</div>' \
                '    <div class="menuItemCenter">&nbsp;</div>' \
                '</div>'


def main():
    # print(html_template.format(number=1, item='test', price=1.23))

    # 2. split into lines based on price
    #
    # items = find_value('(?:[£][0-9]+\.[0-9]{2})(\s*)(?:[0-9]+\.)', text)
    # items = re.split('(?:[£][0-9]+\.[0-9]{2})(\s)', text)


    is_vegetarian = False


    all_items_html = []

    cnt = 0
    # for item in items:
    with open('menu_sections/sides.txt') as file:
        for line in file:
            # 1. tidy text
            line = line.replace('..', ' ')
            line = line.replace('  ', ' ')
            line = line.title()

            cnt = cnt + 1


            # 3. split into menu item name and price
            item_num = find_value('^([0-9]+\.)', line)

            item_name = find_value('^(?:[0-9]+\.)(.*)(?:[£][0-9]+\.[0-9]{2})', line)
            item_name = item_name.strip()

            price = find_value('([£][0-9]+\.[0-9]{2})', line)

            # 4. replace brackets with span tags for italics
            item_name = item_name.replace('(','<div class="menuItemSmallItalicsInline">(')
            item_name = item_name.replace(')',')</div>')

            # 5. Format html
            item_html = html_template.format(number=item_num, item=item_name, price=price, veg_num_class=' menuItemNumVeg' if is_vegetarian else '')
            all_items_html.append(item_html)
            # print(item_html)

            # print('-- ITEM {}'.format(cnt))
            # print(line)
            # print(item_num)
            # print(item_name)
            # print(price)
            # print()

    print()
    # print(all_items_html)
    # print()
    for item in all_items_html:
        print(item)


def find_value(pattern, text):
    # http://pythex.org/
    matches = re.findall(pattern, text)

    if matches:
        return matches[0]
    else:
        return 'UNKNOWN'


if __name__ == "__main__":
    main()