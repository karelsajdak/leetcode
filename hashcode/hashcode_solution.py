with open ("b_better_start_small.in.txt", "r") as myfile: data = myfile.read().splitlines()
count = data[0].split()
input = data[1::]
contributers = []
contributerCount = 0
skillCount = 0
while(contributerCount < int(count[0])):
    person = input[contributerCount+skillCount].split()
    contributer = [person[0]]
    for i in range(int(person[1])):
        skillCount += 1
        contributer.append(input[contributerCount+skillCount])
    contributers.append(contributer)
    contributerCount += 1

projectData = input[contributerCount+skillCount::]
projects = []
projectCount = 0
roleCount = 0
while(projectCount < int(count[1])):
    project = [projectData[projectCount+roleCount]]
    for i in range(int(project[0].split()[4])):
        roleCount += 1
        project.append(projectData[projectCount+roleCount])
    projects.append(project)
    projectCount += 1

outputProjects = []
while(projects):
    for project in projects:
        tempProject = []
        tempProject.append(project[0].split()[0])
        for skill in project[1::]:
            for contributer in contributers:
                for contributerSkill in contributer[1::]:
                    if skill.split()[0] in contributerSkill and int(skill.split()[1]) <= int(contributerSkill.split()[1]):
                        if int(skill.split()[1]) == int(contributerSkill.split()[1]):
                            index = contributer.index(contributerSkill)
                            contributer[index] = contributerSkill.split()[0] + " " + str(int(contributerSkill.split()[1]) + 1)
                            print(contributers)                            
                        tempProject.append(contributer[0])
        if len(tempProject) - 1 == int(project[0].split()[4]):
            outputProjects.append(tempProject)
            projects.remove(project)

file = open("output.txt","w")
file.write(str(len(outputProjects)) + "\n")
for i in range(len(outputProjects)):
    file.write(outputProjects[i][0] + "\n")
    people = ""
    for j in range(1,len(outputProjects[i])):
        people += outputProjects[i][j] + " "
    file.write(people + "\n")
file.close()
