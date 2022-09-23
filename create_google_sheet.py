"""Create a Google Sheet from the command line."""

import ezsheets


def write_dct_to_google_sheet(lst, num):
    for index, header_or_data in enumerate(lst):
        column = letters[index]
        cell = column + str(num)
        sheet[cell] = header_or_data


def prompt_user_to_specify_a_name_for_your_sheet():
    print('give your sheet a name')
    return input('> ')


headers = [
    'First',
    'Last',
    'Favorite Football Team',
]

data = [
    'Alice',
    'Johnson',
    'Bengals',
]

letters = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z'
]

user_specified_name = prompt_user_to_specify_a_name_for_your_sheet()
ss = ezsheets.createSpreadsheet(user_specified_name)
sheet = ss[0]
write_dct_to_google_sheet(headers, 1)
write_dct_to_google_sheet(data, 2)
sheet_name = ss.title
print(f'{sheet_name} was created successfully.')
