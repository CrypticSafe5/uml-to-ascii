import tkinter as tk

"""
+-------------+         +-------------+
| information |         |  something  |
+-------------+         +-------------+
       |                       |
       |---------------------->|
       |                       |
       |                       |
       |<----------------------|
       |                       |
"""

def build_boxes(items):
	print("doot")

def convert_input():
	input = txt_input.get("0.0", tk.END)
	input_lines = input.split("\n")

	output = ""
	entities = []
	activity = []
	# Parse input
	for line in input_lines:
		if len(line) == 0:
			continue
		comments = ""
		if ":" in line:
			comments = line.split(":")[1]
			line = line.split(":")[0]
		items = line.split()
		if items[0] not in entities:
			entities.append(items[0])
		if items[2] not in entities:
			entities.append(items[2])
		# TODO: Add to/from logic
		activity.append({ "to": items[2], "from": items[0] })

	# Use parsed input to generate visual line by line
	# for item in activity:

	txt_output.delete("1.0", tk.END)
	txt_output.insert("1.0", entities)
	txt_output.insert(tk.END, f"\n{activity}")

window = tk.Tk()

frm_input = tk.Frame(master = window)
frm_output = tk.Frame(master = window)

lbl_input = tk.Label(
	master = frm_input,
	text = "Simply type in your UML in the text area below and click \"CONVERT\" when you want to get the ASCII output",
	foreground="white",
	background="#34A2FE"
)
lbl_input.pack()

txt_input = tk.Text(master = frm_input)
txt_input.pack()

button = tk.Button(
	text = "CONVERT",
	command = convert_input
)
button.pack(side = tk.BOTTOM)

lbl_output = tk.Label(
	master = frm_output,
	text = "ACII output here"
)
lbl_output.pack()

txt_output = tk.Text(master = frm_output)
txt_output.pack()

frm_input.pack(
	side = tk.LEFT,
	fill = tk.BOTH
)
frm_output.pack(
	side = tk.LEFT,
	fill = tk.BOTH
)

window.mainloop()
