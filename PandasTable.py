import io
import pandas as pd
from numpy.random import randn
from IPython.display import HTML

cities_df = pd.read_csv('cities.csv')

HTML(cities_df.to_html(buf=None, columns=None, col_space=None, header=True, index=True, na_rep='NaN',
       formatters=None, float_format=None, sparsify=None, index_names=True, justify=None,
       bold_rows=True, classes='table table-striped table-bordered table-hover table-condensed', escape=True, max_rows=None, max_cols=None, show_dimensions=False,
       notebook=False, decimal='.', border=None))


cities_df.to_html("data.html")