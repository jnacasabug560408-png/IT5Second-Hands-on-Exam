class StudentGradingSystem:

  def __init__(self):

    self.grades = []



  def add_grade(self, grade):

    if 0 <= grade <= 100:

      self.grades.append(grade)

    else:

      print(f"Ignored invalid grade: {grade}")



  def calculate_results(self):

    if not self.grades:

      return None



    avg = sum(self.grades) / len(self.grades)

    point = round(((100 - avg) + 10) / 10, 2)



    if avg < 50:

      remarks = "Dropped"

    elif avg < 75:

      remarks = "Failed"

    elif 75 <= avg <= 79:

      remarks = "Passed – Satisfactory"

    elif 80 <= avg <= 84:

      remarks = "Passed – Good"

    elif 85 <= avg <= 89:

      remarks = "Passed – Average"

    elif 90 <= avg <= 99:

      remarks = "Passed – Very Good"

    elif avg == 100:

      remarks = "Passed – Excellent"

    else:

      remarks = "Invalid"



    return {

      "Grades": self.grades,

      "Average": round(avg, 2),

      "Point Grade": point,

      "Remarks": remarks

    }





if __name__ == "__main__":

  grading = StudentGradingSystem()

  print("Enter grades (type -1 to stop):")

  while True:

    try:

      g = int(input("Grade: "))

      if g == -1:

        break

      grading.add_grade(g)

    except ValueError:

      print("Please enter a valid number.")



  result = grading.calculate_results()

  if result:

    print("\n--- Results ---")

    for k, v in result.items():

      print(f"{k}: {v}")