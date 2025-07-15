

import matplotlib.pyplot as plt

def risk_pie(risk_series):
    """
    Risk dağılımını pasta grafiği olarak döndürür.
    """
    counts = risk_series.value_counts()
    fig, ax = plt.subplots()
    ax.pie(
        counts,
        labels=counts.index,
        autopct="%1.1f%%",
        startangle=90,
        shadow=True
    )
    ax.set_title("Risk Dağılımı")
    ax.axis("equal")  # Daire gibi görünmesi için
    return fig
