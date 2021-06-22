import re

s = "14 relevant clinical laboratory abnormality a determine by the investigator e.g plasma sodium 130 mmol/l alanine or aspartate aminotransferase 2.0 time above the upper limit of the range or white blood cell count 3,000 cells/mm3 " # 10000
tokens = s.split()
# print(tokens)

pattern_map = {}
pattern_map[r"(\d+[.]\d+|.\d+|\d/\d|\d \d/\d|\d+,\d+|\d+ , \d+|\d+)( |$)"] = "NUM"
pattern_map[r"[\d.]+ (to|-) [\d.]+( |$)"] = "NUM"
pattern_map[r"[\d.]+[-/][\d.]+( |$)"] = "NUM"
pattern_map[r"\d+%( |$)"] = "NUM"
pattern_map[r"(\\d+|\\d+\\.\\d+)(mg|doz|oz|ml|l|mb|meq)"] = "DOSE"

for pattern, tag in pattern_map.items():
    prog = re.compile(pattern)
    print(tag, re.findall(pattern, s))
    # print(match.groups())

'''
r"^x( |)\\d+( |$)","FREQ");
r"^(\\d+|\\d+\\.\\d+)(mg|doz|oz|ml|l|mb|meq)", "DOSE");
# "^[\\d\\.]+ (to|-)( |$)"#,"NUM"
r"^several (min|minute|minutes|h|hr|hrs|hour|hours|d|day|days|wk|week|weeks|m|month|months)( |$)","DRT");
r"^x\\d+(min|minute|minutes|h|hr|hrs|hour|hours|d|day|days|wk|week|weeks|m|month|months)( |$)","DRT");
# "^(\\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty)( more | )(to|-|)(\\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|)( |)(min|minute|minutes|h|hr|hrs|hour|hours|d|day|days|wk|week|weeks|m|month|months)( |$)","DRT");
r"^(\\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty)( more | )(min|minute|minutes|h|hr|hrs|hour|hours|d|day|days|wk|week|weeks|m|month|months)( |$)","DRT");
r"^\\d{1,2}\\/\\d{1,2} \\- \\d{1,2}\\/\\d{1,2}( |$)","DRT");
r"^x(min|minute|minutes|d|day|days|wk|week|weeks|m|month|months)( |$)","TUNIT");
r"^\\d( |)x( |)(daily|weekly|monthly|a day|a week|a month|per day|per week|per month)","FREQ");
r"^\\d+( |)(am|pm|clock)","TOD");
r"^(every|q|qdaily) (m|mon|t|tue|tues|w|wed|r|thu|thur|f|fri|sat|sun|monday|tuesday|wednesday|thursday|friday|saturday|sunday|,| |and)+( |$)","FREQ");
r"^(m|mon|t|tue|w|wed|r|thu|f|fri|sat|sun|monday|tuesday|wednesday|thursday|friday|saturday|sunday) and (m|mon|t|tue|w|wed|r|thu|f|fri|sat|sun|monday|tuesday|wednesday|thursday|friday|saturday|sunday)( |$)","FREQ");
r"^(one|two|three|four|five|six|seven|eight|nine|ten) to (one|two|three|four|five|six|seven|eight|nine|ten)( |$)"#,"NUM"
r"^q(\\.|)\\d+( |$)","FREQ");
r"^q( \\. | |\\.|)( |)(\\d+|\\d\\-\\d|\\d \\- \\d)?( |)(hrs|hr|h|m|min|d|hour|hours|day|days|minute|minutes|wk|week|weeks|month|months)(prn|)(\\.|)( |$)","FREQ");
r"^(\\d+|one|two|three|four|five|six|seven|eight|nine|ten) times (daily|weekly|monthly|a day|a week|a month|per day|per week|per month)( |$)","FREQ");
r"^(every|each|per) (minute|hour|morning|afternoon|evening|day|wk|week|month|bedtime|breakfast|lunch|dinner)( |$)","FREQ");
r"^every (\\d+|\\d+\\-\\d+|\\d+ to \\d+|\\d+ \\- \\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|twenty-one|twenty-two|twenty-three|twenty-four) ?(hrs|hr|h|m|min|d|hour|hours|day|days|minute|minutes|wk|week|weeks|month|months)( |$)","FREQ");
# r'^\d( |)x( |)(daily|weekly|monthly|a day|a week|a month|per day|per week|per month)', 'FREQ')
'''