
import numpy as np
import pandas as pd
from report import *
import plotly.express as px


def generate_graph(video):
    top_positive_emotions, top_negative_emotions = videoToEmotions(video)
    positives_emo = [i[0] for i in top_positive_emotions]
    positives_values = [j[1] for j in top_positive_emotions]
    negatives_values = [b[1] for b in top_negative_emotions]
    conns = ["positive"] * 5 + ["negative"] * 5
    negatives_emo = [a[0] for a in top_negative_emotions]
    emotions = positives_emo + negatives_emo
    values = positives_values + negatives_values
    df = pd.DataFrame({"Emotions": emotions, "Values": values, "Connotation": conns})

    print(df)

    fig = px.bar(df, x="Emotions", y="Values",
                color="Connotation", 
                height=600, width=800)
    fig.update_layout(bargap=0.2)
    return fig

generate_graph("backend/vid.mp4").show()  

