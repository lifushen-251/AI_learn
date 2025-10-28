students = [
    {"name": "小明", "scores": {"语文": 88, "数学": 92, "英语": 85}},
    {"name": "小红", "scores": {"语文": 95, "数学": 98, "英语": 91}},
    {"name": "小刚", "scores": {"语文": 76, "数学": 82, "英语": 75}},
    {"name": "小丽", "scores": {"语文": 89, "数学": 58, "英语": 92}},
    {"name": "小华", "scores": {"语文": 91, "数学": 98, "英语": 95}},
    {"name": "张伟", "scores": {"语文": 82, "数学": 88, "英语": 80}},
    {"name": "李娜", "scores": {"语文": 90, "数学": 75, "英语": 85}},
    {"name": "王强", "scores": {"语文": 85, "数学": 90, "英语": 88}}
]

#任务一二
TotalScore = 0
Chinese_TotalScore = 0
Math_TotalScore = 0
English_TotalScore = 0
for i in range(len(students)):
    x = students[i]["scores"]  #学生成绩           
    Chinese_TotalScore += x["语文"]
    Math_TotalScore += x["数学"]
    English_TotalScore += x["英语"]
    total_score = 0
    for value in x.values():
        total_score += value
    TotalScore += total_score
    x["total_score"] = total_score
print(students)
AverageScore = TotalScore/len(students)
Chinese_AverageScore = Chinese_TotalScore/len(students)
Math_AverageScore = Math_TotalScore/len(students)
English_AverageScore = English_TotalScore/len(students)
print(f"班级总平均分：{AverageScore}")
print(f"班级语文平均分：{Chinese_AverageScore}")
print(f"班级数学平均分：{Math_AverageScore}")
print(f"班级英语平均分：{English_AverageScore}")


#任务三
Chinese = {}
Math = {}
English = {}
Total = {}
for i in range(len(students)):
    student = students[i]   
    score = student["scores"]   
    Chinese[student["name"]] = score["语文"]
    Math[student["name"]] = score["数学"]
    English[student["name"]] = score["英语"]
    Total[student["name"]] = score["total_score"]
Chinese_score = list(Chinese.values())
Chines_name = list(Chinese.keys())
Math_score = list(Math.values())
Math_name = list(Math.keys())
English_score = list(English.values())
English_name = list(English.keys())
Total_score = list(Total.values())
Total_name = list(Total.keys())
print(Chinese)
print(list(Chinese.keys())[1])
def ascending_order(list1,list2):   #前一个放值列表，后一个放键列表
    n=len(list1)
    for i in range(1,n):
        x_value = list1[i]
        x_key = list2[i]
        j = i-1
        while j >= 0 and list1[j] > x_value:
            list1[j+1] = list1[j]
            list2[j+1] = list2[j]
            j = j-1
        list1[j+1] = x_value
        list2[j+1] = x_key
    return list1,list2


print("---总分排名前三---")
reorder_Total = ascending_order(Total_score,Total_name)
name = reorder_Total[1]
Score = reorder_Total[0]
print(f"第一名：{name[-1]}（{Score[-1]}）")
print(f"第二名：{name[-2]}（{Score[-2]}）")
print(f"第三名：{name[-3]}（{Score[-3]}）")

print("---语文排名前三---")
reorder_Chinese = ascending_order(Chinese_score,Chines_name)
name = reorder_Chinese[1]
Score = reorder_Chinese[0]
print(f"第一名：{name[-1]}（{Score[-1]}）")
print(f"第二名：{name[-2]}（{Score[-2]}）")
print(f"第三名：{name[-3]}（{Score[-3]}）")

print("---数学排名前三---")
reorder_Math = ascending_order(Math_score,Math_name)
name = reorder_Math[1]
Score = reorder_Math[0]
print(f"第一名：{name[-1]}（{Score[-1]}）")
print(f"第二名：{name[-2]}（{Score[-2]}）")
print(f"第三名：{name[-3]}（{Score[-3]}）")

print("---数学排名前三---")
reorder_English = ascending_order(English_score,English_name)
name = reorder_English[1]
Score = reorder_English[0]
print(f"第一名：{name[-1]}（{Score[-1]}）")
print(f"第二名：{name[-2]}（{Score[-2]}）")
print(f"第三名：{name[-3]}（{Score[-3]}）")

#任务四
reorder_TotalScore = reorder_Total[0]
n = len(reorder_TotalScore)
print(f"总分中位数：{(reorder_TotalScore[n//2]+reorder_TotalScore[n//2-1])/2}")
reorder_ChineseScore = reorder_Chinese[0]
n = len(reorder_ChineseScore)
print(f"语文中位数：{(reorder_ChineseScore[n//2]+reorder_ChineseScore[n//2-1])/2}")
reorder_MathScore = reorder_Math[0]
n = len(reorder_MathScore)
print(f"数学中位数：{(reorder_MathScore[n//2]+reorder_MathScore[n//2-1])/2}")
reorder_EnglishScore = reorder_English[0]
n = len(reorder_EnglishScore)
print(f"英语中位数：{(reorder_EnglishScore[n//2]+reorder_EnglishScore[n//2-1])/2}")

#任务五
query_name = input("请输入学生姓名进行成绩查询: ")
found = False
for student in students:
    if student["name"] == query_name:
        print(f"查询到【{student['name']}】的成绩如下:")
        print(f"  语文: {student['scores']['语文']}")
        print(f"  数学: {student['scores']['数学']}")
        print(f"  英语: {student['scores']['英语']}")
        print(f"  总分: {student['scores']['total_score']}")
        found = True
        break
if not found:
    print("查无此人。")

#交互式成绩查询
while True:
    user_input = input("请输入学生姓名进行查询 (输入 '退出' 结束): ")
    if user_input == "退出":
        print("查询系统已关闭。")
        break
    found = False
    for student in students:
        if student["name"] == user_input:
            print("查询结果:")
            print(f"  姓名: {student['name']}")
            print(f"  语文: {student['scores']['语文']}")
            print(f"  数学: {student['scores']['数学']}")
            print(f"  英语: {student['scores']['英语']}")
            print(f"  总分: {student['scores']['total_score']}")
            found = True
            break
    if not found:
        print("查无此人，请重新输入。")


#成绩表
n = len(students)
for i in range(n):
    print(f"总分成绩第{i+1}名：{reorder_Total[1][i]}，分数为{reorder_Total[0][i]}")
    print(f"语文成绩第{i+1}名：{reorder_Chinese[1][i]}，分数为{reorder_Chinese[0][i]}")
    print(f"数学成绩第{i+1}名：{reorder_Math[1][i]}，分数为{reorder_Math[0][i]}")
    print(f"英语成绩第{i+1}名：{reorder_English[1][i]}，分数为{reorder_English[0][i]}")