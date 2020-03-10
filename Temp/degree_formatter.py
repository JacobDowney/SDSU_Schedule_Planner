import DegreeEvaluation as degree

american_history = degree.PHYSICAL_SCIENCES

sections = american_history.split(';')

for j in range(0, len(sections)):
    temp = sections[j].split(':')
    abbr = temp[0].strip()
    nums = temp[1].split(',')

    print_str = "{\"subject\": \"" + abbr + "\","
    length = len(abbr)

    for i in range(0, (5 - len(abbr))):
        print_str += " "

    print_str += " \"numbers\": ["

    for i in range(0, len(nums)):
        print_str += "\"" + nums[i] + "\""
        if (i != len(nums) - 1):
            print_str += ","

    print_str += "]}"
    if (j != len(sections) - 1):
        print_str += ","

    print print_str
