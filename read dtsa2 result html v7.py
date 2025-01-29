import pandas as pd
import tkinter
import tkinter.filedialog
urllocation = tkinter.filedialog.askopenfile(title="select dtsa2 html report")
#url = r'file:///C:/Users/glxbb/Documents/DTSA-II%20Reports/2024/September/26-Sep-2024/index1.html'
url = r'file:///'+urllocation.name
tables = pd.read_html(url)
#sp500_table = tables[0]
TableNo = []
ExperimentName = []
#CNo = 0
for z in range(0,len(tables)):
    for x in tables[z].columns:
        #CNo = CNo + 1
        for y in range(0,len(tables[z])):
            #print("z,x,y")
            #print(z)
            #print(x)
            #print(y)
            if ('Result 1' in str(tables[z][x][y])) == True:
                print("z")
                print(z)
                print(len(tables[z]))
                print(tables[z][x][y])
                TableNo.append(z)
                #ExperimentName.append(tables[z][tables[z].columns.__getitem__(CNo)][y])
                ExperimentName.append(tables[z][x+1][y])

#for a in TableNo:
for a in range(0,len(TableNo)):
    for b in range(0,len(tables[TableNo[0]])):
        if 'Characteristic' == str(tables[TableNo[a]][0][b]):
            print(a)
            print(b)
            vars()['Cht' + str(a)]=tables[TableNo[a]+1]
            vars()['Chn' + str(a)]=ExperimentName[a]
        if 'Characteristic Fluorescence' == str(tables[TableNo[a]][0][b]):
            print(a)
            print(b)
            vars()['ChFt' + str(a)]=tables[TableNo[a]+2]
            vars()['ChFn' + str(a)]=ExperimentName[a]
        if 'Bremsstrahlung Fluorescence' == str(tables[TableNo[a]][0][b]):
            print(a)
            print(b)
            vars()['BrFt' + str(a)]=tables[TableNo[a]+3]
            vars()['BrFn' + str(a)]=ExperimentName[a]
        if 'Comparing Characteristic to Characteristic Fluorescence' == str(tables[TableNo[a]][0][b]):
            print(a)
            print(b)
            vars()['CChChFt' + str(a)]=tables[TableNo[a]+4]
            vars()['CChChFn' + str(a)]=ExperimentName[a]
        if 'Comparing Characteristic to Bremsstrahlung Fluorescence' == str(tables[TableNo[a]][0][b]):
            print(a)
            print(b)
            vars()['CChBrFt' + str(a)]=tables[TableNo[a]+5]
            vars()['CChBrFn' + str(a)]=ExperimentName[a]
ElCt = 0
#checkdoublecount = 0
#combine each x-ray line intensities (chr,chrfl,brfl) for each experiment into variables
for i in range(0,len(ExperimentName)):
    #vars()['El' + str(ElCt)]=[]
    vars()['El' + str(i)]=[]
    ElCt = 0
    for ii in range(0,len(eval('Cht'+str(i)))):
        for iii in range(0,len(eval('ChFt'+str(i)))):
            if eval('Cht'+str(i))[eval('Cht'+str(i)).columns.__getitem__(0)][ii] == eval('ChFt'+str(i))[eval('ChFt'+str(i)).columns.__getitem__(0)][iii]:
                print("yes ChFt")
                print(i)
                print(ElCt)
                #print(eval('Cht'+str(0))[eval('Cht'+str(0)).columns.__getitem__(0)][ii])
                #print(iii)
                vars()['Eln' + str(i) + '_' + str(ElCt)]=[]
                vars()['ElG' + str(i) + '_' + str(ElCt)]=[]
                #vars()['El' + str(ElCt)].append(eval('Cht'+str(0))[eval('Cht'+str(0)).columns.__getitem__(0)][ii])
                vars()['El' + str(i)].append(eval('Cht'+str(i))['Transition'][ii])
                vars()['Eln' + str(i) + '_' + str(ElCt)].append(eval('Cht'+str(i))['Transition'][ii])
                vars()['Eln' + str(i) + '_' + str(ElCt)].append(eval('ChFt'+str(i))[eval('ChFt'+str(0)).columns.__getitem__(0)][iii])
                vars()['ElG' + str(i) + '_' + str(ElCt)]=[]
                #vars()['ElG' + str(ElCt)].append(eval('Cht'+str(0))[eval('Cht'+str(0)).columns.__getitem__(0+1)][ii])
                vars()['ElG' + str(i) + '_' + str(ElCt)].append(eval('Cht'+str(i))['Generated 1/msR'][ii])
                vars()['ElG' + str(i) + '_' + str(ElCt)].append(eval('ChFt'+str(i))[eval('ChFt'+str(0)).columns.__getitem__(0+1)][iii])
                print(eval('Eln' + str(i) + '_' + str(ElCt)))
                ElCt = ElCt + 1
                #checkdoublecount = 1
        for iii in range(0,len(eval('BrFt'+str(i)))):
            if eval('Cht'+str(i))[eval('Cht'+str(i)).columns.__getitem__(0)][ii] == eval('BrFt'+str(i))[eval('BrFt'+str(i)).columns.__getitem__(0)][iii]:
                print("yes BrFt")
                print(i)
                #if checkdoublecount == 1:
                ElCt = ElCt - 1
                #print(eval('Cht'+str(0))[eval('Cht'+str(0)).columns.__getitem__(0)][ii])
                #print(iii)
                #vars()['Eln' + str(i) + '_' + str(ElCt)]=[]
                #vars()['ElG' + str(i) + '_' + str(ElCt)]=[]
                #vars()['El' + str(ElCt)].append(eval('Cht'+str(0))[eval('Cht'+str(0)).columns.__getitem__(0)][ii])
                #vars()['El' + str(i)].append(eval('Cht'+str(i))['Transition'][ii])
                #vars()['Eln' + str(i) + '_' + str(ElCt)].append(eval('Cht'+str(i))['Transition'][ii])
                print(ElCt)
                print(eval('Eln' + str(i) + '_' + str(ElCt)))
                print((eval('ChFt'+str(i))[eval('BrFt'+str(0)).columns.__getitem__(0)][iii]))
                vars()['Eln' + str(i) + '_' + str(ElCt)].append(eval('BrFt'+str(i))[eval('BrFt'+str(0)).columns.__getitem__(0)][iii])
                print(eval('Eln' + str(i) + '_' + str(ElCt)))
                #vars()['ElG' + str(i) + '_' + str(ElCt)]=[]
                #vars()['ElG' + str(ElCt)].append(eval('Cht'+str(0))[eval('Cht'+str(0)).columns.__getitem__(0+1)][ii])
                #vars()['ElG' + str(i) + '_' + str(ElCt)].append(eval('Cht'+str(i))['Generated 1/msR'][ii])
                vars()['ElG' + str(i) + '_' + str(ElCt)].append(eval('BrFt'+str(i))[eval('BrFt'+str(0)).columns.__getitem__(0+1)][iii])
                #if checkdoublecount == 0:
                ElCt = ElCt + 1
        #checkdoublecount = 0
                
#print element list for each experiment
for i in range(0,len(ExperimentName)):
    print(eval('El'+str(i)))
#print element values for each experiment
for i in range(0,len(ExperimentName)):
    print(ExperimentName[i])
    for iv in range(0, len(eval('El'+str(i)))):
        print(eval('Eln'+str(i)+'_'+str(iv)))
        print(eval('ElG'+str(i)+'_'+str(iv)))

#user select which experiment is standard
standardselectionname = []
standardselectionnum = []
import tkinter
import tkinter.messagebox
for i in range(0,len(ExperimentName)):
    standardselection = tkinter.messagebox.askquestion(title="experiment selection", message=ExperimentName[i]+'\r'+"Is this a standard")
    if standardselection == 'yes':
        standardselectionname.append(ExperimentName[i])
        standardselectionnum.append(i)

Elelm = []
for i in range(0,len(ExperimentName)):
    #print('i')
    #print(i)
    vars()['El' + str(i) + 'elm']=[]
    for iv in range(0,len(eval('El'+str(i)))):
        #print('iv')
        #print(iv)
        vars()['El' + str(i) + 'elm'].append(eval('El'+str(i)+'['+str(iv)+']'+'[:2]'))
        vars()['El' + 'elm'].append(eval('El'+str(i)+'['+str(iv)+']'+'[:2]'))
    vars()['El' + str(i) + 'elm2'] = list(dict.fromkeys(eval('El' + str(i) + 'elm')))
vars()['El' + 'elm2'] = list(dict.fromkeys(eval('El' + 'elm')))

elementstandard = []
standardelement = []
standardelementname = []
standardexperimentnum = []
for i in range(0,len(Elelm2)):
    #for iv in range(0,len(eval('El'+str(i)+'elm2'))):
        for ii in range(0,len(standardselectionname)):
            #standardselection = tkinter.messagebox.askquestion(title="standard selection", message=standardselectionname[ii]+'\r'+"Is this the standard for"+'\r'+eval('El'+str(i)+'elm2'+'['+str(iv)+']'))
            standardselection = tkinter.messagebox.askquestion(title="standard selection", message=standardselectionname[ii]+'\r'+"Is this the standard for"+'\r'+Elelm2[i])
            if standardselection == 'yes':
                print(i)
                elementstandard.append(Elelm2[i])
                print(Elelm2[i])
                print(ii)
                print(standardselectionname[ii])
                standardelement.append(ii)
                standardelementname.append(standardselectionname[ii])
                standardexperimentnum.append(standardselectionnum[ii])

#calculate kratio
#f = open("C:/Users/glxbb/Documents/DTSA-II Reports/2024/September/26-Sep-2024/PythonKratios.txt","a")
f = open(urllocation.name.split('index1.html')[0]+'PythonKratios.txt',"a")

for i in range(0,len(ExperimentName)):
    #for each x-ray line in first one experiment then next etc
    for ii in range(0,len(eval('El'+str(i)))):
        try:
            #find standard
            print(elementstandard.index(eval('El'+str(i))[ii][:2]))
            #so experiment no is
            print(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])
            #so kratio is
            #unknown/
            #eval('ElG'+str(i)+'_'+str(ii))/
            print(eval('ElG'+str(i)+'_'+str(ii)))
            #standard intensity is - but ii needs to be determined
            #eval('ElG'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])+'_'+str(ii))
            #standard list of elements is
            print(eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])))
            #position of element for standard is
            print(eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])).index(eval('El'+str(i))[ii]))
            #standard intensity is
            print(eval('ElG'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])+'_'+str(eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])).index(eval('El'+str(i))[ii]))))
            #so kratio is
            sum(eval('ElG'+str(i)+'_'+str(ii)))/sum(eval('ElG'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])+'_'+str(eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])).index(eval('El'+str(i))[ii]))))
            print(sum(eval('ElG'+str(i)+'_'+str(ii)))/sum(eval('ElG'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])+'_'+str(eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])).index(eval('El'+str(i))[ii])))))
            f.write(str(ExperimentName[i])+','+str(eval('El'+str(i))[ii])+','+str(sum(eval('ElG'+str(i)+'_'+str(ii)))/sum(eval('ElG'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])+'_'+str(eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])).index(eval('El'+str(i))[ii])))))+'\n')
        except ValueError:
            print("Element not in standard list")
            print(eval('El'+str(i))[ii][:2])
        except:
            print("Something else went wrong")
f.close()
            
#get from variable
#eval('k'+str(5))
#eval('k'+str(14))
#eval('k'+str(i))
