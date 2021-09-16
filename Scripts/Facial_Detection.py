import cv2,os,tkinter as tk
from tkinter import Message, font, messagebox, Button, Tk,Canvas

file_path = 'D:'
name = 'Image'
save_image = False

save_click = 0
img_name = 'Image'

def main(save_image):
    # The number '0' stands for the WebCam input [ie. if you have multiple webcams pluged-in then select a camera by entering the number]  
    cap = cv2.VideoCapture(0)

    # Use the 'haarcascade_frontalfaces.xml' haarcascade to detect faces in each Frame 
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Use the 'haarcascade_eye.xml' haarcascade to detect faces in each Frame 
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    image_status = False
    detected = False
    while(True):
        # Get each frame from the camera 
        ret,frame = cap.read()

        # Convert the Frames from 'Color' to 'Grayscale' and display the Frames
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect any Faces(upto 5 faces) in the Frame with a probability of '1.3'
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            # Draw a rectangle over the 'Face/Faces'
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

            #Region of Interest
            roi_gray = gray[y:y+w, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            # Detects the eyes in the Frames
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
            for (ex, ey, ew, eh) in eyes:
                detected = True
                # Draw a rectangle over the eyes
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        
        # Display the Frames
        cv2.imshow('Frame',frame)

        #To save the Image if Face and Eyes are detected
        if(image_status == False and detected == True and save_image == True):
            # Choose a Path to save the image
            image_status = True
            cv2.imwrite(file_path +'\\' + name +'.jpg',frame)
        

        # If user enters 'q' then exit the loop and close the window 
        if(cv2.waitKey(1) == ord('q')):
            break
        
    # Close the Camera 
    cap.release()
    cv2.destroyAllWindows()

def check_save_image(var_save,label,check_button):
    global save_image
    if(var_save.get() == 1):
        save_image = True
    else:
        save_image = False
    messagebox.showinfo("Information","Image Saved")
    clear(label)
    clear(check_button)

def change_name(new_name,label_2,entry,save_button):
    global name
    name = new_name.get()
    messagebox.showinfo("Information","Name Entered: " + name)

    clear(label_2)
    clear(save_button)
    clear(entry)
    
def func_save_image(window):
    var_save = tk.IntVar()
    var_name = tk.StringVar()
    label = tk.Label(window,text='Default: Does Not Save Image',font=("Times New Roman", 12),fg='black',bg='#88ddff')
    label.place(relx=0.36,rely=0.22,anchor = 'n')

    check_button = tk.Checkbutton(window,text='yes',variable = var_save,onvalue=1, offvalue=0,command= lambda:check_save_image(var_save,label,check_button))
    check_button.place(relx=0.51,rely=0.22,anchor = 'n')

    label_2 = tk.Label(window,text='Enter Image Name (Default Name: "Image")',font=("Times New Roman", 12),fg='black',bg='#88ddff')
    label_2.place(relx=0.4,rely=0.27,anchor = 'n')

    entry = tk.Entry(window,textvariable=var_name)
    entry.place(relx=0.4,rely=0.32,anchor = 'n')

    save_button = tk.Button(window, text = 'Save',font=("Times New Roman", 12),command=lambda:change_name(var_name,label_2,entry,save_button))
    save_button.place(relx=0.4,rely=0.37,anchor = 'n')

def path_input(label,entry,save_button):
    text = path_var.get()
    if(os.path.exists(text) == True):
        global file_path
        file_path = text
        messagebox.showinfo("Information","File Path Entered: " + text)
        clear(label)
        clear(entry)
        clear(save_button)
    else:
        messagebox.showerror("Error","Path Does not Exists")

def file_path_func():
    label = tk.Label(window,text='Enter Path to Save Image(Saves in "D:" by default)',bg='#88ddff',fg='black',font=("Times New Roman", 12))
    label.place(relx=0.65,rely=0.2,anchor = 'n')
    entry = tk.Entry(window,textvariable=path_var)
    entry.place(relx=0.65,rely=0.25,anchor = 'n')
    save_button = tk.Button(window, text = 'Save Path',font=("Times New Roman", 12),command=lambda:path_input(label,entry,save_button))
    save_button.place(relx=0.65,rely=0.3,anchor = 'n')

def clear(widget):
    widget.destroy()
    

window = tk.Tk()
window.title("Face Detection Program")
window.geometry("1000x1000")
window['background'] = '#88ddff'

lab = tk.Label(font=("Times New Roman", 20),text='Face Detection Program',bg='#88ddff',fg='red')
lab.place(relx=0.5,rely=0.015,anchor='n')

tk.Button(window,font=("Times New Roman", 12),text='Detect_Faces',command = lambda:main(save_image)).place(relx=0.1,rely=0.15,anchor = 'n')

tk.Button(window,text='Save Image',font=("Times New Roman", 12),command=lambda:func_save_image(window)).place(relx=0.4,rely=0.15,anchor = 'n')


path_var = tk.StringVar()
tk.Button(window, text = 'File Path',font=("Times New Roman", 12),command=lambda:file_path_func()).place(relx=0.65,rely=0.15,anchor = 'n')

tk.Button(window,text='Exit',font=("Times New Roman", 12),command= lambda:window.destroy()).place(relx=0.9,rely=0.15,anchor = 'n')
tk.Label(window,text='Enter "q" to exit the Face Detection Window',bg='#88ddff',fg='black',font=("Times New Roman", 12)).place(relx=0.5,rely=0.1,anchor = 'n')

window.mainloop()


