import streamlit as st
import pandas as pd
import pathlib
import sqlite3
file_path="gali.css"
with open(file_path) as p:
    st.html(f"<style>{p.read()}</style>")
st.title("Welcome To Kadapa ATM Gali Sateesh")
conn=sqlite3.connect("gali.db",check_same_thread=False)
cur=conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS ATM (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT,
    PASSWORD TEXT,
    BALANCE INTEGER
)
""")
conn.commit()
st.header("Hi Thank you For Choosing Kadapa ATM")
st.subheader("If you have ATM ID Don't Worry,OtherWise Create ATM ID")
choice=st.selectbox("",["Click Here","Check Validity","Generate","Other[balance cheking,deposit,withdraw]","For ADMIN's Only"],key="gali")
name=""
pas=""
balance=0
if choice=="For ADMIN's Only":
    pass_word=st.text_input("Enter Your Password For Security Purpose:")
    if pass_word=="gali":
        query="select * from ATM"
        cur.execute(query)
        t=cur.fetchall()
        st.write("Registered Holders List:")
        for i in t:
            st.write(i)
if choice=='Generate':
    st.write("Thank You I Will Create")
    name=st.text_input("Enter Your NAME")
    pas=st.text_input("Enter Your PASSWORD")
    balance=st.number_input("Enter Your BALANCE")
    if st.button("Submit"):
        query="insert into ATM(NAME,PASSWORD,BALANCE) values(?,?,?)"
        cur.execute(query,(name,pas,balance))
        conn.commit()
        query="select ID from ATM where PASSWORD=?"
        cur.execute(query,(pas,))
        ID=cur.fetchone()[0]
        st.write(f"Hey {name} You are Successfully Created with the ID Of {ID}")
if choice=="Check Validity":
    ID=st.number_input("Enter Your ID")
    pas=st.text_input("Enter Your PASSWORD")
    query="select * from ATM WHERE ID=? and PASSWORD=?"
    cur.execute(query,(ID,pas))
    t=cur.fetchone()
    if st.button("Enter"):
        if t:
            st.write(t)
            st.write(f"Hey {ID} your are Eligible")
        else:
            st.write("---- SORRY SIR ----")
    
if choice=="Other[balance cheking,deposit,withdraw]":
    ID=st.number_input("Enter Your ID")
    name=st.text_input("Enter Your NAME")
    pas=st.text_input("Enter Your PASSWORD")
    cho=st.selectbox("",["Click Here","Check Bank Balance","Deposit","Withdraw"])
    if cho=="Check Bank Balance":
        query="select BALANCE from ATM WHERE PASSWORD=? and ID=?"
        cur.execute(query,(pas,ID))
        st.write(f"Hey {name} Your Bank Balance is :{cur.fetchone()[0]}")
    if cho=="Deposit":
        amount=st.number_input("Enter Amount to Deposit")
        if st.button("Enter"):
            cur.execute("update ATM set BALANCE=BALANCE+? where PASSWORD=? and ID=?",(amount,pas,ID))
            conn.commit()
            st.write(f"Withdraw Successfull {amount} Added to {name} Account")
            st.write(f"Thank you {name},Have a Nice Day!!!!!")

    if cho=="Withdraw":
        amount=st.number_input("Enter Amount to Withdraw")
        if st.button("Enter"):
            query="select BALANCE from ATM WHERE PASSWORD=? and ID=?"
            cur.execute(query,(pas,ID))
            t=cur.fetchone()[0]
            if amount<=t:
                cur.execute("update ATM set BALANCE=BALANCE-? where ID=?",(amount,ID))
                conn.commit()
                st.write(f"Withdraw Successfull {amount} remove from {name} Account")
                st.write(f"Thank you {name},Have a Nice Day!!!!!")
            else:
                st.write(f"Insuuficent Funds,Sorry {name} I Think You Have To Deposit Some Amount")

    

        

    





    
