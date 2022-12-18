import fileReader as fr
import scheduleGenerator as gen
import DAG as dag
  
def display():
  schedule = ""
  for course in gen.courseArray:
    schedule += "\n" + "Semester: " + str(gen.k) + " " + gen.season() + "\n"
    for i in course:
      schedule += i + "\n"
      gen.k += 1
  return schedule