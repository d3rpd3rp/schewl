#!/usr/bin/Rscript
#r routine to init the db based on set of csv files
#ex. Rscript foo.R arg1 arg2
#provide cmd line arg "path": location of csv files
#and host as IPv4 Address (FQDN not tested)
#ex. Rscript db-init.r /home/ubuntu/

library(DBI)

args<-commandArgs(TRUE)
filepath<-args[1]
#host<-args[2]
skipflag<-TRUE
databasename<-'djuci'
tablename<-'data'


con <- dbConnect(RMySQL::MySQL(), user='root', password='Spring2019!!', host='104.154.56.191')
dbSendQuery(con, "CREATE DATABASE djuci;")
dbSendQuery(con, "USE djuci;")
#credit for the id generation https://programminghistorian.org/en/lessons/getting-started-with-mysql-using-r#create-database
dbSendQuery(con, "CREATE TABLE data (id INT NOT NULL AUTO_INCREMENT, quarter INT, stock VARCHAR(20), date DATE, open FLOAT, \
                                    high FLOAT, low FLOAT, close FLOAT, volume FLOAT, percent_change_price FLOAT, \
                                    percent_change_volume_over_last_wk FLOAT, previous_weeks_volume FLOAT, \
                                    next_weeks_open FLOAT, next_weeks_close FLOAT, percent_change_next_weeks_price FLOAT, \
                                    days_to_next_dividend FLOAT,  percent_return_next_dividend FLOAT, PRIMARY KEY (id));")
dbSendQuery(con, "GRANT ALL PRIVILEGES ON djuci.* TO 'root'@'104.154.56.191' IDENTIFIED BY 'root';")
dbDisconnect(con)


con <- dbConnect(RMySQL::MySQL(), user='root', password='Spring2019!!', dbname='djuci', host='104.154.56.191')
dbSendQuery(con, "USE djuci;")
samplerows <- read.csv(filepath, sep=",", row.names=NULL)
names(samplerows)<-c("quarter","stock","date","open","high","low","close","volume",
                    "percent_change_price","percent_change_volume_over_last_wk",
                    "previous_weeks_volume","next_weeks_open","next_weeks_close",
                    "percent_change_next_weeks_price","days_to_next_dividend","percent_return_next_dividend")
dbWriteTable(con, name=tablename, samplerows, row.names=FALSE, field.types = NULL, append=TRUE )
dbDisconnect(con)

#print(typeof(samplerows))
#print(samplerows[1, ])
#for(i in 1:length(names(samplerows))){
#    print(typeof(names(samplerows[i])))
#}

quit()