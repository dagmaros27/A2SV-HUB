# Problem: Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    grades = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in grades:
            grades[score].append(name)
        else:
            grades[score] = [name]
    
    grades = sorted(grades.items())
    grades[1][1].sort()
    for name in grades[1][1]:
        print(name)
        
        