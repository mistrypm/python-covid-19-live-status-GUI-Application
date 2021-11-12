# ===================================================== Importing libraries ===============================================
import covid                               # pip install covid
import tkinter as tk
import matplotlib.pyplot as plt            # pip install matplotlib
import pandas as pd                        # pip install pandas

#======================================================== End ===============================================================

# ===================================================== defining function that generate status =======================================
def show_data():
    data = covid.Covid()
    patient_name = e1.get()
    status = data.get_status_by_patient_name(patient_name)
    vaccinated = status['vaccinated']
    e2.insert(0,list_of_doses_received)
    partiallyvaccinated = status['partiallyvaccinated']
    e3.insert(0, vaccine_name_with_dose_number)
    notvaccinated = status['not vaccinated']
    e4.insert(0, need_vaccine)
    print(status)
    # intialise data of lists.
    data = {'id': status['id'],
            'patient_name': status['patient_name'],
            'vaccinated': status['receviedbooster'],
            'partiallyvaccinated': status['partiallyvaccinated'],
            'notvaccinated': status['notvaccinated'],
            'Latitude': status['latitude'],
            'Longitude': status['longitude'],
            'Last_Updated': status['last_update']
            }

    # Create DataFrame
    df = pd.DataFrame(data, index=[0])

    # Print the output.
    print(df)
    cadr = {

        key:status[key]
        for key in status.keys() & {"received booster","partially vaccinated","not vaccinated"}
    }
    n = list(cadr.keys())
    v = list(cadr.values())
    plt.title("patient name")
    plt.bar(range(len(cadr)),v,tick_label=n,label=('recevied booster'))
    plt.xlabel('x-labels')
    plt.ylabel('data')

    plt.plot(range(len(cadr)))


    plt.show()

#============================================================== End ======================================================


# ================================================= Window Design =========================================================
master = tk.Tk()
master.title('Covid-19 vaccine status ')

tk.Label(master,text="COVID-19 VACCINE STATUS" ,padx=50).grid(row=0)

tk.Label(master, text="Enter patient's first name : -").grid(row=2)

e1 = tk.Entry(master)
e1.grid(row=2, column=3)

tk.Label(master, text="Enter patient's last name : -").grid(row=3)

e1 = tk.Entry(master)

e1.grid(row=3, column=3)

tk.Label(master, text="Enter patient's date of Birth : -").grid(row=4)

e1 = tk.Entry(master)

e1.grid(row=4, column=3)

tk.Label(master, text="Enter patient's MRN : -").grid(row=5)

e1 = tk.Entry(master)

e1.grid(row=5, column=3)
tk.Button(master,
          text='Show', command=show_data).grid(row=7,
                                                       column=3,
                                                       sticky=tk.W,
                                                       pady=4)


tk.Label(master, text="vaccinated : -").grid(row=10)

e2 = tk.Entry(master)
e2.grid(row=10, column=3)

tk.Label(master, text="partially vaccinated : -").grid(row=11)
e3 = tk.Entry(master)
e3.grid(row=11, column=3)

tk.Label(master, text="not vaccinated : -").grid(row=12)
e4 = tk.Entry(master)
e4.grid(row=12, column=3)

master.mainloop()

#================================================================== End =====================================================

