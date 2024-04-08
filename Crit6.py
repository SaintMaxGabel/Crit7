dictionaryRooM = {"CSC101" : "3004", "CSC102" : "4501", "CSC103" : "6755", "NET110" : "1244", "COM241" : "1411"}

dictionary2 = {"CSC101" : " Haynes", "CSC102" : "Alvarado", "CSC103" : "Rich", "NET110" : "Burke", "COM241" : "Lee"}

dictionary1 = {"CSC101" : "8:00 a.m.", "CSC102" : "9:00 a.m.", "CSC103" : "10:00 a.m.", "NET110" : "11:00 a.m.", "COM241" : "1:00 p.m."}

dictionarY = str(input('Enter a course number.'))
print (dictionarY + ' Room Number: ' + dictionaryRooM[dictionarY] +', Instructor: '+ dictionary2[dictionarY] + ', Meeting time: ' + dictionary1[dictionarY])