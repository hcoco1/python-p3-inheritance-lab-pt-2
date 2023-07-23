class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")
        
        
    def raise_hand(self):
        print("Pick me!")

class ChattyStudent(Student):
    def hello(self):
        super().hello()  
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
    
    def raise_hand(self):
        super().raise_hand()
        super().raise_hand() 
        super().raise_hand() 
        super().raise_hand() 
        super().raise_hand() 
        super().raise_hand() 
        super().raise_hand() 
        super().raise_hand() 
        super().raise_hand() 
        super().raise_hand() 
        
    
# The first class, Student, defines two methods: hello() and raise_hand(). The hello() method prints a message saying that the student is excited to learn stuff. The raise_hand() method prints a message saying "Pick me!".

# The second class, ChattyStudent, inherits from the Student class. This means that the ChattyStudent class has all of the same methods as the Student class, plus any additional methods that are defined in the ChattyStudent class.

# The ChattyStudent class defines a new method called hello(). This method first calls the hello() method from the Student class. This prints the message "Hey there! I'm so excited to learn stuff.". Then, the ChattyStudent method prints a few more messages, including asking how the person is doing and talking about The Walking Dead.

# The ChattyStudent class also defines a new method called raise_hand(). This method calls the raise_hand() method from the Student class 10 times. This prints the message "Pick me!" 10 times. 
