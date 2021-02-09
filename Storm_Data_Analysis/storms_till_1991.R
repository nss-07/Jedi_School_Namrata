library(tidyverse)

dataframe <- read.csv("noaa_storms.csv")

# storing required data in a new DF
required_data <- subset(dataframe, year<='1999')

library(lubridate)

required_data$time = with(required_data, ymd_h(paste(year,month,day,hour,sep=' ')))

required_data = subset(required_data,select=-c(ts_diameter,hu_diameter))

library(dplyr)

summary_data <- required_data %>%
  group_by(name,year,status) %>%
  summarize(mid_point_lat = mean(lat),
            mid_point_long = mean(long),
            avg_wind = mean(wind),
            avg_pressure = mean(pressure),
            start = min(time),
            end = max(time)) %>%
  arrange(year)