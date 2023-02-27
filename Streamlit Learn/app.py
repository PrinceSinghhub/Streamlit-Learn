import streamlit as st


st.title('Hello Codex Coder Chapter 1')
st.text('Introduction Chapter How to work Streamlit and some basic command')
st.header('Header')
st.subheader('Sub Header')
st.text('Hello Codex Coder Game ChANGER')

# use tag like html  
st.markdown('# h1 hello ji Adhrar Card Bnana Hai')
st.markdown('## h2 hello ji Adhrar Card Bnana Hai')
st.markdown('### h3 hello ji Adhrar Card Bnana Hai')
st.markdown('#### h4 hello ji Adhrar Card Bnana Hai')

# ad emoji 
st.markdown(':moon:')
st.markdown(':heart: I Love You')

# mark down cheat sheet 
'''https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet'''

# using for write mathamaetica formula or as its some content write 
st.latex('a ^ 2 +b ^ 2 +2ab')

st.write('Codex','Coder','Python')

# basic documentation of stramlit or any function
st.write(st)

dic = {'Python':90,
       'Java': 80,
       'C':75}
st.write(dic)