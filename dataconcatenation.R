setwd("Downloads/sensor datasets/intel/interpolated/clean")

sensor1_data <- read.csv(file="Node01_interpolated.txt", header=TRUE, sep=",")
sensor2_data <- read.csv(file="Node04_interpolated.txt", header=TRUE, sep=",")
sensor3_data <- read.csv(file="Node06_interpolated.txt", header=TRUE, sep=",")
sensor4_data <- read.csv(file="Node19_interpolated.txt", header=TRUE, sep=",")
sensor5_data <- read.csv(file="Node22_interpolated.txt", header=TRUE, sep=",")
sensor6_data <- read.csv(file="Node23_interpolated.txt", header=TRUE, sep=",")
sensor7_data <- read.csv(file="Node29_interpolated.txt", header=TRUE, sep=",")
sensor8_data <- read.csv(file="Node33_interpolated.txt", header=TRUE, sep=",")
sensor9_data <- read.csv(file="Node34_interpolated.txt", header=TRUE, sep=",")
sensor10_data <- read.csv(file="Node45_interpolated.txt", header=TRUE, sep=",")

dataset <- rbind(sensor1_data, sensor2_data, sensor3_data, sensor4_data, sensor5_data, sensor6_data, sensor7_data, sensor8_data, sensor9_data, sensor10_data)

summary(dataset)
head(dataset)
length(dataset)

hist(dataset$temperature)
hist(dataset$light)

colnames(dataset) <- c("Timestamp", "ID", "has_fault_type", "temperature", "light")

write.csv(dataset, file = "clean_intelsensordata.csv")

setwd("../injected_random")

temp_sensor1_data <- read.csv(file="mote=1_sensortype=light_faulttype=random.txt", header=TRUE, sep=",")
temp_sensor2_data <- read.csv(file="mote=4_sensortype=light_faulttype=random.txt", header=TRUE, sep=",")
temp_sensor3_data <- read.csv(file="mote=6_sensortype=light_faulttype=random.txt", header=TRUE, sep=",")
temp_sensor4_data <- read.csv(file="mote=19_sensortype=light_faulttype=random.txt", header=TRUE, sep=",")
temp_sensor5_data <- read.csv(file="mote=22_sensortype=light_faulttype=random.txt", header=TRUE, sep=",")
temp_sensor6_data <- read.csv(file="mote=23_sensortype=light_faulttype=random.txt", header=TRUE, sep=",")
temp_sensor7_data <- read.csv(file="mote=29_sensortype=light_faulttype=random.txt", header=TRUE, sep=",")
temp_sensor8_data <- read.csv(file="mote=33_sensortype=light_faulttype=random.txt", header=TRUE, sep=",")
temp_sensor9_data <- read.csv(file="mote=34_sensortype=light_faulttype=random.txt", header=TRUE, sep=",")
temp_sensor10_data <- read.csv(file="mote=45_sensortype=light_faulttype=random.txt", header=TRUE, sep=",")

temp_dirty_dataset <- rbind(temp_sensor1_data, temp_sensor2_data, temp_sensor3_data, temp_sensor4_data, temp_sensor5_data, 
                                    temp_sensor6_data, temp_sensor7_data, temp_sensor8_data, temp_sensor9_data, temp_sensor10_data)

colnames(temp_dirty_dataset) <- c("Timestamp", "ID", "has_fault_type", "temperature", "light")

write.csv(temp_dirty_dataset, file = "temp_dirty_intelsensordata_light.csv")


temp_sensor1_data <- read.csv(file="mote=1_sensortype=temperature_faulttype=random.txt", header=TRUE, sep=",")
temp_sensor2_data <- read.csv(file="mote=4_sensortype=temperature_faulttype=random.txt", header=TRUE, sep=",")
temp_sensor3_data <- read.csv(file="mote=6_sensortype=temperature_faulttype=random.txt", header=TRUE, sep=",")
temp_sensor4_data <- read.csv(file="mote=19_sensortype=temperature_faulttype=random.txt", header=TRUE, sep=",")
temp_sensor5_data <- read.csv(file="mote=22_sensortype=temperature_faulttype=random.txt", header=TRUE, sep=",")
temp_sensor6_data <- read.csv(file="mote=23_sensortype=temperature_faulttype=random.txt", header=TRUE, sep=",")
temp_sensor7_data <- read.csv(file="mote=29_sensortype=temperature_faulttype=random.txt", header=TRUE, sep=",")
temp_sensor8_data <- read.csv(file="mote=33_sensortype=temperature_faulttype=random.txt", header=TRUE, sep=",")
temp_sensor9_data <- read.csv(file="mote=34_sensortype=temperature_faulttype=random.txt", header=TRUE, sep=",")
temp_sensor10_data <- read.csv(file="mote=45_sensortype=temperature_faulttype=random.txt", header=TRUE, sep=",")

temp_dirty_dataset <- rbind(temp_sensor1_data, temp_sensor2_data, temp_sensor3_data, temp_sensor4_data, temp_sensor5_data, 
                              temp_sensor6_data, temp_sensor7_data, temp_sensor8_data, temp_sensor9_data, temp_sensor10_data)

colnames(temp_dirty_dataset) <- c("Timestamp", "ID", "has_fault_type", "temperature", "light")

write.csv(temp_dirty_dataset, file = "temp_dirty_intelsensordata_temperature.csv")

