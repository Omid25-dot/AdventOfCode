def safe_levels(levels):
    increasing =  all(1 <= levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
    decreasing =  all(1 <= levels[i] - levels[i + 1] <= 3 for i in range(len(levels) - 1))

    return increasing or decreasing

def safe_with_dampener(levels):
    if safe_levels(levels):  # Already safe
        return True
    # Check if skipping one number makes it safe
    for i in range(len(levels)):
        if safe_levels(levels[:i] + levels[i + 1:]):
            return True
    return False
with open("rows.txt", "r") as file:
    reports = file.read().strip().split("\n")

safe_count = 0
for report in reports:
    levels = list(map(int,report.split()))
    if safe_with_dampener(levels):
        safe_count += 1
print(safe_count)



