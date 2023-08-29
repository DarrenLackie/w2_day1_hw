class Student:
    def __init__ (self, input_student_name, input_cohort):
        self.name = input_student_name
        self.cohort = input_cohort

    def talk(self):
        return "I can talk!"
    
    def say_favourite_language(self, input_fav_language):
        # return "I love " + input_fav_language
    
      return f"I love {input_fav_language}"  #//// formatted string, easier to read when adding more variables


