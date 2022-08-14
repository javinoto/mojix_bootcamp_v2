import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("https://live.staticflickr.com/65535/52284883263_fe574df15e_z.jpg", width=150)

with col2:
    st.caption("")

""
"# 10 Cool Beginner Python Tricks That Will Make Your Life Easier"

st.caption("## Simple but effective tips for every python lovers")
st.image("https://live.staticflickr.com/65535/52283896242_10a45d1877_z.jpg")


''
st.write('''
## Walrus operator

The Walrus **or := operator** is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.
''')

st.caption('### Example')

'If we want to check and print the length of a list:'


st.success('Mylist = [1,2,3]')
st.success('if(l := len(mylist) > 2)')
st.success('print(l)')

st.caption('### Output')

st.success('3')
