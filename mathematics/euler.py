'''
euler number, e
'''
import math
import plotly.express as px


def nth_term(n: int):
    '''
    the power series looks like 1 / 0!  +  1 / 1!  +  1 / 2!  +  1 / 3!  +  ...
    '''
    return 1 / math.factorial(n)


e = 0
e_list = []
for i in range(20):
    e += 1 /  math.factorial(i)
    e_list.append(e)
    print(e)

print(e_list)

fig = px.line(
    x=list(range(20)),
    y=e_list,
    markers=True,
    title="Convergence of Euler's Number e",
    template="plotly_dark"
)

# fig.write_html("outputs/chart.html")
fig.show()

