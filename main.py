class teaching_faculty:
      def __init__(self,name,emp_ID,branch,salary):
         self.name = name
         self.emp_ID = emp_ID
         self.branch = branch
         self.salary = salary

      def displayDetails(self):
         print("name:", self.name, "emp_ID:", self.emp_ID, "branch:",self.branch, "Salary:", self.salary)

A = teaching_faculty('john','john@123','cs',40000)
B = teaching_faculty('ronny','ron@2324','english',30000)
C = teaching_faculty('anand','anand@3434','maths',35000)

A.displayDetails()
B.displayDetails()
C.displayDetails()