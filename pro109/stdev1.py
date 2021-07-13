import csv
import pandas as pd
import statistics as st

df= pd.read_csv("height-weight.csv")
height_list=df["Height(Inches)"].to_list()
weight_list=df["Weight(Pounds)"].to_list()

#calculate mean median mode
mean_height=st.mean(height_list)
mean_weight=st.mean(weight_list)
median_height=st.median(height_list)
median_weight=st.median(weight_list)
mode_height=st.mode(height_list)
mode_weight=st.mode(weight_list)
stdev_height=st.stdev(height_list)
stdev_weight=st.stdev(weight_list)
#print(stdev_height)

height_stdv1_start,height_stdv1_end = mean_height-stdev_height,mean_height+stdev_height
height_stdv2_start,height_stdv2_end = mean_height-(2*stdev_height),mean_height+(2*stdev_height)
height_stdv3_start,height_stdv3_end = mean_height-(3*stdev_height),mean_height+(3*stdev_height)

weight_stdv1_start,weight_stdv1_end = mean_weight-stdev_weight,mean_weight+stdev_weight
weight_stdv2_start,weight_stdv2_end = mean_weight-(2*stdev_weight),mean_weight+(2*stdev_weight)
weight_stdv3_start,weight_stdv3_end = mean_weight-(3*stdev_weight),mean_weight+(3*stdev_weight)

#percentage of stdev in 1,2,3
height_data_stdv1=[result for result in height_list if result>height_stdv1_start and result<height_stdv1_end]
print("{}% of data for height lies within 1 standard deviation".format(len(height_data_stdv1)*100.0/len(height_list)))

height_data_stdv2=[result for result in height_list if result>height_stdv2_start and result<height_stdv2_end]
print("{}% of data for height lies within 2 standard deviation".format(len(height_data_stdv2)*100.0/len(height_list)))

height_data_stdv3=[result for result in height_list if result>height_stdv3_start and result<height_stdv3_end]
print("{}% of data for height lies within 3 standard deviation".format(len(height_data_stdv3)*100.0/len(height_list)))

weight_data_stdv1=[result for result in weight_list if result>weight_stdv1_start and result<weight_stdv1_end]
print("{}% of data for weight lies within 1 standard deviation".format(len(weight_data_stdv1)*100.0/len(weight_list)))

weight_data_stdv2=[result for result in weight_list if result>weight_stdv2_start and result<weight_stdv2_end]
print("{}% of data for weight lies within 2 standard deviation".format(len(weight_data_stdv2)*100.0/len(weight_list)))

weight_data_stdv3=[result for result in weight_list if result>weight_stdv3_start and result<weight_stdv3_end]
print("{}% of data for weight lies within 3 standard deviation".format(len(weight_data_stdv3)*100.0/len(weight_list)))