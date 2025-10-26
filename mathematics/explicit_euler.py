import numpy as np
# import matplotlib.pyplot as plt
import plotly.graph_objects as go


# plt.style.use('seaborn-poster')
# %matplotlib inline

# Define parameters
def f(t, s): 
    return np.exp(-t) # ODE


def main():
    h = 0.1 # Step size
    t = np.arange(0, 1 + h, h) # Numerical grid
    s0 = -1 # Initial Condition

    # Explicit Euler Method
    s_approximate = np.zeros(len(t))
    s_approximate[0] = s0

    for i in range(0, len(t) - 1):
        s_approximate[i + 1] = s_approximate[i] + h * f(t[i], s_approximate[i])

    # Calculate Exact Solution
    s_exact = -np.exp(-t)

    # -----------------------------------------------------
    # PLOTLY REPLACEMENT FOR MATPLOTLIB
    # -----------------------------------------------------

    # 1. Create the 'Approximate' trace (equivalent to 'bo--')
    trace_approximate = go.Scatter(
        x=t,
        y=s_approximate,
        mode='lines+markers',  # 'bo--' is lines with markers
        name='Approximate',
        line=dict(dash='dash', color='blue'),
        marker=dict(symbol='circle', size=5)
    )

    # 2. Create the 'Exact' trace (equivalent to 'g')
    trace_exact = go.Scatter(
        x=t,
        y=s_exact,
        mode='lines',
        name='Exact',
        line=dict(color='green', width=2)
    )

    # 3. Create the Figure and add traces
    fig = go.Figure(data=[trace_approximate, trace_exact])

    # 4. Apply layout and styling (Title, Axes, Grid, Legend, Size)
    fig.update_layout(
        title='Approximate and Exact Solution for Simple ODE',
        xaxis_title='t',
        yaxis_title='f(t)',
        # Equivalent to plt.figure(figsize=(12, 8)) in dimensions
        height=600,
        width=900,
        # Equivalent to plt.grid()
        xaxis=dict(showgrid=True, zeroline=False),
        yaxis=dict(showgrid=True, zeroline=False),
        # Equivalent to plt.legend(loc='lower right')
        legend=dict(
            yanchor="bottom",
            y=0.01,
            xanchor="right",
            x=0.99
        )
    )

    # 5. Display the figure
    fig.write_html("my_plot.html")
    # fig.show()


# main guard idiom
if __name__=='__main__':
    main()