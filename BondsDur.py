import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 800, height = 680)
canvas1.pack()

label1 = tk.Label(root, text='Calculate Bond Duration')
label1.config(font=('helvetica', 14))
canvas1.create_window(235, 40, window=label1)

entry1 = tk.Entry (root) 
canvas1.create_window(330, 100, window=entry1)

entry2 = tk.Entry (root) 
canvas1.create_window(330, 140, window=entry2)

entry3 = tk.Entry (root) 
canvas1.create_window(330, 180, window=entry3)

entry4 = tk.Entry (root) 
canvas1.create_window(330, 220, window=entry4)

entry5 = tk.Entry (root) 
canvas1.create_window(330, 260, window=entry5)

entry6 = tk.Entry (root) 
canvas1.create_window(240, 380, window=entry6)

entry6 = tk.Entry (root) 
canvas1.create_window(240, 420, window=entry6)

label1 = tk.Label(root, text='Number of Payments  :')
label1.config(font=('helvetica', 10))
canvas1.create_window(160, 100, window=label1)

label2 = tk.Label(root, text='Years to Maturity :           ')
label2.config(font=('helvetica', 10))
canvas1.create_window(160, 140, window=label2)

label3 = tk.Label(root, text='Yield to Maturity(YTM) :              ')
label3.config(font=('helvetica', 10))
canvas1.create_window(160, 180, window=label3)

label4 = tk.Label(root, text='Face Value :                               ')
label4.config(font=('helvetica', 10))
canvas1.create_window(160, 220, window=label4)

label5 = tk.Label(root, text='Coupon Rate :                             ')
label5.config(font=('helvetica', 10))
canvas1.create_window(160, 260, window=label5)

label6 = tk.Label(root, text='Macaulay Duration :        ')
label6.config(font=('helvetica', 10))
canvas1.create_window(80, 380, window=label6)

label7 = tk.Label(root, text='Modified Duration :        ')
label7.config(font=('helvetica', 10))
canvas1.create_window(80, 420, window=label7)

def calcBondPrice ():  
    m = float(entry1.get())
    t = float(entry2.get())
    ytm = float(entry3.get())/100
    fv = float(entry4.get())
    c = float(entry5.get())/100
    
    pv = ((fv*c/m*(1-(1+ytm/m)**(-m*t)))/(ytm/m)) + fv*(1+(ytm/m))**(-m*t)
    final_year = (t*fv)/(pv*(1+(ytm/m))**(m*t))
    
    sum = 0
    x = 1

    while x <= m*t:
        tn = x/m
        x = x + 1
        dur = (fv*c*tn)/(pv*m*(1+(ytm/m))**(m*tn))
        sum = sum + dur
    
    #macaulayDuration
    label8 = tk.Label(root, text= sum+final_year,font=('helvetica', 10, 'bold'),bg='white')
    canvas1.create_window(250, 300, window=label8)
     
    #modifiedDuration
    label9 = tk.Label(root, text= (sum+final_year)/(1+ytm/m),font=('helvetica', 10, 'bold'),bg='white')
    canvas1.create_window(240, 420, window=label9)
        
button1 = tk.Button(text='Calculate Bond Duration', command=calcBondPrice, bg='white', fg='black', font=('helvetica', 9, 'bold'))
canvas1.create_window(240, 330, window=button1)

root.mainloop()
