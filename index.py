import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class PTSD_Detector:
    def __init__(self, root):
        self.root = root
        self.root.title("PTSD Detector Pro")
        self.root.geometry("750x800")
        self.root.configure(bg="#F0F8FF")
        
        self.questions = [
            "In the last month, how often have you had distressing thoughts or memories of the traumatic event?",
            "In the last month, how often have you avoided thoughts or feelings related to the traumatic event?",
            "In the last month, how often have you been easily startled or felt tense?",
            "In the last month, how often have you experienced trouble sleeping?"
        ]
        
        self.responses = []
        self.create_widgets()
        self.create_menu()
    
    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Export Results", command=self.export_results)
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)
    
    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(main_frame, text="PTSD Symptom Assessment", font=("Arial", 20, "bold")).pack()
        
        instruction_text = "Please rate your experience of the following symptoms in the past month:"
        ttk.Label(main_frame, text=instruction_text, wraplength=600, font=("Arial", 12)).pack(pady=10)
        
        scale_values = ["Never (0)", "Rarely (1)", "Sometimes (2)", "Often (3)", "Very Often (4)"]
        
        for question in self.questions:
            frame = ttk.Frame(main_frame)
            frame.pack(fill=tk.X, pady=8)
            ttk.Label(frame, text=question, wraplength=600, font=("Arial", 11)).pack(anchor="w")
            response = tk.StringVar(value="0")
            self.responses.append(response)
            ttk.Combobox(frame, values=scale_values, textvariable=response, state="readonly").pack(pady=5)
        
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=20)
        ttk.Button(button_frame, text="Analyze Results", command=self.analyze_responses).pack(side=tk.RIGHT, padx=5)
        ttk.Button(button_frame, text="Reset Form", command=self.reset_responses).pack(side=tk.RIGHT, padx=5)
        
        self.result_var = tk.StringVar()
        result_frame = ttk.Frame(main_frame, relief=tk.SUNKEN, borderwidth=2, padding=10)
        result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        ttk.Label(result_frame, text="Assessment Results:", font=("Arial", 12, "bold")).pack(anchor=tk.W)
        self.result_text = tk.Text(result_frame, height=4, wrap=tk.WORD, font=("Arial", 11), state=tk.DISABLED)
        self.result_text.pack(fill=tk.BOTH, expand=True)
    
    def analyze_responses(self):
        total_score = sum(int(resp.get()[0]) for resp in self.responses)
        
        if total_score <= 6:
            result = "Low likelihood of PTSD. However, consider consulting a mental health professional if needed."
            color = "#27ae60"
        elif 7 <= total_score <= 12:
            result = "Moderate symptoms detected. Scheduling an appointment with a healthcare provider is recommended."
            color = "#f1c40f"
        else:
            result = "High likelihood of PTSD detected. Please seek professional help immediately."
            color = "#e74c3c"
        
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)
        self.result_text.tag_config("color", foreground=color)
        self.result_text.tag_add("color", "1.0", "end")
        self.result_text.config(state=tk.DISABLED)
    
    def reset_responses(self):
        for response in self.responses:
            response.set("0")
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state=tk.DISABLED)
    
    def export_results(self):
        result_text = self.result_text.get(1.0, tk.END).strip()
        if not result_text:
            messagebox.showwarning("Warning", "No results to export!")
            return
        
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write("PTSD Assessment Results:\n\n")
                for i, question in enumerate(self.questions):
                    file.write(f"{question}\nResponse: {self.responses[i].get()}\n\n")
                file.write(f"Final Analysis: {result_text}\n")
            messagebox.showinfo("Success", "Results exported successfully!")
    
    def show_about(self):
        about_text = ("PTSD Detector Pro - Version 2.0\n\n"
                      "This tool is designed for preliminary assessment of PTSD symptoms.\n"
                      "It is not a diagnostic tool. Always consult with a qualified mental\n"
                      "health professional for proper evaluation and diagnosis.\n\n"
                      "Developed with ❤️ by HealthTech Solutions")
        messagebox.showinfo("About PTSD Detector Pro", about_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = PTSD_Detector(root)
    root.mainloop()