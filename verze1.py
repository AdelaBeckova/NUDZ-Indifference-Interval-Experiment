#-*- coding: utf-8 -*-
from psychopy.visual import Window, TextStim, Rect
from psychopy.core import wait, Clock, quit, getTime
from psychopy.event import waitKeys, getKeys, clearEvents
from psychopy import prefs
prefs.hardware['audioLib'] = ['PTB']
from psychopy import sound
from psychopy import gui
from pickle import dump
import time
import random 
from psychopy.hardware import keyboard
from psychopy import core

myDlg = gui.Dlg(title=u'Časový experiment')
myDlg.addText('Informace o participantovi: ')
participant_number=myDlg.addField("ID participanta: ")
participant_age=myDlg.addField(u"Věk participanta: ")
participant_gender=myDlg.addField(u"Pohlaví participanta: ")
date=myDlg.addField(u"Datum: ")
time=myDlg.addField(u"Čas: ")
variant=myDlg.addField(u"Verze: ")
ok_data = myDlg.show()
ok_data=str(ok_data)
if myDlg.OK:
    print(ok_data)
    datalog=open('C:/Users/stazisti/Desktop/indif/mylogfile.txt', "at")
    datalog.write("\n" + ok_data +"\n")
    datalog.close()
    datalog=open('C:/Users/stazisti/Desktop/indif/all.txt', "at")
    datalog.write("\n" + ok_data)
    datalog.close()
    datalog=open('C:/Users/stazisti/Desktop/indif/all_1.txt', "at")
    datalog.write("\n" + ok_data)
    datalog.close()
    datalog=open('C:/Users/stazisti/Desktop/indif/all_ver1.txt', "at")
    datalog.write("\n" + ok_data)
    datalog.close()
    
else:
    print(u'user log out')
    quit()

    

my_time=Clock()
my_time.reset()

#acu_intro:
my_win= Window([1000, 600], color="black", fullscr=False)
intro=TextStim(my_win, text = u"Vítejte v našem experimentu.")
intro.draw()
my_win.flip()
t_hello = my_time.getTime()
wait(3)
intro.text = u"Experiment bude mít dvě části: první bude s akustickými, druhá s vizuálními stimuly.\n\nPro pokračování stiskněte mezerník nebo tlačítko 2."
intro.draw()
my_win.flip()
waitKeys(keyList = ["space","b"])
t_two_parts=my_time.getTime()
intro.text = u"Vaším úkolem je reprodukovat stimul, který uvidíte/uslyšíte.\n\n<mezerník/2>"
intro.draw()
my_win.flip()
t_after=my_time.getTime()
waitKeys(keyList = ["space","b"])
intro.text = u"Po každém stimulu se objeví symbol otazníku:\n\n?\n\nPro reprodukci použijte tlačítko 1.\nStiskněte tlačítko na tak dlouho, jak si myslíte, že stimul trval.\n\n<mezerník/2>"
intro.draw()
my_win.flip()
t_for_reproduction=my_time.getTime()
waitKeys(keyList = ["space","b"])
intro.text = "Prosíme, reprodukujte celou délku trvání stimulu. \n\n<mezerník/2>"
intro.draw()
my_win.flip()
t_whole=my_time.getTime()
waitKeys(keyList = ["space","b"])
intro.text = "Až dokončíte reprodukci, stiskněte tlačítko 2 pro spuštění/zobrazení dalšího stimulu.\n\n<mezerník/2>"
intro.draw()
my_win.flip()
t_next=my_time.getTime()
waitKeys(keyList = ["space","b"])
intro.text=u"Prosíme, soustřeďte se a nepočítejte si délku trvání stimulů.\n\n<mezerník/2>"
intro.draw()
my_win.flip()
t_not_count=my_time.getTime()
waitKeys(keyList = ["space","b"])
intro.text = u"Pokud rozumíte instrukcím a nemáte žádné další otázky, stiskněte mezerník nebo tlačítko 2 pro pokračování."
intro.draw()
my_win.flip()
t_if=my_time.getTime()
waitKeys(keyList = ["space","b"])
kb = keyboard.Keyboard()

datalog=open('C:/Users/stazisti/Desktop/indif/mylogfile.txt', "at")
datalog.write(u"intro:"+ "\n" + u"t_hello:\t" + str(t_hello) + u"\nt_two_parts:\t" + str(t_two_parts) + u"\nt_after:\t" + str(t_after) + u"\nt_for_reproduction:\t" + str(t_for_reproduction) + u"\nt_whole:\t" + str(t_whole) + u"\nt_next:\t" + str(t_next) + u"\nt_not_count:\t" + str(t_not_count)+u"\nt_if:\t"+str(t_if))
datalog.close()

#acu_stimuli:
s_1="C:/Users/stazisti/Desktop/indif/stimuly/230_1.6s.wav"
s_2="C:/Users/stazisti/Desktop/indif/stimuly/230_2.5s.wav"
s_3="C:/Users/stazisti/Desktop/indif/stimuly/230_3.2s.wav"
s_4="C:/Users/stazisti/Desktop/indif/stimuly/230_5s.wav"
s_5="C:/Users/stazisti/Desktop/indif/stimuly/230_6.4s.wav"
s_6="C:/Users/stazisti/Desktop/indif/stimuly/230_8s.wav"
s_7="C:/Users/stazisti/Desktop/indif/stimuly/230_10s.wav"
s_8="C:/Users/stazisti/Desktop/indif/stimuly/230_12.8s.wav"
s_9="C:/Users/stazisti/Desktop/indif/stimuly/230_15s.wav"
z_1="C:/Users/stazisti/Desktop/indif/stimuly/zacvik/230_1.9s.wav"
z_2="C:/Users/stazisti/Desktop/indif/stimuly/zacvik/230_3.5s.wav"
z_3="C:/Users/stazisti/Desktop/indif/stimuly/zacvik/230_4s.wav"


sounds = { '1.6': s_1, '2.5':s_2, '3.2':s_3, '5':s_4, '6.4':s_5, '8':s_6, '10':s_7, '12.8':s_8,'15':s_9} 
soundsList = list(sounds.keys())
sounds_practise = {'1.9':z_1,'3.5':z_2,'4':z_3}
soundsList_practise = list(sounds_practise.keys())

#acu_functions: 


def practise_acu():
    choiceList_practise = list("")
    n_trials=0
    practise=TextStim(my_win, text = u"První část")
    practise.draw()
    my_win.flip()
    wait(3)
    practise.text = u"V této části budete posuzovat délku trvání zvukových stimulů. \n\n<mezerník/2>"
    practise.draw()
    my_win.flip()
    waitKeys(keyList = ["space","b"])
    practise.text=u"Nyní začneme zácvikem.\n\n<mezerník/2>"
    practise.draw()
    my_win.flip()
    waitKeys(keyList = ["space","b"])
    practise.text = "Stisknutím mezerníku nebo tlačítka 2 IHNED spustíte první zkušební nahrávku.\n\n<mezerník/2>"
    practise.draw()
    my_win.flip()
    waitKeys(keyList = ["space","b"])
    for i in range (3):
        n_trials +=1
        while True:
            choice_practise=random.choice(soundsList_practise)
            if choice_practise in choiceList_practise:
                continue
            else:
                choiceList_practise.append(choice_practise)
                print(choiceList_practise)
                break
        choice_practise_sound=sound.Sound(sounds_practise[choice_practise])
        clearEvents()
        while True:
            t_practise_begin = my_time.getTime()
            experiment=TextStim(my_win, text=u"",bold=True, units='pix',height=80)
            experiment.draw()
            my_win.flip()
            choice_practise_sound.play()
            if choice_practise == '1.9':
                wait(3.6)
            if choice_practise == '3.5':
                wait(5.2)
            if choice_practise == '4':
                wait(5.7)
            clearEvents()
            t_repro_begin = my_time.getTime()
            kb.clock.reset()
            experiment.text= u"?"
            experiment.draw()
            my_win.flip()
            keys=kb.waitKeys(keyList = ["space","c","b","right","q"], waitRelease=True)
            if 'q' in keys:
                core.quit()
            for key in keys:
                print(key.name, key.duration, key.rt)
            break
        t_trial_end=my_time.getTime()
        print(choice_practise)
        datalog=open('C:/Users/stazisti/Desktop/indif/mylogfile.txt', "at")
        datalog.write(u"\nTrial number:\t"+str(n_trials))
        datalog.write(u"\nTrial begin:\t" + str(t_practise_begin) + u"\nReproduction begin:\t" + str(t_repro_begin) + u"\nCondition:\t"+str(choice_practise) + u"\nKey name:\t"+str(key.name)+u"\nReproduction:\t"+str(key.duration)+u"\nRT:\t"+ str(key.rt) + u"\nTrial end:\t" + str(t_trial_end))
        datalog.close()
        wait(0.5)
        

def block_acu():
    choiceList = list("")
    n_trials_e=0
    for i in range (9):
        n_trials_e+=1
        while True:
            choice=random.choice(soundsList)
            if choice in choiceList:
                continue
            else:
                choiceList.append(choice)
                print(choiceList)
                break
        choice_sound=sound.Sound(sounds[choice])
        clearEvents()
        while True:
            t_begin_e = my_time.getTime()
            experiment=TextStim(my_win, text=u"",bold=True, units='pix', height=80)
            experiment.draw()
            my_win.flip()
            clearEvents()
            choice_sound.play()
            if choice == '1.6':
                wait(3.3)
            if choice == '2.5':
                wait(4.2)
            if choice == '3.2':
                wait(4.9)
            if choice == '5':
                wait(6.7) 
            if choice == '6.4':
                wait(8.1)
            if choice == '8':
                wait(9.7)
            if choice == '10':
                wait(11.7)
            if choice == '12.8':
                wait(14.5)
            if choice == '15':
                wait(16.7)
            clearEvents()
            t_repro_begin_e = my_time.getTime()
            kb.clock.reset()
            experiment.text= u"?"
            experiment.draw()
            my_win.flip()
            keys=kb.waitKeys(keyList = ["space","c","b","right","q"], waitRelease=True)
            if 'q' in keys:
                core.quit()
            for key in keys:
                print(key.name, key.duration, key.rt)
            break
        t_trial_end=my_time.getTime()
        print(choice)
        datalog=open('C:/Users/stazisti/Desktop/indif/mylogfile.txt', "at")
        datalog.write(u"\nTrial number:\t"+str(n_trials_e))
        datalog.write(u"\nTrial begin:\t" + str(t_begin_e) + u"\nReproduction begin:\t" + str(t_repro_begin_e)+u"\nCondition:\t" + str(choice) + u"\nReproduction:\t" + str(key.duration) +u"\nKey name:\t"+ str(key.name) + u"\nRT:\t" + str(key.rt) + u"\nTrial end:\t" + str(t_trial_end)) 
        datalog.close()
        datalog=open('C:/Users/stazisti/Desktop/indif/all.txt', "at")
        datalog.write(","+str(t_begin_e)+","+str(t_repro_begin_e)+","+str(choice)+","+str(key.duration)+","+str(key.name)+","+str(key.rt)+","+str(t_trial_end))
        datalog.close()
        datalog=open('C:/Users/stazisti/Desktop/indif/all_1.txt', "at")
        datalog.write(","+str(t_begin_e)+","+str(t_repro_begin_e)+","+str(choice)+","+str(key.duration)+","+str(key.name)+","+str(key.rt)+","+str(t_trial_end))
        datalog.close()
        datalog=open('C:/Users/stazisti/Desktop/indif/all_ver1.txt', "at")
        datalog.write("\n" + str(choice)+","+str(key.duration)+","+str(key.rt)+","+"acoustic")
        datalog.close()
        wait(0.5)
        
#code_execution:

#practise_acu:
datalog=open('C:/Users/stazisti/Desktop/indif/mylogfile.txt', "at")
datalog.write(u"\npractise:")
datalog.close()
practise_acu()
t_practise_end_1 = my_time.getTime()
between_block_1 = TextStim(my_win, text = u"Zácvik je u konce. Nyní bude experimentální část.\n\n<mezerník/2>")
between_block_1.draw()
my_win.flip()
waitKeys(keyList = ["space","b"])
between_block_1.text=u"Stisknutím mezerníku nebo tlačítka 2 IHNED spustíte první experimentální nahrávku."
between_block_1.draw()
my_win.flip()
waitKeys(keyList = ["space","b"])

#1st_block_acu:

t_begin_b1 = my_time.getTime()
datalog=open('C:/Users/stazisti/Desktop/indif/mylogfile.txt', "at")
datalog.write(u"\nPractise end 1:\t" + str(t_practise_end_1) + u"\n\nBlock 1 begin:" + str(t_begin_b1))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all.txt', "at")
datalog.write(","+str(t_begin_b1))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all_1.txt', "at")
datalog.write(","+str(t_begin_b1))
datalog.close()
block_acu()
t_end_b1 = my_time.getTime()
between_block_1 = TextStim(my_win, text = u"První blok je u konce. Můžete si dát krátkou pauzu. Stiskněte mezerník/tlačítko 2, až budete připraveni pokračovat.")
between_block_1.draw()
my_win.flip()
waitKeys(keyList = ["space","b"])

#2nd_block_acu:

t_begin_b2=my_time.getTime()
datalog=open('C:/Users/stazisti/Desktop/indif/mylogfile.txt', "at")
datalog.write(u"\nBlock 1 end:\t" + str(t_end_b1) + u"\nPause length" + str(t_begin_b2-t_end_b1)+u"\n\nBlock 2 begin:"+str(t_begin_b2))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all.txt', "at")
datalog.write(","+str(t_begin_b2))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all_1.txt', "at")
datalog.write(","+str(t_begin_b2))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all_ver1.txt', "at")
datalog.write("\nblock break")
datalog.close()
block_acu()
t_end_b2 = my_time.getTime()
between_block_2=TextStim(my_win, text = u"Druhý blok je u konce. Můžete si dát krátkou pauzu. Stiskněte mezerník/tlačítko 2, až budete připraveni pokračovat.")
between_block_2.draw()
my_win.flip()
waitKeys(keyList = ["space","b"])

#3rd_block_acu:

t_begin_b3=my_time.getTime()
datalog=open('C:/Users/stazisti/Desktop/indif/mylogfile.txt', "at")
datalog.write(u"\nBlock 2 end:\t" + str(t_end_b2) + u"\nPause length" + str(t_begin_b3-t_end_b2)+u"\n\nBlock 3 begin:"+str(t_begin_b3))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all.txt', "at")
datalog.write(","+str(t_begin_b3))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all_1.txt', "at")
datalog.write(","+str(t_begin_b3))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all_ver1.txt', "at")
datalog.write("\nblock break")
datalog.close()
block_acu()
t_end_b3 = my_time.getTime()
between_block_3=TextStim(my_win, text = u"Třetí blok je u konce. Můžete si dát krátkou pauzu. Stiskněte mezerník/tlačítko 2, až budete připraveni pokračovat.")
between_block_3.draw()
my_win.flip()
waitKeys(keyList = ["space","b"])

#4th_block_acu:

t_begin_b4=my_time.getTime()
datalog=open('C:/Users/stazisti/Desktop/indif/mylogfile.txt', "at")
datalog.write(u"\nBlock 2 end:\t" + str(t_end_b3) + u"\nPause length" + str(t_begin_b4-t_end_b3)+u"\n\nBlock 4 begin:"+str(t_begin_b4))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all.txt', "at")
datalog.write(","+str(t_begin_b4))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all_1.txt', "at")
datalog.write(","+str(t_begin_b4))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all_ver1.txt', "at")
datalog.write("\nblock break")
datalog.close()
block_acu()
t_end_b4 = my_time.getTime()
datalog=open('C:/Users/stazisti/Desktop/indif/mylogfile.txt', "at")
datalog.write(u"\nBlock 4 end:\t" + str(t_end_b4))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all_ver1.txt', "at")
datalog.write("\nblock break")
datalog.close()

#end_acu

postexp = TextStim(my_win, text = u"Akustická část experimentu je u konce. Stiskněte mezerník nebo tlačítko 2 pro pokračování do druhé části.")

postexp.draw()

my_win.flip()
waitKeys(keyList = ["space","b"])
    
#vis_intro    
intro.text = u"Druhá část"
intro.draw()
my_win.flip()
wait(3)
intro.text = u"V této části budete posuzovat délku trvání vizuálního stimulu na obrazovce.\n\n<mezerník/2>"
intro.draw()
my_win.flip()
t_vis_s=my_time.getTime()
waitKeys(keyList = ["space","b"])
intro.text = "Prosíme, reprodukujte celou dobu trvání stimulu na obrazovce. \n\n<mezerník/2>"
intro.draw()
my_win.flip()
t_whole=my_time.getTime()
waitKeys(keyList = ["space","b"])
intro.text=u"Prosíme, soustřeďte se a nepočítejte si délku trvání stimulů.\n\n<mezerník/2>"
intro.draw()
my_win.flip()
t_not_count=my_time.getTime()
waitKeys(keyList = ["space","b"])
intro.text = u"Pokud nemáte žádné otázky, stiskněte mezerník nebo tlačítko 2 pro pokračování."
intro.draw()
my_win.flip()
t_if=my_time.getTime()
waitKeys(keyList = ["space","b"])
kb = keyboard.Keyboard()
practise=TextStim(my_win, text = u"Nyní začneme zácvikem")
practise.draw()
my_win.flip()
wait(3)
practise.text = "Stisknutím mezerníku nebo tlačítka 2 nyní IHNED zobrazíte první zkušební stimul.\n\n<mezerník/2>"
practise.draw()
my_win.flip()
waitKeys(keyList = ["space","b"])
datalog=open('C:/Users/stazisti/Desktop/indif/mylogfile.txt', "at")
datalog.write(u"intro_vis:"+ "\n" + u"t_vis_s:\t" + str(t_vis_s) + u"\nt_whole:\t" + str(t_whole) + u"\nt_not_count:\t" + str(t_not_count))
datalog.close()

durList_practise = ["4","1.9","3.5"]
durList_exp = ["1.6","2.5","3.2","5","6.4","8","10","12.8","15"]


#vis_functions:

def practise_vis():
    n_trials=0
    my_square = Rect(my_win,width=200,height=200,units='pix',lineColor='#808080',fillColor='#808080',interpolate=True)
    choiceList_practise = list("")
    for i in range (3):
        n_trials +=1
        experiment=TextStim(my_win, text=u"", bold=True,units='pix',height=80)
        while True:
            choice_practise=random.choice(durList_practise)
            if choice_practise in choiceList_practise:
                continue
            else:
                choiceList_practise.append(choice_practise)
                print(choiceList_practise)
                break
        clearEvents()
        while True:
            t_practise_begin = my_time.getTime()
            experiment.draw()
            my_win.flip()
            wait(0.5)
            my_square.draw()
            my_win.flip()
            if choice_practise == "1.9":
                wait(2.9)
            if choice_practise == "3.5":
                wait(3.5)
            if choice_practise == "4":
                wait(4)
            experiment.draw()
            my_win.flip()
            wait(1.2)
            clearEvents()
            t_repro_begin = my_time.getTime()
            kb.clock.reset()
            experiment.text= u"?"
            experiment.draw()
            my_win.flip()
            keys=kb.waitKeys(keyList = ["space","c","b","right","q"], waitRelease=True)
            if 'q' in keys:
                core.quit()
            for key in keys:
                print(key.name, key.duration, key.rt)
            break
        t_trial_end=my_time.getTime()
        print(choice_practise)
        datalog=open('C:/Users/stazisti/Desktop/indif/mylogfile.txt', "at")
        datalog.write(u"\nTrial number:\t"+str(n_trials))
        datalog.write(u"\nTrial begin:\t" + str(t_practise_begin) + u"\nReproduction begin:\t" + str(t_repro_begin) + u"\nCondition:\t"+str(choice_practise) + u"\nKey name:\t"+str(key.name)+u"\nReproduction:\t"+str(key.duration)+u"\nRT:\t"+ str(key.rt) + u"\nTrial end:\t" + str(t_trial_end))
        datalog.close()
        wait(0.5)
        
        
def block_vis():
    n_trials=0
    my_square = Rect(my_win,width=200,height=200,units='pix',lineColor='#808080',fillColor='#808080',interpolate=True)
    choiceList_exp = list("")
    for i in range (9):
        n_trials +=1
        experiment=TextStim(my_win, text=u"",bold=True, units='pix',height=80)
        while True:
            choice_exp=random.choice(durList_exp)
            if choice_exp in choiceList_exp:
                continue
            else:
                choiceList_exp.append(choice_exp)
                print(choiceList_exp)
                break
        clearEvents()
        while True:
            t_exp_begin = my_time.getTime()
            experiment.draw()
            my_win.flip()
            wait(0.5)
            my_square.draw()
            my_win.flip()
            if choice_exp == "1.6":
                wait(1.6)
            if choice_exp == "2.5":
                wait(2.5)
            if choice_exp == "3.2":
                wait(3.2)
            if choice_exp == "5":
                wait(5)    
            if choice_exp == "6.4":
                wait(6.4)
            if choice_exp == "8":
                wait(8)    
            if choice_exp == "10":
                wait(10)
            if choice_exp == "12.8":
                wait(12.8)
            if choice_exp == "15":
                wait(15)    
            experiment.draw()
            my_win.flip()
            wait(1.2)
            clearEvents()
            t_repro_begin = my_time.getTime()
            kb.clock.reset()
            experiment.text= u"?"
            experiment.draw()
            my_win.flip()
            keys=kb.waitKeys(keyList = ["space","c","b","right","q"], waitRelease=True)
            if 'q' in keys:
                core.quit()
            for key in keys:
                print(key.name, key.duration, key.rt)
            break
        t_trial_end=my_time.getTime()
        print(choice_exp)
        datalog=open('C:/Users/stazisti/Desktop/indif/mylogfile.txt', "at")
        datalog.write(u"\nTrial number:\t"+str(n_trials))
        datalog.write(u"\nTrial begin:\t" + str(t_exp_begin) + u"\nReproduction begin:\t" + str(t_repro_begin) + u"\nCondition:\t"+str(choice_exp) + u"\nKey name:\t"+str(key.name)+u"\nReproduction:\t"+str(key.duration)+u"\nRT:\t"+ str(key.rt) + u"\nTrial end:\t" + str(t_trial_end))
        datalog.close()
        datalog=open('C:/Users/stazisti/Desktop/indif/all_ver1.txt', "at")
        datalog.write("\n" + str(choice_exp)+","+str(key.duration)+","+str(key.rt)+","+"visual")
        datalog.close()
        wait(0.5)

my_time=Clock()
my_time.reset()
kb = keyboard.Keyboard()

#vis_code_execution:

#practise_vis:
datalog=open('C:/Users/stazisti/Desktop/indif/mylogfile.txt', "at")
datalog.write(u"\vis_practise:")
datalog.close()
practise_vis()
t_practise_end_1 = my_time.getTime()
between_block_1 = TextStim(my_win, text = u"Zácvik je u konce. Nyní bude experimentální část.\n\n<mezerník/2>")
between_block_1.draw()
my_win.flip()
waitKeys(keyList = ["space","b"])
between_block_1.text=u"Stisknutím mezerníku nebo tlačítka 2 IHNED zobrazíte první experimentální stimul."
between_block_1.draw()
my_win.flip()
waitKeys(keyList = ["space","b"])

#1st_block_vis:

t_begin_b1 = my_time.getTime()
datalog=open('C:/Users/stazisti/Desktop/indif/mylogfile.txt', "at")
datalog.write(u"\nPractise end 1:\t" + str(t_practise_end_1) + u"\n\nBlock 1 begin:" + str(t_begin_b1))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all.txt', "at")
datalog.write(","+str(t_begin_b1))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all_1.txt', "at")
datalog.write(","+str(t_begin_b1))
datalog.close()
block_vis()
t_end_b1 = my_time.getTime()
between_block_1 = TextStim(my_win, text = u"První blok je u konce. Můžete si dát krátkou pauzu. Stiskněte mezerník/tlačítko 2, až budete připraveni pokračovat.")
between_block_1.draw()
my_win.flip()
waitKeys(keyList = ["space","b"])

#2nd_block_vis:

t_begin_b2=my_time.getTime()
datalog=open('C:/Users/stazisti/Desktop/indif/mylogfile.txt', "at")
datalog.write(u"\nBlock 1 end:\t" + str(t_end_b1) + u"\nPause length" + str(t_begin_b2-t_end_b1)+u"\n\nBlock 2 begin:"+str(t_begin_b2))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all.txt', "at")
datalog.write(","+str(t_begin_b2))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all_1.txt', "at")
datalog.write(","+str(t_begin_b2))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all_ver1.txt', "at")
datalog.write("\nblock break")
datalog.close()
block_vis()
t_end_b2 = my_time.getTime()
between_block_2=TextStim(my_win, text = u"Druhý blok je u konce. Můžete si dát krátkou pauzu. Stiskněte mezerník/tlačítko 2, až budete připraveni pokračovat.")
between_block_2.draw()
my_win.flip()
waitKeys(keyList = ["space","b"])

#3rd_block_vis:

t_begin_b3=my_time.getTime()
datalog=open('C:/Users/stazisti/Desktop/indif/mylogfile.txt', "at")
datalog.write(u"\nBlock 2 end:\t" + str(t_end_b2) + u"\nPause length" + str(t_begin_b3-t_end_b2)+u"\n\nBlock 3 begin:"+str(t_begin_b3))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all.txt', "at")
datalog.write(","+str(t_begin_b3))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all_1.txt', "at")
datalog.write(","+str(t_begin_b3))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all_ver1.txt', "at")
datalog.write("\nblock break")
datalog.close()
block_vis()
t_end_b3 = my_time.getTime()
between_block_3=TextStim(my_win, text = u"Třetí blok je u konce. Můžete si dát krátkou pauzu. Stiskněte mezerník/tlačítko 2, až budete připraveni pokračovat.")
between_block_3.draw()
my_win.flip()
waitKeys(keyList = ["space","b"])

#4th_block_vis:

t_begin_b4=my_time.getTime()
datalog=open('C:/Users/stazisti/Desktop/indif/mylogfile.txt', "at")
datalog.write(u"\nBlock 2 end:\t" + str(t_end_b3) + u"\nPause length" + str(t_begin_b4-t_end_b3)+u"\n\nBlock 4 begin:"+str(t_begin_b4))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all.txt', "at")
datalog.write(","+str(t_begin_b4))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all_1.txt', "at")
datalog.write(","+str(t_begin_b4))
datalog.close()
datalog=open('C:/Users/stazisti/Desktop/indif/all_ver1.txt', "at")
datalog.write("\nblock break")
datalog.close()
block_vis()
t_end_b4 = my_time.getTime()
datalog=open('C:/Users/stazisti/Desktop/indif/mylogfile.txt', "at")
datalog.write(u"\nBlock 4 end:\t" + str(t_end_b4))
datalog.close()

#end_vis

postexp.text = u"Experiment je u konce.Děkujeme Vám za účast."

postexp.draw()

my_win.flip()

waitKeys(keyList = ["q"])
