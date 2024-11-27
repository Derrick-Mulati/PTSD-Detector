import tkinter as tk
from tkinter import messagebox

class PTSD_Detector:
    def __init__(self, root):
        self.root = root
        self.root.title("PTSD Detector")
        self.root.geometry("400x400")

        self.questions = [
            "1. In the last month, how often have you had distressing thoughts or memories of the traumatic event?",
            "2. In the last month, how often have you avoided thoughts or feelings related to the traumatic event?",
            "3. In the last month, how often have you been easily startled or felt tense?",
            "4. In the last month, how often have you experienced trouble sleeping?"
        ]
        
        self.responses = []
        
        self.create_widgets()
    
    def create_widgets(self):
        for idx, question in enumerate(self.questions):
            label = tk.Label(self.root, text=question, anchor="w", padx=10, pady=5)
            label.pack(fill="both")
            
            response = tk.StringVar()
            self.responses.append(response)
            
            scale = tk.Scale(self.root, from_=0, to_=4, orient="horizontal", variable=response, tickinterval=1)
            scale.pack(fill="both")
        
        submit_button = tk.Button(self.root, text="Submit", command=self.analyze_responses)
        submit_button.pack(pady=20)
    
    def analyze_responses(self):
        total_score = sum([int(response.get()) for response in self.responses])
        
        if total_score <= 6:
            message = "Low likelihood of PTSD. However, if you're experiencing difficulties, consider seeking help."
        elif 7 <= total_score <= 12:
            message = "Moderate symptoms. We recommend speaking with a healthcare professional."
        else:
            message = "High likelihood of PTSD. Please seek professional help immediately."
        
        messagebox.showinfo("Result", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = PTSD_Detector(root)
    root.mainloop()
