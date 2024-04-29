import streamlit as st
import pandas as pd
import sqlite3
from datetime import timedelta, datetime, date
import pytz
from redis import Redis
from rq_scheduler import Scheduler
from send_email import send_email

scheduler = Scheduler(connection=Redis())

with st.form("info_form"):
   st.title("Welcome to the Composting Scheduler! Please fill out the following information to get started!")
   name = st.text_input("Please insert your name.")
   email = st.text_input("Please insert your email address for notifications.")
   date = st.date_input("Please insert the date you started composting.")

   st.write("""Note: You should have a 2:1 to 3:1 ratio of browns to greens. Greens are high in nitrogen, like food scraps,and browns are high in carbon, like dead leaves, paper, and cardboard. Please check the "Info" page above for more =information on what type of materials qualify as "greens" and "browns", as well as how to insert them into the bin. """)
   greens = st.number_input("Please input the weight of greens you put into your compost bin (in kg).", min_value=0.1)
   browns = st.number_input("Please input the weight of browns you put into your compost bin (in kg).", min_value=0.1)
   submitted = st.form_submit_button("Submit")

st.write(f"Name: {name}")
st.write(f"Email: {email}")
st.write(f"Date: {date}")
st.write(f"Greens: " + str(greens))
st.write(f"Browns: " + str(browns))

c = sqlite3.connect('compostinfo.db')
df = pd.read_sql_query("SELECT * FROM COMPOSTS", c)
dd= df[['NAME', "EMAIL", "KG", "DATE"]]
dd['MONTH'] = dd['DATE'].map(lambda x: x.split('-')[1])
dd['MONTH'] = dd["MONTH"].astype(int)
ddd = dd.groupby('MONTH').sum()[["KG"]]
ddd.reset_index(inplace=True)

st.subheader("Amount of Food Waste Recycled Each Month in 2022 by All Users")
st.bar_chart(ddd, x="MONTH", y="KG")

if(submitted):
   year, mth, day = map(int, date.strftime("%Y/%m/%d").split('/'))
   hr = datetime.now().hour
   min = datetime.now().minute
   mn = str(min)
   if(min % 10 == min):
      mn = '0' + mn
   local_dt = datetime(year, mth, day, hr, min)
   local_dt = local_dt + timedelta(minutes=2)

   utc_dt = local_dt.astimezone(pytz.UTC)
   ratio = browns/greens
   if(ratio < 1.8):
      st.write(f"Your ratio of browns to green is {ratio}:1. The ideal ratio should be around 2:1 to 3:1. Please add more browns to your compost bin.")
   elif(ratio > 3.0):
      st.write(f"Your ratio of browns to green is {ratio}:1. The ideal ratio should be around 2:1 to 3:1. Please add more greens to your compost bin.")
   else:
      st.write(f"Check your email!")
      # st.write(f"""INSERT INTO COMPOSTS (NAME,EMAIL,KG,DATE)
      # VALUES ({name}, {email}, {browns + greens}, {str(year)+"-"+str(mth)+'-'+str(day)})""")

      c.execute(f"""INSERT INTO COMPOSTS (NAME,EMAIL,KG,DATE)
      VALUES ('{name}', '{email}', {browns + greens}, '{str(year)+"-"+str(mth)+'-'+str(day)}')""")
      c.commit()

      scheduler.enqueue_at(utc_dt, 
                           send_email,
                           'egswhwang@gmail.com',
                           email,
                           'Congratulations in Starting Your Compost Bin!',
                              f"""You have inserted <strong> {greens} </strong> kg of greens and <strong> {browns} </strong> kg of browns into your compost bin at local time <strong> {hr}:{mn} on {mth}/{day}/{year} </strong>
                              <br> Happy Composting!
                              """)

      scheduler.enqueue_at(utc_dt + timedelta(minutes=1),
                              send_email,
                              'egswhwang@gmail.com',
                              email,
                              'It is Time to Turn Your Compost Bin!',
                                 f"""This is your 1st time turning your compost bin. Use a garden fork or a similar large tool in order to turn the outside of the compost pile inward.
                                 <br> This allows for the pile to get some fresh air which would speed up the composting process.
                                 """)
      scheduler.enqueue_at(utc_dt + timedelta(minutes=2),
                              send_email,
                              'egswhwang@gmail.com',
                              email,
                              'Check your Compost Bin!',
                                 f"""<strong>It is time to check your compost bin for today! You should check: </strong>
                                 <br> 1. The temperature of the compost bin. The ideal temperature should be between 130 and 160 degrees Fahrenheit. If it is not heating up, you should add more greens and turn it.
                                 <br> 2. The moisture of the compost bin. If it is too dry, add water and turn it. If it is too wet, add more browns and turn it. Your compost should have the consistency of a sponge.
                                 <br> 3. Make sure there are no rodents or other pests. In order to avoid them, bury your food scraps in the pile and
                                  make sure to not put any meat, dairy, or greasy products in your compost bin. Reinforcing your bin with a lid is also recommended.
                                 <br> 4. Make sure there is no bad smell. Your compost should smell earthy and smell like fresh soil. If there is, add more browns and turn it.
                                 """)
      scheduler.enqueue_at(utc_dt + timedelta(minutes=3), 
                              send_email,
                              'egswhwang@gmail.com',
                              email,
                              'It is time to cure your Compost!',
                                 f"""<strong>Your compost has been decomposing for about 3 months now! It is time to cure your compost! </strong> 
                                 <br> Almost all of the material that you have added should have now decomposed and it should no longer heat up after turning. 
                                 If your compost is not ready yet, please continue turning and maintaining the compost bin until it does.
                                 <br> If your compost is now ready, please stop adding more material into the compost bin or remove the oldest section so that the rest of the pile can continue
                                 decomposing. Leave it alone for about four weeks to cure. This will allow the compost to stabilize and for the pH to neutralize.
                                 <br> You will receive an email notification in four weeks to harvest your compost, so please stay tuned!""")
      scheduler.enqueue_at(utc_dt+ timedelta(minutes=4),
                                    send_email,
                                    'egswhwang@gmail.com',
                                    email,
                                    'Congraduation! It is time to harvest your Compost!',
                                       f"""<strong>Congradulations! You have successfully composted for 4 months! It is time to harvest your compost! </strong> 
                                       <br> Your compost should now look dark, loose, and crumbly. If your compost is not ready yet, please continue letting the pile cure.
                                       <br> If your compost is now ready to harvest, please sift the harvest to separate the soil with hard material
                                       that hasn't decomposed. You can use the hard material to add in a new or active compost pile.
                                       <strong> You have now finally obtained compost! Thank you for helping the environment! </strong>
                                       <br> If you would like to start another compost bin, we hope that you will use this app again to help you through the process! :D""")

