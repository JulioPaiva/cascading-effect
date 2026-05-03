from typing import List

import random
import streamlit as st
import pandas as pd
import plotly.express as px


PEOPLES = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Frank",
    "Grace",
    "Heidi",
    "Ivan",
    "Judy"
]

peoples, history = [], []

def clamp(value, min_val, max_val):
    if value < min_val:
        return min_val
    return max_val

class People:
    def __init__(self, name: str):
        self.name: str = name
        self.humor: int = random.randint(-2, 1)
        self.energy: int = random.randint(-1, 5)
        self.influence: int = random.randint(-1, 1)
    
    def interact(self, other_people):
        impact = (
            float(self.humor) * float(self.influence) * random.randint(-1, 1)
        )

        other_people.humor += clamp(impact * 0.5, -10, 3)
        other_people.energy += clamp(impact * 0.1, -10, 10)
        other_people.influence += clamp(impact * 0.2, -1, 1)

        other_people.humor *=  0.98
        other_people.energy *=  0.95


class Environment:
    def __init__(self, peoples: List[People]):
        self.peoples = peoples

    def simulate(self):
        for people in self.peoples:
            for other in self.peoples:
                if people != other:
                    people.interact(other)

st.set_page_config(layout="wide")
st.write("Simulação de Interações Sociais")

quantity_people_slider = st.slider(
    "Selecione o número de pessoas",
    min_value=3,
    max_value=10,
    value=3
)

for _ in range(1, quantity_people_slider):
    peoples = [People(PEOPLES[i]) for i in range(quantity_people_slider)]
    history = []

quantity_interactions_slider = st.slider(
    "Selecione o número de interações",
    min_value=1,
    max_value=100,
    value=5
)

env = Environment(peoples)

for i in range(quantity_interactions_slider):
    for p in env.peoples:
        history.append({
            "step": i+1,
            "name": p.name,
            "humor": p.humor,
            "energy": p.energy,
            "influence": p.influence
        })

    env.simulate()

df = pd.DataFrame(history)

fig = px.line(
    df,
    x="step",
    y="humor",
    color="name",
    title="Evolução do Humor ao Longo das Interações"
)

st.plotly_chart(fig)

df_mean = df.groupby("step")["humor"].mean().reset_index()

fig_mean = px.line(
    df_mean,
    x="step",
    y="humor",
    title="Humor médio do grupo"
)

df_energy = df.groupby("step")["energy"].mean().reset_index()

fig_energy = px.line(
    df_energy,
    x="step",
    y="energy",
    title="Energia média do grupo"
)

col1, col2 = st.columns(2)
col1.plotly_chart(fig_mean)
col2.plotly_chart(fig_energy)


st.write("Dataset gerado:")
st.write(df)
