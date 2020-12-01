''' 
In this code I am importing Cockatrice data from XML into CSV files I can use within Tablea

The XML file has three 'main' children:
    - Info
    - Sets
    - Cards
    
I'll ignore Info as I don't need it.
Sets and Cards will be their own CSV files
'''

import xml.etree.ElementTree as ET
from csv import writer

def main():
    tree=ET.parse('Cockatrice.xml')
    root=tree.getroot()
    
    releasedates = {}
    
    for elem in root:
        if elem.tag=='sets':
            sets(elem, releasedates)
        elif elem.tag=='cards':
            cards(elem, releasedates)  

    
def sets(node, releasedates):
    print('Sets')
    with open('Sets.csv', 'w', newline='', encoding='utf-8') as writecsv:
        output = writer(writecsv, delimiter=',')
        output.writerow(['SetID','Set','Type','Date'])
    
        
        for sets in node:
            code=isnone(sets[0],'')
            name=isnone(sets[1],'')
            tipe=isnone(sets[2],'')
            date=isnone(sets[3],'')
            
            if tipe!='Promo' and tipe!='Funny' and tipe!='Token' and tipe!='Tokens':
                releasedates[code]=date
                output.writerow([code,name,tipe,date])

    
def cards(node, releasedates):
    print('Cards')
    with open('Cards.csv', 'w', newline='', encoding='utf-8') as writecsv:
        output = writer(writecsv, delimiter=',')
        output.writerow(['Card','Rarity','Text','PT','Type','TypeLine','Cost','CMC','Colours','Identity','StandardStatus','ModernStatus','CommanderStatus','SetID'])
    
        for card in node:
            name=card[0].text
            text=card[1].text
            
            # for tags in prop:
            prop=card[2]              
            pt=ifnull(prop.findall('pt'),'')
            tipe=ifnull(prop.findall('maintype'),'')
            typeline=ifnull(prop.findall('type'),'')
            cost=ifnull(prop.findall('manacost'),'')
            cmc=ifnull(prop.findall('cmc'),'')
            colours=ifnull(prop.findall('colors'),'')
            identity=ifnull(prop.findall('coloridentity'),'')
            cstatus=ifnull(prop.findall('format-commander'),'')
            mstatus=ifnull(prop.findall('format-modern'),'')
            sstatus=ifnull(prop.findall('format-standard'),'')
            
            setdate='1990-01-01'
            sett=''
            # grab latest set
            for sets in card.iter('set'):
                setid=sets.text
                if setid in releasedates:
                    currdate=releasedates[setid]
                    if currdate>setdate:
                        rarity=sets.get('rarity')
                        setdate=currdate
                        sett=sets.text
               
            if sett!='':
                output.writerow([name,rarity,text,pt,tipe,typeline,cost,cmc,colours,identity,sstatus,mstatus,cstatus,sett])

def isnone(value, replacement):
    if value.text is None:
        retval=replacement
    else:
        retval=value.text
    return retval

def ifnull(value, replacement):
    try:
        retval = value[0].text
    except IndexError:
        retval = replacement
    return retval
    
if __name__ == "__main__":
    main();