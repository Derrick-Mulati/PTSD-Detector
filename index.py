import tkinter as tk
from tkinter import messagebox

class PTSD_Detector:
    def __init__(self, root):
        self.root = root
        self.root.title("PTSD Detector")
        self.root.geometry("500x600")
        
        self.questions = [
            "1. In the last month, how often have you had distressing thoughts or memories of the traumatic event?",
            "2. In the last month, how often have you avoided thoughts or feelings related to the traumatic event?",
            "3. In the last month, how often have you been easily startled or felt tense?",
            "4. In the last month, how often have you experienced trouble sleeping?"
        ]
        
        self.responses = []
        
        self.create_widgets()
    
    def create_widgets(self):
        # Title and Instructions
        intro_label = tk.Label(self.root, text="PTSD Screening Tool", font=("Helvetica", 18, "bold"))
        intro_label.grid(row=0, column=0, columnspan=2, pady=15)

        instruction_label = tk.Label(self.root, text="Please rate how often you have experienced the following symptoms on a scale of 0 (Not at all) to 4 (Very often).", wraplength=450)
        instruction_label.grid(row=1, column=0, columnspan=2, pady=10)
        
        # Questions and Scales
        for idx, question in enumerate(self.questions):
            label = tk.Label(self.root, text=question, anchor="w", padx=10, pady=5, font=("Helvetica", 12))
            label.grid(row=2 + idx, column=0, sticky="w", padx=20)
            
            response = tk.StringVar()
            self.responses.append(response)
            
            scale = tk.Scale(self.root, from_=0, to_=4, orient="horizontal", variable=response, tickinterval=1, length=300)
            scale.set(0)  # default value to 0
            scale.grid(row=2 + idx, column=1, pady=5, padx=20)
            
            # Adding text labels for scale values
            scale_label_0 = tk.Label(self.root, text="Not at all", font=("Helvetica", 10))
            scale_label_0.grid(row=2 + idx + 1, column=1, sticky="w", padx=20)
            scale_label_4 = tk.Label(self.root, text="Very often", font=("Helvetica", 10))
            scale_label_4.grid(row=2 + idx + 1, column=1, sticky="e", padx=20)
        
        # Submit Button
        submit_button = tk.Button(self.root, text="Submit", command=self.analyze_responses, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        submit_button.grid(row=6, column=0, columnspan=2, pady=20)
        
        # Reset Button
        reset_button = tk.Button(self.root, text="Reset", command=self.reset_responses, bg="#FF6347", fg="white", font=("Helvetica", 12))
        reset_button.grid(row=7, column=0, columnspan=2, pady=10)

    def analyze_responses(self):
        # Check if all questions have been answered
        if any(response.get() == '' for response in self.responses):
            messagebox.showerror("Error", "Please answer all questions before submitting.")
            return
        
        total_score = sum([int(response.get()) for response in self.responses])
        
        if total_score <= 6:
            message = "Low likelihood of PTSD. However, if you're experiencing difficulties, consider seeking help."
        elif 7 <= total_score <= 12:
            message = "Moderate symptoms. We recommend speaking with a healthcare professional."
        else:
            message = "High likelihood of PTSD. Please seek professional help immediately."
        
        # Show result and change button state after submission
        messagebox.showinfo("Result", message)
    
    def reset_responses(self):
        # Reset all scales to 0
        for response in self.responses:
            response.set('')
        
        # Reset the interface for a fresh start
        messagebox.showinfo("Reset", "All responses have been cleared. Please start over.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PTSD_Detector(root)
    root.mainloop()
