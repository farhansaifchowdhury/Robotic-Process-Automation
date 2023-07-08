#for firefox
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.edge.options import Options
#from selenium.webdriver.edge.service import Service

#from subprocess import CREATE_NO_WINDOW
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from tkinter import *
from selenium.common.exceptions import NoSuchElementException
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import time
from selenium.webdriver.common.keys import Keys
from datetime import date
from datetime import datetime
from tkinter.messagebox import askyesno
import threading
#options = Options()
#options.headless = True
app = tk.Tk()
app.title("BUP MISS RPA")
app.geometry("500x500")
app.columnconfigure(0,weight=0)
stop = False
#driver=webdriver.Firefox()

def my_function():
    action = ActionChains(driver);
    search = driver.find_element(By.ID,"save")
    action.move_to_element(search).perform()
    search.click()
def update_progress(value):
    progress_bar["value"] = value
    app.update()

def final_rpa():
    global stop
    stop = False
    while(stop == False):
        if stop == False:
            def save_btn():
                action = ActionChains(driver);
                search = driver.find_element(By.ID,"save")
                action.move_to_element(search).perform()
                search.click()

            def domain1(user_name):
                #update_progress(5)
    
                driver.get("http://localhost/domain2.com")

                search = driver.find_element(By.ID,"adminID")
                search.send_keys("1001")
                search = driver.find_element(By.ID,"adminPass")
                search.send_keys("1234")

                action = ActionChains(driver);
                search = driver.find_element(By.ID,"loginbtn")
                action.move_to_element(search).perform()
                search.click()
    
                #update_progress(25)
                action = ActionChains(driver);
                search = driver.find_element(By.ID,"pr")
                action.move_to_element(search).perform()
                search = driver.find_element(By.ID,"mn")
                action.move_to_element(search).perform()
                search.click()
    
                search = driver.find_element(By.ID,"eid")
                search.send_keys(user_name)

                element = driver.find_element(By.ID,"lock")
                drp=Select(element)
                drp.select_by_visible_text('No')

                action = ActionChains(driver);
                search = driver.find_element(By.ID,"submit")
                action.move_to_element(search).perform()
                search.click()
                #update_progress(75)
                action = ActionChains(driver);
                search1 = driver.find_element(By.ID,"pr")
                action.move_to_element(search1).perform()
   
                search1 = driver.find_element(By.ID,"rp")
                action.move_to_element(search1).perform()
                search1.click()

                search = driver.find_element(By.ID,"u_name")
                search.send_keys(user_name)

                search = driver.find_element(By.ID,"pass")
                search.send_keys("0987")

                action = ActionChains(driver);
                search = driver.find_element(By.ID,"resetbtn")
                action.move_to_element(search).perform()
                search.click()


            driver = webdriver.Firefox()
            driver.get("http://localhost/domain2.com")

            search = driver.find_element(By.ID,"adminID")
            search.send_keys("1001")
            search = driver.find_element(By.ID,"adminPass")
            search.send_keys("1234")

            action = ActionChains(driver);
            search = driver.find_element(By.ID,"loginbtn")
            action.move_to_element(search).perform()
            search.click()

            action = ActionChains(driver);
            search = driver.find_element(By.ID,"ticket")
            action.move_to_element(search).perform()
            search = driver.find_element(By.ID,"ot")
            action.move_to_element(search).perform()
            search.click()

            table = driver.find_element(By.ID,"openticket")
            body = table.find_element(By.TAG_NAME,"tbody")
            rows = table.find_elements(By.TAG_NAME,"tr")
            cells = body.find_elements(By.TAG_NAME,"td")
            #global stop
            #stop = False
            #while(True): 
            for i  in range(len(rows)):
                columns = rows[i].find_elements(By.TAG_NAME,"td")
         
                for j in range(len(columns)):
                    if columns[j].text == "Open":
                        if stop == False:
                            e_id = columns[j-3].text
                            app_name = columns[j-2].text
                            now = datetime.now()
                            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                            f = open("LOG_FILE.txt", "a")
                            f.write(date_time)
                            f.write("  ")
                            f.write(e_id)
                            f.write("      ")
                            f.write(app_name)
                            f.write("\n")
                            f.close()
                            driver.execute_script("window.open('');")
                            driver.switch_to.window(driver.window_handles[1])
                            if app_name == "Domain1.com":
                                domain1(e_id)
                             
                            driver.close()
                            driver.switch_to.window(driver.window_handles[0])
                            columns[j+1].click()

                
            save_btn()
            driver.close()
            time.sleep(15)
            #readOnlyText.configure(state='normal')
            #readOnlyText.delete(1.0,'end')
            #readOnlyText.insert(1.0,"Waiting For New Request")
            
            
            readOnlyText.configure(state='normal')
            readOnlyText.delete(1.0,'end')
            readOnlyText.insert(1.0,"Processing")
    readOnlyText.configure(state='normal')
    readOnlyText.delete(1.0,'end')
    readOnlyText.insert(1.0,"Stopped")



def confirm():
    answer = askyesno(title='confirmation',
                    message='Are you sure that you want to quit?')
    if answer == True:
        global stop
        stop = True
        readOnlyText.configure(state='normal')
        readOnlyText.delete(1.0,'end')
        readOnlyText.insert(1.0,"Stopped")
        readOnlyText.configure(state='disabled')
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        global stop
        stop = True
        app.destroy()

def button_stop_command():
     global stop
     stop = True
def button_starter():
    readOnlyText.configure(state='normal')
    readOnlyText.delete(1.0,'end')
    readOnlyText.insert(1.0,"Processing")
    readOnlyText.configure(state='disabled')
    t = threading.Thread(target=final_rpa)
    t.start()



part_text=StringVar()
part_label1=Label(app,text='Task Status',font=('bold',14),pady=20)
part_label1.place(relx=0.5, rely=0.5, anchor='center')
part_label1.pack()

readOnlyText = tk.Text(app, height=2)
readOnlyText.pack()
add_btn=Button(app, text='Start', width=12, command=button_starter)
add_btn.place(relx=0.5, rely=0.5, anchor='center')
add_btn.pack()

add_btn1=Button(app, text='Stop', width=12, command=confirm)
add_btn1.place(relx=0.5, rely=0.5, anchor='center')
add_btn1.pack()


app.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()

