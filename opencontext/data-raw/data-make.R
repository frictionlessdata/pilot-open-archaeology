library("datapkg")
df <- read.csv("EOL_Zooarchaeology_Metrics_Dataset_Version_2.csv")
datapkg_write(df, path = "../data") #, overwrite = TRUE
