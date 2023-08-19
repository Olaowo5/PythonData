#Project 4  
#Name: Olamide Owolabi
#Date: 12th June-2023
#Section: 23S_CST8333_360
#Declaration:
#This is my own original work and is free from Plagiarism.
#Welcome to my Python Project
import pandas as pd # to handle the data read
#Name Olamide Owolabi

import threading # to allow for MultiThreading
from NewRecord import * # to access the New DTOs
import tkinter as tk #to handle the gui
import matplotlib as mp
import numpy as np

from tkinter import ttk # GUI continued for creating frames
from tkinter import messagebox # Creating Alert boxes
from tkinter import simpledialog #For Popup message

import pickle as pick #Used in save and reload files

import matplotlib.pyplot as plt

import csv


#The View Prsentation Layer
#Responsible for the visual representation and GUI
class View:
    def __init__(self, root): 
        self.root = root
        self.root.title("Olamide Owolabi")
        self.Model = None

        self.table_frame = None 
        #Name Olamide Owolabi
        self.ColumnName =['Condi','Ref_Date','Geo','DGUID','Type of Product',
                'Type of Storage', 'UOM','UOM_ID',
                'SCALAR_FACTOR','SCALAR_ID','VECTOR',
                'Cooridnate','Value','Status',
                'Symbol','Terminated','Decimals']

        self.table = ttk.Treeview(self.table_frame, columns=self.ColumnName, show="headings")

    #To assign the Model to the view    
    def setModal(self,Model):
        self.Model = Model

    #Load the frame
    def LoadTableFrame(self):
        #Create table frame
         #self.table_frame  # Declare table_frame as a global variable
    
         self.table_frame = tk.Frame(self.root)
         self.table_frame.pack()
 
   

        # Create a scrollbar
         self.scrollbar = tk.Scrollbar(self.table_frame)
         self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        #create second scrollbar
         self.scrollbarx = tk.Scrollbar(self.table_frame,orient='horizontal')
         self.scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)

         # Create a table
           #global table
         self.table = ttk.Treeview(self.table_frame,
                        yscrollcommand=self.scrollbar.set, 
                        xscrollcommand=self.scrollbarx.set)


        # Configure the scrollbar to scroll the table
         self.scrollbar.config(command=self.table.yview)
         self.scrollbarx.config(command=self.table.xview)

    #Name: Olamide Owolabi
 #This funnction is to prepare the data to be entered in a table
    def EnterData_In_Table(self, tabled):
        self.table['columns'] = self.ColumnName
        # Configure the column Names    
        for column in self.ColumnName:     
            #self.table.heading(column, text=column)   
            self.table.heading(column, text=column,  #Name: Olamide Owolabi
                               command=lambda c=column: self.Model.on_sort_column(c))
            self.table.column(column, width=100)          

        # Insert the updated data rows
        for index, row in enumerate(tabled):
            self.table.insert(parent='', index='end', iid=index, text='', values=(row.Statola, row.Ref, row.Geo, row.DGUID, row.ToProduct,
                row.ToStorage, row.UOM, row.UOM_ID, row.SCALAR_FACTOR, row.SCALAR_ID,
                row.VECTOR, row.COORD, row.VALUE, row.STATUS, row.SYMBOL, row.TERMINATED, row.DECIMALS))


    def LoadTableo(self, tabled):
        self.ClearTable()  # Remove table to prevent duplicates
        self.LoadTableFrame()  # Load a new table frame

        #Name Olamide Owolabi
        # Create a new thread for loading the table data
       #table_data_thread = threading.Thread(target=self.EnterData_In_Table, args=(tabled,))
        #table_data_thread.start()
        self.EnterData_In_Table(tabled)
        # Wait for the thread to finish
        #table_data_thread.join()

        # Pack the table after the thread has finished loading the data
        self.table.pack()
        
    def LoadListbox(self, tD):
        #tabled.head()
        popup = tk.Toplevel(self.root)
        popup.title("ListBox Ola")
        #dataset = pd.DataFrame(tabled)
       
      


        fieldnames =   list(vars(tD[0]).keys())
        combo_var = tk.StringVar()
        combo = ttk.Combobox(popup, textvariable=combo_var, values=list(fieldnames))
       # combo = ttk.Combobox(popup, textvariable=combo_var, values=list(df.columns))
        combo.set(list(fieldnames)[0])  # Set default value to the first column
        combo.pack(padx=30, pady=50)
        
        
        plot_button = tk.Button(popup, text="Plot Graph", command=lambda: self.Model.plot_graph(tD, combo_var.get()))
        plot_button.pack(pady=5)

        plot_pie = tk.Button(popup, text="Plot Pie", command=lambda: self.Model.plot_graph_pie(tD, combo_var.get()))
        plot_pie.pack(pady=5)
    
    #To delete table
    def ClearTable(self):
         
         try:
              if(self.table_frame is not None):
                   #making sure we have a table frame
                   
                   #delete the table frame
                   self.table_frame.destroy()

                   self.table_frame = None

         except AttributeError:
              self.view.MessageWarn("Error: table frame is not available")

    #To display the form that will be used in adding a 
    # a New record 
    def display_form(self):
        #Assign form
        self.form = tk.Toplevel()
        self.form.title("Add new record, Olamide Owolabi")
        self.form.config(bg="skyblue")
        #Name: Olamide Owolabi
        # Add form fields and widgets here
        #color for the background and Foreground
        bgc ="#F2F2F2"
        fgc="#333333"

        bge="#FFFFFF"
        fge="#333333"
     
        # Following are list of labels ad entry
        # Next will use a for loop
        # Next time
        #Ref_Date
        self.Ref_label = tk.Label(self.form, text="Ref_Date:",bg=bgc,fg=fgc)
        self.Ref_label.pack()
        self.Ref_entry = tk.Entry(self.form,bg=bge,fg=fge,relief="solid",bd=1)
        self.Ref_entry.pack()

        #Name: Olamide Owolabi
        #Geo
        self.geo_label = tk.Label(self.form, text="Geo:",bg=bgc,fg=fgc)
        self.geo_label.pack()
        self.geo_entry = tk.Entry(self.form,bg=bge,fg=fge,relief="solid",bd=1)
        self.geo_entry.pack()
    

        #Dguid
        self.dguid_label = tk.Label(self.form, text="DGUID",bg=bgc,fg=fgc)
        self.dguid_label.pack()
        self.dguid_entry = tk.Entry(self.form,bg=bge,fg=fge,relief="solid",bd=1)
        self.dguid_entry.pack()
        
        #Type of Prdocut
        self.top_label = tk.Label(self.form, text="Type Of Product",bg=bgc,fg=fgc)
        self.top_label.pack()
        self.top_entry = tk.Entry(self.form,bg=bge,fg=fge,relief="solid",bd=1)
        self.top_entry.pack()
        

        #Type of Storage
        self.tos_label = tk.Label(self.form, text="Type Of Storage",bg=bgc,fg=fgc)
        self.tos_label.pack()
        self.tos_entry = tk.Entry(self.form,bg=bge,fg=fge,relief="solid",bd=1)
        self.tos_entry.pack()
        

        #UOM
        self.uom_label = tk.Label(self.form, text="UOM",bg=bgc,fg=fgc)
        self.uom_label.pack()
        self.uom_entry = tk.Entry(self.form,bg=bge,fg=fge,relief="solid",bd=1)
        self.uom_entry.pack()
        

        #UOM_ID
        self.uomid_label = tk.Label(self.form, text="Uom_Id",bg=bgc,fg=fgc)
        self.uomid_label.pack()
        self.uomid_entry = tk.Entry(self.form,bg=bge,fg=fge,relief="solid",bd=1)
        self.uomid_entry.pack()
        

        # Scalar factor
        self.scaf_label = tk.Label(self.form, text="Scalar Factor",bg=bgc,fg=fgc)
        self.scaf_label.pack()
        self.scaf_entry = tk.Entry(self.form,bg=bge,fg=fge,relief="solid",bd=1)
        self.scaf_entry.pack()
        

        #Scalar Id
        self.scaid_label = tk.Label(self.form, text="Scalar_Id",bg=bgc,fg=fgc)
        self.scaid_label.pack()
        self.scaid_entry = tk.Entry(self.form,bg=bge,fg=fge,relief="solid",bd=1)
        self.scaid_entry.pack()
        

        #Vector
        self.vec_label = tk.Label(self.form, text="Vector",bg=bgc,fg=fgc)
        self.vec_label.pack()
        self.vec_entry = tk.Entry(self.form,bg=bge,fg=fge,relief="solid",bd=1)
        self.vec_entry.pack()
        

        #Coordinate
        self.coo_label = tk.Label(self.form, text="Coordinate",bg=bgc,fg=fgc)
        self.coo_label.pack()
        self.coo_entry = tk.Entry(self.form,bg=bge,fg=fge,relief="solid",bd=1)
        self.coo_entry.pack()
        

        #Value
        self.val_label = tk.Label(self.form, text="Value",bg=bgc,fg=fgc)
        self.val_label.pack()
        self.val_entry = tk.Entry(self.form,bg=bge,fg=fge,relief="solid",bd=1)
        self.val_entry.pack()
        

        #Status
        self.stat_label = tk.Label(self.form, text="Status",bg=bgc,fg=fgc)
        self.stat_label.pack()
        self.stat_entry = tk.Entry(self.form,bg=bge,fg=fge,relief="solid",bd=1)
        self.stat_entry.pack()
        

        #Symbol
        self.sym_label = tk.Label(self.form, text="Symbol",bg=bgc,fg=fgc)
        self.sym_label.pack()
        self.sym_entry = tk.Entry(self.form,bg=bge,fg=fge,relief="solid",bd=1)
        self.sym_entry.pack()
        

        #Terminated
        self.term_label = tk.Label(self.form, text="Terminated",bg=bgc,fg=fgc)
        self.term_label.pack()
        self.term_entry = tk.Entry(self.form,bg=bge,fg=fge,relief="solid",bd=1)
        self.term_entry.pack()
        

        #Decimals
        self.dec_label = tk.Label(self.form, text="Decimal",bg=bgc,fg=fgc)
        self.dec_label.pack()
        self.dec_entry = tk.Entry(self.form,bg=bge,fg=fge,relief="solid",bd=1)
        self.dec_entry.pack()
        
        #the function that will be used in submitting a new entry
        #
        def submit_entry():
            # Retrieve the values from the entry widgets
            Value1 = self.Ref_entry.get()
            Value2 = self.geo_entry.get()
            Value3 = self.dguid_entry.get()
            Value4 = self.top_entry.get()
            Value5 = self.tos_entry.get()
            Value6 = self.uom_entry.get()
            Value7 = self.uomid_entry.get()
            Value8 = self.scaf_entry.get()
            Value9 = self.scaid_entry.get()
            Value10 = self.vec_entry.get()
            Value11 = self.coo_entry.get()
            Value12 = self.val_entry.get()
            Value13 = self.stat_entry.get()
            Value14 = self.sym_entry.get()
            Value15 = self.term_entry.get()
            Value16 = self.dec_entry.get()

        

            #Name: Olamide Owolabi
            NewRecord = AddDTO(Value1,Value2,Value3,Value4,Value5,Value6,Value7,Value8,
                            Value9,Value10,Value11,Value12,Value13,
                        Value14,Value15,Value16)
            
            self.Model.AddNewRecord(NewRecord) #add th new record to the Model class
            self.form.destroy() #to close form on submission
        

        #SPawn a button to call the submit_entry function
        self.submit_button = tk.Button(self.form,text="Submit Entry",
                                command= submit_entry)
        self.submit_button.pack()
        # Example: Button to close the form
        # To create a button to close the form
        self.close_button = tk.Button(self.form, text="Close", command=self.form.destroy)
        self.close_button.pack()
    
    #The function to get the frame from the view class
    def GetFrame(self):
        return self.table_frame
    
    #to get the column headers used in view class
    def GetColumn(self):
        return  self.ColumnName
    
    #To reload the table with the inserted data
    def LoadTableQuick(self,intd,row):
         self.table.insert(parent='', index='end', iid=intd, text='', values=(row.Statola, row.Ref, row.Geo, row.DGUID, row.ToProduct,
                            row.ToStorage, row.UOM, row.UOM_ID,
                            row.SCALAR_FACTOR, row.SCALAR_ID,
                            row.VECTOR, row.COORD, row.VALUE, row.STATUS,
                            row.SYMBOL, row.TERMINATED, row.DECIMALS,))
         self.table.pack()

   
    #to create an warning message
    def MessageWarn(self,msg): #Name Olamide Owolabi
        messagebox.showwarning("Warning", msg)
    
    # To create notification message
    def MessageAction(self,msg):
        messagebox.showinfo("Action Done", msg)
    # To change the background color
    def change_color(self, widget, color):
        widget.config(bg=color)

        # To change the forground color
    def change_colorii(self, widget, color):
        widget.config(fg=color)
  

    
#Model
#Handles the data in the project
#and relays the information to the view
# 
class Model:
     def __init__(self,View):
          #Name: Olamide Owolabi
          self.view = View
          self.table_data = [] #a list to hold the data records used
          self.TheRecord = [] # temp array to hold data from csv


      #to print a column
      # just for polymorphism only   
      # Name: Olamide Owolabi  
     def print_statola_info(self,dto):
        dto.print_statola()

     # To load the data from the csv file
     # and display it to a table
     def LoadData(self):
        
        try:
            #first read the csv file attached
            data = pd.read_csv('32100260.csv')  #Name: Olamide Owolabi 
            #Name: Olamide Owolabi 
        except FileNotFoundError: 
            print("Error: File not found. Check File Path.")
        except pd.errors.ParserError:
            print("Error: Unable to parse the dataset. Please check the file .")
        except Exception as e:
            print("An error occurred:", str(e))
        
          #Create DTOs for each row in the dataset/csv
        #and fill em
        # Add the new DTOs into the TheRecord Array
        for index, row in data.iterrows():
            ref_date = row['REF_DATE']
            geo	= row['GEO']  #Name: Olamide Owolabi
            dguid = row['DGUID']
            top =row['Type of product']
            toc	=row['Type of storage']
            uom	= row['UOM']
            uom_id	= row['UOM_ID']
            scalar_factor = row['SCALAR_FACTOR']
            scalar_id	= row['SCALAR_ID']
            vector	= row['VECTOR']
            coordinate	= row['COORDINATE']
            value	= row['VALUE']
            status	=row ['STATUS']
            symbol	= row['SYMBOL']
            terminated	= row['TERMINATED']
            decimals = row['DECIMALS']  #Name: Olamide Owolabi
            NewRecord = LoadDto(ref_date,geo,dguid,top,toc,uom,uom_id,scalar_factor,
                            scalar_id,vector,coordinate,value,status,
                            symbol,terminated,decimals)
            self.TheRecord.append(NewRecord)
        #Print info from LoadData
        #Name: Olamide
        self.print_statola_info(self.TheRecord[0])
        self.table_data.clear() #clear table so we can load new from scratch

        #Only get the first 120 records from the data csv
        # and display them
        for indx in self.TheRecord[:120]:
            self.table_data.append(indx)

        #Name: Olamide Owolabi 
        # Load the table from the View class
        self.view.LoadTableo(self.table_data)
        
     
    #to add a new record to the table
     def AddNewRecord(self, recordValue):
        #the new record   
        NewRecord = recordValue
        # Add the new record to 
        self.table_data.append(NewRecord)

        intd = len(self.table_data)

        row = NewRecord

        self.print_statola_info(NewRecord)

       # messagebox.showinfo("Action Done", "Record added" + row.Ref +" "+ str(intd))
        #global table_frame
        #create a new frame if its doesnt exist
        if self.view.GetFrame() is None:
            self.view.LoadTableo(self.table_data) #Load table for application
        else:
            #global table
            #add the new record to existing table
           self.view.LoadTableQuick(intd,row)
        
        #To create the notification box
        new = "Record added"  +" "+ str(intd)
        self.view.MessageAction(new)
       
    #To delete a selected record
     def delete_record(self):
         #Name: Olamide Owolabi
        selected_row = self.view.table.focus()
        if selected_row:
            #item = table.item(selected_row)
            record_index = int(selected_row)  # Assuming the first column contains the index

            # Delete the record from the table data
            del self.table_data[record_index]
            
            self.view.MessageAction("Record deleted successfully")
            #Clear the table so it can be reloaded
            self.view.ClearTable()
            #Load a new table with the updated Data
            self.view.LoadTableo(self.table_data)
           
        else:
           #show warnig message if called with no row selected
            self.view.MessageWarn("No Record selected")

        
    #To edit a selected record
     def edit_record(self):
        selected_row = self.view.table.focus()
        #Name Olamide Owolabi
        if selected_row:
            #item = table.item(selected_row)
            record_index = int(selected_row)  # Assuming the first column contains the index
            #Name Olamide Owolabi
            # Get the record data
            record = self.table_data[record_index]

            # Open the form to edit the record
            form = tk.Toplevel()
            form.title("Edit Record, Olamide Owolabi")
            
            Ref_label = tk.Label(form, text="Ref_Date:")
            Ref_label.pack()
            Ref_entry = tk.Entry(form)
            Ref_entry.insert(tk.END, record.Ref)
            Ref_entry.pack()

            geo_label = tk.Label(form, text="Geo:")
            geo_label.pack()
            geo_entry = tk.Entry(form)
            geo_entry.insert(tk.END, record.Geo)
            geo_entry.pack()

            dguid_label = tk.Label(form, text="DGUID")
            dguid_label.pack()
            dguid_entry = tk.Entry(form)
            dguid_entry.insert(tk.END, record.DGUID)
            dguid_entry.pack()

            top_label = tk.Label(form, text="Type Of Product")
            top_label.pack()
            top_entry = tk.Entry(form)
            top_entry.insert(tk.END, record.ToProduct)
            top_entry.pack()

            tos_label = tk.Label(form, text="Type Of Storage")
            tos_label.pack()
            tos_entry = tk.Entry(form)
            tos_entry.insert(tk.END, record.ToStorage)
            tos_entry.pack()

            #UOM
            uom_label = tk.Label(form, text="UOM")
            uom_label.pack()
            uom_entry = tk.Entry(form)
            uom_entry.insert(tk.END, record.UOM)
            uom_entry.pack()
            

            #UOM_ID
            uomid_label = tk.Label(form, text="Uom_Id")
            uomid_label.pack()
            uomid_entry = tk.Entry(form)
            uomid_entry.insert(tk.END, record.UOM_ID)
            uomid_entry.pack()
            

            # Scalar factor
            scaf_label = tk.Label(form, text="Scalar Factor")
            scaf_label.pack()
            scaf_entry = tk.Entry(form)
            scaf_entry.insert(tk.END, record.SCALAR_FACTOR)
            scaf_entry.pack()
            

            #Scalar Id
            scaid_label = tk.Label(form, text="Scalar_Id")
            scaid_label.pack()
            scaid_entry = tk.Entry(form)
            scaid_entry.insert(tk.END, record.SCALAR_ID)
            scaid_entry.pack()
            

            #Vector
            vec_label = tk.Label(form, text="Vector")
            vec_label.pack()
            vec_entry = tk.Entry(form)
            vec_entry.insert(tk.END, record.VECTOR)
            vec_entry.pack()
            

            #Coordinate
            coo_label = tk.Label(form, text="Coordinate")
            coo_label.pack()
            coo_entry = tk.Entry(form)
            coo_entry.insert(tk.END, record.COORD)
            coo_entry.pack()
            

            #Value
            val_label = tk.Label(form, text="Value")
            val_label.pack()
            val_entry = tk.Entry(form)
            val_entry.insert(tk.END, record.VALUE)
            val_entry.pack()
            

            #Status
            stat_label = tk.Label(form, text="Status")
            stat_label.pack()
            stat_entry = tk.Entry(form)
            stat_entry.insert(tk.END, record.STATUS)
            stat_entry.pack()
            

            #Symbol
            sym_label = tk.Label(form, text="Symbol")
            sym_label.pack()
            sym_entry = tk.Entry(form)
            sym_entry.insert(tk.END, record.SYMBOL)
            sym_entry.pack()
            

            #Terminated
            term_label = tk.Label(form, text="Terminated")
            term_label.pack()
            term_entry = tk.Entry(form)
            term_entry.insert(tk.END, record.TERMINATED)
            term_entry.pack()
            
            #Name Olamide Owolabi
            #Decimals
            dec_label = tk.Label(form, text="Decimal")
            dec_label.pack()
            dec_entry = tk.Entry(form)
            dec_entry.insert(tk.END, record.DECIMALS)
            dec_entry.pack()

            

            # Update the selected record on button submit

            def submit_edit():
                # Update the record with the edited values
                record.Ref = Ref_entry.get()
                record.Geo = geo_entry.get()
                record.DGUID = dguid_entry.get()
                record.ToProduct = top_entry.get()
                record.ToStorage = tos_entry.get()
                record.UOM = uom_entry.get()
                record.UOM_ID = uomid_entry.get()
                record.SCALAR_FACTOR = scaf_entry.get()
                record.SCALAR_ID =scaid_entry.get()
                record.VECTOR = vec_entry.get()
                record.COORD = coo_entry.get()
                record.VALUE = val_entry.get()
                record.STATUS = stat_entry.get()
                record.SYMBOL = sym_entry.get()
                record.TERMINATED = term_entry.get()
                record.DECIMALS = dec_entry.get()
                
                
               # NewRecord = EditDTO(Ref_entry.get(),geo_entry(),dguid_entry(),top_entry(),
                #                    tos_entry.get(),uom_entry.get(),
                 #                   uomid_entry.get(),scaf_entry.get(),
                  #          scaid_entry.get(),vec_entry.get(),coo_entry.get(),val_entry.get(),
                   #         stat_entry.get(),sym_entry.get(),term_entry.get(),dec_entry.get())
                #Name: Olamide Owolabi

                record.Statola = "Editted"

                self.view.MessageAction("Record edited successfully")
                form.destroy()
                self.view.ClearTable()
                self.view.LoadTableo(self.table_data)

            #Create submit button to call submit_edit function
            submit_button = tk.Button(form, text="Submit Edit", command=submit_edit)
            submit_button.pack()
            
            #Create as close button to close the form
            close_button = tk.Button(form, text="Close", command=form.destroy)
            close_button.pack()
        else:
            #create warning alert when no record is selected
            self.view.MessageWarn("No Record Selected")
    
    # to save the current table as a file
    #under the directory saves  name Olamide Owolabi
     def Save_record(self):
        # Open a file in write mode
        if(self.table_data):
   
            with open('Saves/data_Olamide.csv', 'w', newline='') as file:
                writer = csv.writer(file)
              
              #use to get names of headers from list
                fieldnames =   list(vars(self.table_data[0]).keys())

                 #Name: Olamide Owolabi             
                                   
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()  # Write the header row

                
                writer.writerows(vars(rec) for rec in self.table_data)  # Write the data rows
         
            self.view.MessageAction("Record saved")
        else:
           #No frames, alert warning message
           self.view.MessageWarn("No records to Save")

     def List_Box(self):
         # Create a combo box to select the column
         #Name: Olamide Owolabi 
        if self.table_data is None or len(self.table_data) < 1:
            return;
        self.view.LoadListbox(self.table_data)
         

     # to load the savd file and display the data in a table frame
     def Reload_record(self):
            data = []
            try:
                print("Reading CSV file...")
                #Read saved data
                data = pd.read_csv('Saves/data_Olamide.csv')
                print("CSV file reading complete.")
                #Name: Olamide Owolabi
                
            except FileNotFoundError: 
                self.view.MessageWarn("Error: File not found. Check File Path.")
            
            except Exception as e:
                self.view.MessageWarn("An error occurred:", str(e))

            print("check here i.")
         #Create DTOs for each row in the dataset/csv
        #and fill em
        # Add the new DTOs into the TheRecord Array
            for index, row in data.iterrows():
                ref_date = row['Ref']
                geo	= row['Geo']  #Name: Olamide Owolabi
                dguid = row['DGUID']
                top =row['ToProduct']
                toc	=row['ToStorage']
                uom	= row['UOM']
                uom_id	= row['UOM_ID']
                scalar_factor = row['SCALAR_FACTOR']
                scalar_id	= row['SCALAR_ID']
                vector	= row['VECTOR']
                coordinate	= row['COORD']
                value	= row['VALUE']
                status	=row ['STATUS']
                symbol	= row['SYMBOL']
                terminated	= row['TERMINATED']
                decimals = row['DECIMALS']  #Name: Olamide Owolabi
                condi = row['Statola']
                NewRecord = ReloadDTO(ref_date,geo,dguid,top,toc,uom,uom_id,scalar_factor,
                                scalar_id,vector,coordinate,value,status,
                                symbol,terminated,decimals,condi)
                self.TheRecord.append(NewRecord)
            
           
           # load from record
            #Using Mutlithread
            #loadThread = threading.Thread(target=self.reload_tabledata, args=(self.table_data,))
            #clear table so we can load new from scratch
            self.ClearRecord()
            #Name: Olamide Owolabi
            
            for indx in self.TheRecord:
                self.table_data.append(indx)

           
           #call the thread from earlier           
            #loadThread.start()
           #loadThread.join()
            self.reload_tabledata(self.table_data)
        # Function to load the table data in a separate thread
     
     #to sort out the data
     #Name Olamide Owolabi
     def on_sort_column(self,col):
        print("Sort");
        sorted_data = sorted(self.table_data, key=lambda x: x.get_column_value(col))
        self.table_data = sorted_data
        self.view.LoadTableo(sorted_data)
       
     #the function to load the table from the reloaded data
     #will be called by multithreading
     def reload_tabledata(self,table_data):
        self.view.LoadTableo(table_data)
        self.view.MessageAction("Record uploaded")

    #To delete the table (frame)
    #clear the result on the gui
     def ClearRecord(self): #Olamide Owolabi
         self.table_data.clear() #clear the data in memory
         self.view.ClearTable() #drop the table UI

     def CallForm(self):
         self.view.display_form()

       #To plot the bar chart using the dataset and selected column 
     def plot_graph(self,dataset, selected_column):
        
        # Iterate through the rows and match with column heads
       # TestVal = dataset.get_Values(selected_column)
        #print(f"values: {TestVal}")
        # Name: Olamide Owolabi   
        values = [getattr(row, selected_column) for row in dataset]

    
        if all(pd.notna(value) for value in values):

            #Name Olamide Owolabi
            plt.figure(figsize=(8, 6))
            value_counts = pd.Series(values).value_counts() #.plot(kind='bar')
            unique_values = value_counts.index.tolist()

             # Create a colormap with a unique color for each bar
            cmap = plt.get_cmap('tab20')  # Choose a colormap (e.g., 'tab10')
            colors = cmap(np.arange(len(unique_values)))
            TitleName = self.Title_Check(selected_column)    

            # Plot the bar chart with the specified colors
            value_counts.plot(kind='bar', color=colors)
            plt.title(f"Bar Chart of {TitleName} - Olamide Owolabi")
            plt.xlabel(TitleName)
            plt.ylabel("Count")
           
            #Name Olamide Owolabi
            plt.xticks(rotation=45)
            plt.show()
        else:
            print(f"The column '{selected_column}' contains null values and cannot be plotted.")
       

    #To Plot the Pie chart, using the dataset loaded
    # aqnd selected column
     def plot_graph_pie(self,dataset, selected_column):
        #Name Olamide Owolabi
        # Iterate through the rows and match with column heads
       # TestVal = dataset.get_Values(selected_column)
        #print(f"values: {TestVal}")
        
        values = [getattr(row, selected_column) for row in dataset]

       # print(f"values: {values}")

        if all(pd.notna(value) for value in values):
            #Name Olamide Owolabi
             # Continue with plotting the pie chart
            TitleName = self.Title_Check(selected_column)
            value_counts = pd.Series(values).value_counts()
            plt.figure(figsize=(10, 7))
            plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%')
            plt.title(f"Pie chart of {TitleName} - Olamide Owolabi")
            plt.show()
           
 
           
        else:
            print(f"The column '{selected_column}' contains null values and cannot be plotted.")

     def Title_Check(self,columnstr):
         if(columnstr == "ToProduct"):
            return "Type Of Product"
         elif(columnstr == "ToStorage"):
             return "Type Of Storage"
         elif(columnstr == "Ref"):
             return "Ref_Date"
         else:
             return columnstr

    

#The Contoller handles the user inputs and relays to
#the appropriate function in the modal
class Controller:
    def __init__(self, window):
        self.window = window
       # self.Fc = FgCol
       # self.Bc = BgCol
        #LoadData()
        #okay now the gui
        #window = tk.Tk() # the root of the gui window

        #call and assign the view class
        viewer = View(self.window)
        #call and assign the controller class
        Mod = Model(viewer)
        #need to set the controller class to the view 
        viewer.setModal(Mod)

        #assign the frame for the menu buttons
        menu_frame = tk.Frame(self.window)
        menu_frame.pack()

        btn_all = []
        #Button to load the data from the csv file
        btn_load = tk.Button(menu_frame,text="Load Dataset", command=Mod.LoadData)

        btn_load.pack(side=tk.LEFT)
        btn_all.append(btn_load)
        #Button to edit a record in the table
        edit_button = tk.Button(menu_frame, text="Edit Record", command=Mod.edit_record)
        edit_button.pack(side=tk.LEFT)
        btn_all.append(edit_button)

        # button to delete a record in the table
        btn_delete = tk.Button(menu_frame,text="Delete Record", command=Mod.delete_record)
        btn_delete.pack(side=tk.LEFT)
        btn_all.append(btn_delete)
        #button to drop the table
        btn_drop = tk.Button(menu_frame,text="Drop table", command=Mod.ClearRecord)
        btn_drop.pack(side=tk.LEFT)
        btn_all.append(btn_drop)

        #button to spawn a form that will be sued to dd a new record
        btn_Form = tk.Button(menu_frame,text="Add Record", command=Mod.CallForm)
        btn_Form.pack(side=tk.LEFT)
        btn_all.append(btn_Form)

        #button that will be use to save the data from the table to a file
        btn_Save = tk.Button(menu_frame,text="Save Record", command=Mod.Save_record)
        btn_Save.pack(side=tk.LEFT)
        btn_all.append(btn_Save)

        #button that will use to load a save file to a new table
        btn_Rel = tk.Button(menu_frame,text="Reload Record", command=Mod.Reload_record)
        btn_Rel.pack(side=tk.LEFT)
        btn_all.append(btn_Rel)

        #Button to satrt the graph phase
        btn_Graph = tk.Button(menu_frame,text="Call Graph", command=Mod.List_Box)
        btn_Graph.pack(side=tk.LEFT)
        btn_all.append(btn_Graph)

        # Apply the color changes using a loop
      #  if  self.check_if_null(self.Fc) and self.check_if_null(self.Bc):
       #     for button in btn_all:
        #        viewer.change_color(button, self.Fc)
         #       viewer.change_colorii(button, self.Bc)
       
        window.mainloop()

    def check_if_null(self,variable):
        if variable is None:
            return False
        else:
            return True

if __name__ == "__main__":
    window = tk.Tk() # the root of the gui window
    Controller(window)  