import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import Bio.Seq
import Bio.SeqUtils
from Bio.Seq import Seq
from Bio.SeqUtils import GC


####################
# Page Title
####################

image = Image.open('Pycendo Logo.png')
st.image(image, use_column_width=True)
st.write("""
# Pycendo: Protein Sequence Analysis
Sequence Length & Amino Acid Composition
***
""")

####################
# Input Text Box
####################

#st.sidebar.header('Enter Protein Sequence')
st.header('Enter Protein Sequence')

sequence_input =""

#sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = ''.join(sequence) # Concatenates list to string

st.write("""
***
""")

## Prints the input Protein Sequence
st.header('INPUT (Protein Query)')
sequence

## Prints the results
st.header('OUTPUT')

## 1. Sequence Length
st.subheader('1. Sequence Length')
def amino_acid_count(seq):
    d = dict([
        ('Sequence Length',len(seq))
        ])
    return d

Y = amino_acid_count(sequence)

#Y_label = list(Y)
#Y_values = list(Y.values())

Y

## 2. Amino Acid Count
st.subheader('2. Amino Acid Count')
def amino_acid_count(seq):
    d = dict([
        ('Ala',seq.count('A')),
        ('Arg',seq.count('R')),
        ('Asn',seq.count('N')),
        ('Asp',seq.count('D')),
        ('Cys',seq.count('C')),
        ('Glu',seq.count('E')),
        ('Gln',seq.count('Q')),
        ('Gly',seq.count('G')),
        ('His',seq.count('H')),
        ('Ile',seq.count('I')),
        ('Leu',seq.count('L')),
        ('Lys',seq.count('K')),
        ('Met',seq.count('M')),
        ('Phe',seq.count('F')),
        ('Pro',seq.count('P')),
        ('Ser',seq.count('S')),
        ('Thr',seq.count('T')),
        ('Trp',seq.count('W')),
        ('Tyr',seq.count('Y')),
        ('Val',seq.count('V'))
        ])
    return d

X = amino_acid_count(sequence)

#X_label = list(X)
#X_values = list(X.values())

X

### 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'Amino Acids'})
st.write(df)

### 4. Display Bar Chart using Altair
st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='Amino Acids',
    y='count'
)
p = p.properties(
    width=alt.Step(25) # controls width of bar
)
st.write(p)

st.subheader('Pycendo Project Beta Version - Chaidir Adam 2021')
