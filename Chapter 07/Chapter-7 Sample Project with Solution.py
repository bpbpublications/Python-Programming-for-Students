# Sample project with solution
# Create a CRUD application for the hospital database, maintaining tables for doctors and patients with their diagnosis reports
	
	import  sqlite3
	connection  =  sqlite3.connect(r'C:\sqlite\db\HMSDatabase.db')
	cursor  =  connection.cursor()
	error  =  1
	cursor.execute("""select  count(name)  from  sqlite_master  where  type='table'  and  name='DoctorDetails'""")
	if  cursor.fetchone()[0]  ==  0:
	        cursor.execute("""CREATE  TABLE  DoctorDetails  (  
	        doc_id  INTEGER  primary  key,  dnamedfirst  TEXT,  
	        dnamedlast  TEXT,  password  TEXT  not  null,
	        speciality  TEXT  not  null,  shift  TEXT  not  null,
	        phone  number(10)  not  null);""")
	cursor.execute("""select  count(name)  from  sqlite_master  where  type='table'  and  name='PatientDetails'""")
	if  cursor.fetchone()[0]  ==  0:
	        cursor.execute("""CREATE  TABLE  PatientDetails  (  pat_id  number  primary  key,  pfirst  TEXT,  pdlast  TEXT,  City  TEXT  not  null,  DOB  date  not  null,  age  INTEGER  not  null,
	        DOA  date  not  null,  number  number(10)  not  null);""")
	        cursor.execute("""CREATE  TABLE  ViralDisease  (  pat_id  number  not  null,  dname  TEXT  primary  key,vname  TEXT,  treatment  TEXT,  symptoms  TEXT  not  null);""")
	        cursor.execute("""CREATE  TABLE  BacteriaDisease  (  pat_id  number  not  null,  dname  TEXT  primary  key,  bname  TEXT,  treatment  TXET,  symptoms  TEXT  not  null);""")
	        cursor.execute("""CREATE  TABLE  WoundsInjury  (pat_id  number  not  null,  iname  TEXT  primary  key,idiagnosis  TEXT,  type  TEXT  not  null);""")
	        print("Database  created  successfully")
	else:
	        e  =  1
	        while  e  !=  0:
	                e  =  int(input("1.  Log  In  To  My  Account\n2.  Create  a  New  Doctor  Account\n"))
	                if  e  ==  2:
	                        d_id  =  int(input('Enter  Doctor  id  :  '))
	                        d_nf  =  input('Enter    Doctor  first  name  :  ')
	                        d_nl  =  input('Enter    Doctor  last  name  :  ')
	                        d_pas  =  input('Enter  password  :  ')
	                        d_spec  =  input('Enter    Doctor  speciality  :  ')
	                        d_shf  =  input('Enter  working  shift  :  ')
	                        d_ph  =  int(input('Enter    Doctor  phone  number  :  '))
	                        cursor.execute("""insert  into  DoctorDetails  values(?,?,?,?,?,?,?)""",  (d_id,  d_nf,  d_nl,  d_pas,  d_spec,  d_shf,  d_ph))
	                        e  =  1
	                elif  e  ==  1:
	                        while  error  ==  1:
	                                i  =  int(input("Enter  your  ID  :  "))
	                                p  =  input("Enter  your  Password  :  ")
	                                cursor.execute("""select  count(doc_id)  from  DoctorDetails  where  doc_id=(?)""",  (i,))
	                                if  cursor.fetchone()[0]  ==  1:
	                                        cursor.execute("""select  count(password)  from  DoctorDetails  where  password=?""",  (p,))
	                                        if  cursor.fetchone()[0]  ==  1:
	                                                print("\nSign  in  successful!")
	                                                error  =  0
	                                                e  =  0
	                                                r  =  1
	                                                cursor.execute("""select  *  from  DoctorDetails  where  doc_id=(?)""",  (i,))
	                                                for  row  in  cursor.fetchall():
	                                                        print("ID-",  row[0],  "Name,  row[1],  row[2],"Speciality  -",  row[4],  "\nShift  -",
	                                                                    row[5],  "    Phone  Number  -",  row[6])
	                                                while  r  !=  0:
	                                                        print("\n1.  View  Patient  details\n2.  Add  a  New  Patient\n3.  Delete  Patient  Details\n0.  Exit")
	                                                        r  =  int(input())
	                                                        if  r  ==  1:
	                                                                access  =  input("\nEnter  Patient  ID:-  ")
	                                                                cursor.execute("""select  count(*)  from  PatientDetails  where  pat_id=(?)""",  (access,))
	                                                                if  cursor.fetchone()[0]  !=  0:
	                                                                        cursor.execute("""select  *  from  PatientDetails  where  pat_id=(?)""",  (access,))
	                                                                        print("\nPatient  Details  -  ")
	                                                                        for  row  in  cursor.fetchall():
	                                                                                print("Id:  ",  row[0])
	                                                                                print("First  Name:  ",  row[1])
	                                                                                print("Last  Name:  ",  row[2])
	                                                                                print("City:  ",  row[3])
	                                                                                print("Date  of  Birth:  ",  row[4])
	                                                                                print("Age:  ",  row[5])
	                                                                                print("Date  of  Admission:  ",  row[6])
	                                                                        print("\nDiagnosis  Report  -  ")
	                                                                        cursor.execute("""select  count(*)  from  ViralDisease  where  pat_id=(?)""",  (access,))
	                                                                        if  cursor.fetchone()[0]  !=  0:
	                                                                                cursor.execute("""select  *  from  ViralDisease  where  pat_id=(?)""",  (access,))
	                                                                                for  row  in  cursor.fetchall():
	                                                                                        print("Id:  ",  row[0])
	                                                                                        print("Disease  Name:  ",  row[1])
	                                                                                        print("ViralDisease  Name:  ",  row[2])
	                                                                                        print("Treatment:  ",  row[3])
	                                                                                        print("Symptoms:  ",  row[4])
	                                                                                print("\n")
	                                                                        cursor.execute("""select  count(*)  from  BacteriaDisease  where  pat_id=(?)""",  (access,))
	                                                                        if  cursor.fetchone()[0]  !=  0:
	                                                                                cursor.execute("""select  *  from  BacteriaDisease  where  pat_id=(?)""",  (access,))
	                                                                                for  row  in  cursor.fetchall():
	                                                                                        print("Id:  ",  row[0])
	                                                                                        print("Disease  Name:  ",  row[1])
	                                                                                        print("BacteriaDisease  Name:  ",  row[2])
	                                                                                        print("Treatment:  ",  row[3])
	                                                                                        print("Symptoms:  ",  row[4])
	                                                                                print("\n")
	                                                                        cursor.execute("""select  count(*)  from  WoundsInjury  where  pat_id=(?)""",  (access,))
	                                                                        if  cursor.fetchone()[0]  !=  0:
	                                                                                cursor.execute("""select  *  from  WoundsInjury  where  pat_id=(?)""",  (access,))
	                                                                                for  row  in  cursor.fetchall():
	                                                                                        print("Id:  ",  row[0])
	                                                                                        print("WoundsInjury  Name:  ",  row[1])
	                                                                                        print("Diagnosis  Name:  ",  row[2])
	                                                                                        print("Type:  ",  row[3])
	                                                                                print("\n")
	                                                                else:
	                                                                        print("Incorrect  Patient  id")
	                                                        elif  r  ==  2:
	                                                                pid  =  int(input('\nEnter  id  -  '))
	                                                                pnf  =  input('Enter  first  name  -  ')
	                                                                pnl  =  input('Enter  last  name  -  ')
	                                                                pcity  =  input('Enter  city  -  ')
	                                                                pdob  =  input('Enter  date  of  birth  -  ')
	                                                                page  =  int(input('Enter  age  -  '))
	                                                                pdoa  =  input('Enter  date  of  admission  -  ')
	                                                                pnum  =  int(input('Enter  phone  number  -  '))
	                                                                cursor.execute("""insert  into  PatientDetails  values(?,?,?,?,?,?,?,?)""",(pid,  pnf,  pnl,  pcity,  pdob,  page,  pdoa,  pnum))
	                                                                print("1.  ViralDisease\n2.  BacteriaDisease\n3.  Wounds")
	                                                                m  =  int(input())
	                                                                if  m  ==  1:
	                                                                        dname  =  input("\nEnter  disease  name  -  ")
	                                                                        bname  =  input("Enter  ViralDisease  name  -  ")
	                                                                        treatment  =  input("Enter  treatment  -  ")
	                                                                        symptoms  =  input("Enter  symptoms  -  ")
	                                                                        cursor.execute("""insert  into  ViralDisease  values(?,?,?,?,?)""",(pid,  dname,  bname,  treatment,  symptoms))
	                                                                elif  m  ==  2:
	                                                                        dname  =  input("\nEnter  disease  name  -  ")
	                                                                        bname  =  input("Enter  BacteriaDisease  name  -  ")
	                                                                        treatment  =  input("Enter  treatment  -  ")
	                                                                        symptoms  =  input("Enter  symptoms  -  ")
	                                                                        cursor.execute("""insert  into  BacteriaDisease  values(?,?,?,?,?)""",(pid,  dname,  bname,  treatment,  symptoms))
	                                                                elif  m  ==  3:
	                                                                        iname  =  input("\nEnter  WoundsInjury  name  -  ")
	                                                                        idiag  =  input("Enter  diagnosis  -  ")
	                                                                        itype  =  input("Enter  WoundsInjury  type  -  ")
	                                                                        cursor.execute("""insert  into  WoundsInjury  values(?,?,?,?)""",  (pid,  iname,  idiag,  itype))
	                                                                print("\nPatient  Added")
	                                                                connection.commit()
	                                                        elif  r  ==  3:
	                                                                access  =  input("\nEnter  Patient  ID:-  ")
	                                                                cursor.execute("""select  count(*)  from  PatientDetails  where  pat_id=(?)""",  (access,))
	                                                                if  cursor.fetchone()[0]  !=  0:
	                                                                        cursor.execute("""delete  from  PatientDetails  where  pat_id=(?)""",  (access,))
	                                                                        cursor.execute("""select  count(*)  from  ViralDisease  where  pat_id=(?)""",  (access,))
	                                                                        if  cursor.fetchone()[0]  !=  0:
	                                                                                cursor.execute("""delete  from  ViralDisease  where  pat_id=(?)""",  (access,))
	                                                                        cursor.execute("""select  count(*)  from  BacteriaDisease  where  pat_id=(?)""",  (access,))
	                                                                        if  cursor.fetchone()[0]  !=  0:
	                                                                                cursor.execute("""delete  from  BacteriaDisease  where  pat_id=(?)""",  (access,))
	                                                                        cursor.execute("""select  count(*)  from  WoundsInjury  where  pat_id=(?)""",  (access,))
	                                                                        if  cursor.fetchone()[0]  !=  0:
	                                                                                cursor.execute("""delete  from  WoundsInjury  where  pat_id=(?)""",  (access,))
	                                                                else:  print("Incorrect  ID  Patient  does  not  exist")
	                                                                print("\nPatient  Deleted")
	                                                                connection.commit()
	                                                        elif  r  ==  0:  break
	                                        else:  print("Incorrect  passoword.  Please  retry  ")
	                                else:  print("Incorrect  User  ID.  Please  retry  ")
	                        break
	                elif  e  ==  2212:
	                        cursor.execute("""select  *  from  DoctorDetails""")
	                        print(cursor.fetchall())
	                        cursor.execute("""select  *  from  ViralDisease""")
	                        print(cursor.fetchall())
	                        cursor.execute("""select  *  from  BacteriaDisease""")
	                        print(cursor.fetchall())
	                        cursor.execute("""select  *  from  WoundsInjury""")
	                        print(cursor.fetchall())
	                        break
	connection.commit()
	connection.close()
