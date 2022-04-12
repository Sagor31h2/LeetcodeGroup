s = "this is a string" 

st = []
fs = ""
for i in range(len(s)):
    if(s[i] == " "):
        while len(st):
            fs+= st.pop()
        fs+=" "
    else:
        st.append(s[i])
while len(st):
    fs+= st.pop()

print(fs)