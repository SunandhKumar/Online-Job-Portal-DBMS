from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root=Tk()
root.title("Online Job Portal")
root.geometry("600x250")

#jobWin  window
jobWin=Tk()
jobWin.title("JOBSEEKER")
jobWin.geometry('600x600')
jobWin.withdraw()

#recWin  window
recWin=Tk()
recWin.title("RECRUITER")
recWin.geometry('500x400')
recWin.withdraw()


#DATABASE CREATION
conn=sqlite3.connect("job_portal.db")

c=conn.cursor()
#TABLE
#
# CREATION
'''
c.execute("""CREATE TABLE t3(
        f_name text,
        l_name text,
        mail_id text,
        phone_no integer,
        country text,
        state text,
        education text,
        comp_name text,
        jsjobid text,
        prgm_lang text,
        skills text,
        yofexp integer
        )""")
c.execute("""CREATE TABLE tr4(
        rcomp_name text,
        salary integer,
        position text,
        plc_of_wrk text,
        main_dom text,
        skills_req text,
        ryofexp integer,
        jobid text
       )""")
'''
#jobseek function
def jobseek():
    jobWin.deiconify()
    root.withdraw()
#recruit function
def recruit():
    recWin.deiconify()
    root.withdraw()

#jsubmit function
def jsubmit():
    conn = sqlite3.connect("job_portal.db")

    c = conn.cursor()

    c.execute("INSERT INTO t3 VALUES(:f_name, :l_name, :mail_id, :phone_no, :country, :state, :education, :comp_name, :jsjobid, :prgm_lang, :skills, :yofexp)",
              {
                "f_name":f_name.get(),
                "l_name":l_name.get(),
                "mail_id":mail_id.get(),
                "phone_no":phone_no.get(),
                "country":country.get(),
                "state":state.get(),
                "education":education.get(),
                "comp_name":comp_name.get(),
                "jsjobid":jsjobid.get(),
                "prgm_lang":prgm_lang.get(),
                "skills":skills.get(),
                "yofexp":yofexp.get()
            })

    conn.commit()
    conn.close()

    f_name.delete(0,END)
    l_name.delete(0,END)
    mail_id.delete(0,END)
    phone_no.delete(0,END)
    country.delete(0,END)
    state.delete(0, END)
    education.delete(0, END)
    comp_name.delete(0, END)
    jsjobid.delete(0,END)
    prgm_lang.delete(0, END)
    skills.delete(0, END)
    yofexp.delete(0, END)

    reg=Tk()
    reg.title("Registered")
    reg.geometry('300x100')

    reg_label=Label(reg,text="\n\tRegistered Successfully")
    reg_label.grid(row=0,column=0)
    reg_label.config(anchor=CENTER)

    reg.mainloop()

def jback():
    root.deiconify()
    jobWin.withdraw()


def rback():
    root.deiconify()
    recWin.withdraw()

#rsubmit function
def rsubmit():
    conn = sqlite3.connect("job_portal.db")

    c = conn.cursor()

    rjob_id=""
    a=str(rcomp_name.get()).split()
    b=str(position.get()).split()
    for x in a:
        rjob_id+=x[0].upper()
    for x in b:
        rjob_id+=x[0].upper()

    c.execute("INSERT INTO tr4 VALUES(:rcomp_name, :salary, :position, :plc_of_wrk, :main_dom, :skills_req, :ryofexp, :jobid)",{
        "rcomp_name":rcomp_name.get(),
        "salary":salary.get(),
        "position":position.get(),
        "plc_of_wrk":plc_of_wrk.get(),
        "main_dom":main_dom.get(),
        "skills_req":skills_req.get(),
        "ryofexp":ryofexp.get(),
        "jobid":rjob_id
    })

    jid = Tk()
    jid.title("Registered")
    jid.geometry('300x100')

    jid_label = Label(jid, text="\n\tJOB ID " + rjob_id)
    jid_label.grid(row=0, column=0)
    jid_label.config(anchor=CENTER)

    jid.mainloop()

    conn.commit()
    conn.close()

    rcomp_name.delete(0,END)
    salary.delete(0, END)
    position.delete(0, END)
    plc_of_wrk.delete(0, END)
    main_dom.delete(0, END)
    skills_req.delete(0, END)
    ryofexp.delete(0, END)

#jobs avaliable function
def joff_aval():

    jobs_aval=Tk()
    jobs_aval.title("JOB OFFERS AVALIABLE")
    jobs_aval.geometry('900x400')

    conn = sqlite3.connect("job_portal.db")
    c = conn.cursor()

    c.execute("SELECT * FROM tr4")
    records=c.fetchall()

    label1=Label(jobs_aval,text="\nJOBS AVALIABLE\n",font=50)
    label1.grid(row=0,column=0,padx=5)

    label2=Label(jobs_aval,text="Company Name")
    label2.grid(row=2,column=0,padx=5)

    label3 = Label(jobs_aval, text="Salary")
    label3.grid(row=2, column=1,padx=5)

    label4 = Label(jobs_aval, text="position")
    label4.grid(row=2, column=2,padx=5)

    label5 = Label(jobs_aval, text="Place of Work")
    label5.grid(row=2, column=3, padx=5)

    label6 = Label(jobs_aval, text="Main-Domain")
    label6.grid(row=2, column=4, padx=5)

    label7 = Label(jobs_aval, text="Skill needed")
    label7.grid(row=2, column=5, padx=5)

    label8 = Label(jobs_aval, text="Years of experience")
    label8.grid(row=2, column=6, padx=5)

    label8 = Label(jobs_aval, text="Reference ID")
    label8.grid(row=2, column=7, padx=5)

    val=3
    for x in records:
        label1 = Label(jobs_aval, text=str(x[0]))
        label1.grid(row=val, column=0,padx=5)

        label2 = Label(jobs_aval, text=str(x[1]))
        label2.grid(row=val, column=1,padx=5)

        label3 = Label(jobs_aval, text=str(x[2]))
        label3.grid(row=val, column=2,padx=5)

        label4 = Label(jobs_aval, text=str(x[3]))
        label4.grid(row=val, column=3, padx=5)

        label5 = Label(jobs_aval, text=str(x[4]))
        label5.grid(row=val, column=4, padx=5)

        label6 = Label(jobs_aval, text=str(x[5]))
        label6.grid(row=val, column=5, padx=5)

        label7 = Label(jobs_aval, text=str(x[6]))
        label7.grid(row=val, column=6, padx=5)

        label8 = Label(jobs_aval, text=str(x[7]))
        label8.grid(row=val, column=7, padx=5)

        val+=1


    conn.commit()
    conn.close()

    jobs_aval.mainloop()

#registered application
def rappl():
    appl_reg = Tk()
    appl_reg.title("APPLICATIONS")
    appl_reg.geometry('900x400')

    conn = sqlite3.connect("job_portal.db")
    c = conn.cursor()

    c.execute("SELECT * FROM t3 WHERE jsjobid='"+search.get()+"'")
    records = c.fetchall()

    label1 = Label(appl_reg, text="\nREGISTERED APPLICATIONS:\n")
    label1.grid(row=0, column=4, padx=5)

    label2 = Label(appl_reg, text="Name")
    label2.grid(row=2, column=0, padx=5)

    label3 = Label(appl_reg, text="Mail-ID")
    label3.grid(row=2, column=1, padx=5)

    label4 = Label(appl_reg, text="Contact")
    label4.grid(row=2, column=2, padx=5)

    label5 = Label(appl_reg, text="Education")
    label5.grid(row=2, column=3, padx=5)

    label6 = Label(appl_reg, text="Programming Languages")
    label6.grid(row=2, column=4, padx=5)

    label7 = Label(appl_reg, text="Skills")
    label7.grid(row=2, column=5, padx=5)

    label8 = Label(appl_reg, text="Years of experience")
    label8.grid(row=2, column=6, padx=5)

    label9 = Label(appl_reg, text="Reference ID")
    label9.grid(row=2, column=7, padx=5)

    val = 3
    for x in records:
        label1 = Label(appl_reg, text=str(x[0])+" "+str(x[1]))
        label1.grid(row=val, column=0, padx=5)

        label2 = Label(appl_reg, text=str(x[2]))
        label2.grid(row=val, column=1, padx=5)

        label3 = Label(appl_reg, text=str(x[3]))
        label3.grid(row=val, column=2, padx=5)

        label4 = Label(appl_reg, text=str(x[6]))
        label4.grid(row=val, column=3, padx=5)

        label5 = Label(appl_reg, text=str(x[9]))
        label5.grid(row=val, column=4, padx=5)

        label6 = Label(appl_reg, text=str(x[10]))
        label6.grid(row=val, column=5, padx=5)

        label7 = Label(appl_reg, text=str(x[11]))
        label7.grid(row=val, column=6, padx=5)

        label8 = Label(appl_reg, text=str(x[8]))
        label8.grid(row=val, column=7, padx=5)

        val += 1

    conn.commit()
    conn.close()

    appl_reg.mainloop()

#create jdelete function
def jdelete():
    conn = sqlite3.connect('fuhrer_database.db')

    c = conn.cursor()

    c.execute("DELETE FROM addresse WHERE mail_id='"+jdel.get()+"'")

    conn.commit()

    conn.close()

def des_all():
    root.destroy()
    recWin.destroy()
    jobWin.destroy()

#root window widgets
desc_label=Label(root,text="SELECT THE REQUIRED FIELD",font=50)
desc_label.grid(row=0,column=0,padx=50,pady=50)

jobWin_btn=Button(root,text="JOBSEEKER",command=jobseek)
jobWin_btn.grid(row=1,column=0,padx=200,pady=5,ipadx=50)

recWin_btn=Button(root,text="RECRUITER",command=recruit)
recWin_btn.grid(row=2,column=0,padx=50,pady=10,ipadx=50)


des_all_btn=Button(root,text="EXIT",command=des_all)
des_all_btn.grid(row=3,column=0,padx=50,pady=10,ipadx=25)

#jobWin window widgets

f_name_label=Label(jobWin,text="First Name")
f_name_label.grid(row=0,column=1,padx=10,pady=5)
f_name=Entry(jobWin,width=30)
f_name.grid(row=0,column=2,padx=5,pady=5)

l_name_label=Label(jobWin,text="Last Name")
l_name_label.grid(row=1,column=1,padx=10,pady=5)
l_name=Entry(jobWin,width=30)
l_name.grid(row=1,column=2,padx=5,pady=5)

mail_id_label=Label(jobWin,text="EMAIL_ID")
mail_id_label.grid(row=2,column=1,padx=10,pady=5)
mail_id=Entry(jobWin,width=30)
mail_id.grid(row=2,column=2,padx=5,pady=5)

phone_no_label=Label(jobWin,text="Phone Number")
phone_no_label.grid(row=3,column=1,padx=10,pady=5)
phone_no=Entry(jobWin,width=30)
phone_no.grid(row=3,column=2,padx=5,pady=5)

country_label=Label(jobWin,text="Country")
country_label.grid(row=4,column=1,padx=10,pady=5)
country=Entry(jobWin,width=30)
country.grid(row=4,column=2,padx=5,pady=5)

state_label=Label(jobWin,text="State")
state_label.grid(row=5,column=1,padx=10,pady=5)
state=Entry(jobWin,width=30)
state.grid(row=5,column=2,padx=5,pady=5)

education_label=Label(jobWin,text="Highest Education Level")
education_label.grid(row=6,column=1,padx=10,pady=5)
education=Entry(jobWin,width=30)
education.grid(row=6,column=2,padx=5,pady=5)

comp_name_label=Label(jobWin,text="Company Name")
comp_name_label.grid(row=7,column=1,padx=10,pady=5)
comp_name=Entry(jobWin,width=30)
comp_name.grid(row=7,column=2,padx=5,pady=5)

jsjobid_label=Label(jobWin,text="JOB-ID")
jsjobid_label.grid(row=8,column=1,padx=10,pady=5)
jsjobid=Entry(jobWin,width=30)
jsjobid.grid(row=8,column=2,padx=5,pady=5)

prgm_lang_label=Label(jobWin,text="Programming Languages Known")
prgm_lang_label.grid(row=9,column=1,padx=10,pady=5)
prgm_lang=Entry(jobWin,width=30)
prgm_lang.grid(row=9,column=2,padx=5,pady=5)

skills_label=Label(jobWin,text="Skills")
skills_label.grid(row=10,column=1,padx=10,pady=5)
skills=Entry(jobWin,width=30)
skills.grid(row=10,column=2,padx=5,pady=5)

yofexp_label=Label(jobWin,text="Years of Experience")
yofexp_label.grid(row=11,column=1,padx=10,pady=5)
yofexp=Entry(jobWin,width=30)
yofexp.grid(row=11,column=2,padx=5,pady=5)

jsub_btn=Button(jobWin,text="SUBMIT",command=jsubmit)
jsub_btn.grid(row=12,column=2,padx=10,pady=5,ipadx=25)

joff_aval_button=Button(jobWin,text="Job Offers AVAILABLE",command=joff_aval)
joff_aval_button.grid(row=13,column=2,padx=10,pady=5,ipadx=30)

jdel_label=Label(jobWin,text="MAIL_ID")
jdel_label.grid(row=14,column=1,padx=10,pady=5)
jdel=Entry(jobWin,width=30)
jdel.grid(row=14,column=2,padx=5,pady=5)

jdel_btn=Button(jobWin,text="DELETE APPLICATION",command=jsubmit)
jdel_btn.grid(row=14,column=3,padx=10,pady=5,ipadx=20)

jback_btn=Button(jobWin,text="Back",command=jback)
jback_btn.grid(row=15,column=2,ipadx=10)
#recWin window widgets

rcomp_name_label=Label(recWin,text="Company Name")
rcomp_name_label.grid(row=0,column=1,padx=10,pady=5)
rcomp_name=Entry(recWin,width=30)
rcomp_name.grid(row=0,column=2,padx=5,pady=5)

salary_label=Label(recWin,text="Salary")
salary_label.grid(row=1,column=1,padx=10,pady=5)
salary=Entry(recWin,width=30)
salary.grid(row=1,column=2,padx=5,pady=5)

position_label=Label(recWin,text="Position")
position_label.grid(row=2,column=1,padx=10,pady=5)
position=Entry(recWin,width=30)
position.grid(row=2,column=2,padx=5,pady=5)

plc_of_wrk_label=Label(recWin,text="Place of Work")
plc_of_wrk_label.grid(row=3,column=1,padx=10,pady=5)
plc_of_wrk=Entry(recWin,width=30)
plc_of_wrk.grid(row=3,column=2,padx=5,pady=5)

main_dom_label=Label(recWin,text="Main Domain")
main_dom_label.grid(row=4,column=1,padx=10,pady=5)
main_dom=Entry(recWin,width=30)
main_dom.grid(row=4,column=2,padx=5,pady=5)


skills_req_label=Label(recWin,text="Skills Required")
skills_req_label.grid(row=5,column=1,padx=10,pady=5)
skills_req=Entry(recWin,width=30)
skills_req.grid(row=5,column=2,padx=5,pady=5)

ryofexp_label=Label(recWin,text="years of experience")
ryofexp_label.grid(row=6,column=1,padx=10,pady=5)
ryofexp=Entry(recWin,width=30)
ryofexp.grid(row=6,column=2,padx=5,pady=5)

rsub_btn=Button(recWin,text="SUBMIT",command=rsubmit)
rsub_btn.grid(row=7,column=2,padx=10,pady=5,ipadx=25)

search_label=Label(recWin,text="Applications")
search_label.grid(row=8,column=1,padx=10,pady=5)
search=Entry(recWin,width=30)
search.grid(row=8,column=2,padx=5,pady=5)

appl_btn=Button(recWin,text="Applications",command=rappl)
appl_btn.grid(row=8,column=3,padx=10,pady=5,ipadx=25)

rback_btn=Button(recWin,text="Back",command=rback)
rback_btn.grid(row=9,column=2,ipadx=10)


conn.commit()
conn.close()

root.mainloop()

jobWin.mainloop()

recWin.mainloop()