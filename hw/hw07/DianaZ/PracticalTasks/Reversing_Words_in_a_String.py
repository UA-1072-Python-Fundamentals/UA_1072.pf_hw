def reverse(st):
    # Your Code Here
    s = st.split(" ")
    st = s[1]+" "+s[0]
    return st

print(reverse('Hello World'))
print(reverse('Hi There.'))