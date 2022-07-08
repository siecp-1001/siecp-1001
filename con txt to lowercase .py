text=['This is introduction to NLP','It is likely to be useful,to people ','Machine learning is the new electrcity','Therewould be less hype around AI and more action goingforward','pyhon is the best tool!','R is good langauage','Ilike this book','I want more books like this']
import pandas as pd
df =pd.DataFrame({'tweet':text})
print(df)
x = 'Testing'
x2 = x.lower()
print(x2)