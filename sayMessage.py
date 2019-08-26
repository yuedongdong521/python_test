content = input("content:")
screen_width = 80
text_width = len(content)
print(text_width)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2

print()
print('' * left_margin + '+' + '-' * (box_width - 2) + '+')
print('' * left_margin + '|' + '-' * text_width      + '|')
print('' * left_margin + '|' +            content    + '|')
print('' * left_margin + '|' + '-' * text_width      + '|')
print('' * left_margin + '+' + '-' * (box_width - 2) + '+')
print()
