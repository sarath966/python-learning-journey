## Module Student_utils
def calculate_average(marks):
    avg = sum(marks)/len(marks)
    return avg

def find_highest(marks):
    highest_mark = max(marks)
    return highest_mark

def find_lowest(marks):
    lowest_mark = min(marks)
    return lowest_mark

def count_passed(marks):
    pass_count = [mark for mark in marks if mark >= 50]
    return len(pass_count)
