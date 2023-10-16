import spacy

nlp = spacy.load("./model/model-best")

text = """
GUDIPALLI JYOTHI
Phone number: +91-6304026390 
Email: jyothigudipalli8@gmail.com
CAREER OBJECTIVES
• To be associated with an organization which provides challenging work environment and proving my excellence at every step is my long term career goal.
• Highly efficient, and passionate for learning new concepts,ideas and techniques. Reach the heights in my career with proven expertise.
EDUCATION
Degree Institute Board/University CGPA/percentage Year of passing
B.Tech ECE Rajiv Gandhi University of knowledge 
Technologies-Nuzvid
RGUKT-NUZVID 9.24 2024
PUC-12th Rajiv Gandhi University of knowledge 
Technologies-Nuzvid
RGUKT-NUZVID 9.21 2020
SSC Government High school Board of secondary 
Education
10.0 2018
PERSONAL SKILLS
• Problem solving abilities. 
• Willing to learn ,team facilitator and hard worker 
• Good communication skills.
• Disciplined and punctual.
• Always be infront of exploring the learnt skills.
PROJECTS
➪ Smart watch to monitor health 
➪ Diabetic retinopathy
➪ Implementation of digital clock(on bread board)
➪Liver segmentation using unet
TECHNICAL SKILLS 
➪C/C++
➪Python
➪Xilinx Vivado
ACHIVEMENTS 
• District level certificate for essay writting
•Certificate from the Government of Andhra Pradesh for the getting 10.0 CGPA
•Best student of the year Award in 2017 conducted by LIC(Life Insurance Corporation)
PERSONAL INFORMATION 
• Nationality :Indian 
• Date of Birth :23-05-2002
• Marital Status : Unmarried 
• Religion : Hindu 
• Gender : Female
DECLARATION
 I solemnly declare that all the information furnished in this document is free of errors to the best of my 
knowledge..
 
Place: Signature: 
Nuzvid G.Jyothi

"""

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)