import re


with open("mul.txt", "r") as file:
    content = file.read()

# Define the regex patterns
mul_pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
toggle_pattern = r"do\(\)|don't\(\)"


mul_matches = list(re.finditer(mul_pattern, content))


do_matches = list(re.finditer(toggle_pattern, content))


mul_enabled = True
result = 0
index = 0


for mul_match in mul_matches:
    mul_pos = mul_match.start()


    while index < len(do_matches) and do_matches[index].start() < mul_pos:
        toggle = do_matches[index].group()
        mul_enabled = (toggle == "do()")  # Enable or disable
        index += 1

    # If multiplications process the mul
    if mul_enabled:
        num1, num2 = map(int, mul_match.groups())
        result += num1 * num2


print(result)

