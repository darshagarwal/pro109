import statistics as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df =  pd.read_csv("StudentsPerformance.csv")
data_list = df["math score"].tolist()
mean = st.mean(df)
median = st.median(df)
mode = st.mode(df)
stdev = st.stdev(df)

stdev_start,stdev_end = mean-stdev,mean+stdev
stdev_start2,stdev_end2 = mean-(2*stdev),mean+(2*stdev)
stdev_start3,stdev_end3 = mean-(3*stdev),mean+(3*stdev)

data_stdv1=[result for result in data_list if result>stdev_start and result<stdev_end]
print("{}% of data lies within 1 standard deviation".format(len(data_stdv1)*100.0/len(data_list)))

data_stdv2=[result for result in data_list if result>stdev_start2 and result<stdev_end2]
print("{}% of data lies within 2 standard deviation".format(len(data_stdv2)*100.0/len(data_list)))

data_stdv3=[result for result in data_list if result>stdev_start3 and result<stdev_end3]
print("{}% of data within 3 standard deviation".format(len(data_stdv3)*100.0/len(data_list)))

fig=ff.create_distplot([mean],["math score"],show_hist=False)
fig.add_trace(go.Scatter(x=[stdev_start,stdev_start],y=[2],mode="lines",name="stdev start 1"))
fig.add_trace(go.Scatter(x=[stdev_start2,stdev_start2],y=[2],mode="lines",name="stdev start 2"))
fig.add_trace(go.Scatter(x=[stdev_start3,stdev_start3],y=[2],mode="lines",name="stdev start 3"))
fig.add_trace(go.Scatter(x=[stdev_end,stdev_end],y=[2],mode="lines",name="stdev end 1"))
fig.add_trace(go.Scatter(x=[stdev_end2,stdev_end2],y=[2],mode="lines",name="stdev end 2"))
fig.add_trace(go.Scatter(x=[stdev_end3,stdev_end3],y=[2],mode="lines",name="stdev end 3"))
fig .show()