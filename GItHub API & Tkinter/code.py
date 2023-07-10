import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600



def format_response(user_data):
	try:
		followers = user_data['followers']
		following = user_data['following']

		final_str = 'Followers: %s \n Following: %s' % (followers, following)
	except:
		final_str = 'There was a problem retrieving that information'

	return final_str

def get_user_data(userName):
    url = f"https://api.github.com/users/{userName}"
    user_data = requests.get(url).json()
    label['text'] = format_response(user_data)


	



root = tk.Tk()
root.title('Devnetics GitHub Aggregrator API')
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='Devnetics.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#00050a', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get details", font=40, command=lambda: get_user_data(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#00050a', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()
